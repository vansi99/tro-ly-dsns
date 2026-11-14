---
name: luu-link
description: "Lưu một đường link vào vault kèm tóm tắt ngắn lấy từ chính trang đó. Dùng khi người dùng gửi link, lưu link, bookmark."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, web]
---

# luu-link

1. Xác định vault theo SOUL.md. Lấy ngày hôm nay (YYYY-MM-DD).
2. Đọc trang bằng công cụ web (web_extract). Chỉ tóm tắt từ nội dung thật đọc được.
3. Ghi `<vault>/Nguon/<YYYY-MM-DD>-<tên-ngắn-không-dấu>.md`:
   ```
   # <tiêu đề trang>
   - Link: <URL đầy đủ, giữ nguyên>
   - Ngày lưu: <YYYY-MM-DD>
   - Người dùng ghi chú: <lời người dùng nhắn kèm, nếu có>

   ## Tóm tắt
   - 3 đến 5 gạch đầu dòng, mỗi dòng là ý có trong trang
   ```
4. Nếu không đọc được trang: vẫn lưu URL, phần Tóm tắt ghi đúng câu "Chưa đọc được nội dung trang." Không đoán nội dung.
5. Trả lời: tóm tắt 2 dòng + "Đã lưu vào Nguon/<tên file>."
