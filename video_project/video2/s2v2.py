from manim import *

# Cấu hình màn hình dọc 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9


class RandomArrival(Scene):
    def construct(self):
        # 1. Logo Fami
        try:
            logo = ImageMobject("video_project/demo/assets/images/fami.png")
            logo.width = 1.5
            logo.to_edge(UP, buff=0.4)
        except:
            logo = Text("LOGO", color=GREY).to_edge(UP, buff=0.4)
        self.add(logo)

        # 2. Hàm tạo Subtitle
        def create_bilingual_sub(vn_text, en_text):
            en = Text(en_text, font="Arial", font_size=19, color=WHITE)
            vn = Text(vn_text, font="Arial", font_size=19, color=YELLOW)
            sub_group = VGroup(en, vn).arrange(DOWN, buff=0.15)
            background_rect = SurroundingRectangle(
                sub_group, color=WHITE, fill_color=BLACK, fill_opacity=0.8, buff=0.3
            )
            return VGroup(background_rect, sub_group).move_to(DOWN * 3.8)

        # 3. Icon Siêu thị & Đồng hồ (Sửa kim giờ thành 3h)
        try:
            market = ImageMobject("video_project/video2/assets2/supermarket.png")
            market.height = 3.0
            market.shift(UP * 2)
        except:
            market = Rectangle(height=3, width=4, color=GRAY).shift(UP * 2)

        clock_circle = Circle(radius=0.5, color=WHITE)
        minute_hand = Line(ORIGIN, UP * 0.4, color=RED)  # Chỉ 12h
        hour_hand = Line(ORIGIN, RIGHT * 0.25, color=WHITE)  # SỬA: Chỉ 3h (RIGHT)

        clock = VGroup(clock_circle, minute_hand, hour_hand).next_to(market, LEFT, buff=0.5).shift(UP * 0.5)
        time_label = Text("15:00", font="Arial", font_size=24).next_to(clock, DOWN, buff=0.1)

        # 4. Hàm tạo khách hàng (Size 1.01)
        def create_customer_icon():
            try:
                c = ImageMobject("video_project/video2/assets2/customer.png")
                c.height = 1.01
                return c
            except:
                return Dot(radius=0.3, color=BLUE)

        # --- TIẾN TRÌNH VIDEO ---
        self.play(FadeIn(logo))
        self.play(FadeIn(market), Create(clock), Write(time_label))

        sub = create_bilingual_sub(
            "Đồng hồ chỉ 15:00, khách hàng bước vào không đều.",
            "The clock strikes 15:00, customers arrive inconsistently."
        )
        self.play(FadeIn(sub))
        self.wait(0.5)

        # LOGIC: 3 người đến -> đi vào -> biến mất
        group_3 = Group(*[create_customer_icon() for _ in range(3)]).arrange(RIGHT, buff=0.5)
        group_3.move_to(DOWN * 1.5)

        self.play(FadeIn(group_3, lag_ratio=0.2, shift=UP * 0.5))
        self.play(
            group_3.animate.move_to(market.get_center()).scale(0.2).set_opacity(0),
            run_time=2
        )

        # LOGIC: 0 người (Khoảng lặng)
        self.wait(1)

        # LOGIC: 7 người đến -> đi vào -> biến mất
        sub_update = create_bilingual_sub(
            "Khi 3 người, khi 0 người, khi dồn 7 người.",
            "Sometimes 3, sometimes 0, then suddenly 7 people."
        )
        self.play(ReplacementTransform(sub, sub_update))

        # Để tránh đè nhau, 7 người được xếp thành 2 hàng nhỏ trước khi đi vào
        group_7 = Group(*[create_customer_icon() for _ in range(7)]).arrange_in_grid(2, 4, buff=0.4)
        group_7.move_to(DOWN * 1.5)

        self.play(FadeIn(group_7, lag_ratio=0.1, shift=UP * 0.5))

        # Di chuyển dồn dập vào siêu thị và tan biến
        move_to_market = []
        for person in group_7:
            move_to_market.append(
                Succession(
                    person.animate.move_to(market.get_center()).scale(0.1),
                    FadeOut(person)
                )
            )

        self.play(AnimationGroup(*move_to_market, lag_ratio=0.1), run_time=3)

        self.wait(0.5)