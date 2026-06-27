from base_scene import TikTokBaseScene
from manim import *


class IntroLLN(TikTokBaseScene):
    def construct(self):
        self.add_header("LUẬT SỐ LỚN")

        # Chữ Luật số lớn to rõ, chiếm trọng tâm màn hình
        main_text = Text("Luật số lớn", font="Arial", font_size=85, color="#40E0D0")

        self.play(Write(main_text), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(main_text, run_time=0.8))

        try:
            q_mark = ImageMobject("video_project/video3/assets/question-mark.png")
            # Phóng to ảnh dấu hỏi
            q_mark.scale_to_fit_height(3.5)
            self.play(FadeIn(q_mark, scale=1.2), run_time=1)
            self.wait(1)
        except Exception as e:
            print("Lỗi tải ảnh dấu hỏi:", e)

        self.play_subtitle(
            "Applications of the Law of Large Numbers in practice",
            "Ứng dụng của Luật số lớn trong thực tế",
            duration=4
        )
        self.wait(1)