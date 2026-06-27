from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class FootballDataReality(TikTokBaseScene):
    def construct(self):
        # 1. Header chính của phân cảnh
        self.add_header("DỮ LIỆU NGOẠI HẠNG ANH")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
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
        # PHẦN 1: THIẾT LẬP BIỂU ĐỒ CỘT THỦ CÔNG (Đã hạ thấp & kéo giãn số liệu)
        # ======================================================================
        # Đẩy tiêu đề biểu đồ xuống để không chạm vào Header
        chart_title = Text("Kết quả 380 trận Premier League 24-25", font="Arial", font_size=16, color=GRAY,
                           weight=BOLD).move_to(UP * 2.6)

        # Dời toàn bộ hệ trục xuống dưới (base_y = -0.2)
        base_y = -0.2
        baseline = Line(LEFT * 2.8, RIGHT * 2.8, color=GRAY, stroke_width=3).move_to(UP * base_y)

        # Thu nhỏ tỷ lệ chiều cao một chút để gọn gàng hơn
        h_scale = 0.05

        bar1 = Rectangle(width=0.9, height=40.8 * h_scale, fill_color="#1DD1A1", fill_opacity=0.9, stroke_width=1.5,
                         stroke_color=WHITE).move_to([-1.8, base_y + (40.8 * h_scale) / 2, 0])
        bar2 = Rectangle(width=0.9, height=24.5 * h_scale, fill_color="#54A0FF", fill_opacity=0.9, stroke_width=1.5,
                         stroke_color=WHITE).move_to([0, base_y + (24.5 * h_scale) / 2, 0])
        bar3 = Rectangle(width=0.9, height=34.7 * h_scale, fill_color="#FF4B4B", fill_opacity=0.9, stroke_width=1.5,
                         stroke_color=WHITE).move_to([1.8, base_y + (34.7 * h_scale) / 2, 0])

        # Nhãn trục hoành
        lbl1 = Text("Đội nhà", font="Arial", font_size=15, color=WHITE, weight=BOLD).next_to(bar1, DOWN, buff=0.2)
        lbl2 = Text("Hòa", font="Arial", font_size=15, color=WHITE, weight=BOLD).next_to(bar2, DOWN, buff=0.2)
        lbl3 = Text("Đội khách", font="Arial", font_size=15, color=WHITE, weight=BOLD).next_to(bar3, DOWN, buff=0.2)

        # Số liệu hiển thị (Kéo giãn buff=0.35 để không đè lên viền cột)
        val1 = Text("155 trận\n(40.8%)", font="Arial", font_size=13, color=WHITE, weight=BOLD).next_to(bar1, UP,
                                                                                                       buff=0.35)
        val2 = Text("93 trận\n(24.5%)", font="Arial", font_size=13, color=WHITE, weight=BOLD).next_to(bar2, UP,
                                                                                                      buff=0.35)
        val3 = Text("132 trận\n(34.7%)", font="Arial", font_size=13, color=WHITE, weight=BOLD).next_to(bar3, UP,
                                                                                                       buff=0.35)

        chart_group = Group(bar1, bar2, bar3, lbl1, lbl2, lbl3, val1, val2, val3)

        # ======================================================================
        # PHẦN 2: THIẾT LẬP THẺ BẢNG SỐ LIỆU TÌNH TRẠNG SÚT BÓNG (xSOG)
        # ======================================================================
        # Đẩy bảng xuống vị trí an toàn (DOWN * 2.0)
        table_box = RoundedRectangle(corner_radius=0.15, width=6.2, height=1.6, color=GRAY, stroke_width=2,
                                     fill_opacity=0.15, fill_color=BLACK).move_to(DOWN * 2.0)
        table_title = Text("Số cú sút trúng đích trung bình/trận", font="Arial", font_size=15, color=GRAY,
                           weight=BOLD).next_to(table_box, UP, buff=0.2)

        col1 = VGroup(
            Text("Đội chiến thắng:", font="Arial", font_size=16, color=WHITE),
            Text("Đội thất bại:", font="Arial", font_size=16, color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        val_win = Text("5.84", font="Arial", font_size=20, color=GREEN, weight=BOLD)
        val_lose = Text("3.42", font="Arial", font_size=20, color=RED, weight=BOLD)
        col2 = VGroup(val_win, val_lose).arrange(DOWN, buff=0.25, aligned_edge=RIGHT)

        table_content = Group(col1, col2).arrange(RIGHT, buff=1.2).move_to(table_box.get_center())
        full_table = Group(table_box, table_title, table_content)

        # ======================================================================
        # DIỄN HOẠT ĐỒNG BỘ THEO TIẾN TRÌNH LỜI THOẠI
        # ======================================================================

        sync_subtitle(
            "First, let's look at the data of 380 Premier League matches.",
            "Trước tiên, hãy nhìn vào dữ liệu của 380 trận Ngoại hạng Anh.",
            [FadeIn(chart_title), Create(baseline)], total_time=3.0
        )

        sync_subtitle(
            "Home teams win 40.8%, draws are 24.5%, and away teams win 34.7%.",
            "Đội nhà thắng 40.8% số trận, hòa 24.5%, và đội khách thắng 34.7%.",
            [FadeIn(chart_group, shift=UP * 0.3)], total_time=4.5
        )

        sync_subtitle(
            "Interestingly, the home advantage is no longer as dominant as traditionally.",
            "Điều thú vị: lợi thế sân nhà không còn quá áp đảo như truyền thống.",
            [Indicate(bar1, color="#1DD1A1"), Indicate(val1, color="#1DD1A1")], total_time=3.5
        )

        sync_subtitle(
            "Now, let's look at our main metric: shots on target.",
            "Bây giờ, hãy nhìn vào số liệu chúng ta quan tâm: số cú sút trúng đích.",
            [FadeIn(table_box), FadeIn(table_title), FadeIn(col1)], total_time=3.5
        )

        self.play(FadeIn(col2, shift=LEFT * 0.2), run_time=0.5)

        self.play(Indicate(val_win, color=GREEN, scale_factor=1.2), run_time=1.5)
        self.play(Indicate(val_lose, color=RED, scale_factor=1.2), run_time=1.5)

        sync_subtitle(
            "Winners average 5.84 shots on target per match, while losers only have 3.42.",
            "Trung bình, đội thắng có 5.84 cú sút trúng đích, còn đội thua chỉ có 3.42.",
            [], total_time=1.5
        )

        sync_subtitle(
            "But is this 2.4 shot difference statistically significant, or just a fluke?",
            "Nhưng chênh lệch 2.4 cú sút này — liệu có ý nghĩa thống kê, hay chỉ là may rủi?",
            [Circumscribe(table_box, color=YELLOW, time_width=2.0)], total_time=4.5
        )

        self.wait(1)