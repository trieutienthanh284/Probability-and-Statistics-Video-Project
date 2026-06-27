from manim import *
import numpy as np

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene2(Scene):
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
        BLUE_PLAYER_PATH = "video_project/video2/assets2/soccer-player.png"
        RED_PLAYER_PATH = "video_project/video2/assets2/referee.png"
        PITCH_PATH = "video_project/video2/assets2/pitch.png"

        # ==========================================
        # PHẦN 1: MÔ PHỎNG SA BÀN PRESSING (Khoảng 8-9s)
        # ==========================================
        pitch_bg = Rectangle(width=8.5, height=5.5, color=WHITE, fill_color="#2E7D32", fill_opacity=1)
        center_line = Line(pitch_bg.get_top(), pitch_bg.get_bottom(), color=WHITE)
        center_circle = Circle(radius=0.8, color=WHITE).move_to(pitch_bg.get_center())

        left_box = Rectangle(width=1.5, height=3, color=WHITE).align_to(pitch_bg, LEFT)
        right_box = Rectangle(width=1.5, height=3, color=WHITE).align_to(pitch_bg, RIGHT)
        left_goal = Rectangle(width=0.2, height=1, color=WHITE).next_to(pitch_bg.get_left(), LEFT, buff=0)
        right_goal = Rectangle(width=0.2, height=1, color=WHITE).next_to(pitch_bg.get_right(), RIGHT, buff=0)

        tactical_board = VGroup(
            pitch_bg, center_line, center_circle, left_box, right_box, left_goal, right_goal
        ).scale(0.8).move_to(UP * 0.5)

        # ĐỘI ĐỎ/SỌC (Phòng ngự khối thấp)
        reds = Group()
        red_coords = [
            (RIGHT * 3.5 + UP * 0),      # 1. Thủ môn
            (RIGHT * 2.8 + UP * 0.8),    # 2. Trung vệ phải
            (RIGHT * 2.8 + DOWN * 0.8),  # 3. Trung vệ trái
            (RIGHT * 2.8 + UP * 2.0),    # 4. Hậu vệ phải
            (RIGHT * 2.8 + DOWN * 2.0),  # 5. Hậu vệ trái
            (RIGHT * 1.8 + UP * 0.8),    # 6. Tiền vệ trung tâm
            (RIGHT * 1.8 + DOWN * 0.8),  # 7. Tiền vệ trung tâm
            (RIGHT * 1.8 + UP * 2.0),    # 8. Tiền vệ phải
            (RIGHT * 1.8 + DOWN * 2.0),  # 9. Tiền vệ trái
            (RIGHT * 0.9 + UP * 0.6),    # 10. RS (Tiền đạo phải) - Kéo về nửa sân nhà
            (RIGHT * 0.5 + DOWN * 0.4)   # 11. LS (Tiền đạo trái) - Kéo về nửa sân nhà, so le với RS
        ]

        red_base_img = ImageMobject(RED_PLAYER_PATH)
        for coord in red_coords:
            # Tăng 10% kích thước: 0.043 * 1.1 ≈ 0.047
            red = red_base_img.copy().scale(0.047).move_to(tactical_board.get_center() + coord)
            reds.add(red)

        # ĐỘI XANH (Pressing) - ĐẨY CAO ĐỘI HÌNH NGAY TỪ ĐẦU
        blues = Group()
        blue_coords = [
            (LEFT * 2.5 + UP * 0),       # 1. Thủ môn (Dâng lên cao)
            (LEFT * 1.0 + UP * 0.8),     # 2. Trung vệ
            (LEFT * 1.0 + DOWN * 0.8),   # 3. Trung vệ
            (LEFT * 0.5 + UP * 2.0),     # 4. Hậu vệ cánh (Qua vạch giữa sân)
            (LEFT * 0.5 + DOWN * 2.0),   # 5. Hậu vệ cánh (Qua vạch giữa sân)
            (LEFT * 0.2 + UP * 0),       # 6. Tiền vệ mỏ neo (CDM)
            (RIGHT * 0.3 + UP * 0.8),    # 7. Tiền vệ trung tâm (Bám sát phần sân đối phương)
            (RIGHT * 0.3 + DOWN * 0.8),  # 8. Tiền vệ trung tâm
            (RIGHT * 0.7 + UP * 2.0),    # 9. Tiền đạo cánh trái
            (RIGHT * 0.7 + DOWN * 2.0),  # 10. Tiền đạo cánh phải
            (RIGHT * 1.2 + UP * 0)       # 11. Tiền đạo cắm (Áp sát khu vực cấm địa đỏ)
        ]

        blue_base_img = ImageMobject(BLUE_PLAYER_PATH)
        for coord in blue_coords:
            # Tăng 10% kích thước: 0.047
            blue = blue_base_img.copy().scale(0.047).move_to(tactical_board.get_center() + coord)
            blues.add(blue)

        # Phụ đề 1
        sub1 = self.create_boxed_subtitle("PSG coaches want to answer a specific question",
                                          "Ban huấn luyện PSG muốn trả lời một câu hỏi")

        self.play(FadeIn(tactical_board), FadeIn(reds), FadeIn(blues), FadeIn(sub1))

        # --- Di chuyển Pressing nhịp 1 (Cả đội tiếp tục dâng lên chiếm không gian) ---
        self.play(
            blues[0].animate.shift(RIGHT * 0.2),  # Thủ môn
            *[b.animate.shift(RIGHT * 0.3 + UP * np.random.uniform(-0.05, 0.05)) for b in blues[1:]],
            run_time=2.5,
            rate_func=linear
        )

        # Phụ đề 2
        sub2 = self.create_boxed_subtitle("Does high pressing win more balls?",
                                          "Pressing tầm cao có giúp giành lại bóng?")
        self.play(ReplacementTransform(sub1, sub2))

        # --- Di chuyển Pressing nhịp 2 (Siết chặt thòng lọng, KHÔNG đè) ---
        self.play(
            blues[0].animate.shift(RIGHT * 0.2),                                # Thủ môn dâng
            *[b.animate.shift(RIGHT * 0.4) for b in blues[1:5]],                # Hậu vệ dâng khóa đuôi
            blues[5].animate.shift(RIGHT * 0.5 + DOWN * 0.2),                   # CDM chéo xuống theo kèm LS đội sọc
            blues[6].animate.shift(RIGHT * 0.5),                                # CM luồn vào khe hở
            blues[7].animate.shift(RIGHT * 0.5),                                # CM luồn vào khe hở
            blues[8].animate.shift(RIGHT * 0.6 + DOWN * 0.3),                   # Cánh cắt chéo vào trung lộ
            blues[9].animate.shift(RIGHT * 0.6 + UP * 0.3),                     # Cánh cắt chéo vào trung lộ
            blues[10].animate.shift(RIGHT * 0.8),                               # ST lao vào khoảng trống giữa 2 CB
            run_time=3.5,
            rate_func=smooth
        )

        # ==========================================
        # PHẦN 2: DỮ LIỆU 20 TRẬN ĐẤU (Khoảng 5s)
        # ==========================================
        sub3 = self.create_boxed_subtitle("To test this, they collect data from 20 matches",
                                          "Họ thu thập dữ liệu từ 20 trận đấu")

        self.play(
            FadeOut(tactical_board), FadeOut(reds), FadeOut(blues),
            ReplacementTransform(sub2, sub3)
        )

        try:
            pitch_img = ImageMobject(PITCH_PATH).scale_to_fit_width(6.8).move_to(UP * 0.5)
            pitch_img.set_opacity(0.4)
            self.play(FadeIn(pitch_img))
        except:
            pass

        number_20 = Text("20", font="Arial", font_size=160, color=YELLOW, weight=BOLD).move_to(UP * 0.8)
        text_matches = Text("TRẬN ĐẤU", font="Arial", font_size=40, color=WHITE, weight=BOLD).next_to(number_20, DOWN,
                                                                                                      buff=0.2)
        group_20 = VGroup(number_20, text_matches)

        self.play(
            FadeIn(group_20, scale=0.3, rate_func=rate_functions.ease_out_back),
            run_time=1.5
        )

        flash = Flash(number_20, color=YELLOW, line_length=0.6, num_lines=16, flash_radius=1.8)
        self.play(flash)
        self.wait(2.5)

        self.play(*(map(FadeOut, self.mobjects)))