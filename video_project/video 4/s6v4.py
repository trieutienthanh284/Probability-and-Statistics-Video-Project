from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class HypothesisStep23(TikTokBaseScene):
    def construct(self):
        # 1. Header chính
        self.add_header("BƯỚC 2 & 3")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa chiều rộng ---
        # Chức năng: Rút gọn caption và container gọn hơn
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            # Khóa giới hạn chiều rộng hẹp hơn ban đầu để nhường chỗ
            max_width = 6.6
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)

            # Container nhỏ gọn hơn buff=0.6, buff=0.4
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.5, height=g.height + 0.3, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            full_sub = VGroup(bg, g).to_edge(DOWN, buff=0.4)  # buff=0.4 neo sát đáy an toàn

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: BƯỚC 2 - PAIRED DATA (DỮ LIỆU GHÉP ĐÔI) Ở NỬA TRÊN
        # ======================================================================
        dot_w = VGroup(*[Dot(color="#3498db", radius=0.12) for _ in range(3)]).arrange(DOWN, buff=0.4)
        dot_l = VGroup(*[Dot(color="#e74c3c", radius=0.12) for _ in range(3)]).arrange(DOWN, buff=0.4)
        dot_l.next_to(dot_w, RIGHT, buff=1.8)

        lines = VGroup(
            *[DashedLine(dot_w[i].get_right(), dot_l[i].get_left(), color=GRAY, dash_length=0.1) for i in range(3)])

        lbl_w = Text("Đội thắng", font="Arial", font_size=15, color="#3498db", weight=BOLD).next_to(dot_w, UP, buff=0.2)
        lbl_l = Text("Đội thua", font="Arial", font_size=15, color="#e74c3c", weight=BOLD).next_to(dot_l, UP, buff=0.2)
        match_lbls = VGroup(
            *[Text(f"Trận {i + 1}", font="Arial", font_size=11, color=GRAY).next_to(lines[i], UP, buff=0.08) for i in
              range(3)])

        # Đẩy paired_group lên cao UP * 2.2 để trống không gian bụng video
        paired_group = VGroup(dot_w, dot_l, lines, lbl_w, lbl_l, match_lbls).move_to(UP * 2.2 + LEFT * 1.5)

        ttest_txt = Text("Paired T-test", font="Arial", font_size=20, color=WHITE, weight=BOLD)
        ttest_bg = RoundedRectangle(corner_radius=0.15, width=ttest_txt.width + 0.8, height=ttest_txt.height + 0.5,
                                    fill_color="#1DD1A1", fill_opacity=0.9, stroke_width=2, stroke_color=WHITE)
        ttest_badge = VGroup(ttest_bg, ttest_txt).next_to(paired_group, RIGHT, buff=1.0)

        arrow_to_badge = Arrow(start=paired_group.get_right() + RIGHT * 0.1, end=ttest_badge.get_left() + LEFT * 0.1,
                               color=WHITE, stroke_width=4, buff=0)

        # ======================================================================
        # PHẦN 2: BƯỚC 3 - ĐẠI TU BIỂU ĐỒ T-DIST & VÙNG BÁC BỎ ALPHA
        # (NỚI RỘNG, KÉO XUỐNG, TÁCH TEXT RA NGOÀI)
        # ======================================================================
        # Đ_ ĐÃ SỬA:
        # 1. Kéo xuống UP * 2.6 -> DOWN * 2.6.
        # 2. Giãn ra: Tăng x_length=6.6, giảm y_length=1.4 để flatten và spread.
        # 3. y_range giảm đỉnh xuống 0.25 để cong dẹt hơn.
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 0.25, 0.05], x_length=6.6, y_length=1.4,
                    axis_config={"color": GRAY, "stroke_width": 2}).move_to(DOWN * 2.6)

        # Công thức cong Gauss phẳng và dẹt hơn (0.2 * np.exp(-0.15)) để spread
        curve = axes.plot(lambda x: 0.15 * np.exp(-0.25 * x ** 2), color=YELLOW, stroke_width=3)

        # Shading regions with clear critical value boundary at x=±1.96
        critical_val = 1.96
        left_tail = axes.get_area(curve, x_range=[-4, -critical_val], color="#FF4B4B", opacity=0.8)
        right_tail = axes.get_area(curve, x_range=[critical_val, 4], color="#FF4B4B", opacity=0.8)

        line_l = DashedLine(axes.c2p(-critical_val, 0), axes.c2p(-critical_val, 0.2), color=WHITE, stroke_width=2.5)
        line_r = DashedLine(axes.c2p(critical_val, 0), axes.c2p(critical_val, 0.2), color=WHITE, stroke_width=2.5)

        # Đ_ ĐÃ SỬA: Tách Text và Mũi tên không cho đè. Đặt Text ra ngoài.
        # Neo một điểm trên cao để làm điểm xuất phát cho mũi tên
        arrow_origin = axes.c2p(0, 0.45)

        lbl_alpha = MathTex(r"\alpha = 0.05", font_size=28, color=WHITE).next_to(arrow_origin, UP, buff=0.2)

        # Tách con số ra khỏi biểu đồ, đặt hoàn toàn ra ngoài 2 bên.
        lbl_tail_l = MathTex(r"2.5\%", font_size=18, color="#FF4B4B").move_to(axes.c2p(-3.6, 0.12))
        lbl_tail_r = MathTex(r"2.5\%", font_size=18, color="#FF4B4B").move_to(axes.c2p(3.6, 0.12))

        # Vẽ mũi tên cong trỏ rõ ràng và sạch sẽ vào vùng shading
        arrow_l = CurvedArrow(start_point=axes.c2p(-1.0, 0.35), end_point=axes.c2p(-2.8, 0.05), color=RED,
                              angle=-TAU / 4)
        arrow_r = CurvedArrow(start_point=axes.c2p(1.0, 0.35), end_point=axes.c2p(2.8, 0.05), color=RED, angle=TAU / 4)

        # Vùng chú thích bác bỏ tách ra xa khỏi số liệu
        reject_lbl1 = Text("Vùng bác bỏ H0", font="Arial", font_size=12, color="#FF4B4B", weight=BOLD).next_to(
            lbl_tail_l, DOWN, buff=0.15)
        reject_lbl2 = Text("Vùng bác bỏ H0", font="Arial", font_size=12, color="#FF4B4B", weight=BOLD).next_to(
            lbl_tail_r, DOWN, buff=0.15)

        # ======================================================================
        # DIỄN HOẠT KHỚP LỜI THOẠI VÀ CHỈNH SỬA TEXT (RÚT GỌN)
        # ======================================================================
        # Lời thoại 1: Giới thiệu Bước 2 (D dữ liệu ghép đôi)
        sync_subtitle(
            "Step two: choose the test. We have paired match data:",
            "Bước hai: chọn phép kiểm định. Ta có cặp dữ liệu ghép đôi:",
            [
                FadeIn(lbl_w, lbl_l),
                LaggedStart(*[FadeIn(d) for d in dot_w], lag_ratio=0.1),
                LaggedStart(*[FadeIn(d) for d in dot_l], lag_ratio=0.1)
            ], total_time=5.0
        )

        # Lời thoại 2: Chốt Paired T-test
        sync_subtitle(
            "one winner and one loser per match—we use the Paired T-test.",
            "cùng trận, một đội thắng và một thua — ta dùng Paired T-test.",
            [
                LaggedStart(*[Create(line) for line in lines], lag_ratio=0.1),
                FadeIn(match_lbls),
                Create(arrow_to_badge),
                GrowFromCenter(ttest_badge)
            ], total_time=5.5
        )

        # Lời thoại 3 & 4 (RÚT GỌN CHỮ VÀ DÍCH CHART XUỐNG DƯỚI)
        sync_subtitle(
            "Step three: alpha level to 0.05.",
            "Bước ba: đặt mức ý nghĩa alpha bằng 0.05,",
            [FadeIn(axes), Create(curve), Write(lbl_alpha)], total_time=3.5
        )

        sync_subtitle(
            "which sets a 5% maximum chance of error in rejection.",
            "tức là chấp nhận sai lầm tối đa 5% khi bác bỏ.",
            [Circumscribe(lbl_alpha, color=YELLOW, time_width=2.0)], total_time=5.5
        )

        # Lời thoại 5 & 6 (DỮ LIỆU THÔNG THOÁNG TUYỆT ĐỐI KHÔNG ĐÈ NHAU)
        sync_subtitle(
            "Two red regions are rejection areas —",
            "Vùng màu đỏ hai đuôi này là vùng bác bỏ —",
            [
                Create(line_l), Create(line_r),
                FadeIn(left_tail, right_tail),
                Write(lbl_tail_l), Write(lbl_tail_r),
                Create(arrow_l), Create(arrow_r),
                FadeIn(reject_lbl1, reject_lbl2)
            ], total_time=4.5
        )

        sync_subtitle(
            "if T-value is in here, the difference is real.",
            "nếu giá trị T ở đây, ta đủ bằng chứng chênh lệch là thực.",
            [
                Indicate(left_tail, color=RED, scale_factor=1.1),
                Indicate(right_tail, color=RED, scale_factor=1.1)
            ], total_time=6.0
        )

        self.wait(1)