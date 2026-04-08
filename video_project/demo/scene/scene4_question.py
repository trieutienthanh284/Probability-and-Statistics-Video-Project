from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class Question(Scene):
    def construct(self):
        # ── SETTINGS ──
        logo_pos = UP * 6
        sub_pos = DOWN * 3.8

        # ── LOGO ──
        logo = ImageMobject("video_project/demo/assets/images/fami.png").scale(0.3).move_to(logo_pos)
        self.add(logo)

        # ── HÀM SUBTITLE ──
        def create_dual_sub(en, vi):
            max_w = config.frame_width - 1.5

            en_text = Paragraph(
                en, font="Arial", font_size=22, weight=BOLD,
                alignment="center", width=max_w
            ).set_color(WHITE)

            vi_text = Paragraph(
                vi, font="Arial", font_size=18,
                alignment="center", width=max_w
            ).set_color(YELLOW)

            group = VGroup(en_text, vi_text).arrange(DOWN, buff=0.15).move_to(sub_pos)
            return group

        # ==============================
        # SCENE 1
        # ==============================

        top_image = ImageMobject(
            "video_project/demo/assets/images/analyst.png"
        ).scale_to_fit_width(3.6).move_to(UP * 3.6)

        profit_icon = ImageMobject(
            "video_project/demo/assets/icons/profit.png"
        ).scale(0.22)

        risk_icon = ImageMobject(
            "video_project/demo/assets/icons/risk.png"
        ).scale(0.22)

        profit_note = MarkupText(
            "<b><span foreground='#2ecc71'>+ 800 tr/năm</span></b>",
            font_size=28
        )

        risk_note = MarkupText(
            "<b><span foreground='#e74c3c'>- 300 tr/năm</span></b>",
            font_size=28
        )

        profit_group = Group(profit_icon, profit_note).arrange(RIGHT, buff=0.4)
        risk_group = Group(risk_icon, risk_note).arrange(RIGHT, buff=0.4)

        icons_block = Group(
            profit_group,
            risk_group
        ).arrange(
            DOWN,
            buff=0.6
        ).move_to(UP * 0.8)

        sub1 = create_dual_sub(
            "Hiring a strong candidate brings 800M VND/year, while a weak one costs 300M VND/year.",
            "Biết rằng: Tuyển đúng người giỏi lợi 800 triệu, tuyển nhầm người yếu hại 300 triệu."
        )

        self.play(FadeIn(top_image), FadeIn(sub1))
        self.play(FadeIn(icons_block))

        self.wait(3)

        self.play(
            FadeOut(top_image),
            FadeOut(icons_block),
            FadeOut(sub1)
        )

        # ==============================
        # SCENE 2
        # ==============================

        top_image2 = ImageMobject(
            "video_project/demo/assets/images/decision.png"
        ).scale_to_fit_width(4).move_to(UP * 3.4)

        question_icon = ImageMobject(
            "video_project/demo/assets/icons/problem.png"
        ).scale(0.4).move_to(UP * 0.3)

        sub2 = create_dual_sub(
            "Should the company hire all candidates who pass the 3 rounds?",
            "Ban lãnh đạo hỏi: Có nên tuyển tất cả ứng viên vượt qua 3 vòng hay không?"
        )

        self.play(FadeIn(top_image2), FadeIn(sub2))
        self.play(FadeIn(question_icon, shift=UP * 0.3))
        self.wait(3)

        self.play(FadeOut(question_icon), FadeOut(sub2))

        # ==============================
        # SCENE 3
        # ==============================

        top_image3 = ImageMobject(
            "video_project/demo/assets/images/solution-mindset.png"
        ).scale_to_fit_width(3.5).move_to(UP * 3.6)

        formula = ImageMobject(
            "video_project/demo/assets/formula/expectation.png"
        ).scale_to_fit_width(5.5).move_to(UP * 0.5).set_color(WHITE)

        sub3 = create_dual_sub(
            "We need to calculate the expected value of a hired candidate: E(X) = Σ xi·pi",
            "Ta cần tính kỳ vọng khi tuyển một ứng viên: E(X) = Σ xi·pi = ..."
        )

        self.play(
            FadeOut(top_image2),
            FadeIn(top_image3),
            run_time=0.8
        )

        self.play(FadeIn(formula), FadeIn(sub3))

        surprise_icon = ImageMobject(
            "video_project/demo/assets/icons/surprise.png"
        ).scale(0.4).move_to(DOWN * 1.8)

        # delay 0.5s
        self.wait(0.5)

        self.play(FadeIn(surprise_icon, shift=UP * 0.3))

        self.wait(4)