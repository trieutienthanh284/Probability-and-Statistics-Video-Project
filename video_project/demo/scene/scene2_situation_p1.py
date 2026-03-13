from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class SituationScene(Scene):
    def construct(self):
        text = Text("Công ty IT cần tuyển 100 kỹ sư phần mềm", font_size=40)
        self.play(Write(text))
        self.wait(1)
        
        prob = MathTex(r"P(\text{Giỏi}) = 0.3 \quad P(\text{Trung bình}) = 0.7", font_size=48).next_to(text, DOWN, buff=1)
        self.play(Write(prob))
        self.wait(2)
        
        self.play(FadeOut(VGroup(text, prob)))