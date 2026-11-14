---
name: nap-may
description: "Nạp tài liệu trong một thư mục người dùng tự chọn vào vault (chỉ mục + trích đoạn ngắn), cập nhật hằng ngày. Dùng khi người dùng nói /nap-may, nạp máy, nạp thư mục tài liệu."
version: 1.0.1
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [vault, local, privacy]
---

# nap-may

Việc quét do script chạy trên máy, không gọi model, không lên mạng: `$HERMES_HOME/scripts/tro-ly-dsns-nap-may.py`. Lịch `nap-may-cap-nhat` chạy script này lúc 6:30 mỗi ngày sau khi người dùng bật lịch.

## Quy tắc cứng
- Chỉ nạp thư mục người dùng tự chọn. Script từ chối thư mục nhà, Documents, Desktop, Downloads và cả ổ đĩa; không tìm cách lách.
- Script luôn bỏ qua thư mục ẩn, `.ssh`, Keychain, `Library`, `AppData`, ảnh, và file có tên chứa CCCD, căn cước, hộ chiếu, sao kê, ngân hàng, hoá đơn, bảng lương, hợp đồng, mật khẩu, token.
- Chỉ đọc trích đoạn trong `Chi-muc-may/*.jsonl`. Không mở toàn văn file gốc trừ khi người dùng hỏi đích danh file đó.

## Các bước
1. Xác định vault theo SOUL.md.
2. Hỏi người dùng thư mục muốn nạp (nếu chưa nói). Gợi ý: tạo riêng thư mục `Documents/Thu vien DSNS`, chép tài liệu muốn trợ lý biết vào đó.
3. Chạy (thay `<thư mục>` bằng đường dẫn tuyệt đối):
   - Mac: `python3 "$HERMES_HOME/scripts/tro-ly-dsns-nap-may.py" --them-thu-muc "<thư mục>"`
   - Windows: `python "$HERMES_HOME/scripts/tro-ly-dsns-nap-may.py" --them-thu-muc "<thư mục>"`
   Người dùng chỉ muốn cập nhật (đã chọn thư mục từ trước): dùng `--chay-ngay` thay cho `--them-thu-muc "<thư mục>"`.
4. Nếu lệnh báo không có Python hoặc bật hộp thoại cài đặt:
   - Mở `<vault>/nap-may.yaml`, thêm dòng `  - "<thư mục>"` ngay dưới dòng `scan_paths:`. Không thêm thư mục bị cấm ở trên.
   - Chạy `hermes cron run dsns-nap-may`. Lịch này dùng Python có sẵn của Hermes; kết quả gửi về Telegram ở lần chạy kế tiếp của bộ lập lịch (trong vòng 1 phút).
5. Báo lại đúng câu script in ra.
6. Muốn tóm tắt: đọc file `Chi-muc-may/<ngày>.jsonl` mới nhất, tóm tắt tối đa 10 file theo tên và trích đoạn, kèm đường dẫn từng file.
7. Nhắc bật lịch `nap-may-cap-nhat` nếu chưa bật.
