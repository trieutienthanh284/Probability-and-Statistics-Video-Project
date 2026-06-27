from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class HypothesisTestingSteps(TikTokBaseScene):
    def construct(self):
        # 1. Header chính của phân cảnh
        self.add_header("QUY TRÌNH KIỂM ĐỊNH")

        asset_path = "video_project/video3/assets/"

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

            # ĐÃ SỬA: Đẩy sub lên vị trí tiêu chuẩn ban đầu (buff=1.0)
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # THIẾT LẬP CẤU TRÚC 5 BƯỚC FLOWCHART DỌC
        # ======================================================================
        def create_step_node(color_theme, step_num_str, title_str, icon_mobject):
            bg = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.75,
                                  fill_color=color_theme, fill_opacity=0.15,
                                  stroke_color=color_theme, stroke_width=2)

            step_lbl = Text(step_num_str + ": ", font="Arial", font_size=15, color=color_theme, weight=BOLD)
            title_lbl = Text(title_str, font="Arial", font_size=15, color=WHITE)
            text_g = VGroup(step_lbl, title_lbl).arrange(RIGHT, buff=0.08)

            icon_mobject.scale_to_fit_height(0.35).set_color(color_theme)
            content = Group(icon_mobject, text_g).arrange(RIGHT, buff=0.25).move_to(bg.get_center())

            return Group(bg, content)

        icon1 = VGroup(Text("?", font="Arial", font_size=20), Text("!", font="Arial", font_size=20)).arrange(RIGHT,
                                                                                                             buff=0.1)
        icon2 = MathTex("T", font_size=24)
        icon3 = MathTex(r"\alpha", font_size=24)
        icon4 = MathTex(r"\sum", font_size=22)
        icon5 = Text("OK", font="Arial", font_size=15, weight=BOLD)

        step1 = create_step_node("#FF7675", "Bước 1", "Phát biểu hai giả thuyết (H0 & H1)", icon1)
        step2 = create_step_node("#74B9FF", "Bước 2", "Chọn phép kiểm định phù hợp", icon2)
        step3 = create_step_node("#A29BFE", "Bước 3", "Đặt mức ý nghĩa Alpha (Thường 5%)", icon3)
        step4 = create_step_node("#FAB1A0", "Bước 4", "Tính giá trị thống kê kiểm định", icon4)
        step5 = create_step_node("#55E6C1", "Bước 5", "So sánh ngưỡng & Đưa ra kết luận", icon5)

        # Đ_ LỢI DỤNG TOÀN BỘ KHÔNG GIAN: Hạ flowchart xuống UP * 0.3 để giảm khoảng trống đen phía dưới
        flowchart = Group(step1, step2, step3, step4, step5).arrange(DOWN, buff=0.22).move_to(UP * 0.3)

        # Tự động kết nối mũi tên theo tọa độ mới của các khối
        arrows = VGroup()
        for i in range(4):
            arr = Arrow(start=flowchart[i].get_bottom(), end=flowchart[i + 1].get_top(),
                        buff=0.04, color=GRAY, stroke_width=3, max_tip_length_to_length_ratio=0.2)
            arrows.add(arr)

        # ======================================================================
        # DIỄN HOẠT ĐỒNG BỘ THEO NHỊP ĐỌC CỦA LỜI THOẠI
        # ======================================================================
        sync_subtitle(
            "The hypothesis testing process consists of 5 standard steps.",
            "Quy trình kiểm định giả thuyết gồm 5 bước chuẩn mực.",
            [], total_time=3.5
        )

        sync_subtitle(
            "Step one: state two hypotheses—the null and the alternative hypothesis.",
            "Bước một: phát biểu hai giả thuyết — giả thuyết không và giả thuyết thay thế.",
            [FadeIn(step1, shift=DOWN * 0.2)], total_time=5.0
        )

        sync_subtitle(
            "Step two: choose the appropriate test for data type and research question.",
            "Bước hai: chọn phép kiểm định phù hợp với loại dữ liệu và câu hỏi.",
            [Create(arrows[0]), FadeIn(step2, shift=DOWN * 0.2)], total_time=5.0
        )

        sync_subtitle(
            "Step three: set the alpha significance level, usually 5%.",
            "Bước ba: đặt mức ý nghĩa alpha, thường là 5%.",
            [Create(arrows[1]), FadeIn(step3, shift=DOWN * 0.2)], total_time=3.5
        )

        sync_subtitle(
            "Step four: calculate the test statistic value from the data.",
            "Bước bốn: tính giá trị thống kê kiểm định từ dữ liệu.",
            [Create(arrows[2]), FadeIn(step4, shift=DOWN * 0.2)], total_time=4.0
        )

        sync_subtitle(
            "Step five: compare with the critical threshold and make conclusion.",
            "Bước năm: so sánh với ngưỡng tới hạn rồi đưa ra kết luận.",
            [Create(arrows[3]), FadeIn(step5, shift=DOWN * 0.2)], total_time=4.5
        )

        self.play(flowchart.animate.scale(1.03), run_time=0.4)
        self.play(flowchart.animate.scale(1 / 1.03), run_time=0.4)

        sync_subtitle(
            "Now let's apply each step to our Premier League problem.",
            "Bây giờ hãy áp dụng từng bước vào bài toán Premier League của chúng ta.",
            [flowchart.animate.set_opacity(0.4)], total_time=4.0
        )

        self.wait(1)