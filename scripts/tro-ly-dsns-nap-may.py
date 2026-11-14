#!/usr/bin/env python3
"""Index the folders a learner chose into the vault. Pure stdlib, no LLM, no network.

Reads `<vault>/nap-may.yaml`. Scans ONLY the folders listed under `scan_paths`;
with no folders listed it does nothing. Hard exclusions always apply and cannot
be turned off. Writes `<vault>/Chi-muc-may/<YYYY-MM-DD>.jsonl` (path, size,
mtime, short excerpt) and `<vault>/Chi-muc-may/.state.json` so the next run only
handles new or changed files. Prints a short Vietnamese summary; prints nothing
when there is nothing new (silent cron tick).
"""
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
import unicodedata
from datetime import datetime
from pathlib import Path

VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH") or "~/Documents/Tro Ly DSNS").expanduser()
CONFIG = VAULT / "nap-may.yaml"
OUT_DIR = VAULT / "Chi-muc-may"
STATE = OUT_DIR / ".state.json"
EXCERPT_CHARS = 300
DEFAULT_DAILY_CAP = 200

# Folder names never entered, wherever they appear.
HARD_DIRS = {
    ".ssh", ".gnupg", ".aws", ".config", ".git", "node_modules", "Library",
    "Keychains", "Photos Library.photoslibrary", "Application Support",
    "System", "Applications", "AppData", ".Trash", "$RECYCLE.BIN",
}
# File-name words that mark personal or financial documents (checked without accents).
HARD_NAME_WORDS = re.compile(
    r"cccd|cmnd|can[-_ ]?cuoc|ho[-_ ]?chieu|passport|sao[-_ ]?ke|statement|"
    r"mat[-_ ]?khau|password|passwd|secret|private|token|hoa[-_ ]?don|invoice|"
    r"bank|ngan[-_ ]?hang|luong|payslip|hop[-_ ]?dong|contract|\.env|id_rsa|\.pem|\.key",
    re.IGNORECASE,
)
TEXT_EXT = {".md", ".txt"}
DOC_EXT = {".docx", ".pdf"}


def strip_accents(s):
    s = unicodedata.normalize("NFD", s).replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def load_config():
    """Minimal parser for the flat nap-may.yaml written by khoi-tao-vault."""
    cfg = {"scan_paths": [], "exclude_globs": [], "max_files_per_day": DEFAULT_DAILY_CAP}
    if not CONFIG.exists():
        return cfg
    key = None
    for raw in CONFIG.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if not line.startswith((" ", "-")) and ":" in line:
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip().strip("\"'")
            if key == "max_files_per_day" and val.isdigit():
                cfg[key] = int(val)
            continue
        item = line.strip()
        if item.startswith("- ") and key in ("scan_paths", "exclude_globs"):
            cfg[key].append(item[2:].strip().strip("\"'"))
    return cfg


def is_excluded(path, user_globs):
    if any(part in HARD_DIRS for part in path.parts):
        return True
    if path.name.startswith("."):
        return True
    if HARD_NAME_WORDS.search(strip_accents(path.name)):
        return True
    return any(fnmatch.fnmatch(str(path), g) or fnmatch.fnmatch(path.name, g) for g in user_globs)


def excerpt(path):
    ext = path.suffix.lower()
    try:
        if ext in TEXT_EXT:
            text = path.read_text(encoding="utf-8", errors="ignore")
        elif ext == ".docx":
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
            text = re.sub(r"<[^>]+>", " ", xml.replace("</w:p>", "\n"))
        elif ext == ".pdf" and shutil.which("pdftotext"):
            text = subprocess.run(
                ["pdftotext", "-l", "2", str(path), "-"],
                capture_output=True, text=True, timeout=30,
            ).stdout
        else:
            return ""
    except Exception:
        return ""
    return re.sub(r"\s+", " ", text).strip()[:EXCERPT_CHARS]


def main():
    cfg = load_config()
    roots = [Path(p).expanduser() for p in cfg["scan_paths"]]
    roots = [r for r in roots if r.is_dir() and r.resolve() != Path.home().resolve()]
    if not roots:
        print("Chưa chọn thư mục nào để nạp. Mở nap-may.yaml trong vault, thêm thư mục dưới scan_paths.")
        return

    state = json.loads(STATE.read_text()) if STATE.exists() else {"seen": {}}
    seen = state["seen"]
    cap = cfg["max_files_per_day"]
    rows, skipped = [], 0
    vault_resolved = VAULT.resolve()

    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            here = Path(dirpath)
            if vault_resolved in (here.resolve(), *here.resolve().parents):
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames if not is_excluded(here / d, cfg["exclude_globs"])]
            for name in filenames:
                p = here / name
                if p.suffix.lower() not in TEXT_EXT | DOC_EXT or is_excluded(p, cfg["exclude_globs"]):
                    continue
                try:
                    st = p.stat()
                except OSError:
                    continue
                key = str(p)
                if seen.get(key) == st.st_mtime:
                    continue
                if len(rows) >= cap:
                    skipped += 1
                    continue
                rows.append({
                    "path": key,
                    "size": st.st_size,
                    "mtime": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
                    "excerpt": excerpt(p),
                })
                seen[key] = st.st_mtime

    if not rows:
        return
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{datetime.now():%Y-%m-%d}.jsonl"
    with out.open("a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    STATE.write_text(json.dumps(state, ensure_ascii=False))
    msg = f"Đã nạp {len(rows)} file mới vào {out.relative_to(VAULT)}."
    if skipped:
        msg += f" Còn {skipped} file, sẽ nạp tiếp lần sau (giới hạn {cap} file/ngày)."
    print(msg)


if __name__ == "__main__":
    sys.exit(main())
