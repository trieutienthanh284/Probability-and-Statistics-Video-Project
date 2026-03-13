from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class Question(Scene):
    def construct(self):

        # ==============================
        # SCENE 1 — BUSINESS CONTEXT
        # ==============================

        top_image = ImageMobject(
            "video_project/demo/assets/images/analyst.png"
        ).scale_to_fit_width(5).move_to(UP * 4.8)

        # ICON (giảm size ~3-4 lần)
        profit_icon = ImageMobject(
            "video_project/demo/assets/icons/profit.png"
        ).scale(0.25).move_to(LEFT * 2.6 + UP * 1.6)

        risk_icon = ImageMobject(
            "video_project/demo/assets/icons/risk.png"
        ).scale(0.25).move_to(LEFT * 2.6 + DOWN * 1.2)

        # NOTE (font nhỏ hơn + arrow fix)
        profit_note = MarkupText(
            "<b><span foreground='green'>↑ 800 triệu / năm</span></b>",
            font_size=47
        ).next_to(profit_icon, RIGHT, buff=0.6)

        risk_note = MarkupText(
            "<b><span foreground='red'>↓ 300 triệu / năm</span></b>",
            font_size=47
        ).next_to(risk_icon, RIGHT, buff=0.6)

        # Animation scene 1 (≈7s)

        self.play(FadeIn(top_image), run_time=1.2)

        self.wait(0.4)

        self.play(
            FadeIn(profit_icon),
            Write(profit_note),
            run_time=2.2
        )

        self.wait(0.5)

        self.play(
            FadeIn(risk_icon),
            Write(risk_note),
            run_time=2.0
        )

        self.wait(0.7)

        scene1 = Group(
            top_image,
            profit_icon,
            risk_icon,
            profit_note,
            risk_note
        )

        self.play(FadeOut(scene1), run_time=0.6)

        # ==============================
        # SCENE 2 — DECISION QUESTION
        # ==============================

        top_image2 = ImageMobject(
            "video_project/demo/assets/images/decision.png"
        ).scale_to_fit_width(5).move_to(UP * 4.8)

        question_icon = ImageMobject(
            "video_project/demo/assets/icons/problem.png"
        ).scale(0.25).move_to(LEFT * 2.6 + UP * 1.3)

        question_text = Paragraph(
            "Should the company hire",
            "all candidates",
            "who pass the 3 rounds?",
            alignment="left",
            font_size=39
        ).move_to(RIGHT * 2 + UP * 1.3)

        calc_icon = ImageMobject(
            "video_project/demo/assets/icons/idea.png"
        ).scale(0.25).move_to(LEFT * 2.6 + UP * 1.3)

        calc_text = Paragraph(
            "Let's calculate the",
            "expected economic value",
            "of a hired candidate",
            alignment="left",
            font_size=39
        ).move_to(RIGHT * 2 + UP * 1.3)

        formula = ImageMobject(
            "video_project/demo/assets/images/expectation-formula.png"
        ).scale_to_fit_width(4).move_to(UP * 0.7)

        # Animation scene 2 (≈11s)

        self.play(FadeIn(top_image2), run_time=1.0)

        self.wait(0.6)

        # câu hỏi
        self.play(
            FadeIn(question_icon),
            Write(question_text),
            run_time=3.2
        )

        self.wait(1.0)

        # chuyển sang phần tính
        self.play(
            FadeOut(question_icon),
            FadeOut(question_text),
            run_time=0.8
        )

        self.play(
            FadeIn(calc_icon),
            Write(calc_text),
            run_time=3.0
        )

        self.wait(0.8)

        # icon2 + text2 biến mất → formula xuất hiện
        self.play(
            FadeOut(calc_icon),
            FadeOut(calc_text),
            run_time=0.7
        )

        self.play(
            FadeIn(formula),
            run_time=2.0
        )

        self.wait(1.0)