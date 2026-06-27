from base_scene import TikTokBaseScene
from manim import *


class ComparisonScene(TikTokBaseScene):
    def construct(self):
        self.add_header("PHÂN TÍCH ĐỐI CHIẾU")

        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        def create_comp_card(title_str, stats_tex, conc_parts, color_theme, pos_y):
            box = RoundedRectangle(corner_radius=0.25, width=6.8, height=2.2, color=color_theme, fill_color=BLACK,
                                   fill_opacity=0.7, stroke_width=4).move_to(UP * pos_y)
            lbl_title = Text(title_str, font="Arial", font_size=32, color=color_theme, weight=BOLD).move_to(
                box.get_top() + DOWN * 0.45)
            lbl_stats = MathTex(stats_tex, font_size=42, color=WHITE).next_to(lbl_title, DOWN, buff=0.25)
            lbl_conc = VGroup(*conc_parts).arrange(RIGHT, buff=0.08).next_to(lbl_stats, DOWN, buff=0.25)
            return VGroup(box, lbl_title, lbl_stats, lbl_conc)

        c1_parts = [Text("CÓ Ý NGHĨA THỐNG KÊ (BÁC BỎ ", font="Arial", font_size=20, color="#1DD1A1", weight=BOLD),
                    MathTex("H_0", font_size=26, color="#1DD1A1"),
                    Text(")", font="Arial", font_size=20, color="#1DD1A1", weight=BOLD)]
        card_shots = create_comp_card("DỨT ĐIỂM TRÚNG ĐÍCH", r"T = 12.41 \quad | \quad p \approx 0", c1_parts,
                                      "#1DD1A1", 1.4)

        c2_parts = [
            Text("KHÔNG Ý NGHĨA (CHƯA ĐỦ BẰNG CHỨNG BÁC BỎ ", font="Arial", font_size=18, color="#E74C3C", weight=BOLD),
            MathTex("H_0", font_size=24, color="#E74C3C"),
            Text(")", font="Arial", font_size=18, color="#E74C3C", weight=BOLD)]
        card_poss = create_comp_card("TỶ LỆ KIỂM SOÁT BÓNG", r"T = 0.60 \quad | \quad p = 0.55", c2_parts, "#E74C3C",
                                     -1.0)

        sync_subtitle("Here is the visual comparison between the two tests.",
                      "Đây là kết quả so sánh trực quan giữa hai kiểm định.", [], 4.0)
        sync_subtitle("Shots on Goal: T is 12.41, p-value is near 0 — statistically significant.",
                      "Dứt điểm trúng đích: T = 12.41, p ≈ 0 — có ý nghĩa thống kê.",
                      [FadeIn(card_shots, shift=UP * 0.3)], 5.0)
        sync_subtitle("Ball Possession: T is 0.60, p-value is 0.55 — not statistically significant.",
                      "Kiểm soát bóng: T = 0.60, p = 0.55 — không có ý nghĩa thống kê.",
                      [FadeIn(card_poss, shift=UP * 0.3)], 5.5)

        sync_subtitle("Important lesson: hypothesis testing not only confirms what is true,",
                      "Kiểm định giả thuyết không chỉ giúp xác nhận các giả định đúng,",
                      [Indicate(card_shots, color="#1DD1A1")], 4.5)
        sync_subtitle("but also helps us detect what is false.", "mà còn giúp bác bỏ các trực giác sai lầm thực tế.",
                      [Indicate(card_poss, color="#E74C3C")], 3.5)

        self.wait(1)