---
name: mass-video-producer
description: Tự động sản xuất hàng loạt video về ứng dụng xác suất thống kê trong kinh tế & quản lý
---

# Khi nào kích hoạt
Bất kỳ yêu cầu nào chứa "produce", "generate", "tạo", "batch video", "xác suất thống kê kinh tế"

# Quy trình bắt buộc (thực hiện tuần tự)
1. Đọc/ tạo topic từ scriptwriting/topic.txt (nếu rỗng → tự sinh 10–20 topic liên quan xác suất/thống kê kinh tế/quản lý)
2. Với mỗi topic:
   - Sinh script Markdown 5–7 phút (dùng prompt từ prompt.txt hoặc mặc định)
   - Lưu: scriptwriting/raw_script/{slug}.md
   - Sinh visual (matplotlib biểu đồ, histogram, regression...)
   - Lưu: visual/{slug}/
   - Sinh audio (gTTS, ưu tiên tiếng Việt)
   - Ghép MP4 bằng moviepy → output_videos/{slug}.mp4
3. Cập nhật aggregated_scripts.xlsx
4. Báo cáo danh sách video + đường dẫn

# Prompt mặc định nếu không có file
"Bạn là MC video giáo dục tiếng Việt. Viết script YouTube 5-7 phút về: {topic}. Lĩnh vực: Ứng dụng xác suất thống kê trong kinh tế - quản lý. Cấu trúc: Hook 15s + Tiêu đề + Lý thuyết đơn giản + Ví dụ thực tế VN/quốc tế + Tính toán minh họa + Kết luận + CTA. Giọng gần gũi."

# Thư viện cần (agent tự install nếu thiếu)
google-generativeai matplotlib numpy moviepy gtts pandas openpyxl