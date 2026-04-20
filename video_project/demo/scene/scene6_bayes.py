from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ExplanationScene(Scene):
    def construct(self):
        # ── SETTINGS ──
        logo_pos = UP * 6
        sub_pos = DOWN * 4.2
        eq_pos = DOWN * 1.5  # Vị trí cố định để hiện các dòng tính toán

        # ── LOGO ──
        logo = ImageMobject("video_project/demo/assets/images/fami.png").scale(0.3).move_to(logo_pos)
        self.add(logo)

        # ── HÀM TẠO SUBTITLE CÓ KHUNG VIỀN (ĐÃ CẬP NHẬT) ──
        def create_dual_sub(en, vi):
            max_w = config.frame_width - 1.5

            en_text = Paragraph(
                en, font="Arial", font_size=22, weight=BOLD,
                alignment="center", width=max_w
            ).set_color(WHITE)

            vi_text = Paragraph(
                vi, font="Arial", font_size=18,
                alignment="center", width=max_w
            ).set_color(YELLOW)

            # Gom nhóm chữ
            text_group = VGroup(en_text, vi_text).arrange(DOWN, buff=0.15)

            # Tạo khung viền bao quanh chữ
            frame = SurroundingRectangle(
                text_group,
                color=WHITE,
                buff=0.3,
                stroke_width=2,
                corner_radius=0.1
            )

            # Tạo lớp nền đen mờ
            background = BackgroundRectangle(
                frame,
                color=BLACK,
                fill_opacity=0.6,  # Tăng nhẹ độ đậm để tách khỏi 100 icons
                buff=0
            )

            # Gộp tất cả và đặt vào vị trí
            full_sub = VGroup(background, frame, text_group).move_to(sub_pos)
            full_sub.set_z_index(100)

            return full_sub

        # ── GRID 100 ICONS ──
        icon_path = "video_project/demo/assets/icons/man.png"
        people = Group()
        icon_scale = 0.08
        spacing_x = 0.5
        spacing_y = 0.45

        for i in range(100):
            p = ImageMobject(icon_path).scale(icon_scale)
            row = i // 10
            col = i % 10
            p.move_to(UP * (4.5 - row * spacing_y) + LEFT * (2.25 - col * spacing_x))
            people.add(p)

        self.play(FadeIn(people), run_time=1.5)

        # =========================
        # CÁC GIAI ĐOẠN TÍNH TOÁN
        # =========================

        # 1. PRIOR (Xác suất ban đầu)
        sub1 = create_dual_sub("Assume 30% are Good and 70% are Average candidates.",
                               "Giả sử 30% ứng viên Giỏi và 70% ứng viên Trung bình.")
        eq1 = VGroup(
            MathTex(r"P(\text{Good}) = 0.3", font_size=32),
            MathTex(r"P(\text{Avg}) = 0.7", font_size=32)
        ).arrange(DOWN).move_to(eq_pos)

        self.play(FadeIn(sub1), Write(eq1))
        self.play(
            people[:30].animate.set_color(GREEN),
            people[30:].animate.set_color(ORANGE),
            run_time=1
        )
        self.wait(2)
        self.play(FadeOut(eq1), run_time=0.25)

        # 2. GOOD PASS (Giỏi vượt qua)
        sub2 = create_dual_sub("Probability of a Good candidate passing all 3 rounds.",
                               "Xác suất ứng viên Giỏi vượt qua cả 3 vòng.")
        eq2 = MathTex(r"P(\text{Pass 3} \mid \text{Good}) = 0.8 \times 0.85 \times 0.9 = 0.612", font_size=32,
                      color=BLUE).move_to(eq_pos)

        self.play(ReplacementTransform(sub1, sub2), Write(eq2))
        self.play(people[:18].animate.set_color(BLUE), run_time=1)
        self.wait(2)
        self.play(FadeOut(eq2), run_time=0.25)

        # 3. AVG PASS (Trung bình vượt qua)
        sub3 = create_dual_sub("Probability of an Average candidate passing 3 rounds.",
                               "Xác suất ứng viên Trung bình vượt qua 3 vòng.")
        eq3 = MathTex(r"P(\text{Pass 3} \mid \text{Avg}) = 0.5 \times 0.4 \times 0.3 = 0.06", font_size=32,
                      color=RED).move_to(eq_pos)

        self.play(ReplacementTransform(sub2, sub3), Write(eq3))
        self.play(people[30:34].animate.set_color(RED), run_time=1)
        self.wait(2)
        self.play(FadeOut(eq3), run_time=0.25)

        # 4. TOTAL & BAYES (Xác suất toàn phần & Bayes)
        sub4 = create_dual_sub("Using Bayes' theorem to find actual Good candidates.",
                               "Dùng Bayes tính xác suất thực sự Giỏi khi đã đỗ.")
        eq4 = VGroup(
            MathTex(r"P(\text{Pass 3}) = 0.2256", font_size=32, color=YELLOW),
            MathTex(r"P(\text{Good} \mid \text{Pass}) = \frac{0.612 \times 0.3}{0.2256} = 0.814", font_size=32,
                    color=PURPLE)
        ).arrange(DOWN).move_to(eq_pos)

        self.play(ReplacementTransform(sub3, sub4), Write(eq4))
        self.wait(3)
        self.play(FadeOut(eq4), run_time=0.25)

        # 5. EXPECTATION (Kỳ vọng)
        sub5 = create_dual_sub("Expected value E > 0: The decision is to HIRE ALL.",
                               "Kỳ vọng E > 0: Quyết định là TUYỂN TẤT CẢ.")
        eq5 = VGroup(
            MathTex(r"E = 0.814 \times 800 + 0.186 \times (-300) = 595.4", font_size=34),
            Text("DECISION: HIRE ALL", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.4).move_to(eq_pos)

        self.play(ReplacementTransform(sub4, sub5), Write(eq5))
        self.wait(4)

        # OUTRO
        self.play(FadeOut(Group(*[m for m in self.mobjects if m != logo])))