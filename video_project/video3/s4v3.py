from base_scene import TikTokBaseScene
from manim import *


class TheoryToReality(TikTokBaseScene):
    def construct(self):
        # 1. Header phân đoạn
        self.add_header("ỨNG DỤNG THỰC TẾ")

        asset_path = "video_project/video3/assets/"

        # ======================================================================
        # CẢNH 1: QUYỂN SÁCH & LỜI THOẠI LÝ THUYẾT
        # ======================================================================
        try:
            book = ImageMobject(asset_path + "book.png")
            book.scale_to_fit_height(3.0)
            book.move_to(ORIGIN)  # Đặt chính giữa màn hình

            self.play(FadeIn(book, scale=0.5, shift=UP * 0.3), run_time=1)

            self.play_subtitle(
                "This rule might seem to exist only in textbooks...",
                "Đây là quy luật tưởng chừng chỉ tồn tại trong sách giáo trình…",
                duration=4
            )

            # Hiệu ứng quyển sách mờ đi để chuyển sang thực tế
            self.play(FadeOut(book, scale=1.5), run_time=0.8)
        except Exception as e:
            print("Lỗi tải book.png:", e)

        # ======================================================================
        # CẢNH 2: NGÀNH BẢO HIỂM & 4 LOGO
        # ======================================================================

        # Chữ "Ngành Bảo hiểm !!!" - To, đậm, màu xanh ngọc
        insurance_title = Text("Ngành Bảo hiểm !!!", font="Arial", font_size=55, color="#00FFFF", weight=BOLD)
        insurance_title.move_to(UP * 2.5)  # Đặt cao bên dưới Header

        self.play_subtitle(
            "but in fact, it operates a multi-trillion dollar industry:",
            "nhưng thực ra, nó đang vận hành cả một ngành công nghiệp...",
            duration=3
        )

        self.play(Write(insurance_title), run_time=1)

        # Chuẩn bị 4 ảnh bảo hiểm
        try:
            # Load 4 ảnh
            img1 = ImageMobject(asset_path + "health.png").scale_to_fit_height(1.8)
            img2 = ImageMobject(asset_path + "life-insurance.png").scale_to_fit_height(1.8)
            img3 = ImageMobject(asset_path + "insurance.png").scale_to_fit_height(1.8)
            img4 = ImageMobject(asset_path + "insurance-company.png").scale_to_fit_height(1.8)

            # Sắp xếp theo dạng lưới 2x2 để không bị đè lên nhau
            # Hàng 1
            img1.move_to(LEFT * 1.8 + UP * 0.5)
            img2.move_to(RIGHT * 1.8 + UP * 0.5)
            # Hàng 2
            img3.move_to(LEFT * 1.8 + DOWN * 1.8)
            img4.move_to(RIGHT * 1.8 + DOWN * 1.8)

            # Tạo Group để quản lý (Tránh lỗi vGroup nếu bạn muốn thao tác chung)
            insurance_logos = Group(img1, img2, img3, img4)

            # Hiện từng ảnh từ từ (one by one)
            for logo in insurance_logos:
                self.play(FadeIn(logo, scale=1.2), run_time=0.6)
                self.wait(0.2)

        except Exception as e:
            print("Lỗi tải các file ảnh bảo hiểm:", e)

        self.play_subtitle(
            "worth trillions of dollars every year: the Insurance industry.",
            "trị giá hàng nghìn tỷ đô la mỗi năm: ngành Bảo hiểm.",
            duration=4
        )

        self.wait(2)