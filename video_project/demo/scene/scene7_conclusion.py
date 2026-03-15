from manim import *

# Vertical video 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ConclusionScene(Scene):
    def construct(self):

        # ===================== PART 1: FORMULA SUMMARY =====================

        summary1 = ImageMobject(
            "video_project/demo/assets/images/conclusion.png"
        ).scale(0.55)

        mul = MathTex(
            r"P(A \cap B) = P(A) \cdot P(B \mid A)",
            font_size=36
        )

        total = MathTex(
            r"P(B) = P(B \mid G)P(G) + P(B \mid \neg G)P(\neg G)",
            font_size=36
        )

        bayes = MathTex(
            r"P(G \mid B) = \frac{P(B \mid G)P(G)}{P(B)}",
            font_size=40
        )

        expect = MathTex(
            r"E = 800 \cdot P(G \mid \text{Pass}) - 300 \cdot P(\neg G \mid \text{Pass})",
            font_size=36
        )

        formulas_top = VGroup(mul, total).arrange(DOWN, buff=0.8)

        arrow = Arrow(
            UP,
            DOWN,
            color=YELLOW,
            stroke_width=6
        ).scale(0.6)

        formulas_bottom = VGroup(bayes, expect).arrange(DOWN, buff=1)

        formula_block = VGroup(
            formulas_top,
            arrow,
            formulas_bottom
        ).arrange(DOWN, buff=0.7)

        part1_layout = Group(summary1, formula_block).arrange(
            DOWN,
            buff=1
        ).move_to(UP * 0.5)

        self.play(FadeIn(summary1))

        self.play(
            LaggedStart(*[Write(f) for f in formulas_top], lag_ratio=0.3)
        )

        self.play(Create(arrow))

        self.play(
            LaggedStart(*[Write(f) for f in formulas_bottom], lag_ratio=0.3)
        )

        self.wait(1.5)

        self.play(FadeOut(part1_layout))

        # ===================== PART 2: KEY CONCEPTS =====================

        summary2 = ImageMobject(
            "video_project/demo/assets/images/ttkw.png"
        ).scale(0.55)

        keywords_data = [
            ("Multiplication Rule", "video_project/demo/assets/icons/x.png"),
            ("Total Probability", "video_project/demo/assets/icons/full.png"),
            ("Bayes' Theorem", "video_project/demo/assets/icons/search.png"),
            ("Expected Value", "video_project/demo/assets/icons/expectation.png"),
        ]

        rows = []

        for text, icon_path in keywords_data:

            icon = ImageMobject(icon_path).scale(0.12)

            label = Text(text, font_size=32)

            if text == "Bayes' Theorem":
                label.set_color(YELLOW)

            row = Group(icon, label).arrange(
                RIGHT,
                buff=0.5
            )

            rows.append(row)

        keyword_rows = Group(*rows).arrange(
            DOWN,
            buff=0.9,
            aligned_edge=LEFT
        )

        content_block = Group(
            summary2,
            keyword_rows
        ).arrange(
            DOWN,
            buff=1.2
        )

        # Đưa block lên trên để chừa 1/4 phía dưới
        content_block.move_to(UP * 1.2)

        self.play(FadeIn(summary2))

        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.3) for row in keyword_rows],
                lag_ratio=0.8
            )
        )

        self.wait(2)

        self.play(FadeOut(content_block))

        # ===================== PART 3: FINAL QUESTION =====================

        final_icon = ImageMobject(
            "video_project/demo/assets/icons/question-mark.png"
        ).scale(0.8)

        question = Text(
            "Is the actual productivity\nreally what we expected?",
            font_size=36,
            color=YELLOW,
            line_spacing=1.2
        )

        final_block = Group(
            final_icon,
            question
        ).arrange(
            DOWN,
            buff=1
        ).move_to(UP * 1)

        self.play(FadeIn(final_icon, scale=1.2))

        self.play(Write(question))

        self.wait(2)