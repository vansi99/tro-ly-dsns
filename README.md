# Trợ lý DSNS — Trợ lý AI riêng trên Telegram (v1.0.0)

Trợ lý ấm, mộc mạc dành cho cộng đồng ĐSNS (người 35-65 tuổi, không cần biết code). Dùng Hermes + Telegram + vault Obsidian.

## Cài đặt nhanh (học viên)

### Cách 1: Từ GitHub (khuyến nghị)
```bash
hermes profile install github.com/vansi99/tro-ly-dsns --name tro-ly-dsns --alias
```

### Cách 2: File .tar.gz (bàn giao trực tiếp)
1. Nhận file `tro-ly-dsns.tar.gz`
2. Mở Hermes Desktop → ⌘K → "Import profile…" (Windows: Ctrl+K) chọn file
   hoặc CLI: `hermes profile import tro-ly-dsns.tar.gz --name tro-ly-dsns`

Sau khi import:
- Tạo profile `tro-ly-dsns`
- Tạo file `.env` từ `.env.EXAMPLE`

## 3 thứ BẮT BUỘC phải điền (trong ~/.hermes/profiles/tro-ly-dsns/.env)

```
OPENCODE_ZEN_API_KEY=sk-...          # Lấy từ opencode.ai/zen (miễn phí)
TELEGRAM_BOT_TOKEN=123456:ABC...     # Tạo bot tại @BotFather
TELEGRAM_ALLOWED_USERS=123456789     # User ID của bạn (dùng @userinfobot)
OBSIDIAN_VAULT_PATH=~/Documents/Tro Ly DSNS   # tuỳ chọn, có default
```

## Bật gateway Telegram (sau khi điền token)
```bash
tro-ly-dsns gateway start
# hoặc trong Desktop: Messaging → Telegram → Start gateway
```
Sau đó nhắn bot `/sethome` để bản tin sáng gửi về đúng khung chat này.

## Bật cron jobs (bản tin sáng & nap máy)
```bash
tro-ly-dsns cron list          # thấy 2 job đang paused
tro-ly-dsns cron resume dsns-ban-tin-sang
tro-ly-dsns cron resume dsns-nap-may
```

## Lệnh chính cho học viên (gõ trong Telegram hoặc chat)

- `/khoi-tao-vault` — tạo cấu trúc vault mẫu (Inbox, Ghi-chu, Nhan-Duyen-Qua, ...)
- `ghi lại: ...` — ghi nhanh nội dung vào Ghi-chu/
- `hỏi ...` hoặc `tìm trong vault ...` — hỏi dựa trên vault (chỉ trả lời nếu có thật)
- `lưu link https://...` — lưu link + tóm tắt vào Nguon/
- Gửi voice note — tự STT + ghi vào Voice/
- `/ban-tin-sang` — chạy thủ công bản tin sáng
- `/tac-phong` — chỉnh xưng hô/giọng văn (sửa file tac-phong.md)
- `/nap-nhan-duyen-qua` — nạp file bài Nhân Duyên Quả (hoặc đặt file vào thư mục)
- `/nap-may` — quét thư mục máy (chỉ file mới, loại trừ an toàn), cập nhật chỉ mục

## Cấu trúc vault mẫu (tạo bởi /khoi-tao-vault)

```
Tro Ly DSNS/
├── Inbox/
├── Ghi-chu/
├── Nguon/
├── Voice/
├── Nhan-Duyen-Qua/          ← ghi đầy đủ "Nhân Duyên Quả", không viết tắt
├── Ban-tin/
├── Chi-muc-may/
├── tac-phong.md             ← chỉnh xưng hô ở đây
├── nap-may.yaml             ← cấu hình loại trừ + thư mục quét
└── README.md
```

## Lưu ý an toàn quan trọng

- Vault, chỉ mục và voice note nằm trên **máy bạn**. Voice được chép lời ngay trên máy.
- Nội dung bạn nhắn bot và đoạn ghi chú bot đọc để trả lời **được gửi tới model trên OpenCode Zen**. Các model mặc định có chính sách không lưu và không dùng để huấn luyện, nhưng vẫn đừng gửi CCCD, số tài khoản, mật khẩu.
- Bot chỉ trả lời user ID trong `TELEGRAM_ALLOWED_USERS`.
- Cron jobs được cài **paused**, bạn phải tự bật sau khi xem.
- `/nap-may` chỉ quét thư mục bạn tự chọn, luôn bỏ qua giấy tờ cá nhân và thư mục hệ thống.
- "Không có trong vault" là câu trả lời trung thực khi không tìm thấy.

## Cập nhật distribution sau này

```bash
hermes profile update tro-ly-dsns   # khi cài từ GitHub; giữ nguyên ghi chú, phiên chat và khoá
```
Cài bằng file `.tar.gz` thì nhận file mới từ BTC và import lại; vault nằm ngoài profile nên không mất ghi chú.

---

Workshop "Trợ lý AI riêng trên Telegram" • Chủ nhật 15/11 và 22/11/2026 • Cộng đồng ĐSNS

## Đổi model (sau khi import)

Mặc định distribution dùng `glm-5.3-flash-free` (0đ zero-retention).

```bash
tro-ly-dsns config set model.default deepseek-v4.1-flash-free
tro-ly-dsns config set model.provider opencode-zen
```

Hoặc edit ~/.hermes/profiles/tro-ly-dsns/config.yaml .
