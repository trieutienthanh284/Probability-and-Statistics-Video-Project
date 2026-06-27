from manim import *

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene8(Scene):
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
        """Hàm tạo phụ đề chuẩn: Đã giảm cỡ chữ để chống tràn"""
        # Cỡ chữ giảm xuống 20 và 16
        eng_sub = Text(eng_text, font="Arial", font_size=20, color=WHITE)
        vie_sub = Text(vie_text, font="Arial", font_size=16, color=YELLOW)
        sub_group = VGroup(eng_sub, vie_sub).arrange(DOWN, buff=0.15)

        bg_box = BackgroundRectangle(sub_group, color=BLACK, fill_opacity=0.85, buff=0.3)
        sub_box = SurroundingRectangle(sub_group, color=GRAY_A, buff=0.3, stroke_width=2, corner_radius=0.1)

        full_sub = VGroup(bg_box, sub_box, sub_group).move_to(DOWN * 4.5)
        return full_sub

    def construct(self):
        # --- ĐƯỜNG DẪN ASSETS ---
        PITCH_PATH = "video_project/video2/assets2/pitch.png"

        # ĐƯỜNG DẪN 3 ICON
        ICON_DATA_PATH = "video_project/video2/assets2/data-warehouse.png"
        ICON_STAT_PATH = "video_project/video2/assets2/analytics.png"
        ICON_HYPO_PATH = "video_project/video2/assets2/exploratory-analysis.png"

        # ==========================================
        # PHẦN 1: CAMERA BAY KHỎI SÂN VẬN ĐỘNG
        # ==========================================
        sub1 = self.create_boxed_subtitle(
            "Today, football is no longer just about emotions.",
            "Ngày nay, bóng đá không còn chỉ là cảm xúc."
        )

        try:
            # Giảm 30% kích thước sân (8.5 * 0.7 = 5.95)
            pitch_img = ImageMobject(PITCH_PATH).scale_to_fit_width(5.95).move_to(UP * 0.5)
            self.play(FadeIn(pitch_img), FadeIn(sub1))
            self.wait(1)

            # Hiệu ứng Camera bay ra xa
            self.play(
                pitch_img.animate.scale(0.2).set_opacity(0).shift(UP * 2),
                run_time=3.5,
                rate_func=linear
            )
            self.remove(pitch_img)
        except:
            self.play(FadeIn(sub1))
            self.wait(4.5)

        # ==========================================
        # PHẦN 2: XUẤT HIỆN CÁC KEYWORD VÀ ICON
        # ==========================================
        # Hiện lưới dữ liệu lên nền
        grid = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-16, 16, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1.5, "stroke_opacity": 0.2},
            axis_config={"stroke_width": 0, "stroke_opacity": 0}
        )
        self.play(FadeIn(grid))

        # Hàm trợ giúp gom Icon và Text
        def create_keyword_group(icon_path, text_str, color):
            # Giảm cỡ chữ đi 20% (40 * 0.8 = 32)
            text_obj = Text(text_str, font="Arial", font_size=28, color=color, weight=BOLD)
            try:
                # Icon cũng giảm tỷ lệ thuận (từ 1.0 xuống 0.8)
                icon_img = ImageMobject(icon_path).scale_to_fit_height(0.8)
                kw_group = Group(icon_img, text_obj).arrange(RIGHT, buff=0.4)
            except:
                fallback_icon = Circle(radius=0.4, color=color, fill_opacity=0.5)
                kw_group = Group(fallback_icon, text_obj).arrange(RIGHT, buff=0.4)
            return kw_group

        # Khởi tạo 3 khối Keyword
        kw_data = create_keyword_group(ICON_DATA_PATH, "DỮ LIỆU", TEAL).move_to(UP * 2)
        kw_stat = create_keyword_group(ICON_STAT_PATH, "THỐNG KÊ", ORANGE).move_to(ORIGIN)
        kw_hypo = create_keyword_group(ICON_HYPO_PATH, "KIỂM ĐỊNH GIẢ THUYẾT", RED).move_to(DOWN * 2)

        # --- Lời thoại 2: DỮ LIỆU ---
        sub2 = self.create_boxed_subtitle(
            "Behind every tactic...\nis data.",
            "Đằng sau mỗi chiến thuật...\nlà dữ liệu."
        )
        self.play(ReplacementTransform(sub1, sub2))
        self.play(FadeIn(kw_data, shift=RIGHT * 0.5), run_time=1.5)
        self.wait(2)

        # --- Lời thoại 3: THỐNG KÊ ---
        sub3 = self.create_boxed_subtitle(
            "Behind every decision...\nis statistics.",
            "Đằng sau mỗi quyết định...\nlà thống kê."
        )
        self.play(ReplacementTransform(sub2, sub3))
        self.play(FadeIn(kw_stat, shift=RIGHT * 0.5), run_time=1.5)
        self.wait(2)

        # --- Lời thoại 4: KIỂM ĐỊNH GIẢ THUYẾT ---
        sub4 = self.create_boxed_subtitle(
            "And hypothesis testing is one of the most\nimportant tools in modern football.",
            "Và kiểm định giả thuyết chính là một trong những\ncông cụ quan trọng nhất của bóng đá hiện đại."
        )
        self.play(ReplacementTransform(sub3, sub4))
        self.play(FadeIn(kw_hypo, shift=RIGHT * 0.5), run_time=1.5)

        # Nhịp chót: Phóng to nhấn mạnh toàn bộ các từ khóa
        self.play(
            kw_data.animate.scale(1.1),
            kw_stat.animate.scale(1.1),
            kw_hypo.animate.scale(1.1),
            run_time=2, rate_func=there_and_back
        )
        self.wait(3.5)

        # ==========================================
        # FADE OUT KẾT THÚC VIDEO
        # ==========================================
        self.play(*(map(FadeOut, self.mobjects)), run_time=2)