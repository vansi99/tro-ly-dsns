---
name: khoi-tao-vault
description: "Tạo vault ghi chú lần đầu: các thư mục Inbox, Ghi-chu, Nguon, Voice, Nhan-Duyen-Qua, Ban-tin, Chi-muc-may và file tac-phong.md, nap-may.yaml, README.md. Không ghi đè file đã có. Dùng khi người dùng nói /khoi-tao-vault, khởi tạo vault, tạo sổ ghi chú."
version: 1.0.1
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [vault, setup]
---

# khoi-tao-vault

1. Xác định vault theo SOUL.md (biến `OBSIDIAN_VAULT_PATH`, trống thì `~/Documents/Tro Ly DSNS`).
2. Thử chạy script:
   - Mac: `python3 "${HERMES_SKILL_DIR}/scripts/create-vault.py"`
   - Windows: `python "${HERMES_SKILL_DIR}/scripts/create-vault.py"`
3. Nếu lệnh báo không có Python hoặc bật hộp thoại cài đặt: không chờ, làm bằng công cụ file. Với mỗi file trong `${HERMES_SKILL_DIR}/templates/` (tac-phong.md, nap-may.yaml, README.md), đọc nội dung rồi ghi sang gốc vault **chỉ khi file đó chưa có**. Tạo thêm file trống `.giu-cho` trong mỗi thư mục Inbox, Ghi-chu, Nguon, Voice, Nhan-Duyen-Qua, Ban-tin, Chi-muc-may.
4. Báo lại đường dẫn vault và các file vừa tạo.
5. Hướng dẫn tiếp: "Anh/chị nhắn /tac-phong để em biết cách xưng hô, và /sethome để nhận bản tin sáng ở khung chat này."
