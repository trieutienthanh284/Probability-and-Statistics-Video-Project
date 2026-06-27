from base_scene import TikTokBaseScene
from manim import *


class InsuranceFormula(TikTokBaseScene):
    def construct(self):
        # 1. Header phân đoạn
        self.add_header("ỨNG DỤNG THỰC TẾ")

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
        # PHẦN 1: THIẾT LẬP CÁC ĐỐI TƯỢNG (Để không bị đè lên nhau)
        # ======================================================================

        # --- Giải nghĩa biến (Nằm ngay dưới Header một chút) ---
        var_n = Text("N: Số lượng khách hàng", font="Arial", font_size=20, color=GRAY)
        var_p = Text("p: Xác suất rủi ro", font="Arial", font_size=20, color=GRAY)
        var_c = Text("c: Chi phí bồi thường TB", font="Arial", font_size=20, color=GRAY)
        var_group = VGroup(var_n, var_p, var_c).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        var_group.move_to(UP * 0.5)

        # --- Công thức 1: Tổng chi phí (Nằm cao nhất) ---
        t_tong = Text("Tổng chi phí", font="Arial", font_size=30, color=WHITE)
        eq1 = MathTex("=", font_size=40)
        n_sym = MathTex("N", font_size=40, color=WHITE)
        times1 = MathTex(r"\times", font_size=40)
        p_sym1 = MathTex("p", font_size=40, color="#00FFFF")
        times2 = MathTex(r"\times", font_size=40)
        c_sym1 = MathTex("c", font_size=40, color=GREEN)
        f1 = VGroup(t_tong, eq1, n_sym, times1, p_sym1, times2, c_sym1).arrange(RIGHT, buff=0.2).move_to(UP * 2.0)

        # --- Công thức 2: Phí rủi ro (Nằm dưới giải nghĩa biến) ---
        t_phi_rr1 = Text("Phí rủi ro", font="Arial", font_size=30, color="#00FFFF")
        eq2 = MathTex("=", font_size=40)
        p_sym2 = MathTex("p", font_size=40, color="#00FFFF")
        times3 = MathTex(r"\times", font_size=40)
        c_sym2 = MathTex("c", font_size=40, color=GREEN)
        f2 = VGroup(t_phi_rr1, eq2, p_sym2, times3, c_sym2).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        # --- Công thức 3: Phí thực tế (Nằm dưới cùng) ---
        t_phi_tt = Text("Phí thực tế", font="Arial", font_size=30, color=YELLOW)
        eq3 = MathTex("=", font_size=40)
        t_phi_rr2 = Text("Phí rủi ro", font="Arial", font_size=30, color="#00FFFF")
        plus = MathTex("+", font_size=40)
        t_margin = Text("Margin", font="Arial", font_size=30, color=YELLOW)
        f3 = VGroup(t_phi_tt, eq3, t_phi_rr2, plus, t_margin).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.2)

        # ======================================================================
        # DIỄN HOẠT (ANIMATION) KHỚP VỚI LỜI THOẠI MỚI
        # ======================================================================

        # 1. Công thức 1
        sync_subtitle(
            "The company calculates: Total expected cost",
            "Từ đó, công ty có thể tính: tổng chi phí dự kiến phải chi trả",
            [Write(f1)], total_time=3.5
        )

        sync_subtitle(
            "equals customers times probability times average cost.",
            "bằng số khách hàng nhân xác suất nhân chi phí trung bình.",
            [FadeIn(var_group, shift=UP * 0.2)], total_time=4.0
        )

        # 2. Công thức 2
        sync_subtitle(
            "Dividing by customers, we get the basic risk premium",
            "Chia cho số khách hàng, ta được phần phí rủi ro cơ bản",
            [TransformMatchingShapes(f1.copy(), f2)], total_time=3.5
        )

        sync_subtitle(
            "(also known as the expected risk premium value).",
            "(hay còn gọi là giá trị phí rủi ro kỳ vọng).",
            [Indicate(f2[0], color="#00FFFF")], total_time=3.0
        )

        # 3. Công thức 3
        sync_subtitle(
            "By adding a margin - for operations, reserves, and profit -",
            "Cộng thêm một khoản margin - vận hành, dự phòng và lợi nhuận -",
            [TransformMatchingShapes(f2.copy(), f3)], total_time=4.0
        )

        sync_subtitle(
            "we have the actual premium on the contract.",
            "ta có mức phí bảo hiểm thực tế trên hợp đồng.",
            [f3.animate.set_color(YELLOW)], total_time=3.5
        )

        # Chốt hạ bằng hiệu ứng nhấn mạnh
        self.play(Circumscribe(f3, color=YELLOW, time_width=2))
        self.wait(1.5)