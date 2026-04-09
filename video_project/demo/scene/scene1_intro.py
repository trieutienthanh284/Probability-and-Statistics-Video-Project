from manim import *

# Cấu hình video dọc 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class IntroScene(Scene):
    def construct(self):

        # LOGO TRÊN CÙNG
        logo = ImageMobject("video_project/demo/assets/images/fami.png")\
            .scale(0.3)\
            .move_to(UP * 6)

        # PHẦN CHỮ
        title = MarkupText(
            f'<span weight="bold">Nắm <span color="{YELLOW}">bí quyết</span>\n'
            f'<span color="{BLUE}">tuyển dụng</span> <span color="{GREEN}">nhân sự</span>\n'
            f'chỉ bằng\n'
            f'<span color="{RED}">MỘT công thức</span></span>',
            font="Be Vietnam Pro",
            font_size=44,
            line_spacing=1.5,
            justify=True
        ).move_to(UP * 2.2)

        # ===== 2 HÌNH THAY CHO NHÂN VẬT =====
        bayes_img = ImageMobject("video_project/demo/assets/images/bayes-theorem.png")\
            .scale(0.45)\
            .move_to(DOWN * 2.5 + LEFT * 1.5)

        prob_img = ImageMobject("video_project/demo/assets/images/probability.png")\
            .scale(0.45)\
            .move_to(DOWN * 2.5 + RIGHT * 1.5)

        # Animation intro
        self.play(
            FadeIn(logo, shift=DOWN),
            Write(title),
            run_time=1.5
        )

        # Ảnh 1 xuất hiện
        self.play(
            FadeIn(bayes_img, shift=UP, scale=0.4),
            run_time=0.5
        )

        # Ảnh 2 xuất hiện sau (lần lượt)
        self.play(
            FadeIn(prob_img, shift=UP, scale=0.4),
            run_time=0.5
        )

        # Pulse nhẹ cho cả cụm
        self.play(
            bayes_img.animate.scale(1.05),
            prob_img.animate.scale(1.05),
            title.animate.scale(1.03),
            rate_func=there_and_back,
            run_time=0.5
        )

        # Thoát cảnh
        self.play(
            FadeOut(bayes_img),
            FadeOut(prob_img),
            FadeOut(title),
            FadeOut(logo),
            run_time=0.4
        )