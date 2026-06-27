from base_scene import TikTokBaseScene
from manim import *


class HypothesisStep1(TikTokBaseScene):
    def construct(self):
        # 1. Header chính
        self.add_header("BƯỚC 1")

        asset_path = "video_project/video3/assets/"

        # --- Helper: Phụ đề cố định size 18/16 & Khóa chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            # Neo phụ đề ở đáy với buff=1.0 tiêu chuẩn
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: NỀN SÂN CỎ BÓNG ĐÁ (MỜ PHÍA SAU)
        # ======================================================================
        try:
            pitch_bg = ImageMobject(asset_path + "pitch.png")
            pitch_bg.scale_to_fit_height(16).set_opacity(0.12).set_z_index(-1)
            self.add(pitch_bg)
        except Exception as e:
            print(f"[CẢNH BÁO] Không nạp được ảnh pitch.png: {e}")

        # ======================================================================
        # PHẦN 2: THIẾT KẾ UI CARDS CHO CÁC GIẢ THUYẾT
        # ======================================================================
        # Hàm tạo thẻ chứa giả thuyết cực kỳ gọn gàng
        def create_hypo_card(math_tex_list, sub1, sub2, color_theme, pos_y):
            bg = RoundedRectangle(corner_radius=0.25, width=5.8, height=1.6,
                                  fill_color=color_theme, fill_opacity=0.15,
                                  stroke_color=color_theme, stroke_width=2.5)
            bg.move_to(UP * pos_y)

            # Công thức Toán
            m_tex = MathTex(*math_tex_list, font_size=50, color=color_theme)
            m_tex.move_to(bg.get_top() + DOWN * 0.45)

            # Chú thích tiếng Việt
            t1 = Text(sub1, font="Arial", font_size=17, color=WHITE, weight=BOLD)
            t2 = Text(sub2, font="Arial", font_size=14, color=GRAY)
            txt_g = VGroup(t1, t2).arrange(DOWN, buff=0.1).next_to(m_tex, DOWN, buff=0.2)

            return bg, m_tex, txt_g, VGroup(bg, m_tex, txt_g)

        # 1. Thẻ H0 (Màu Đỏ Nhạt - Cảnh báo không có gì đặc biệt)
        h0_bg, h0_math, h0_txt, h0_card = create_hypo_card(
            ["H_0", ":", r"\mu_d", "=", "0"],
            "KHÔNG có sự khác biệt",
            "(Đội Thắng = Đội Thua)",
            "#FF7675",
            1.8  # Tọa độ Y
        )

        # Nhãn "Ngẫu nhiên" gắn vào H0
        random_txt = Text("Do ngẫu nhiên!", font="Arial", font_size=13, color=WHITE, weight=BOLD)
        random_bg = RoundedRectangle(corner_radius=0.1, width=random_txt.width + 0.4, height=random_txt.height + 0.2,
                                     fill_color="#FF7675", fill_opacity=0.8, stroke_width=0)
        h0_badge = VGroup(random_bg, random_txt).next_to(h0_bg, UP, buff=-0.2).shift(RIGHT * 1.5)

        # 2. Thẻ H1 (Màu Xanh Lá - Có sự khác biệt ý nghĩa)
        h1_bg, h1_math, h1_txt, h1_card = create_hypo_card(
            ["H_1", ":", r"\mu_d", r"\neq", "0"],
            "CÓ sự khác biệt thực sự",
            "(Đội Thắng khác Đội Thua)",
            "#1DD1A1",
            -0.4  # Tọa độ Y
        )

        # 3. Con dấu "BÁC BỎ?" (Stamp Effect)
        reject_txt = Text("BÁC BỎ H0?", font="Arial", font_size=32, color="#E74C3C", weight=BOLD)
        reject_bg = BackgroundRectangle(reject_txt, color=WHITE, fill_opacity=0.9, buff=0.15)
        reject_stamp = VGroup(reject_bg, reject_txt).move_to(h0_card.get_center()).rotate(PI / 8)

        # ======================================================================
        # DIỄN HOẠT KHỚP LỜI THOẠI
        # ======================================================================
        sync_subtitle(
            "Step one: state hypotheses.",
            "Bước một: đặt giả thuyết.",
            [], total_time=2.0
        )

        # Mở thẻ H0
        sync_subtitle(
            "The null hypothesis — denoted as H zero — states that:",
            "Giả thuyết không — ký hiệu H không — phát biểu rằng:",
            [DrawBorderThenFill(h0_bg), Write(h0_math[0:2])], total_time=3.5
        )

        sync_subtitle(
            "There is NO real difference in shots on target between winners and losers;",
            "KHÔNG có sự khác biệt thực sự về số cú sút trúng đích giữa đội thắng và thua;",
            [Write(h0_math[2:]), FadeIn(h0_txt, shift=UP * 0.2)], total_time=5.0
        )

        sync_subtitle(
            "any difference observed is just due to random chance.",
            "mọi chênh lệch ta quan sát chỉ là do ngẫu nhiên.",
            [FadeIn(h0_badge, shift=DOWN * 0.2)], total_time=3.5
        )

        # Mở thẻ H1
        sync_subtitle(
            "The alternative hypothesis — denoted as H one — states that:",
            "Giả thuyết thay thế — ký hiệu H một — phát biểu rằng:",
            [DrawBorderThenFill(h1_bg), Write(h1_math[0:2])], total_time=3.5
        )

        sync_subtitle(
            "THERE IS a statistically significant difference.",
            "CÓ sự khác biệt có ý nghĩa thống kê.",
            [Write(h1_math[2:]), FadeIn(h1_txt, shift=UP * 0.2)], total_time=3.0
        )

        # Hiệu ứng Final Punchline (Đóng dấu Bác bỏ)
        sync_subtitle(
            "The goal of the test is: is the evidence from data strong enough...",
            "Mục tiêu của kiểm định là: bằng chứng từ dữ liệu có đủ mạnh...",
            [h0_bg.animate.set_fill("#FF7675", opacity=0.3)], total_time=3.0
        )

        sync_subtitle(
            "...to reject the null hypothesis H zero?",
            "...để bác bỏ H không không?",
            [FadeIn(reject_stamp, scale=2.0), Wiggle(reject_stamp, rotation_angle=0.05, scale_value=1.1)],
            total_time=2.5
        )

        self.wait(1)