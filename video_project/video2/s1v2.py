from manim import *

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Intro(Scene):
    def setup(self):
        # 1. Thiết lập nền đen
        self.camera.background_color = BLACK

        # 2. Thiết lập Logo Fami (Sát mép trên)
        logo_path = "video_project/demo/assets/images/fami_hust.png"
        try:
            # Chỉ nạp ảnh trong suốt, không dùng hàm đóng khung vuông nữa.
            # (Bạn hãy tạo viền trắng ôm sát logo ngay từ file ảnh gốc nhé)
            fami_logo = ImageMobject(logo_path).scale_to_fit_width(1.2)
            fami_logo.to_edge(UP, buff=0.2)
            self.add(fami_logo)
        except:
            pass

        # 3. Dòng chữ chủ đề Video (Tọa độ UP * 5.8) - Đã in hoa toàn bộ
        topic_title = Text(
            "KIỂM ĐỊNH GIẢ THUYẾT\nCHIẾN THUẬT PRESSING",
            font="Arial",
            font_size=28,
            color=TEAL,
            weight=BOLD
        ).move_to(UP * 5.8)
        self.add(topic_title)

    def create_boxed_subtitle(self, eng_text, vie_text):
        """Hàm tạo phụ đề chuẩn có viền (Theo chuẩn DOWN * 4.5)"""
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
        # --- ĐƯỜNG DẪN ASSETS ---
        ICON_QUESTION_PATH = "video_project/video2/assets2/problem.png"
        PRESSING_IMAGE_PATH = "video_project/video2/assets2/pressing.jpg"
        PSG_LOGO_PATH = "video_project/video2/assets2/psg.png"

        # ==========================================
        # PHẦN 1: INTRO (2s)
        # ==========================================
        # Đẩy cụm Text và Icon lên cao (UP * 3.2) để tránh đè vào phụ đề
        question_text = Text("What is\npressing?", font="Arial", font_size=50, weight=BOLD).move_to(UP * 3.2)
        icon_q = ImageMobject(ICON_QUESTION_PATH).scale(0.6).next_to(question_text, DOWN, buff=0.5)

        sub1 = self.create_boxed_subtitle("What is pressing tactic?", "Chiến thuật pressing là gì?")

        self.play(Write(question_text), run_time=0.8)

        # Đã đổi hiệu ứng Icon thành FadeIn từ từ, đồng bộ thời gian với Subtitle
        self.play(
            FadeIn(icon_q, run_time=1.2),
            FadeIn(sub1, run_time=1.2)
        )
        self.wait(1)
        self.play(FadeOut(question_text), FadeOut(icon_q), FadeOut(sub1))

        # ==========================================
        # PHẦN 2: ĐỊNH NGHĨA PRESSING (8s)
        # ==========================================
        pressing_img = ImageMobject(PRESSING_IMAGE_PATH).scale_to_fit_width(7).move_to(UP * 0.5)

        sub2_1 = self.create_boxed_subtitle("Proactive defensive strategy", "Chiến thuật phòng ngự chủ động")
        sub2_2 = self.create_boxed_subtitle("Pressuring to regain possession", "Áp sát nhanh để giành bóng")

        self.play(FadeIn(pressing_img), FadeIn(sub2_1))
        self.wait(3.5)

        self.play(ReplacementTransform(sub2_1, sub2_2))
        self.wait(3.5)

        self.play(FadeOut(pressing_img), FadeOut(sub2_2))

        # ==========================================
        # PHẦN 3: PSG & KIỂM ĐỊNH GIẢ THUYẾT (18s)
        # ==========================================
        # Giảm thêm 15% kích thước theo yêu cầu (0.86 * 0.85 = 0.73)
        psg_logo = ImageMobject(PSG_LOGO_PATH).scale(0.73).move_to(ORIGIN)

        sub3_1 = self.create_boxed_subtitle("Popular modern tactical weapon", "Vũ khí chiến thuật phổ biến")
        sub3_2 = self.create_boxed_subtitle("Is PSG's pressing effective?", "Pressing của PSG có hiệu quả?")
        sub3_3 = self.create_boxed_subtitle("Analyzing via hypothesis testing", "Phân tích bằng kiểm định giả thuyết")

        # Hiệu ứng hiện ra từ từ, mượt mà thay vì nảy
        self.play(
            FadeIn(psg_logo, run_time=1.5),
            FadeIn(sub3_1)
        )
        self.wait(3.5)

        self.play(ReplacementTransform(sub3_1, sub3_2))
        self.wait(4.5)

        # Hiệu ứng nổi bật lên rồi thu nhỏ vào (sử dụng there_and_back)
        self.play(
            psg_logo.animate(rate_func=rate_functions.there_and_back).scale(1.3),
            ReplacementTransform(sub3_2, sub3_3),
            run_time=1.5
        )

        flash = Flash(psg_logo, color=YELLOW, line_length=0.4, num_lines=12, flash_radius=1.8)
        self.play(flash)
        self.wait(5.5)

        self.play(*(map(FadeOut, self.mobjects)))