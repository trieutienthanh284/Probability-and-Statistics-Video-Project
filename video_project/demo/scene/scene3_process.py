from manim import *

class ProcessScene(Scene):
    def construct(self):
        title = Text("Quy trình 3 vòng lọc", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        
        rounds = VGroup(
            Text("Vòng 1: Lọc CV", font_size=32).shift(LEFT*4),
            Text("Vòng 2: Phỏng vấn", font_size=32),
            Text("Vòng 3: Test kỹ thuật", font_size=32).shift(RIGHT*4)
        ).arrange(RIGHT, buff=2).shift(DOWN*1)
        
        self.play(Write(rounds))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, rounds)))

        