#!/usr/bin/env python3
"""Pure fs creator for khoi-tao-vault. No LLM."""
import os, sys
from pathlib import Path
from datetime import datetime

VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH", "~/Documents/Tro Ly DSNS")).expanduser()

STRUCT = ["Inbox", "Ghi-chu", "Nguon", "Voice", "Nhan-Duyen-Qua", "Ban-tin", "Chi-muc-may"]

TEMPLATES = {
    "tac-phong.md": """# tac-phong.md — Xưng hô & giọng văn của Trợ lý DSNS

Mặc định: xưng "anh" / "chị" với user, "em" khi tự xưng (nếu user >40).
Giọng: ấm, mộc mạc, gần gũi như bạn cũ, ngắn gọn, thực tế.
Không sến, không khách sáo, không nói suông.

Ví dụ:
- User: "Chào em"
- Trợ lý: "Chào anh ạ. Hôm nay anh cần em ghi gì vào vault?"

User có thể sửa file này rồi nói "cập nhật tac-phong".
""",
    "nap-may.yaml": """# Thư mục tài liệu muốn trợ lý nạp. Thêm từng dòng bắt đầu bằng "  - ".
# Ví dụ:
#   - "~/Documents/Thu vien DSNS"
# Không đưa cả thư mục nhà (~) hay cả ổ đĩa vào đây.
scan_paths:
# Mẫu tên file muốn bỏ qua thêm (ngoài danh sách luôn bỏ qua có sẵn).
exclude_globs:
  - "*nhap*"
max_files_per_day: 200
""",
    "README.md": """# Tro Ly DSNS — Vault của tôi

Đây là vault Obsidian cho Trợ lý DSNS.

- Ghi-chu/ : ghi nhanh
- Nhan-Duyen-Qua/ : bài học Nhân Duyên Quả (viết đầy đủ)
- Chi-muc-may/ : chỉ mục máy tính (tự động)
- Ban-tin/ : bản tin sáng

Dùng /khoi-tao-vault nếu cần reset cấu trúc.
"""
}

def main():
    VAULT.mkdir(parents=True, exist_ok=True)
    for d in STRUCT:
        (VAULT / d).mkdir(exist_ok=True)
    for name, content in TEMPLATES.items():
        f = VAULT / name
        if not f.exists():
            f.write_text(content, encoding="utf-8")
            print(f"Created {f}")
    print(f"Vault ready at {VAULT}")
    print("Tiếp theo: mở nap-may.yaml để chọn thư mục, hoặc nhắn /nap-may.")

if __name__ == "__main__":
    main()
