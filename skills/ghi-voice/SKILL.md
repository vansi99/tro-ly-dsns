---
name: ghi-voice
description: "Lưu lời chép của voice note vào vault. Dùng khi người dùng gửi voice note hoặc tin nhắn thoại."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, voice]
---

# ghi-voice

Hermes đã tự chép lời voice note trên máy trước khi tin đến em (em nhận được phần chữ và đường dẫn file âm thanh).

1. Xác định vault theo SOUL.md. Lấy ngày giờ hiện tại.
2. Thêm vào cuối `<vault>/Voice/<YYYY-MM-DD>.md` (chưa có thì tạo, dòng đầu `# Voice note ngày <YYYY-MM-DD>`):
   ```
   ## <HH:MM>
   <phần chữ đã chép, giữ nguyên>
   - File âm thanh: <đường dẫn, nếu có>
   ```
3. Nếu phần chữ rỗng hoặc vô nghĩa: báo "Em chưa nghe rõ, anh/chị gửi lại giúp em nhé." và không ghi.
4. Nếu voice có ý "ghi lại" hay câu hỏi, làm tiếp theo skill ghi-lai hoặc hoi-vault.
5. Trả lời: một câu tóm ý + "Đã ghi vào Voice/<YYYY-MM-DD>.md."
