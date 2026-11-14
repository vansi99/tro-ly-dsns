#!/usr/bin/env python3
"""Create the vault folders and copy templates. Never overwrites existing files. No LLM."""
import os
import shutil
from pathlib import Path

VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH") or "~/Documents/Tro Ly DSNS").expanduser()
TEMPLATES = Path(__file__).resolve().parent.parent / "templates"
FOLDERS = ["Inbox", "Ghi-chu", "Nguon", "Voice", "Nhan-Duyen-Qua", "Ban-tin", "Chi-muc-may"]


def main():
    for d in FOLDERS:
        (VAULT / d).mkdir(parents=True, exist_ok=True)
    created = []
    for src in sorted(TEMPLATES.iterdir()):
        dst = VAULT / src.name
        if not dst.exists():
            shutil.copyfile(src, dst)
            created.append(src.name)
    print(f"Vault sẵn sàng tại: {VAULT}")
    print("Đã tạo: " + (", ".join(created) if created else "không có file mới (đã có từ trước)"))


if __name__ == "__main__":
    main()
