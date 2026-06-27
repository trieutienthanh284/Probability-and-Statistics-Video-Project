from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class HypothesisStep4(TikTokBaseScene):
    def construct(self):
        # 1. Header chính
        self.add_header("BƯỚC 4")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            # ĐÃ FIX: Khôi phục kích thước khung viền tiêu chuẩn ban đầu
            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            # ĐÃ FIX: Neo phụ đề chuẩn buff=1.0
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: BẢNG TÓM TẮT THÔNG SỐ (ĐÃ ĐƯỢC NỚI RỘNG THÔNG THOÁNG)
        # ======================================================================
        # ĐÃ FIX: Tăng width lên 6.4 và height lên 2.4 để rộng rãi hơn
        param_box = RoundedRectangle(corner_radius=0.2, width=6.4, height=2.4, color=GRAY, fill_color=BLACK,
                                     fill_opacity=0.5, stroke_width=2).move_to(UP * 0.4)

        p_title = Text("Hiệu số (Thắng - Thua)", font="Arial", font_size=16, color="#3498db", weight=BOLD).next_to(
            param_box.get_top(), DOWN, buff=0.25)

        p1 = MathTex(r"\bar{x}_d = 2.425", font_size=36)
        p2 = MathTex(r"S_d = 3.311", font_size=36)
        p3 = MathTex(r"n = 287", font_size=36)

        # Sai số chuẩn (SE)
        p4 = MathTex(r"SE = \frac{S_d}{\sqrt{n}} \approx 0.195", font_size=36, color=YELLOW)

        # ĐÃ FIX: Tăng buff=0.8 để giãn khoảng cách 3 thông số
        param_group = VGroup(p1, p2, p3).arrange(RIGHT, buff=0.8).next_to(p_title, DOWN, buff=0.35)
        se_eqn = p4.next_to(param_group, DOWN, buff=0.35)

        full_params = VGroup(param_box, p_title, param_group, se_eqn)

        # ======================================================================
        # PHẦN 2: CÔNG THỨC VÀ BIẾN ĐỔI TOÁN HỌC (TRÊN CÙNG)
        # ======================================================================
        eq_base = MathTex("T", "=", r"\frac{\bar{x}_d}{SE}", font_size=55).move_to(UP * 2.6)
        eq_sub = MathTex("T", "=", r"\frac{2.425}{0.195}", font_size=55).move_to(UP * 2.6)
        eq_result = MathTex("T", "=", "12.41", font_size=70, color=YELLOW).move_to(UP * 2.6)
        result_box = SurroundingRectangle(eq_result, color=YELLOW, buff=0.2, stroke_width=3)

        # ======================================================================
        # PHẦN 3: ĐỒ THỊ T-DISTRIBUTION VÀ VALUE TRACKER (ĐÃ HẠ XUỐNG & GIÃN RA)
        # ======================================================================
        # ĐÃ FIX: Hạ xuống DOWN * 2.5, giãn trục ngang x_length=6.4
        axes = Axes(x_range=[-3, 14, 2], y_range=[0, 0.3, 0.1], x_length=6.4, y_length=1.5,
                    axis_config={"color": GRAY, "stroke_width": 2}).move_to(DOWN * 2.5)

        curve = axes.plot(lambda x: 0.15 * np.exp(-0.25 * x ** 2), color=GRAY, stroke_width=2)

        t_crit = 1.97
        line_crit_l = DashedLine(axes.c2p(-t_crit, 0), axes.c2p(-t_crit, 0.2), color=WHITE, stroke_width=2)
        line_crit_r = DashedLine(axes.c2p(t_crit, 0), axes.c2p(t_crit, 0.2), color=WHITE, stroke_width=2)

        # ĐÃ FIX: Dịch số liệu lên 1 chút (buff=0.1) để không đè vào vạch kẻ
        lbl_crit_l = MathTex("-1.97", font_size=16, color=WHITE).next_to(line_crit_l, UP, buff=0.1)
        lbl_crit_r = MathTex("1.97", font_size=16, color=WHITE).next_to(line_crit_r, UP, buff=0.1)

        reject_zone = Line(axes.c2p(t_crit, 0), axes.c2p(14, 0), color=RED, stroke_width=8).set_opacity(0.8)
        reject_zone_l = Line(axes.c2p(-3, 0), axes.c2p(-t_crit, 0), color=RED, stroke_width=8).set_opacity(0.8)

        # --- SETUP VALUE TRACKER CHO CON TRỎ CHẠY ---
        tracker = ValueTracker(0)

        pointer = Arrow(UP, DOWN, color=WHITE, buff=0).scale(0.6)
        val_label = Text("T = 0.00", font="Arial", font_size=16, color=WHITE, weight=BOLD)
        pointer_group = VGroup(pointer, val_label)

        def update_pointer(mob):
            val = tracker.get_value()
            mob[0].put_start_and_end_on(axes.c2p(val, 0.18), axes.c2p(val, 0.02))
            # Đẩy chữ số lên một khoảng an toàn (buff=0.08)
            mob[1].become(
                Text(f"T = {val:.2f}", font="Arial", font_size=16, color=WHITE, weight=BOLD).next_to(mob[0], UP,
                                                                                                     buff=0.08))

            if val >= t_crit:
                mob[0].set_color(RED)
                mob[1].set_color(RED)
            else:
                mob[0].set_color(WHITE)
                mob[1].set_color(WHITE)

        pointer_group.add_updater(update_pointer)

        # ======================================================================
        # DIỄN HOẠT KHỚP LỜI THOẠI (THỜI GIAN GIỮ NGUYÊN 100%)
        # ======================================================================
        sync_subtitle(
            "Step four: calculate the T-statistic. We find the difference for each match:",
            "Bước bốn: tính T-statistic. Chúng ta tính hiệu số cho mỗi trận:",
            [FadeIn(param_box), Write(p_title)], total_time=4.5
        )

        sync_subtitle(
            "shots on target of the winning team minus the losing team.",
            "số sút trúng đích của đội thắng trừ đội thua.",
            [], total_time=3.0
        )

        sync_subtitle(
            "From 287 clear matches, the mean difference is 2.425,",
            "Từ 287 trận có kết quả rõ ràng, trung bình hiệu số là 2.425,",
            [Write(p1), Write(p3)], total_time=4.0
        )

        sync_subtitle(
            "the standard deviation is 3.311. Sample size n is 287.",
            "độ lệch chuẩn của hiệu số là 3.311. Cỡ mẫu n bằng 287.",
            [Write(p2), FadeIn(se_eqn, shift=UP * 0.2)], total_time=5.0
        )

        sync_subtitle(
            "The T-statistic is calculated by dividing the mean difference by the standard error—",
            "T-statistic tính ra bằng trung bình hiệu chia cho sai số chuẩn —",
            [Write(eq_base)], total_time=4.5
        )

        self.play(ReplacementTransform(eq_base, eq_sub), run_time=0.5)

        sync_subtitle(
            "which is 2.425 divided by 0.195, resulting exactly in 12.41.",
            "bằng 2.425 chia 0.195, ra đúng 12.41.",
            [
                ReplacementTransform(eq_sub, eq_result),
                Create(result_box)
            ], total_time=4.5
        )

        sync_subtitle(
            "Looking at the T-distribution: the critical value at 5% significance level...",
            "Quan sát trên đường phân phối T: giá trị tới hạn ở mức ý nghĩa 5%...",
            [FadeIn(axes), Create(curve)], total_time=4.5
        )

        sync_subtitle(
            "...is plus or minus 1.97.",
            "...là cộng trừ 1.97.",
            [
                Create(line_crit_l), Create(line_crit_r),
                Write(lbl_crit_l), Write(lbl_crit_r),
                Create(reject_zone), Create(reject_zone_l),
                FadeIn(pointer_group)
            ], total_time=3.5
        )

        sync_subtitle(
            "Our T-value is 12.41 — it lies very deep in the rejection region...",
            "Giá trị T của chúng ta là 12.41 — nằm rất sâu trong vùng bác bỏ...",
            [tracker.animate.set_value(12.41)], total_time=4.5
        )

        pointer_group.clear_updaters()

        sync_subtitle(
            "...being more than 10 units away from the critical threshold.",
            "...cách tới hạn tới hơn 10 đơn vị.",
            [
                Indicate(pointer_group, color=RED, scale_factor=1.2),
                Wiggle(result_box)
            ], total_time=4.0
        )

        self.wait(1)