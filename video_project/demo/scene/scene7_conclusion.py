from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ConclusionScene(Scene):
    def construct(self):
        # ==================================================
        # SETTINGS
        # ==================================================
        logo_pos = UP * 6
        sub_pos = DOWN * 3.8

        # ==================================================
        # LOGO
        # ==================================================
        logo = ImageMobject(
            "video_project/demo/assets/images/fami.png"
        ).scale(0.3).move_to(logo_pos)

        self.add(logo)

        # ==================================================
        # SUBTITLE BOX FUNCTION
        # ==================================================
        def create_dual_sub(en, vi):
            max_w = config.frame_width - 1.2
            en_text = Paragraph(
                en, font="Arial", font_size=20,
                weight=BOLD, alignment="center", width=max_w
            ).set_color(WHITE)
            vi_text = Paragraph(
                vi, font="Arial", font_size=18,
                alignment="center", width=max_w
            ).set_color(YELLOW)
            text_group = VGroup(en_text, vi_text).arrange(DOWN, buff=0.15)
            frame = SurroundingRectangle(
                text_group, color=WHITE, buff=0.3,
                stroke_width=2, corner_radius=0.1
            )
            background = BackgroundRectangle(
                frame, color=BLACK, fill_opacity=0.5, buff=0
            )
            full_sub = VGroup(background, frame, text_group).move_to(sub_pos)
            full_sub.set_z_index(100)
            return full_sub

        # ==================================================
        # PART 1 : FORMULA SUMMARY
        # ==================================================
        sub1 = create_dual_sub(
            "Remember the Multiplication and Total Probability rules to solve key metrics,",
            "Cần nhớ công thức nhân và xác suất toàn phần để giải quyết các thông số,"
        )
        sub1b = create_dual_sub(
            "and Bayes' Theorem to find candidate probabilities and expected value.",
            "và công thức Bayes để tính xác suất, từ đó tính giá trị kỳ vọng."
        )

        summary1 = ImageMobject("video_project/demo/assets/images/conclusion.png").scale(0.45).move_to(UP * 5)
        mul = MathTex(r"P(A \cap B) = P(A) \cdot P(B \mid A)", font_size=32)
        total = MathTex(r"P(B) = P(B \mid G)P(G) + P(B \mid \overline{G})P(\overline{G})", font_size=28)
        bayes = MathTex(r"P(G \mid B) = \frac{P(B \mid G)P(G)}{P(B)}", font_size=32)
        expect = MathTex(r"E = 800P(G \mid \text{Pass}) - 300P(\overline{G} \mid \text{Pass})", font_size=28)

        formulas_top = VGroup(mul, total).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        arrow = Arrow(UP, DOWN, color=YELLOW, stroke_width=6).scale(0.45)
        formulas_bottom = VGroup(bayes, expect).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        formula_block = VGroup(formulas_top, arrow, formulas_bottom).arrange(DOWN, buff=0.35).move_to(DOWN * 0.2)

        self.play(FadeIn(summary1), FadeIn(sub1))
        self.play(LaggedStart(Write(mul), Write(total), lag_ratio=0.4))
        self.play(Create(arrow))
        self.play(ReplacementTransform(sub1, sub1b), LaggedStart(Write(bayes), Write(expect), lag_ratio=0.4))
        self.wait(2)
        self.play(FadeOut(Group(summary1, formula_block, sub1b)))

        # ==================================================
        # PART 2 : KEYWORDS
        # ==================================================
        sub2 = create_dual_sub(
            "Key keywords: Multiplication Rule, Total Probability, Bayes, and Expected Value.",
            "Các từ khóa: công thức nhân, công thức toàn phần, Bayes, Kỳ vọng."
        )
        summary2 = ImageMobject("video_project/demo/assets/images/ttkw.png").scale(0.45).move_to(UP * 3.5)
        keywords_data = [
            ("Multiplication Rule", "video_project/demo/assets/icons/x.png"),
            ("Total Probability", "video_project/demo/assets/icons/full.png"),
            ("Bayes' Theorem", "video_project/demo/assets/icons/search.png"),
            ("Expected Value", "video_project/demo/assets/icons/expectation.png"),
        ]

        rows = []
        for text, icon_path in keywords_data:
            icon = ImageMobject(icon_path).scale(0.1)
            label = Text(text, font_size=30)
            if text == "Bayes' Theorem": label.set_color(YELLOW)
            row = Group(icon, label).arrange(RIGHT, buff=0.4)
            rows.append(row)

        keyword_rows = Group(*rows).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(DOWN * 0.5)

        self.play(FadeIn(summary2), FadeIn(sub2))
        self.play(LaggedStart(*[FadeIn(row, shift=RIGHT * 0.3) for row in keyword_rows], lag_ratio=0.8))
        self.wait(2)
        self.play(FadeOut(Group(summary2, keyword_rows, sub2)))

        # ==================================================
        # PART 3 : FINAL QUESTION (WITH BOBBING EFFECT)
        # ==================================================
        sub3 = create_dual_sub(
            "Is the actual productivity really what we expected?",
            "Tuyển rồi thì năng suất thực tế có đúng như kỳ vọng không?"
        )

        final_icon = ImageMobject(
            "video_project/demo/assets/icons/question-mark.png"
        ).scale(0.6).move_to(UP * 1.5)

        # --- HIỆU ỨNG NỔI (BOBBING) ---
        # Lưu vị trí gốc để tính toán dao động
        final_icon.initial_y = final_icon.get_y()

        def bobbing_effect(mobject, dt):
            # dt là thời gian trôi qua, nhưng chúng ta dùng thời gian thực của scene
            t = self.renderer.time
            # Biên độ: 0.2 unit, Tốc độ: 3 rad/s
            new_y = mobject.initial_y + 0.2 * np.sin(3 * t)
            mobject.set_y(new_y)

        question = Text(
            "Is the actual productivity\nreally what we expected?",
            font_size=36, color=YELLOW, line_spacing=1.2
        ).next_to(final_icon, DOWN, buff=0.8)

        self.play(
            FadeIn(final_icon, scale=1.2),
            FadeIn(sub3)
        )

        # Bắt đầu hiệu ứng nổi ngay sau khi xuất hiện
        final_icon.add_updater(bobbing_effect)

        self.play(Write(question))
        self.wait(4)  # Tăng thời gian chờ để thấy rõ hiệu ứng nổi

        # ==================================================
        # END SCENE
        # ==================================================
        # Xóa updater trước khi kết thúc để tránh lỗi tính toán vị trí khi FadeOut
        final_icon.clear_updaters()

        others = Group(*[m for m in self.mobjects if m != logo])
        self.play(FadeOut(others))