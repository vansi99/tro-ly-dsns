---
name: khoi-tao-vault
description: "Khởi tạo cấu trúc vault mẫu cho Trợ lý DSNS: Inbox, Ghi-chu, Nhan-Duyen-Qua, Voice, Ban-tin, Chi-muc-may, tac-phong.md, nap-may.yaml, README. An toàn, không ghi đè nếu đã có."
version: 1.0.0
author: DSNS
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [vault, setup, obsidian, dsns]
---

# khoi-tao-vault

Dùng khi user nói: `/khoi-tao-vault`, "khởi tạo vault", "tạo cấu trúc", "setup vault lần đầu".

Kỹ năng này tạo cây thư mục + file mẫu tối thiểu để các skill khác hoạt động ngay.

Cấu trúc tạo:
- Inbox/
- Ghi-chu/
- Nguon/
- Voice/
- Nhan-Duyen-Qua/
- Ban-tin/
- Chi-muc-may/
- tac-phong.md (mẫu xưng hô)
- nap-may.yaml (cấu hình quét an toàn)
- README.md (hướng dẫn ngắn)

Luôn kiểm tra OBSIDIAN_VAULT_PATH trước khi tạo. Không ghi đè file người dùng đã có nội dung.
Sau khi chạy xong, hướng dẫn user điền tac-phong.md và chạy /nap-may lần đầu.
