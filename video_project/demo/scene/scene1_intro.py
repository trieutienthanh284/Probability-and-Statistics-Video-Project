from manim import *

class IntroScene(Scene):
    def construct(self):
        self.wait(0.5)

        # ── Thêm nhân vật (ảnh của bạn) ───────────────────────────────
        # Đặt tên file ảnh là character.png (hoặc đổi tên tùy ý)
        character = ImageMobject("Anh ộ i i.png") \
            .scale(0.6) \
            .to_edge(LEFT, buff=1.2) \
            .shift(DOWN * 0.8)   # điều chỉnh vị trí lên/xuống nếu cần

        # Có thể thêm hiệu ứng nhỏ cho nhân vật (tùy chọn)
        character.shift(LEFT * 2)  # bắt đầu từ ngoài màn hình bên trái

        # ── Dòng chữ chính ─────────────────────────────────────────────
        title = Text(
            "Bạn sẽ nắm được bí quyết tuyển dụng nhân sự tốt\nchỉ bằng một công thức",
            font_size=48,
            t2c={
                "bí quyết": YELLOW,
                "tuyển dụng": BLUE,
                "nhân sự tốt": GREEN,
                "một công thức": RED
            },
            line_spacing=0.9,
            weight=BOLD
        ).scale(0.9).next_to(character, RIGHT, buff=0.8).align_to(character, UP)

        # ── Animation ──────────────────────────────────────────────────
        # Nhân vật trượt vào từ bên trái + chữ hiện lên cùng lúc
        self.play(
            character.animate.shift(RIGHT * 2),   # trượt vào vị trí cuối
            Write(title, run_time=2.2),
            title.animate.set_color_by_gradient(BLUE, PURPLE, RED),
            run_time=2.2,
            lag_ratio=0.3   # nhân vật bắt đầu trước chữ một chút
        )

        # Pulse nhẹ cả nhân vật + chữ
        self.play(
            character.animate.scale(1.08),
            title.animate.scale(1.08).set_opacity(0.95),
            rate_func=there_and_back,
            run_time=0.8
        )

        self.wait(1.0)

        # Fade out cả hai
        self.play(
            FadeOut(character),
            FadeOut(title),
            run_time=0.7
        )

        self.wait(0.3)