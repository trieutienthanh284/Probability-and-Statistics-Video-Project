import json
import pandas as pd
import os

json_file = "script_bank.json"
excel_file = "script_bank_new.xlsx"  # Tên file mới để tránh ghi đè cũ

print(f"Đang đọc file JSON mới: {json_file}")

if not os.path.exists(json_file):
    print(f"Lỗi: Không tìm thấy {json_file}")
else:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Chuyển thành DataFrame với đúng 10 cột
    columns = [
        "topic", "cau_dan_nhap", "mo_ta_minh_hoa_dan_nhap", "tinh_huong_dan_nhap",
        "mo_phong_tinh_huong", "mo_ta_bai_toan", "minh_hoa_bai_toan",
        "dien_giai_minh_hoa", "mo_phong_tinh_toan", "tong_ket_kien_thuc",
        "tom_tat_tu_khoa", "goi_y_tiep_theo"
    ]

    df = pd.DataFrame(data)

    # Nếu tom_tat_tu_khoa là list → nối thành chuỗi
    if 'tom_tat_tu_khoa' in df.columns:
        df['tom_tat_tu_khoa'] = df['tom_tat_tu_khoa'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    # Xuất ra Excel với tên mới
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Đã xuất thành công file Excel mới: {excel_file}")
    print(f"File nằm tại: {os.path.abspath(excel_file)}")
    print("Upload lên Google Drive và mở bằng Google Sheets để xem bảng đẹp!")