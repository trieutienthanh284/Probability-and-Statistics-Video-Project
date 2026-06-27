from manim import *
import random

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene6(Scene):
    def setup(self):
        # 1. Thiết lập nền đen
        self.camera.background_color = BLACK

        # 2. Thiết lập Logo Fami
        logo_path = "video_project/demo/assets/images/fami_hust.png"
        try:
            fami_logo = ImageMobject(logo_path).scale_to_fit_width(1.2)
            fami_logo.to_edge(UP, buff=0.2)
            self.add(fami_logo)
        except:
            pass

        # 3. Dòng chữ chủ đề Video
        topic_title = Text(
            "KIỂM ĐỊNH GIẢ THUYẾT\nCHIẾN THUẬT PRESSING",
            font="Arial",
            font_size=28,
            color=TEAL,
            weight=BOLD
        ).move_to(UP * 5.8)
        self.add(topic_title)

    def create_boxed_subtitle(self, eng_text, vie_text):
        """Hàm tạo phụ đề chuẩn: Có viền và nền đen chống đè chữ"""
        eng_sub = Text(eng_text, font="Arial", font_size=22, color=WHITE)
        vie_sub = Text(vie_text, font="Arial", font_size=18, color=YELLOW)
        sub_group = VGroup(eng_sub, vie_sub).arrange(DOWN, buff=0.15)

        bg_box = BackgroundRectangle(sub_group, color=BLACK, fill_opacity=0.85, buff=0.3)
        sub_box = SurroundingRectangle(sub_group, color=GRAY_A, buff=0.3, stroke_width=2, corner_radius=0.1)

        full_sub = VGroup(bg_box, sub_box, sub_group).move_to(DOWN * 4.5)
        return full_sub

    def construct(self):
        # ==========================================
        # BACKGROUND: CYBER / MATH VIBE + MATRIX HUD
        # ==========================================
        # Lưới tọa độ cyber
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-16, 16, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1.5,
                "stroke_opacity": 0.2
            },
            axis_config={"stroke_width": 0, "stroke_opacity": 0}
        )
        self.add(grid)

        # Hiệu ứng Matrix-like numbers (Các dải số nhị phân mờ ở nền)
        matrix_group = VGroup()
        for i in range(12):
            binary_str = "".join([str(random.randint(0, 1)) for _ in range(25)])
            row = Text(binary_str, font="Monospace", font_size=16, color=TEAL, fill_opacity=0.15)
            row.move_to(UP * (4 - i * 0.7))
            matrix_group.add(row)
        self.play(FadeIn(matrix_group, run_time=2))

        # ==========================================
        # PHẦN 1: CÔNG THỨC T-TEST (Khoảng 8-10s)
        # ==========================================
        # Phụ đề 1
        sub1 = self.create_boxed_subtitle(
            "After performing the two-sample t-test...",
            "Sau khi thực hiện kiểm định t hai mẫu..."
        )
        self.play(FadeIn(sub1))

        # Công thức T-Test
        t_formula = MathTex(
            r"t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}",
            font_size=60, color=WHITE
        ).move_to(UP * 1.5)

        # HUD overlay (Khung quét phân tích)
        hud_box = SurroundingRectangle(t_formula, color=TEAL, buff=0.5, stroke_width=1, stroke_opacity=0.5)
        hud_lines = VGroup(
            Line(hud_box.get_corner(UL), hud_box.get_corner(UL) + RIGHT * 0.5 + DOWN * 0.5, color=TEAL),
            Line(hud_box.get_corner(DR), hud_box.get_corner(DR) + LEFT * 0.5 + UP * 0.5, color=TEAL)
        )

        self.play(Write(t_formula), Create(hud_box), Create(hud_lines), run_time=2.5)
        self.wait(3.5)

        # ==========================================
        # PHẦN 2: DIGITAL CALCULATION VÀ P-VALUE (Khoảng 8s)
        # ==========================================
        # Digital Calculation Effect (Số chạy phân tích)
        calc_tracker = ValueTracker(1.0000)
        calc_number = DecimalNumber(1.0000, num_decimal_places=4, font_size=50, color=YELLOW)
        calc_number.add_updater(lambda m: m.set_value(calc_tracker.get_value()).next_to(t_formula, DOWN, buff=1))

        calc_label = Text("Calculating p-value...", font="Monospace", font_size=18, color=TEAL).next_to(calc_number,
                                                                                                        DOWN, buff=0.2)

        self.play(FadeIn(calc_number), FadeIn(calc_label))
        self.play(calc_tracker.animate.set_value(0.0001), run_time=2, rate_func=linear)
        self.wait(0.5)

        # Phụ đề 2
        sub2 = self.create_boxed_subtitle(
            "We obtain a p-value of less than 0.001.",
            "Ta thu được p-value nhỏ hơn 0.001."
        )

        # Biến đổi thành p-value chốt
        calc_number.clear_updaters()
        p_value_tex = MathTex(r"p < 0.001", font_size=65, color=WHITE).move_to(DOWN * 0.5)

        self.play(
            ReplacementTransform(sub1, sub2),
            FadeOut(t_formula), FadeOut(hud_box), FadeOut(hud_lines), FadeOut(calc_label),
            ReplacementTransform(calc_number, p_value_tex),
            run_time=2
        )
        self.wait(4)

        # ==========================================
        # PHẦN 3: CAMERA ZOOM VÀ RED GLOW (Khoảng 5s)
        # ==========================================
        # Phụ đề 3
        sub3 = self.create_boxed_subtitle(
            "Which means...",
            "Điều này có nghĩa..."
        )
        self.play(ReplacementTransform(sub2, sub3))

        # Hiệu ứng phóng to (Zoom) và đổi màu đỏ sáng
        red_glow = p_value_tex.copy().set_color(RED).set_stroke(RED, width=15, opacity=0.6)

        self.play(
            p_value_tex.animate.scale(1.5).set_color(RED).move_to(UP * 0.5),
            FadeIn(red_glow),
            run_time=2.5,
            rate_func=smooth
        )
        # Giữ hiệu ứng sáng bám theo chữ
        red_glow.add_updater(lambda m: m.move_to(p_value_tex.get_center()).scale_to_fit_height(p_value_tex.height))
        self.wait(1.5)

        # ==========================================
        # PHẦN 4: CHỐT HẠ THÔNG ĐIỆP (Khoảng 8-10s)
        # ==========================================
        # Phụ đề 4 (Ngắt dòng cẩn thận để không tràn viền)
        sub4 = self.create_boxed_subtitle(
            "The probability of this difference occurring\nby chance is extremely low.",
            "Xác suất để sự khác biệt này xảy ra do\nngẫu nhiên là cực kỳ thấp."
        )

        self.play(ReplacementTransform(sub3, sub4))

        # Hiệu ứng nhịp đập (Pulse) cho p-value để giữ sự chú ý trong lúc đọc thoại dài
        self.play(p_value_tex.animate.scale(1.1), run_time=1.5, rate_func=there_and_back)
        self.play(p_value_tex.animate.scale(1.1), run_time=1.5, rate_func=there_and_back)
        self.play(p_value_tex.animate.scale(1.1), run_time=1.5, rate_func=there_and_back)

        self.wait(2.5)

        # Dọn dẹp scene
        red_glow.clear_updaters()
        self.play(*(map(FadeOut, self.mobjects)))