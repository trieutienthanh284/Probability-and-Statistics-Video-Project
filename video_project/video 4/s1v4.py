from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class FootballHypothesisIntro(TikTokBaseScene):
    def construct(self):
        # 1. Header chính của phân cảnh
        self.add_header("DỮ LIỆU & BÓNG ĐÁ")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
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

        # ======================================================================
        # PHẦN 1: MÔ PHỎNG PHA SÚT BÓNG (2D Pixel-art Style)
        # ======================================================================

        # Tạo cầu môn bằng hình chữ nhật
        goal_post = Rectangle(width=4.2, height=2.2, color=WHITE, stroke_width=4).move_to(UP * 1.5)
        # SỬA LỖI Ở ĐÂY: Dùng DashedVMobject thay vì DashedRectangle
        goal_net = DashedVMobject(goal_post.copy(), num_dashes=40).set_color(GRAY).set_stroke(width=1).set_opacity(0.5)
        goal_group = VGroup(goal_post, goal_net)

        self.play(FadeIn(goal_group), run_time=0.8)

        # --- Pha sút 1: Chệch khung thành (Miss) ---
        ball = Dot(color=YELLOW, radius=0.15).move_to(DOWN * 1.5)
        miss_target = UP * 2.8 + LEFT * 2.8
        arrow_miss = Line(ball.get_center(), miss_target, color=GRAY, stroke_width=2).add_tip(tip_length=0.2)

        txt_miss = Text("0 GOALS", font="Arial", font_size=32, color=RED, weight=BOLD).move_to(UP * 2.8 + LEFT * 1.2)

        sync_subtitle(
            "People often say: the team that shoots more on target wins.",
            "Người ta vẫn hay nói: đội nào sút trúng đích nhiều hơn thì thắng.",
            [Create(arrow_miss), ball.animate.move_to(miss_target)], total_time=3.5
        )

        self.play(Write(txt_miss), run_time=0.5)

        sync_subtitle(
            "But is this just a 'feeling' from watching football?",
            "Nhưng đây chỉ là 'cảm giác' từ việc xem bóng đá?",
            [FadeOut(arrow_miss), FadeOut(txt_miss), ball.animate.move_to(DOWN * 1.5)], total_time=3.0
        )

        # --- Pha sút 2: Vào góc hiểm (Goal) ---
        goal_target = UP * 2.2 + RIGHT * 1.8
        arrow_goal = Line(ball.get_center(), goal_target, color=GRAY, stroke_width=2).add_tip(tip_length=0.2)

        txt_goal = Text("GOAL!", font="Arial", font_size=36, color=GREEN, weight=BOLD).move_to(UP * 1.5)

        sync_subtitle(
            "Or is it a truth that can be verified with data and statistics?",
            "Hay đây là một sự thật có thể kiểm chứng bằng dữ liệu và thống kê?",
            [Create(arrow_goal), ball.animate.move_to(goal_target)], total_time=3.5
        )

        self.play(Write(txt_goal), Flash(goal_target, color=GREEN, flash_radius=0.5))

        # --- Đặt Câu Hỏi Lớn ---
        self.play(FadeOut(goal_group), FadeOut(arrow_goal), FadeOut(ball), FadeOut(txt_goal))

        q1 = Text("Đội sút TRÚNG ĐÍCH nhiều hơn", font="Arial", font_size=24, color=WHITE, weight=BOLD)
        q2 = Text("thì THẮNG — thật sự đúng không?", font="Arial", font_size=24, color=WHITE, weight=BOLD)
        question_block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(UP * 1.5)

        highlight_box = SurroundingRectangle(question_block, color=YELLOW, buff=0.3, stroke_width=3)

        sync_subtitle(
            "Today, we will answer that using a mathematical tool: Hypothesis Testing.",
            "Hôm nay, chúng ta sẽ trả lời câu hỏi đó bằng Kiểm định giả thuyết.",
            [Write(question_block), Create(highlight_box)], total_time=4.0
        )

        self.play(FadeOut(question_block), FadeOut(highlight_box))

        # ======================================================================
        # PHẦN 2: GIỚI THIỆU MỤC LỤC 3 PHẦN
        # ======================================================================

        def create_card(title_text):
            card_bg = RoundedRectangle(
                corner_radius=0.15, width=6.5, height=1.1,
                fill_color="#00FF00", fill_opacity=0.15, stroke_color="#00FF00", stroke_width=2
            )
            card_txt = Text(title_text, font="Arial", font_size=22, color=WHITE, weight=BOLD)
            return Group(card_bg, card_txt)

        card1 = create_card("1. Kiểm định giả thuyết là gì?")
        card2 = create_card("2. Bài toán từ dữ liệu thực tế")
        card3 = create_card("3. Kết quả cực kỳ bất ngờ")

        cards_group = Group(card1, card2, card3).arrange(DOWN, buff=0.4).move_to(UP * 0.5)

        fade_in_cards = LaggedStart(
            *[FadeIn(card, shift=UP * 0.5) for card in cards_group],
            lag_ratio=0.4
        )

        sync_subtitle(
            "In this video, we will go through three parts.",
            "Trong video này, chúng ta sẽ đi qua ba phần chính.",
            [fade_in_cards], total_time=3.5
        )

        self.play(Indicate(card1, scale_factor=1.05, color=GREEN), run_time=0.8)
        sync_subtitle(
            "One: quickly understand the hypothesis testing process.",
            "Một: hiểu nhanh quy trình kiểm định giả thuyết trong thống kê.",
            [], total_time=3.5
        )

        self.play(Indicate(card2, scale_factor=1.05, color=GREEN), run_time=0.8)
        sync_subtitle(
            "Two: apply directly to 380 Premier League matches of the 24-25 season.",
            "Hai: áp dụng trực tiếp vào 380 trận đấu Premier League mùa 24-25.",
            [], total_time=4.0
        )

        self.play(Indicate(card3, scale_factor=1.05, color=YELLOW), run_time=0.8)
        self.play(Circumscribe(card3, color=YELLOW, time_width=1.5))

        sync_subtitle(
            "And three: a surprising result that contradicts most fans' expectations.",
            "Và ba: một kết quả bất ngờ mà hầu hết người xem bóng đá đều nghĩ ngược lại.",
            [], total_time=4.5
        )

        self.wait(1)