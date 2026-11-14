---
name: ban-tin-sang
description: "Soạn bản tin sáng từ ghi chú, voice, link và bài Nhân Duyên Quả mới trong 24 giờ qua, lưu vào Ban-tin/. Dùng khi người dùng nhắn /ban-tin-sang hoặc khi lịch 7:00 chạy."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, cron]
---

# ban-tin-sang

1. Xác định vault theo SOUL.md. Lấy ngày hôm nay (YYYY-MM-DD). Đọc `<vault>/tac-phong.md`.
2. Tìm file mới hoặc vừa sửa trong 24 giờ qua:
   - Mac: `find "<vault>" -name "*.md" -newermt "-24 hours" -not -path "*/Ban-tin/*"`
   - Windows: `powershell -c "Get-ChildItem -Path '<vault>' -Recurse -Filter *.md | Where-Object { $_.LastWriteTime -gt (Get-Date).AddHours(-24) -and $_.FullName -notmatch 'Ban-tin' } | ForEach-Object FullName"`
   Thêm file `Chi-muc-may/<hôm nay>.jsonl` nếu có.
3. Không có file nào: khi chạy theo lịch thì trả lời đúng `[SILENT]`; khi người dùng tự gọi thì báo "Hôm qua chưa có ghi chú mới."
4. Có file: đọc và soạn bản tin 5–8 dòng theo giọng trong tac-phong.md:
   - việc sắp tới (lịch, hẹn có trong ghi chú);
   - ý chính đã ghi, link đã lưu;
   - tài liệu mới nạp;
   mỗi dòng kèm đường dẫn note nguồn. Không thêm việc không có trong ghi chú.
5. Ghi bản tin vào `<vault>/Ban-tin/<YYYY-MM-DD>.md` (đã có thì ghi đè bằng bản mới).
6. Trả lời bằng nội dung bản tin + dòng cuối "Đã lưu Ban-tin/<YYYY-MM-DD>.md".
