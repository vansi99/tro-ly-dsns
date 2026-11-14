---
name: nap-nhan-duyen-qua
description: "Nạp bài Nhân Duyên Quả người dùng gửi vào thư mục Nhan-Duyen-Qua của vault, và soạn nháp bài chia sẻ dựa trên các bài đã nạp. Dùng khi người dùng gửi file kèm /nap-nhan-duyen-qua, nói nạp bài Nhân Duyên Quả, hoặc nhờ soạn bài chia sẻ."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, nhan-duyen-qua]
---

# nap-nhan-duyen-qua

Luôn viết đầy đủ "Nhân Duyên Quả".

## Nạp bài
1. Xác định vault theo SOUL.md. Lấy ngày hôm nay.
2. Lấy nội dung chữ của file người dùng gửi (Hermes đã lưu file đính kèm và đưa đường dẫn cho em). File `.md`/`.txt`: đọc trực tiếp. File `.docx`/`.pdf`: dùng công cụ đọc tài liệu có sẵn; không đọc được thì báo người dùng gửi lại dạng chữ hoặc dán nội dung.
3. Ghi `<vault>/Nhan-Duyen-Qua/<tên-bài-không-dấu>.md`:
   ```
   # <tên bài>
   - Nạp ngày: <YYYY-MM-DD>
   - File gốc: <tên file người dùng gửi>

   <toàn văn nội dung chữ, giữ nguyên>
   ```
   Không tóm tắt thay toàn văn, không sửa câu chữ của bài.
4. Trả lời: "Đã nạp bài <tên bài> vào Nhan-Duyen-Qua/<tên file>."

## Soạn nháp bài chia sẻ
1. Chỉ dùng nội dung trong các file `Nhan-Duyen-Qua/*.md`. Không gán thêm ý ngoài bài cho tác giả. Không có bài phù hợp thì nói "Không có trong vault."
2. Viết theo giọng trong tac-phong.md (thường xưng "mình", gọi "anh chị em"). Độ dài theo yêu cầu của người dùng; không nói thì 150–250 chữ. Đếm lại số chữ trước khi trả lời.
3. Trả lời đúng khung sau, không bỏ dòng nào:
   ```
   <bài chia sẻ>

   Nguồn: <đường dẫn từng bài Nhân Duyên Quả đã dùng>
   Có sự hỗ trợ của AI, cần người duyệt trước khi đăng.
   ```
4. Kiểm tra lần cuối: câu trả lời phải có dòng "Có sự hỗ trợ của AI, cần người duyệt trước khi đăng." Thiếu thì thêm vào.
5. Không gửi bài đi đâu. Hỏi người dùng có muốn lưu nháp vào `Ghi-chu/` không.
