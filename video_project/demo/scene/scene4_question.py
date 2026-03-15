from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class Question(Scene):
    def construct(self):
        # ==============================
        # SCENE 1 — BUSINESS CONTEXT (~8s)
        # ==============================

        top_image = ImageMobject(
            "video_project/demo/assets/images/analyst.png"
        ).scale_to_fit_width(5).move_to(UP * 4.8)

        profit_icon = ImageMobject(
            "video_project/demo/assets/icons/profit.png"
        ).scale(0.25).move_to(LEFT * 2.6 + UP * 1.6)

        risk_icon = ImageMobject(
            "video_project/demo/assets/icons/risk.png"
        ).scale(0.25).move_to(LEFT * 2.6 + DOWN * 1.2)

        profit_note = MarkupText(
            "<b><span foreground='green'>↑ 800 tr/năm</span></b>",
            font_size=44
        ).next_to(profit_icon, RIGHT, buff=0.6)

        risk_note = MarkupText(
            "<b><span foreground='red'>↓ 300 tr/năm</span></b>",
            font_size=44
        ).next_to(risk_icon, RIGHT, buff=0.6)

        self.play(FadeIn(top_image), run_time=0.8)

        self.play(
            FadeIn(profit_icon),
            Write(profit_note),
            run_time=2.5
        )

        self.play(
            FadeIn(risk_icon),
            Write(risk_note),
            run_time=2.5
        )

        self.wait(1.5)

        scene1 = Group(
            top_image,
            profit_icon,
            risk_icon,
            profit_note,
            risk_note
        )

        self.play(FadeOut(scene1), run_time=0.5)

        # ==============================
        # SCENE 2 — DECISION QUESTION (~10s)
        # ==============================

        # Giữ nguyên ảnh decision.png ở phân đoạn này theo yêu cầu
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
            font_size=30
        ).move_to(RIGHT * 1 + UP * 1.3)

        self.play(FadeIn(top_image2), run_time=0.8)

        self.play(
            FadeIn(question_icon),
            Write(question_text),
            run_time=3.0
        )
        self.wait(1.0)

        self.play(
            FadeOut(question_icon),
            FadeOut(question_text),
            run_time=0.4
        )

        # ==============================
        # SCENE 3 — SOLUTION & FORMULA
        # Khớp với: "Ta cần tính được kỳ vọng..."
        # ==============================

        # 1. Thay ảnh decision bằng solution-mindset
        top_image3 = ImageMobject(
            "video_project/demo/assets/images/solution-mindset.png"
        ).scale_to_fit_width(5).move_to(UP * 4.8)

        # Hiển thị ảnh solution-mindset trước
        self.play(
            FadeOut(top_image2, run_time=0.3),
            FadeIn(top_image3, run_time=0.6)
        )

        calc_icon = ImageMobject(
            "video_project/demo/assets/icons/idea.png"
        ).scale(0.25).move_to(LEFT * 2.6 + UP * 1.3)

        calc_text = Paragraph(
            "Let's calculate the",
            "expected economic value",
            "of a hired candidate",
            alignment="left",
            font_size=30
        ).move_to(RIGHT * 1 + UP * 1.3)

        # Kích thước công thức lớn (scale_to_fit_width=6)
        formula = ImageMobject(
            "video_project/demo/assets/formula/expectation.png"
        ).scale_to_fit_width(6).move_to(UP * 0.7)
        formula.set_color(WHITE)

        surprise_icon = ImageMobject(
            "video_project/demo/assets/icons/surprise.png"
        ).scale(0.4).next_to(formula, DOWN, buff=1.0)

        # Hiển thị text dẫn dắt
        self.play(
            FadeIn(calc_icon),
            Write(calc_text),
            run_time=2.0
        )

        self.wait(0.5)

        self.play(
            FadeOut(calc_icon),
            FadeOut(calc_text),
            run_time=0.4
        )

        # 2. Hiển thị ảnh công thức sau
        self.play(
            FadeIn(formula),
            run_time=1.0
        )
        self.wait(0.5)  # Chờ một chút trước khi hiện icon

        # 3. Cuối cùng mới đến ảnh icon surprise
        self.play(
            FadeIn(surprise_icon, shift=UP * 0.5),  # Hiệu ứng nhảy lên nhẹ
            run_time=0.8
        )

        self.wait(2.0)