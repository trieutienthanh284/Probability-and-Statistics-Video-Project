from manim import *


class IntroScene(Scene):
    def construct(self):
        title = Text("Ứng dụng Xác suất trong Cây Quyết định", font_size=48, color=BLUE)
        subtitle = Text("Tuyển dụng Kỹ sư phần mềm – Decision Tree", font_size=36, color=YELLOW).next_to(title, DOWN,
                                                                                                         buff=0.5)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)

        # Minh họa nhanh cây quyết định đơn giản
        tree = Text("Cây Quyết định", font_size=32, color=GREEN).shift(DOWN * 2)
        self.play(Write(tree))
        self.wait(2)

        self.play(FadeOut(VGroup(title, subtitle, tree)))