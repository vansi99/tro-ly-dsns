---
name: ghi-lai
description: "Ghi nhanh điều người dùng nói vào ghi chú trong vault. Dùng khi người dùng nhắn ghi lại:, nhớ giúp:, lưu note."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, note]
---

# ghi-lai

1. Xác định vault theo SOUL.md.
2. Lấy ngày giờ hiện tại bằng lệnh `date "+%Y-%m-%d %H:%M"` (Windows: `powershell -c "Get-Date -Format 'yyyy-MM-dd HH:mm'"`).
3. Ghi vào `<vault>/Ghi-chu/<YYYY-MM-DD>.md`. File chưa có thì tạo với dòng đầu `# Ghi chú ngày <YYYY-MM-DD>`. File đã có thì thêm xuống cuối, không xoá nội dung cũ.
4. Mỗi mục có dạng:
   ```
   ## <HH:MM>
   <nguyên văn điều người dùng muốn ghi, bỏ chữ "ghi lại:">
   ```
5. Không sửa ý, không thêm ý của mình. Nếu nội dung có CCCD, số tài khoản, mật khẩu thì không ghi phần đó và nhắc người dùng.
6. Trả lời: "Đã ghi vào Ghi-chu/<YYYY-MM-DD>.md."
