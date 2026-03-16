from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ExplanationScene(Scene):
    def construct(self):

        icon_path = "video_project/demo/assets/icons/man.png"

        people = Group()

        icon_scale = 0.1
        spacing = 0.6

        # =========================
        # GRID ICON (ĐẨY LÊN CAO)
        # =========================

        for i in range(100):

            p = ImageMobject(icon_path).scale(icon_scale)

            row = i // 10
            col = i % 10

            p.move_to(
                UP * (5.5 - row * spacing) +
                LEFT * (2.7 - col * spacing)
            )

            people.add(p)

        self.play(FadeIn(people), run_time=1.5)

        # =========================
        # PRIOR PROBABILITY
        # =========================

        eq0 = MathTex(
            r"P(\mathrm{Good}) = 0.3,\quad P(\mathrm{Average}) = 0.7",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.5)

        self.play(Write(eq0))
        self.wait(0.5)

        self.play(
            people[:30].animate.set_color(GREEN),
            people[30:].animate.set_color(ORANGE),
            run_time=1.2
        )

        # =========================
        # PROBABILITY PASS 3 ROUNDS
        # =========================

        eq1 = MathTex(
            r"P(\mathrm{Pass\ 3}|Good) = 0.8 \times 0.85 \times 0.9 = 0.612",
            font_size=26,
            color=BLUE
        ).next_to(eq0, DOWN, buff=0.4)

        self.play(Write(eq1))
        self.wait(0.5)

        # good pass 3 rounds = 18
        self.play(
            people[:18].animate.set_color(BLUE),
            run_time=1.3
        )

        # =========================
        # BAD PASS PROBABILITY
        # =========================

        eq2 = MathTex(
            r"P(\mathrm{Pass\ 3}|Average) = 0.5 \times 0.4 \times 0.3 = 0.06",
            font_size=26,
            color=RED
        ).next_to(eq1, DOWN, buff=0.4)

        self.play(Write(eq2))
        self.wait(0.5)

        # bad pass = 4
        self.play(
            people[30:34].animate.set_color(RED),
            run_time=1.3
        )

        # =========================
        # TOTAL PROBABILITY
        # =========================

        eq3 = MathTex(
            r"P(\mathrm{Pass\ 3}) = 0.3 \times 0.612 + 0.7 \times 0.06 = 0.2256",
            font_size=26,
            color=YELLOW
        ).next_to(eq2, DOWN, buff=0.4)

        self.play(Write(eq3))
        self.wait(0.5)

        # =========================
        # BAYES
        # =========================

        eq4 = MathTex(
            r"P(\mathrm{Good}|Pass) = \frac{0.612\times0.3}{0.2256} = 0.814",
            font_size=28,
            color=PURPLE
        ).next_to(eq3, DOWN, buff=0.4)

        self.play(Write(eq4))
        self.wait(0.5)

        # highlight final good candidates
        self.play(
            people[:18].animate.set_color(GREEN),
            run_time=1.2
        )

        # =========================
        # EXPECTED VALUE
        # =========================

        eq5 = MathTex(
            r"E = 0.814 \times 800 + 0.186 \times (-300) = 595.4 > 0",
            font_size=28,
            color=WHITE
        ).next_to(eq4, DOWN, buff=0.4)

        self.play(Write(eq5))

        conclusion = Text(
            "HIRE ALL",
            font_size=36,
            color=GREEN
        ).next_to(eq5, DOWN)

        self.play(FadeIn(conclusion))

        self.wait(2)