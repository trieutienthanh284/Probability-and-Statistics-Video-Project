from manim import *

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene4(Scene):
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
        """Hàm tạo phụ đề chuẩn có viền (Tại DOWN * 4.5)"""
        eng_sub = Text(eng_text, font="Arial", font_size=22, color=WHITE)
        vie_sub = Text(vie_text, font="Arial", font_size=18, color=YELLOW)
        sub_group = VGroup(eng_sub, vie_sub).arrange(DOWN, buff=0.15)

        sub_box = SurroundingRectangle(
            sub_group,
            color=GRAY_A,
            buff=0.3,
            stroke_width=2,
            corner_radius=0.1
        )
        full_sub = VGroup(sub_box, sub_group).move_to(DOWN * 4.5)
        return full_sub

    def construct(self):
        # ==========================================
        # BACKGROUND: CYBER / MATH VIBE
        # ==========================================
        # Tạo lưới tọa độ mờ phía sau để tăng cảm giác "toán học"
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-16, 16, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1.5,
                "stroke_opacity": 0.2
            },
            # Tàng hình hoàn toàn 2 trục X, Y trắng đè ngang màn hình
            axis_config={"stroke_width": 0, "stroke_opacity": 0}
        )
        self.play(FadeIn(grid, run_time=2))

        # Phụ đề 1 (Đã ngắt dòng để không bị tràn)
        sub1 = self.create_boxed_subtitle(
            "In hypothesis testing, we assume\npressing makes NO difference",
            "Trong kiểm định giả thuyết, ta giả định\npressing KHÔNG tạo ra khác biệt"
        )
        self.play(FadeIn(sub1))
        self.wait(2.5)

        # ==========================================
        # KHỐI XANH: GIẢ THUYẾT GỐC (H0)
        # ==========================================
        # Text H0
        h0_label = MathTex("H_0", font_size=40, color=TEAL)
        h0_desc = Text(": Pressing không hiệu quả hơn", font="Arial", font_size=24, color=WHITE)
        h0_text = VGroup(h0_label, h0_desc).arrange(RIGHT, buff=0.2)

        # Khối hộp xanh
        h0_box = SurroundingRectangle(h0_text, color=TEAL, buff=0.4, corner_radius=0.2, stroke_width=3)
        h0_bg = BackgroundRectangle(h0_text, color=TEAL, fill_opacity=0.1, buff=0.4)
        h0_group = VGroup(h0_bg, h0_box, h0_text).move_to(UP * 2.5)

        # Công thức H0
        h0_formula = MathTex(r"H_0: \mu_1 = \mu_2", font_size=50, color=TEAL).next_to(h0_group, DOWN, buff=0.4)

        # Phụ đề 2
        sub2 = self.create_boxed_subtitle(
            "This is the null hypothesis — H0",
            "Đó là giả thuyết gốc — H0"
        )

        self.play(
            ReplacementTransform(sub1, sub2),
            Create(h0_box), FadeIn(h0_bg), Write(h0_text),
            run_time=2
        )
        self.wait(1)

        # Vẽ công thức H0
        self.play(Write(h0_formula), run_time=1.5)
        self.wait(2)

        # ==========================================
        # KHỐI ĐỎ: GIẢ THUYẾT ĐỐI (H1)
        # ==========================================
        # Text H1
        h1_label = MathTex("H_1", font_size=40, color=RED)
        h1_desc = Text(": Pressing hiệu quả hơn", font="Arial", font_size=24, color=WHITE)
        h1_text = VGroup(h1_label, h1_desc).arrange(RIGHT, buff=0.2)

        # Khối hộp đỏ
        h1_box = SurroundingRectangle(h1_text, color=RED, buff=0.4, corner_radius=0.2, stroke_width=3)
        h1_bg = BackgroundRectangle(h1_text, color=RED, fill_opacity=0.1, buff=0.4)
        h1_group = VGroup(h1_bg, h1_box, h1_text).move_to(DOWN * 0.5)

        # Công thức H1
        h1_formula = MathTex(r"H_1: \mu_1 > \mu_2", font_size=50, color=RED).next_to(h1_group, DOWN, buff=0.4)

        # Phụ đề 3 (Đã ngắt dòng để không bị tràn)
        sub3 = self.create_boxed_subtitle(
            "Then, we check if the data is strong enough\nto reject this hypothesis",
            "Sau đó, ta kiểm tra xem dữ liệu có đủ mạnh\nđể bác bỏ giả thuyết này không"
        )

        self.play(
            ReplacementTransform(sub2, sub3),
            Create(h1_box), FadeIn(h1_bg), Write(h1_text),
            run_time=2
        )
        self.wait(1)

        # Vẽ công thức H1
        self.play(Write(h1_formula), run_time=1.5)
        self.wait(2)

        # ==========================================
        # HIỆU ỨNG NHẤN MẠNH (CAMERA PAN TƯƠNG ĐƯƠNG)
        # ==========================================
        # Phụ đề 4
        sub4 = self.create_boxed_subtitle(
            "This leads to the alternative hypothesis — H1",
            "Dẫn đến giả thuyết đối — H1"
        )
        self.play(ReplacementTransform(sub3, sub4))

        # Gom toàn bộ nội dung để làm hiệu ứng phóng to
        content_group = VGroup(h0_group, h0_formula, h1_group, h1_formula)

        # Tạo hiệu ứng phát sáng mờ (Glow)
        glow_effect = h1_box.copy().set_stroke(color=RED, width=15, opacity=0.3)

        self.play(
            FadeIn(glow_effect),
            content_group.animate.scale(1.1).shift(UP * 0.5),
            run_time=3,
            rate_func=there_and_back
        )
        self.wait(1.5)

        # Dọn dẹp scene
        self.play(*(map(FadeOut, self.mobjects)))