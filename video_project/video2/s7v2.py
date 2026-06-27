from manim import *

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene7(Scene):
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
        # --- ĐƯỜNG DẪN ASSETS ---
        # Bạn chèn đường dẫn ảnh PSG pressing vào đây nhé:
        PSG_PRESSING_PATH = "video_project/video2/assets2/psg_pressing.jpg"

        # ==========================================
        # PHẦN 1: SO SÁNH P-VALUE & BÁC BỎ H0 (Khoảng 8-9s)
        # ==========================================
        # Lưới tọa độ mờ giữ nhịp từ cảnh trước
        grid = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-16, 16, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1.5, "stroke_opacity": 0.2},
            axis_config={"stroke_width": 0, "stroke_opacity": 0}
        )
        self.add(grid)

        # Phụ đề 1
        sub1 = self.create_boxed_subtitle(
            "And since the p-value is less than\nthe 0.05 significance level...",
            "Và vì p-value nhỏ hơn\nmức ý nghĩa 0.05..."
        )

        p_value_compare = MathTex(
            r"p = 0.001 < 0.05",
            font_size=60, color=RED
        ).move_to(UP * 1.5)

        self.play(FadeIn(sub1), Write(p_value_compare), run_time=2)
        self.wait(2)

        # Phụ đề 2
        sub2 = self.create_boxed_subtitle(
            "We reject the null hypothesis.",
            "Chúng ta bác bỏ giả thuyết gốc."
        )

        # H0 bị gạch bỏ
        h0_label = MathTex("H_0:", font_size=45, color=TEAL)
        h0_text = Text(" Pressing không hiệu quả", font="Arial", font_size=30, color=WHITE)
        h0_group = VGroup(h0_label, h0_text).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)

        cross_line = Line(h0_group.get_left() + LEFT * 0.2, h0_group.get_right() + RIGHT * 0.2, color=RED,
                          stroke_width=6)

        self.play(ReplacementTransform(sub1, sub2), FadeIn(h0_group), run_time=1.5)
        self.play(Create(cross_line), run_time=0.5)
        self.wait(2)

        # ==========================================
        # PHẦN 2: EPIC ZOOM & STADIUM FLASH (Khoảng 6-7s)
        # ==========================================
        # Phụ đề 3
        sub3 = self.create_boxed_subtitle(
            "Final conclusion:",
            "Kết luận cuối cùng:"
        )

        # Hiệu ứng Stadium Light Flash (Màn hình chớp trắng)
        flash_rect = FullScreenRectangle(color=WHITE, fill_opacity=0.8)

        # Dòng chữ lớn xuất hiện
        epic_text = Text(
            "PRESSING CỦA PSG\nTHỰC SỰ HIỆU QUẢ",
            font="Arial", font_size=55, color=YELLOW, weight=BOLD, line_spacing=1.2
        ).move_to(UP * 0.5)

        self.play(
            FadeOut(p_value_compare), FadeOut(h0_group), FadeOut(cross_line), FadeOut(grid),
            ReplacementTransform(sub2, sub3)
        )

        # Đánh Flash và hiện chữ
        self.play(FadeIn(flash_rect, run_time=0.1))
        self.add(epic_text)
        self.play(FadeOut(flash_rect, run_time=0.4))

        # Epic Zoom chậm
        self.play(epic_text.animate.scale(1.2), run_time=4, rate_func=linear)

        # ==========================================
        # PHẦN 3: KẾT LUẬN & HÌNH ẢNH THỰC TẾ (Khoảng 9-10s)
        # ==========================================
        # Phụ đề 4 (Cẩn thận ngắt dòng để không tràn)
        sub4 = self.create_boxed_subtitle(
            "High pressing helps PSG win more balls\nin a statistically significant way.",
            "Pressing tầm cao giúp PSG giành lại bóng\nnhiều hơn một cách có ý nghĩa thống kê."
        )

        # Load hình ảnh PSG Pressing
        psg_image = None
        try:
            # Scale ảnh choán khoảng 70% bề ngang màn hình
            psg_image = ImageMobject(PSG_PRESSING_PATH).scale_to_fit_width(8.5).move_to(UP * 0.5)
            # Thêm viền trắng mỏng cho ảnh điện ảnh hơn
            img_border = SurroundingRectangle(psg_image, color=WHITE, stroke_width=2, buff=0)
            img_group = Group(psg_image, img_border)
        except:
            # Fallback nếu đường dẫn sai
            img_group = Group(
                Rectangle(width=8.5, height=5, fill_color=BLUE_E, fill_opacity=0.5, stroke_color=WHITE),
                Text("CẦN CHÈN ẢNH PSG_PRESSING", font_size=30, color=WHITE)
            ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(sub3, sub4),
            FadeOut(epic_text),
            FadeIn(img_group, scale=0.9),
            run_time=2
        )

        # Cinematic Pan/Zoom nhẹ vào bức ảnh thực tế
        self.play(img_group.animate.scale(1.15), run_time=6, rate_func=linear)

        self.wait(1)

        # Kết thúc Scene
        self.play(*(map(FadeOut, self.mobjects)))