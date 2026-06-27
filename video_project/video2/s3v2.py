from manim import *
import numpy as np

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene3(Scene):
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
        # --- ĐƯỜNG DẪN ASSETS ---
        PITCH_PATH = "video_project/video2/assets2/pitch.png"

        # ==========================================
        # PHẦN 1: GIẢI THÍCH CHỈ SỐ PPDA TRÊN SÂN
        # ==========================================
        sub1 = self.create_boxed_subtitle("To measure pressing, we use a key metric: PPDA",
                                          "Để đo lường pressing, ta sử dụng chỉ số: PPDA")

        pitch_img = None
        try:
            pitch_img = ImageMobject(PITCH_PATH).scale_to_fit_width(7.5).move_to(UP * 0.5)
            pitch_img.set_opacity(0.4)
            self.play(FadeIn(pitch_img), FadeIn(sub1))
        except:
            self.play(FadeIn(sub1))

        ppda_text = Text("PPDA", font="Arial", font_size=65, color=WHITE, weight=BOLD).move_to(UP * 2.5)
        self.play(FadeIn(ppda_text))

        flash = Flash(UP * 0.5, color=YELLOW, line_length=0.4, num_lines=12, flash_radius=1.5)
        self.play(flash)

        sub2 = self.create_boxed_subtitle("Passes allowed before a defensive action occurs",
                                          "Đường chuyền trước khi có hành động phòng ngự")

        # Hộp thoại định nghĩa PPDA
        ppda_def = Text(
            "PPDA là số đường chuyền trung bình\nđối phương thực hiện được trước khi\ncó một hành động phòng ngự.",
            font="Arial", font_size=22, line_spacing=1.5,
            t2c={"đường chuyền trung bình": TEAL, "hành động phòng ngự": ORANGE}
        )
        ppda_box = SurroundingRectangle(ppda_def, color=GRAY_A, buff=0.4, stroke_width=2, corner_radius=0.1)
        group_def = VGroup(ppda_box, ppda_def).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(sub1, sub2),
            FadeIn(group_def, scale=0.8)
        )
        self.wait(2)

        # SỬA LỖI Ở ĐÂY: Dùng Group() thay vì VGroup() để có thể chứa cả chữ và ảnh
        fade_out_group = Group(ppda_text, group_def, sub2)
        if pitch_img:
            fade_out_group.add(pitch_img)
        self.play(FadeOut(fade_out_group))

        # ==========================================
        # PHẦN 2: BẢNG DATASET SO SÁNH PPDA
        # ==========================================
        sub3 = self.create_boxed_subtitle("Each number represents the PPDA index in a match",
                                          "Mỗi con số biểu thị chỉ số PPDA trong 1 trận đấu")

        dataset_title = Text("DATASET", font="Arial", font_size=50, color=WHITE, weight=BOLD).move_to(UP * 3.5)

        # --- Dữ liệu High Pressing (Màu Xanh Teal) ---
        teal_label = Text("10 trận có Pressing", font="Arial", font_size=26, color=TEAL, weight=BOLD).move_to(UP * 2.0)
        teal_data_str = "18  -  20  -  17  -  21  -  19  -  22  -  18  -  23  -  20  -  21"
        teal_data = Text(teal_data_str, font="Arial", font_size=26, color=WHITE)
        if teal_data.width > 8.0: teal_data.scale_to_fit_width(8.0)
        teal_data.next_to(teal_label, DOWN, buff=0.4)

        # --- Dữ liệu No Pressing (Màu Cam) ---
        orange_label = Text("10 trận Bình thường", font="Arial", font_size=26, color=ORANGE, weight=BOLD).move_to(
            DOWN * 0.2)
        orange_data_str = "11  -  13  -  10  -  12  -  14  -  11  -  13  -  12  -  10  -  12"
        orange_data = Text(orange_data_str, font="Arial", font_size=26, color=WHITE)
        if orange_data.width > 8.0: orange_data.scale_to_fit_width(8.0)
        orange_data.next_to(orange_label, DOWN, buff=0.4)

        # Trình diễn Animation
        self.play(FadeIn(sub3), FadeIn(dataset_title, scale=0.8))

        self.play(FadeIn(teal_label))
        # Hiệu ứng từng số xuất hiện
        self.play(AddTextLetterByLetter(teal_data), run_time=2)

        sub4 = self.create_boxed_subtitle("Looking at the data, the pressing group seems superior",
                                          "Nhìn bằng mắt thường... nhóm pressing có vẻ vượt trội")
        self.play(ReplacementTransform(sub3, sub4))

        self.play(FadeIn(orange_label))
        self.play(AddTextLetterByLetter(orange_data), run_time=2)
        self.wait(1)

        # ==========================================
        # PHẦN 3: CÂU HỎI CHỐT CẢNH
        # ==========================================
        sub5 = self.create_boxed_subtitle("But in data science, feeling is not enough. We need statistics.",
                                          "Nhưng trong khoa học dữ liệu, ta cần bằng chứng thống kê.")

        closing_group = VGroup(
            Text("VẬY THÌ,", font="Arial", font_size=32, color=WHITE, weight=BOLD),
            Text("DATASET ĐÓ NÓI LÊN ĐIỀU GÌ?", font="Arial", font_size=32, color=TEAL, weight=BOLD)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)

        self.play(
            ReplacementTransform(sub4, sub5),
            FadeIn(closing_group, scale=0.5, rate_func=rate_functions.ease_out_back)
        )

        flash_closing = Flash(closing_group, color=YELLOW, line_length=0.6, num_lines=16, flash_radius=1.8)
        self.play(flash_closing)

        self.wait(2.5)

        # Xóa toàn bộ màn hình để chuẩn bị cho cảnh 4
        self.play(*(map(FadeOut, self.mobjects)))