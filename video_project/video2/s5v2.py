from manim import *
import numpy as np

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene5(Scene):
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
        """Hàm tạo phụ đề chuẩn: Có viền và CÓ NỀN ĐEN để không bị đè bởi lưới phía sau"""
        eng_sub = Text(eng_text, font="Arial", font_size=22, color=WHITE)
        vie_sub = Text(vie_text, font="Arial", font_size=18, color=YELLOW)
        sub_group = VGroup(eng_sub, vie_sub).arrange(DOWN, buff=0.15)

        # Thêm nền đen che mờ các cảnh vật phía sau
        bg_box = BackgroundRectangle(sub_group, color=BLACK, fill_opacity=0.85, buff=0.3)
        # Viền ngoài
        sub_box = SurroundingRectangle(sub_group, color=GRAY_A, buff=0.3, stroke_width=2, corner_radius=0.1)

        full_sub = VGroup(bg_box, sub_box, sub_group).move_to(DOWN * 4.5)
        return full_sub

    def construct(self):
        # ==========================================
        # BACKGROUND: CYBER / MATH VIBE
        # ==========================================
        # Tạo lưới tọa độ mờ phía sau
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

        # Trục X làm nền cho biểu đồ cột
        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=4).move_to(DOWN * 2)

        # Phụ đề 1
        sub1 = self.create_boxed_subtitle(
            "After calculating...",
            "Sau khi tính toán..."
        )
        self.play(FadeIn(sub1), Create(x_axis))
        self.wait(1)

        # ==========================================
        # BIỂU ĐỒ CỘT 1: NHÓM PRESSING (TEAL)
        # ==========================================
        # Setup thông số: Giá trị max là ~20, ta scale xuống để 20 đơn vị = 4.5 đơn vị Manim
        scale_factor = 4.5 / 20.0

        # Trackers để đồng bộ đếm số và độ cao cột
        tracker1 = ValueTracker(0.001)

        # Cột 1 (Teal)
        bar1 = Rectangle(width=2, height=0.001, fill_color=TEAL, fill_opacity=0.8, stroke_color=TEAL)
        bar1.next_to(x_axis, UP, buff=0).shift(LEFT * 2)

        # Nhãn trục X
        label1 = Text("PRESSING", font="Arial", font_size=24, color=TEAL, weight=BOLD).next_to(x_axis, DOWN,
                                                                                               buff=0.3).shift(LEFT * 2)

        # Con số chạy (Number counter)
        num1 = DecimalNumber(0, num_decimal_places=1, font_size=50, color=TEAL)

        # Hàm tự động cập nhật chiều cao và vị trí số
        bar1.add_updater(
            lambda m: m.stretch_to_fit_height(tracker1.get_value() * scale_factor).next_to(x_axis, UP, buff=0).shift(
                LEFT * 2))
        num1.add_updater(lambda m: m.set_value(tracker1.get_value()).next_to(bar1, UP, buff=0.2))

        # Phụ đề 2 (Đã ngắt dòng để chống tràn viền)
        sub2 = self.create_boxed_subtitle(
            "The pressing group averages nearly 20\nball recoveries per match",
            "Nhóm pressing có trung bình gần 20\nlần đoạt bóng mỗi trận."
        )

        self.play(
            ReplacementTransform(sub1, sub2),
            FadeIn(bar1), FadeIn(label1), FadeIn(num1)
        )
        # Hiệu ứng cột lớn lên và số chạy
        self.play(tracker1.animate.set_value(19.9), run_time=3.5, rate_func=smooth)

        # Chuyển đổi con số đếm thành công thức x1 = 19.9
        bar1.clear_updaters()
        num1.clear_updaters()
        x1_tex = MathTex(r"\bar{x}_1 = 19.9", font_size=50, color=TEAL).move_to(num1.get_center())
        self.play(ReplacementTransform(num1, x1_tex))

        # Thêm hiệu ứng Glow PSG color cho cột 1
        glow1 = bar1.copy().set_fill(opacity=0).set_stroke(TEAL, width=15, opacity=0.4)
        self.play(FadeIn(glow1))

        # ==========================================
        # BIỂU ĐỒ CỘT 2: NHÓM BÌNH THƯỜNG (ORANGE)
        # ==========================================
        tracker2 = ValueTracker(0.001)

        bar2 = Rectangle(width=2, height=0.001, fill_color=ORANGE, fill_opacity=0.8, stroke_color=ORANGE)
        bar2.next_to(x_axis, UP, buff=0).shift(RIGHT * 2)

        label2 = Text("BÌNH THƯỜNG", font="Arial", font_size=24, color=ORANGE, weight=BOLD).next_to(x_axis, DOWN,
                                                                                                    buff=0.3).shift(
            RIGHT * 2)

        num2 = DecimalNumber(0, num_decimal_places=1, font_size=50, color=ORANGE)

        bar2.add_updater(
            lambda m: m.stretch_to_fit_height(tracker2.get_value() * scale_factor).next_to(x_axis, UP, buff=0).shift(
                RIGHT * 2))
        num2.add_updater(lambda m: m.set_value(tracker2.get_value()).next_to(bar2, UP, buff=0.2))

        # Phụ đề 3 (Đã ngắt dòng để chống tràn viền)
        sub3 = self.create_boxed_subtitle(
            "While the normal tactic\nis only about 12 times.",
            "Trong khi chiến thuật thông thường\nchỉ khoảng 12 lần."
        )

        self.play(
            ReplacementTransform(sub2, sub3),
            FadeIn(bar2), FadeIn(label2), FadeIn(num2)
        )
        self.play(tracker2.animate.set_value(11.8), run_time=3.5, rate_func=smooth)

        # Chuyển đổi con số đếm thành công thức x2 = 11.8
        bar2.clear_updaters()
        num2.clear_updaters()
        x2_tex = MathTex(r"\bar{x}_2 = 11.8", font_size=50, color=ORANGE).move_to(num2.get_center())
        self.play(ReplacementTransform(num2, x2_tex))

        # ==========================================
        # NHẤN MẠNH KHOẢNG CÁCH & ĐẶT CÂU HỎI
        # ==========================================
        # Phụ đề 4
        sub4 = self.create_boxed_subtitle(
            "This gap is quite large.",
            "Khoảng cách này khá lớn."
        )
        self.play(ReplacementTransform(sub3, sub4))

        # Vẽ đường gióng và mũi tên chênh lệch TỰ ĐỘNG CĂN CHỈNH
        # Lấy tọa độ Y của đỉnh 2 cột để vẽ
        y_top_bar1 = bar1.get_top()[1]
        y_top_bar2 = bar2.get_top()[1]

        # Đường gióng nét đứt từ đỉnh cột cam chạy ngang sang trái
        dashed_line = DashedLine(
            start=np.array([0, y_top_bar2, 0]),
            end=bar2.get_left(),
            color=WHITE
        )

        # Mũi tên 2 chiều nằm chính giữa khoảng trống (x=0)
        gap_arrow = DoubleArrow(
            start=np.array([0, y_top_bar2, 0]),
            end=np.array([0, y_top_bar1, 0]),
            color=RED, stroke_width=5, buff=0
        )

        self.play(Create(dashed_line))
        self.play(GrowArrow(gap_arrow), run_time=1.5)
        self.wait(1.5)

        # Phụ đề 5
        sub5 = self.create_boxed_subtitle(
            "But is it statistically significant?",
            "Nhưng liệu nó có đủ lớn về mặt thống kê?"
        )

        # Nhấn mạnh câu hỏi bằng chớp sáng quanh phụ đề
        self.play(ReplacementTransform(sub4, sub5))
        flash = Flash(sub5, color=YELLOW, line_length=0.5, num_lines=16, flash_radius=2.5)
        self.play(flash)
        self.wait(3)

        # Dọn dẹp scene
        self.play(*(map(FadeOut, self.mobjects)))