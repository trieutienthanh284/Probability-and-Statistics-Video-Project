from base_scene import TikTokBaseScene
from manim import *


class KeywordScene(TikTokBaseScene):
    def construct(self):
        self.add_header("TỪ KHÓA")

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

        def make_kw_badge(kw_parts):
            content = VGroup(*kw_parts).arrange(RIGHT, buff=0.1)
            # ĐÃ SỬA: Viền thẻ mỏng lại và ôm sát chữ hơn để tiết kiệm diện tích dọc
            bg = RoundedRectangle(corner_radius=0.15, width=content.width + 0.5, height=content.height + 0.35,
                                  fill_color="#1A6B3C", fill_opacity=0.95, stroke_width=2, stroke_color=WHITE)
            return Group(bg, content)

        # ĐÃ SỬA: Kích thước font giảm nhẹ (Text 18, MathTex 24) để 5 hàng lưới không bị tràn đáy
        badges = [
            make_kw_badge([Text("Kiểm định giả thuyết", font="Arial", font_size=18, color=WHITE, weight=BOLD)]),
            make_kw_badge([Text("Giả thuyết không /", font="Arial", font_size=18, color=WHITE, weight=BOLD),
                           MathTex("H_0", font_size=24, color=WHITE)]),
            make_kw_badge([Text("Giả thuyết thay thế /", font="Arial", font_size=18, color=WHITE, weight=BOLD),
                           MathTex("H_1", font_size=24, color=WHITE)]),
            make_kw_badge([Text("Paired T-test", font="Arial", font_size=18, color=WHITE, weight=BOLD)]),
            make_kw_badge([Text("Giá trị p (p-value)", font="Arial", font_size=18, color=WHITE, weight=BOLD)]),
            make_kw_badge([Text("Mức ý nghĩa", font="Arial", font_size=18, color=WHITE, weight=BOLD),
                           MathTex(r"\alpha", font_size=24, color=WHITE)]),
            make_kw_badge([Text("T-statistic", font="Arial", font_size=18, color=WHITE, weight=BOLD)]),
            make_kw_badge([Text("Khoảng tin cậy 95%", font="Arial", font_size=18, color=WHITE, weight=BOLD)]),
            make_kw_badge([Text("Kích thước hiệu ứng", font="Arial", font_size=18, color=WHITE, weight=BOLD)])
        ]

        # ĐÃ SỬA: Rút gọn khoảng cách lưới buff chiều dọc từ 0.4 xuống 0.25
        grid_top = Group(*badges[:8]).arrange_in_grid(cols=2, buff=(0.3, 0.25))
        badges[8].next_to(grid_top, DOWN, buff=0.25)

        # Đẩy cao lên UP * 0.3 để gánh độ cao của 5 hàng từ khóa
        full_grid = Group(grid_top, badges[8]).move_to(UP * 0.3)

        sync_subtitle("Keywords you should remember and explore further:",
                      "Các thuật ngữ cốt lõi bạn cần ghi nhớ và nghiên cứu thêm:", [], 3.5)

        for i in range(0, 9, 3):
            sync_subtitle("Learning more about statistical methods...",
                          "Hệ thống hóa kiến thức thông qua các từ khóa chuyên ngành...",
                          [LaggedStart(*[FadeIn(badges[j], scale=0.8) for j in range(i, min(i + 3, 9))],
                                       lag_ratio=0.3)], 4.5)

        self.play(full_grid.animate.scale(1.05).set_color(YELLOW), run_time=2.0)
        self.wait(1.5)