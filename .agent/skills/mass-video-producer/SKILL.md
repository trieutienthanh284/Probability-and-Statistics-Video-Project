---
name: script-bank-producer
description: Chỉ sinh ngân hàng kịch bản (script) theo cấu trúc chuẩn 7 phần. Không tạo video, không visual, không audio, không MP4. Output duy nhất là file script_bank.json
---

# Script Bank Producer - Chỉ sinh kịch bản

## Khi nào dùng
Bất kỳ yêu cầu nào chứa "ngân hàng kịch bản", "script bank", "chỉ script", "json script".

## Quy trình bắt buộc (chỉ làm phần này)
1. Đọc tất cả topic từ scriptwriting/topic.txt
2. Với mỗi topic:
   - Sử dụng prompt từ prompt.txt
   - Sinh script theo đúng 7 phần:
     - Câu dẫn nhập
     - Tình huống dẫn nhập
     - Mô tả bài toán/vấn đề cần giải quyết
     - Diễn giải/Minh họa
     - Tổng kết kiến thức liên quan
     - Tóm tắt từ khóa
     - Gợi ý tiếp theo
   - Lưu vào cấu trúc JSON
3. Sau khi xong tất cả → ghi đè file `script_bank.json` ở thư mục gốc workspace (chứa mảng JSON của tất cả kịch bản).
4. Báo danh sách topic đã sinh và đường dẫn file JSON.

## Prompt mặc định (sẽ được dùng)
Xem file prompt.txt (đã được cập nhật theo cấu trúc mới).

## Output
Chỉ tạo file: **script_bank.json** (không tạo thư mục visual, output_videos, không chạy moviepy, gtts).

## Sau khi xong
Hiển thị nội dung 2-3 kịch bản đầu tiên trong chat và đường dẫn file JSON.