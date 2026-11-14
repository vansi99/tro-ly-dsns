---
name: nap-may
description: "Nạp tài liệu trong các thư mục người dùng tự chọn vào vault (chỉ mục + trích đoạn ngắn). Dùng khi người dùng nói /nap-may, nạp máy, quét thư mục, cập nhật tài liệu trong máy."
version: 1.0.0
author: DSNS Workshop
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [vault, local, privacy]
---

# nap-may: nạp tài liệu trong máy vào vault

Việc quét do script chạy trên máy, không gọi model, không lên mạng:
`$HERMES_HOME/scripts/tro-ly-dsns-nap-may.py`. Lịch tự động `nap-may-cap-nhat` chạy script này lúc 6:30 mỗi ngày (sau khi người dùng bật lịch).

## Quy tắc cứng
- Chỉ quét các thư mục có trong `scan_paths` của `nap-may.yaml` ở gốc vault. Danh sách trống thì không quét gì.
- Không bao giờ đề nghị đưa cả thư mục nhà (`~`), ổ đĩa, `Library`, `AppData` vào `scan_paths`.
- Script luôn bỏ qua: thư mục ẩn, `.ssh`, Keychain, `Library`, ảnh, và file có tên chứa CCCD, căn cước, hộ chiếu, sao kê, ngân hàng, hoá đơn, lương, hợp đồng, mật khẩu, token. Không tìm cách vượt qua danh sách này.
- Chỉ đọc trích đoạn trong `Chi-muc-may/*.jsonl`. Không mở toàn văn file gốc trừ khi người dùng hỏi đích danh file đó.

## Các bước
1. Đọc `nap-may.yaml` trong vault. Nếu `scan_paths` trống: hỏi người dùng muốn nạp thư mục tài liệu nào (ví dụ `~/Documents/Thu vien DSNS`), giải thích ngắn danh sách bị bỏ qua, rồi ghi thư mục họ chọn vào `scan_paths`.
2. Chạy: `python3 "$HERMES_HOME/scripts/tro-ly-dsns-nap-may.py"` (Windows: `python`).
3. Báo lại đúng câu script in ra. Nếu script không in gì: "Không có file mới kể từ lần nạp trước."
4. Nếu người dùng muốn tóm tắt: đọc file `Chi-muc-may/<ngày>.jsonl` mới nhất, tóm tắt tối đa 10 file theo tên và trích đoạn, kèm đường dẫn từng file.
5. Nhắc bật lịch tự động nếu chưa bật: trong Hermes Desktop vào mục lịch tự động, bật `nap-may-cap-nhat`.
