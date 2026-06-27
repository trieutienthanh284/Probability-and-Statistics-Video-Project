from base_scene import TikTokBaseScene
from manim import *


class HypothesisStep5(TikTokBaseScene):
    def construct(self):
        # 1. Header chính phân cảnh
        self.add_header("BƯỚC 5")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            # TIÊU CHUẨN BAN ĐẦU: Khóa giới hạn chiều rộng 6.8
            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            # TIÊU CHUẨN BAN ĐẦU: Neo phụ đề ở đáy với buff=1.0
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: Ô KẾT LUẬN LỚN "BÁC BỎ H0" (ĐÃ FIX LỖI FONT H0)
        # ======================================================================
        t_bacbo = Text("BÁC BỎ", font="Arial", font_size=28, color=WHITE, weight=BOLD)
        t_h0 = MathTex("H_0", font_size=36, color=WHITE)
        stamp_txt = VGroup(t_bacbo, t_h0).arrange(RIGHT, buff=0.15)

        stamp_bg = RoundedRectangle(corner_radius=0.15, width=stamp_txt.width + 0.8, height=stamp_txt.height + 0.4,
                                    fill_color="#1A6B3C", fill_opacity=0.85,
                                    stroke_color=WHITE, stroke_width=2.5)

        stamp_group = VGroup(stamp_bg, stamp_txt).move_to(UP * 2.4)

        # ======================================================================
        # PHẦN 2: THE CARD TÓM TẮT CHỈ SỐ (XẾP DỌC, ÔM VỪA KHÍT)
        # ======================================================================
        stat1 = MathTex("T = 12.41", font_size=36, color=WHITE)
        stat2 = MathTex(r"p\text{-value} = 1.4 \times 10^{-28}", font_size=36, color=YELLOW)
        stat3 = MathTex(r"t_{\text{critical}} = \pm 1.97", font_size=36, color=WHITE)
        stat4 = MathTex(r"95\% \text{ CI: } [+2.04; +2.81]", font_size=36, color=WHITE)

        stats_table = VGroup(stat1, stat2, stat3, stat4).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary_box = SurroundingRectangle(stats_table, corner_radius=0.2, color=GRAY, fill_color=BLACK,
                                           fill_opacity=0.5, stroke_width=2, buff=0.35)

        full_card = VGroup(summary_box, stats_table).move_to(UP * 0.4)

        # ======================================================================
        # PHẦN 3: CÂU KẾT LUẬN THỰC TẾ (ĐÃ HẠ XUỐNG DOWN * 2.2 ĐỂ PHÂN BỔ THOÁNG)
        # ======================================================================
        conc_g1 = Text("Đội thắng sút trúng đích NHIỀU HƠN", font="Arial", font_size=16, color=YELLOW, weight=BOLD)
        conc_g2 = Text("đội thua trung bình 2.4 cú / trận.", font="Arial", font_size=16, color=WHITE, weight=BOLD)

        sog_main = Text(" SHOTS ON GOAL ", font="Arial", font_size=16, color=BLACK, weight=BOLD)
        sog_bg = RoundedRectangle(corner_radius=0.1, width=sog_main.width + 0.2, height=sog_main.height + 0.1,
                                  fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sog_badge = VGroup(sog_bg, sog_main)

        conc_g3_prefix = Text("—", font="Arial", font_size=16, color=GRAY)
        conc_g3_suffix = Text("quyết định thắng thua —", font="Arial", font_size=16, color=GRAY, slant=ITALIC)

        conc_g3 = VGroup(conc_g3_prefix, sog_badge, conc_g3_suffix).arrange(RIGHT, buff=0.15)

        # ĐÃ FIX: Chuyển từ DOWN * 1.5 xuống DOWN * 2.2 giúp kết cấu khít và đẹp mắt hơn
        conclusion_block = VGroup(conc_g1, conc_g2, conc_g3).arrange(DOWN, buff=0.2).move_to(DOWN * 2.2)

        # ======================================================================
        # DIỄN HOẠT ĐỒNG BỘ CHÍNH XÁC THEO TIMING LỜI THOẠI (GIỮ NGUYÊN)
        # ======================================================================

        # Ý 1: Phát biểu kết luận dựa trên giá trị T
        sync_subtitle(
            "Step five: conclusion. T of 12.41 is much larger than 1.97 —",
            "Bước năm: kết luận. T bằng 12.41 lớn hơn nhiều so với ngưỡng 1.97 —",
            [FadeIn(stamp_group, scale=1.2)], total_time=4.5
        )

        sync_subtitle(
            "we reject the null hypothesis with extremely high confidence.",
            "chúng ta bác bỏ giả thuyết không với mức tin cậy cực cao.",
            [Circumscribe(stamp_bg, color=WHITE, time_width=1.5)], total_time=4.5
        )

        # Ý 2: Hiện bảng thông số
        sync_subtitle(
            "The p-value is calculated as 1.4 times 10 to the power of minus 28 —",
            "P-value tính ra bằng 1.4 nhân 10 mũ âm 28 —",
            [FadeIn(full_card, shift=UP * 0.2)], total_time=4.5
        )

        # Highlight p-value
        sync_subtitle(
            "practically, this is a probability of zero.",
            "về mặt thực tiễn đây là xác suất bằng 0.",
            [Indicate(stat2, color=YELLOW, scale_factor=1.25)], total_time=3.5
        )

        # Ý 3: Phân tích Khoảng tin cậy 95% CI
        sync_subtitle(
            "The 95% confidence interval for the difference is from 2.04 to 2.81 shots —",
            "Khoảng tin cậy 95% cho hiệu số là từ 2.04 đến 2.81 cú sút —",
            [Indicate(stat4, color=WHITE, scale_factor=1.15)], total_time=5.0
        )

        sync_subtitle(
            "this entire interval is greater than 0, excluding 'no difference'.",
            "toàn bộ khoảng này lớn hơn 0, tức không bao gồm trường hợp bằng 0.",
            [], total_time=4.5
        )

        # Ý 4: Viết câu kết luận thực tế
        sync_subtitle(
            "Conclusion in plain language: there is extremely strong statistical evidence...",
            "Kết luận thực tế: có bằng chứng thống kê cực kỳ mạnh rằng...",
            [Write(conc_g1)], total_time=4.5
        )

        sync_subtitle(
            "...that winning teams shoot on target more than losing teams by 2.4 shots.",
            "...đội thắng sút trúng đích nhiều hơn đội thua trung bình 2.4 cú/trận.",
            [Write(conc_g2)], total_time=4.5
        )

        # Ý 5: Chốt hạ cực cháy với Badge Shots on Goal
        sync_subtitle(
            "Answer to the opening question: Yes — Shots on Goal is a true differentiator.",
            "Câu trả lời đầu video: Đúng — Shots on Goal là yếu tố phân biệt thực sự.",
            [
                FadeIn(conc_g3, shift=UP * 0.1),
                Circumscribe(conclusion_block, color=YELLOW, time_width=2.0)
            ], total_time=5.0
        )

        self.wait(1)