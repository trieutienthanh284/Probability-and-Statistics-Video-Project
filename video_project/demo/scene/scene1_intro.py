from manim import *

# Cấu hình video dọc 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class IntroScene(Scene):
    def construct(self):

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
        ).move_to(UP * 3.8)

        # NHÂN VẬT
        character = ImageMobject("video_project/demo/assets/images/DoMixi.png")\
            .scale(1.15)\
            .move_to(DOWN * 1.5)

        character.shift(DOWN * 1.8)

        # Nhân vật + chữ xuất hiện
        self.play(
            character.animate.shift(UP * 1.8),
            FadeIn(character, scale=0.9),
            Write(title),
            run_time=2.0,
            lag_ratio=0.05
        )

        # Pulse nhẹ
        self.play(
            character.animate.scale(1.05),
            title.animate.scale(1.03),
            rate_func=there_and_back,
            run_time=0.7
        )

        # Thoát cảnh
        self.play(
            FadeOut(character),
            FadeOut(title),
            run_time=0.8
        )