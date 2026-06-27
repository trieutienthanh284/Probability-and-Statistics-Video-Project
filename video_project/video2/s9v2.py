from manim import *
import numpy as np

# Cấu hình video dọc 9x16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60


class PSG_Pressing_Scene9_Outro(Scene):
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
        BLUE_PLAYER_PATH = "video_project/video2/assets2/soccer-player.png"

        # ==========================================
        # PHẦN 1: SETUP SÂN BÓNG & CẦU THỦ (NODES)
        # ==========================================
        # Sân bóng mờ (Tỷ lệ 5.95 như đã fix ở cảnh trước để có lề an toàn)
        try:
            pitch_img = ImageMobject(PITCH_PATH).scale_to_fit_width(5.95).move_to(UP * 0.5)
            pitch_img.set_opacity(0.4)
            self.add(pitch_img)
        except:
            pitch_bg = Rectangle(width=5.95, height=3.85, color=WHITE, fill_color="#2E7D32", fill_opacity=0.4).move_to(
                UP * 0.5)
            self.add(pitch_bg)

        # Tạo 3 cầu thủ đại diện cho 3 trạng thái (Nodes) của Chuỗi Markov
        # 1: Hậu vệ (Dưới), 2: Tiền vệ (Giữa), 3: Tiền đạo (Trên)
        pos_1 = DOWN * 1.5 + RIGHT * 0.5
        pos_2 = UP * 0.5 + LEFT * 0.8
        pos_3 = UP * 2.2 + RIGHT * 1.0

        # SỬ DỤNG GROUP() ĐỂ CHỨA HÌNH ẢNH, TRÁNH LỖI TYPE_ERROR CỦA VGROUP
        players = Group()

        try:
            base_blue = ImageMobject(BLUE_PLAYER_PATH)
            for pos in [pos_1, pos_2, pos_3]:
                # Kích thước icon cầu thủ (để to một chút 0.06 cho rõ)
                player = base_blue.copy().scale(0.06).move_to(pos)
                players.add(player)
        except:
            for pos in [pos_1, pos_2, pos_3]:
                players.add(Dot(pos, radius=0.15, color=BLUE))

        # --- Lời thoại 1 ---
        sub1 = self.create_boxed_subtitle(
            "Hypothesis testing helps us see through the past\nto know if a tactic is truly effective.",
            "Kiểm định giả thuyết giúp chúng ta nhìn thấu quá khứ\nđể biết một chiến thuật có thực sự hiệu quả."
        )
        self.play(FadeIn(sub1), FadeIn(players), run_time=2)
        self.wait(3.5)

        # ==========================================
        # PHẦN 2: VẼ MẠNG LƯỚI MARKOV (EDGES)
        # ==========================================
        # --- Lời thoại 2 ---
        sub2 = self.create_boxed_subtitle(
            "But football is a continuous flow.\nIf a midfielder has the ball...",
            "Nhưng bóng đá là một dòng chảy liên tục.\nNếu một tiền vệ đang cầm bóng..."
        )
        self.play(ReplacementTransform(sub1, sub2))

        # Tạo hiệu ứng phát sáng cho tiền vệ (Node 2) đang cầm bóng
        active_glow = Circle(radius=0.3, color=YELLOW, fill_opacity=0.3).move_to(pos_2)
        self.play(FadeIn(active_glow), run_time=0.5)
        self.play(active_glow.animate.scale(1.2), rate_func=there_and_back, run_time=1)
        self.wait(1.5)

        # Vẽ các mũi tên xác suất (Edges) - ĐÃ SỬA RED_3 THÀNH RED
        arrow_1_2 = CurvedArrow(pos_1, pos_2, angle=TAU / 6, color=WHITE, stroke_width=3)
        arrow_2_3 = CurvedArrow(pos_2, pos_3, angle=TAU / 6, color=YELLOW, stroke_width=4)
        arrow_2_1 = CurvedArrow(pos_2, pos_1, angle=TAU / 6, color=RED, stroke_width=3)

        # Các con số % (Markov transition probabilities) - ĐÃ SỬA RED_3 THÀNH RED
        pct_2_3 = Text("65%", font="Arial", font_size=20, color=YELLOW, weight=BOLD).next_to(arrow_2_3, LEFT, buff=0.1)
        pct_2_1 = Text("20%", font="Arial", font_size=18, color=RED, weight=BOLD).next_to(arrow_2_1, RIGHT, buff=0.1)
        pct_1_2 = Text("15%", font="Arial", font_size=18, color=WHITE, weight=BOLD).next_to(arrow_1_2, LEFT, buff=0.1)

        # --- Lời thoại 3 ---
        sub3 = self.create_boxed_subtitle(
            "Can we calculate the exact probability\nof where his next pass will go?",
            "Liệu ta có thể tính toán chính xác xác suất\nđường chuyền tiếp theo của anh ta sẽ đi về đâu?"
        )
        self.play(ReplacementTransform(sub2, sub3))

        # Mũi tên từ Tiền vệ bay ra
        self.play(Create(arrow_2_3), Create(arrow_2_1), Create(arrow_1_2), run_time=2)
        self.play(Write(pct_2_3), Write(pct_2_1), Write(pct_1_2), run_time=1.5)
        self.wait(1.5)

        # ==========================================
        # PHẦN 3: CÂU HỎI GỢI MỞ (THE HOOK)
        # ==========================================
        # Tạo hiệu ứng nền tối dần để tôn lên câu hỏi chốt
        dark_overlay = FullScreenRectangle(color=BLACK, fill_opacity=0.6)

        hook_text = Text(
            "LIỆU DỮ LIỆU CÓ THỂ\nDỰ ĐOÁN TƯƠNG LAI?",
            font="Arial", font_size=40, color=TEAL, weight=BOLD, line_spacing=1.5
        ).move_to(UP * 0.5)

        # Khung viền HUD cho câu hỏi
        hook_box = SurroundingRectangle(hook_text, color=TEAL, buff=0.4, stroke_width=2, corner_radius=0.1)

        # --- Lời thoại 4 ---
        sub4 = self.create_boxed_subtitle(
            "That's not fortune-telling.\nIt's the power of Data Analytics.",
            "Đó không phải là bói toán.\nĐó là sức mạnh của Phân tích dữ liệu."
        )
        self.play(ReplacementTransform(sub3, sub4))

        self.play(FadeIn(dark_overlay, run_time=1))
        self.play(
            FadeIn(hook_text, scale=0.5, rate_func=rate_functions.ease_out_back),
            Create(hook_box),
            run_time=1.5
        )

        # Chớp sáng nhấn mạnh câu hỏi
        flash = Flash(hook_box, color=YELLOW, line_length=0.5, num_lines=16, flash_radius=3)
        self.play(flash)

        self.wait(3.5)

        # Fade out kết thúc video
        self.play(*(map(FadeOut, self.mobjects)), run_time=2)