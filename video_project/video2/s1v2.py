from manim import *

# Cấu hình màn hình dọc 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9


class QueueSimulation(Scene):
    def construct(self):
        # 1. Chèn Logo Fami
        try:
            logo = ImageMobject("video_project/demo/assets/images/fami.png")
            logo.width = 1.5
            logo.to_edge(UP, buff=0.4)
        except:
            logo = Text("LOGO", color=GREY).to_edge(UP, buff=0.4)
        self.add(logo)

        # 2. Hàm tạo Subtitle (Font Arial, Size 19, Tọa độ -3.8)
        def create_bilingual_sub(vn_text, en_text):
            en = Text(en_text, font="Arial", font_size=19, color=WHITE)
            vn = Text(vn_text, font="Arial", font_size=19, color=YELLOW)
            sub_group = VGroup(en, vn).arrange(DOWN, buff=0.15)
            background_rect = SurroundingRectangle(
                sub_group, color=WHITE, fill_color=BLACK, fill_opacity=0.8, buff=0.3
            )
            return VGroup(background_rect, sub_group).move_to(DOWN * 3.8)

        # 3. Quầy thanh toán (Nâng lên UP * 4.5)
        counter_1 = Rectangle(height=0.8, width=2.2, color=BLUE, fill_opacity=0.8).shift(UP * 4.5)
        label_1 = Text("Quầy 1", font="Arial", font_size=22).next_to(counter_1, UP, buff=0.2)

        # 4. Khởi tạo khách hàng (Kích thước lớn 1.01)
        def create_customer(img_path):
            try:
                customer = ImageMobject(img_path)
                customer.height = 1.01
                return customer
            except:
                return Dot(radius=0.3, color=RED)

        path_angry = "video_project/video2/assets2/angry.png"
        path_happy = "video_project/video2/assets2/satisfied.png"

        queue_left = Group(*[create_customer(path_angry) for _ in range(4)])
        queue_right = Group(*[create_customer(path_angry) for _ in range(4)])

        # THAY ĐỔI CHÍNH Ở ĐÂY:
        # buff=0.65: Thu hẹp khoảng cách dọc giữa các icon
        # buff=0.3 trong next_to: Kéo hàng người sát lên Quầy 1 hơn
        queue_left.arrange(DOWN, buff=0.65).next_to(counter_1, DOWN, buff=0.3).shift(LEFT * 1.3)
        queue_right.arrange(DOWN, buff=0.65).next_to(counter_1, DOWN, buff=0.3).shift(RIGHT * 1.3)

        full_queue = Group(queue_left, queue_right)

        # --- TIẾN TRÌNH VIDEO ---
        self.play(FadeIn(logo))

        # Cảnh 1: Chật kín người
        sub1 = create_bilingual_sub(
            "Hôm nay bạn đi siêu thị, quầy thanh toán chật kín người.",
            "Today you go to supermarket, the checkout is crowded."
        )
        self.play(Create(counter_1), Write(label_1))
        self.play(FadeIn(full_queue, lag_ratio=0.1, shift=UP * 0.2), FadeIn(sub1))
        self.wait(2)
        self.play(FadeOut(sub1))

        # Cảnh 2: Mở thêm quầy
        counter_2 = counter_1.copy().scale(0.8).shift(LEFT * 2.8 + DOWN * 0.8)
        label_2 = Text("Quầy 2", font="Arial", font_size=20).next_to(counter_2, UP)
        counter_3 = counter_1.copy().scale(0.8).shift(RIGHT * 2.8 + DOWN * 0.8)
        label_3 = Text("Quầy 3", font="Arial", font_size=20).next_to(counter_3, UP)

        sub2 = create_bilingual_sub(
            "Nhưng bỗng nhiên, thêm 2 quầy nữa mở ra...",
            "But suddenly, two more counters opened..."
        )

        happy_anims = []
        new_happy_people = Group()

        for person in [*queue_left, *queue_right]:
            happy_p = create_customer(path_happy)
            happy_p.move_to(person.get_center())
            new_happy_people.add(happy_p)
            happy_anims.append(FadeTransform(person, happy_p))

        self.play(
            FadeIn(sub2),
            ReplacementTransform(counter_1.copy(), counter_2),
            ReplacementTransform(counter_1.copy(), counter_3),
            Write(label_2), Write(label_3),
            *happy_anims,
            run_time=1.5
        )
        self.wait(1)

        # Cảnh 3: Tan biến
        sub3 = create_bilingual_sub(
            "Ngày mai, cùng giờ đó, lại chẳng có ai chờ.",
            "Tomorrow, at the same time, no one is waiting."
        )
        self.play(FadeOut(sub2), FadeIn(sub3))

        move_anims = []
        for i, p in enumerate(new_happy_people):
            if i % 3 == 0:
                target = counter_1.get_center()
            elif i % 3 == 1:
                target = counter_2.get_center()
            else:
                target = counter_3.get_center()

            move_anims.append(Succession(
                p.animate.move_to(target).scale(0.3),
                FadeOut(p)
            ))

        self.play(AnimationGroup(*move_anims, lag_ratio=0.1), run_time=2.5)
        self.play(FadeOut(sub3))

        # Cảnh 4: Kết luận
        sub4 = create_bilingual_sub(
            "Điều gì đứng sau sự biến động này?",
            "What stands behind this fluctuation?"
        )
        self.play(FadeIn(sub4))
        self.wait(3)