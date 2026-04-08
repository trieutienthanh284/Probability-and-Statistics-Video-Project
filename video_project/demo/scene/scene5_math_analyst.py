from manim import *

# Vertical 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class MathAnalystScene(Scene):
    def construct(self):

        # ======================
        # LOGO + SUB POSITION
        # ======================

        logo_pos = UP * 6
        sub_pos = DOWN * 3.8

        logo = ImageMobject(
            "video_project/demo/assets/images/fami.png"
        ).scale(0.3).move_to(logo_pos)

        self.add(logo)

        def create_dual_sub(en, vi):
            max_w = config.frame_width - 1.5

            en_text = Paragraph(
                en,
                font="Arial",
                font_size=22,
                weight=BOLD,
                alignment="center",
                width=max_w
            ).set_color(WHITE)

            vi_text = Paragraph(
                vi,
                font="Arial",
                font_size=18,
                alignment="center",
                width=max_w
            ).set_color(YELLOW)

            return VGroup(en_text, vi_text).arrange(
                DOWN, buff=0.15
            ).move_to(sub_pos)

        sub = create_dual_sub(
            "We compute prior probabilities and conditional probabilities for each interview round.",
            "Ta xác định xác suất tiên nghiệm và xác suất điều kiện của từng vòng phỏng vấn."
        )

        # vị trí công thức (đẩy xuống để tránh logo)
        RIGHT_X = -1
        ICON_SCALE = 0.3

        # ======================
        # PRIOR
        # ======================

        p_good = MathTex(
            r"P(\text{Good}) = 0.3",
            font_size=42
        ).set_color(GREEN)

        p_bad = MathTex(
            r"P(\text{Not Good}) = 0.7",
            font_size=42
        ).set_color(RED)

        priors = VGroup(p_good, p_bad).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )

        # đẩy xuống thấp hơn để không đụng logo
        priors.move_to([RIGHT_X, 4.2, 0], aligned_edge=LEFT)

        main_icon = ImageMobject(
            "video_project/demo/assets/icons/calculating.png"
        ).scale(ICON_SCALE)

        main_icon.next_to(priors, LEFT, buff=0.6)

        # ======================
        # GOOD
        # ======================

        v1_good = MathTex(
            r"P(R1 \mid \text{Good}) = 0.8",
            font_size=40
        ).set_color(GREEN)

        v2_good = MathTex(
            r"P(R2 \mid \text{Good}) = 0.85",
            font_size=40
        ).set_color(GREEN)

        v3_good = MathTex(
            r"P(R3 \mid \text{Good}) = 0.9",
            font_size=40
        ).set_color(GREEN)

        good_group = VGroup(
            v1_good, v2_good, v3_good
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.45
        )

        good_group.next_to(priors, DOWN, buff=1.3, aligned_edge=LEFT)

        good_icon = ImageMobject(
            "video_project/demo/assets/icons/quality.png"
        ).scale(ICON_SCALE)

        good_icon.next_to(good_group, LEFT, buff=0.6)

        # ======================
        # NOT GOOD
        # ======================

        v1_bad = MathTex(
            r"P(R1 \mid \text{Not Good}) = 0.5",
            font_size=40
        ).set_color(RED)

        v2_bad = MathTex(
            r"P(R2 \mid \text{Not Good}) = 0.4",
            font_size=40
        ).set_color(RED)

        v3_bad = MathTex(
            r"P(R3 \mid \text{Not Good}) = 0.3",
            font_size=40
        ).set_color(RED)

        bad_group = VGroup(
            v1_bad, v2_bad, v3_bad
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.45
        )

        bad_group.next_to(good_group, DOWN, buff=1.3, aligned_edge=LEFT)

        bad_icon = ImageMobject(
            "video_project/demo/assets/icons/switch.png"
        ).scale(ICON_SCALE)

        bad_icon.next_to(bad_group, LEFT, buff=0.6)

        # ======================
        # ANIMATION
        # ======================

        self.play(FadeIn(sub))

        self.play(FadeIn(main_icon), run_time=1)

        self.play(Write(p_good), run_time=1.2)
        self.play(Write(p_bad), run_time=1.2)

        self.wait(0.4)

        self.play(FadeIn(good_icon, shift=RIGHT), run_time=0.8)

        self.play(Write(v1_good), run_time=1.1)
        self.play(Write(v2_good), run_time=1.1)
        self.play(Write(v3_good), run_time=1.1)

        self.wait(0.4)

        self.play(FadeIn(bad_icon, shift=RIGHT), run_time=0.8)

        self.play(Write(v1_bad), run_time=1.1)
        self.play(Write(v2_bad), run_time=1.1)
        self.play(Write(v3_bad), run_time=1.1)

        self.wait(2)

        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.2
        )