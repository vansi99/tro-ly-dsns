---
name: ghi-voice
description: "Xử lý voice note: STT local (nếu có), ghi transcript + file gốc vào Voice/. Dùng obsidian."
version: 1.0.0
---
# ghi-voice

User gửi voice note trên Telegram.

1. Nhận audio, chạy STT local nếu cấu hình (voice.stt.local).
2. Ghi transcript vào Voice/voice-YYYY-MM-DD.md
3. Lưu file audio gốc (nếu gateway hỗ trợ).
4. Trả lời: "Đã ghi voice vào Voice/..."
