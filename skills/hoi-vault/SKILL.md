---
name: hoi-vault
description: "Trả lời câu hỏi chỉ dựa trên ghi chú và tài liệu trong vault, kèm đường dẫn; không thấy thì nói Không có trong vault. Dùng khi người dùng hỏi mình đã ghi gì, tìm trong ghi chú, tuần này có việc gì, bài Nhân Duyên Quả nói gì."
version: 1.0.1
metadata:
  hermes:
    tags: [vault, search]
---

# hoi-vault

1. Xác định vault theo SOUL.md.
2. Tìm từ khoá chính của câu hỏi (thử cả có dấu và không dấu) trong:
   - mọi file `*.md` dưới vault;
   - các file `Chi-muc-may/*.jsonl` (chỉ mục tài liệu trong máy; mỗi dòng có `path` và `excerpt`).
   Lệnh gợi ý: `grep -ril "<từ khoá>" "<vault>" --include="*.md" --include="*.jsonl"`.
3. Đọc các file khớp. Chỉ dùng nội dung có thật trong đó.
4. Trả lời ngắn, mỗi ý kèm nguồn, ví dụ: "Thứ 7 họp nhóm lúc 8h (Ghi-chu/2026-11-16.md)." Với kết quả từ chỉ mục máy, ghi đường dẫn file gốc trong trường `path`.
5. Không tìm thấy: trả lời đúng câu "Không có trong vault." và gợi ý "Anh/chị có thể nhắn: ghi lại: ..."
