from base_scene import TikTokBaseScene
from manim import *


class LLNSummary(TikTokBaseScene):
    def construct(self):
        # 1. Header phân đoạn
        self.add_header("TỔNG KẾT KIẾN THỨC")

        asset_path = "video_project/video3/assets/"

        # --- Helper: Phụ đề chống tràn ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: 3 Ý CHÍNH (Với Icon và Text 2 dòng)
        # ======================================================================

        # Hàm tạo một mục danh sách gọn gàng (Đã thêm in lỗi chi tiết)
        def create_bullet(icon_name, title_str, desc_str):
            try:
                icon = ImageMobject(asset_path + icon_name).scale_to_fit_height(0.6)
            except Exception as e:
                # In thẳng lỗi thật ra Terminal để bắt bệnh thay vì giấu đi
                print(f"\n[LỖI QUAN TRỌNG] Không thể nạp ảnh {icon_name}. Chi tiết lỗi: {e}\n")
                icon = Circle(radius=0.3, color=WHITE, fill_opacity=0.5)  # Fallback

            title = Text(title_str, font="Arial", font_size=20, color=WHITE, weight=BOLD)
            desc = Text(desc_str, font="Arial", font_size=16, color=LIGHT_GREY)
            text_group = VGroup(title, desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

            return Group(icon, text_group).arrange(RIGHT, buff=0.3)

        # 3 Mục tóm tắt (Sử dụng đúng tên ảnh của bạn)
        bullet1 = create_bullet("histogram.png", "1. Hội tụ về giá trị kỳ vọng:",
                                "TB mẫu lớn tiến gần đến kỳ vọng lý thuyết.")
        bullet2 = create_bullet("parallel.png", "2. Điều kiện bắt buộc:",
                                "Các quan sát phải độc lập và cùng phân phối.")
        bullet3 = create_bullet("safety.png", "3. Gộp rủi ro (Risk Pooling):",
                                "Biến rủi ro cá nhân thành tổng thể dự đoán được.")

        # Sắp xếp dọc và căn lề trái
        bullet2.next_to(bullet1, DOWN, buff=0.5).align_to(bullet1, LEFT)
        bullet3.next_to(bullet2, DOWN, buff=0.5).align_to(bullet1, LEFT)

        # Đặt khối này ở nửa trên màn hình
        summary_group = Group(bullet1, bullet2, bullet3).move_to(UP * 1.8 + RIGHT * 0.2)

        # ======================================================================
        # PHẦN 2: WORD CLOUD (CÁC TỪ KHÓA QUAN TRỌNG)
        # ======================================================================

        # Hàm tạo "chip" (viên nhộng từ khóa)
        def create_chip(text_str, bg_color, f_size=20):
            t = Text(text_str, font="Arial", font_size=f_size, color=WHITE, weight=BOLD)
            bg = RoundedRectangle(
                corner_radius=0.25, width=t.width + 0.6, height=t.height + 0.35,
                fill_color=bg_color, fill_opacity=0.9, stroke_width=1, stroke_color=WHITE
            )
            return VGroup(bg, t)

        # Tạo các từ khóa
        chip1 = create_chip("Luật số lớn", BLUE, 26)
        chip2 = create_chip("Giá trị kỳ vọng", ORANGE, 22)
        chip3 = create_chip("Biến độc lập – cùng phân phối", PURPLE, 20)
        chip4 = create_chip("Gộp rủi ro", GREEN, 24)
        chip5 = create_chip("Phí bảo hiểm", TEAL, 22)

        # Xếp thành đám mây (3 hàng) để nằm gọn nửa dưới màn hình
        row1 = VGroup(chip1, chip2).arrange(RIGHT, buff=0.3)
        row2 = VGroup(chip3)
        row3 = VGroup(chip4, chip5).arrange(RIGHT, buff=0.3)

        cloud = VGroup(row1, row2, row3).arrange(DOWN, buff=0.3).move_to(DOWN * 1.5)

        # ======================================================================
        # DIỄN HOẠT THEO LỜI THOẠI
        # ======================================================================

        # Mở bài
        sync_subtitle("Let's summarize three main points.", "Tổng kết lại ba ý chính.", [], total_time=2.5)

        # Ý 1
        sync_subtitle(
            "One: The Law of Large Numbers shows that the average of a large sample",
            "Một: Luật số lớn cho biết trung bình của một mẫu lớn các quan sát độc lập",
            [FadeIn(bullet1, shift=RIGHT * 0.5)], total_time=4.0
        )
        sync_subtitle(
            "will approach the theoretical expected value.",
            "sẽ tiến gần đến giá trị kỳ vọng lý thuyết.",
            [], total_time=2.5
        )

        # Ý 2
        sync_subtitle(
            "Two: The strict condition is that observations must be independent",
            "Hai: điều kiện bắt buộc là các quan sát phải độc lập",
            [FadeIn(bullet2, shift=RIGHT * 0.5)], total_time=3.5
        )
        sync_subtitle(
            "and identically distributed.",
            "và cùng phân phối xác suất.",
            [], total_time=2.5
        )

        # Ý 3
        sync_subtitle(
            "Three: In insurance, the risk pooling principle",
            "Ba: trong ngành bảo hiểm, nguyên lý gộp rủi ro — risk pooling —",
            [FadeIn(bullet3, shift=RIGHT * 0.5)], total_time=3.5
        )
        sync_subtitle(
            "relies on the LLN to turn unpredictable individual risks",
            "dựa trên Luật số lớn để biến rủi ro cá nhân không đoán được",
            [], total_time=3.5
        )
        sync_subtitle(
            "into a predictable aggregate number to price premiums.",
            "thành con số tổng thể dự đoán được, từ đó định giá phí bảo hiểm.",
            [], total_time=4.0
        )

        # Nhóm từ khóa
        sync_subtitle(
            "Some key terms you should remember:",
            "Một số từ khóa quan trọng bạn nên ghi nhớ:",
            [], total_time=3.0
        )

        # Hiện từng hàng của Word Cloud
        sync_subtitle(
            "Law of Large Numbers, Expected Value,",
            "Luật số lớn, Giá trị kỳ vọng,",
            [FadeIn(row1, shift=UP * 0.2, scale=0.8)], total_time=3.0
        )
        sync_subtitle(
            "Independent and Identically Distributed,",
            "Biến độc lập – cùng phân phối,",
            [FadeIn(row2, shift=UP * 0.2, scale=0.8)], total_time=3.0
        )
        sync_subtitle(
            "Risk Pooling, Insurance Premium.",
            "Gộp rủi ro, Phí bảo hiểm.",
            [FadeIn(row3, shift=UP * 0.2, scale=0.8)], total_time=3.5
        )

        # Đẩy sáng nhẹ toàn bộ Word Cloud
        self.play(cloud.animate.scale(1.05), run_time=1.0)
        self.play(cloud.animate.scale(1 / 1.05), run_time=1.0)

        self.wait(2)