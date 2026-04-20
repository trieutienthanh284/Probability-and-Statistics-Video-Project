from manim import *
from pathlib import Path

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class SituationScene(Scene):

    # REALTIME SUBTITLE - ĐÃ CHỈNH SỬA ĐỂ THÊM KHUNG VIỀN
    def create_realtime_sub(self, en, vi):
        # Xác định chiều rộng tối đa cho phép (trừ đi lề hai bên)
        max_w = config.frame_width - 1.5

        en_text = Paragraph(
            en,
            font="Arial",
            font_size=18,
            weight=BOLD,
            alignment="center",
            width=max_w
        ).set_color(WHITE)

        vi_text = Paragraph(
            vi,
            font="Arial",
            font_size=18,
            alignment="center",
            width=max_w
        ).set_color(YELLOW)

        text_group = VGroup(en_text, vi_text).arrange(
            DOWN,
            buff=0.2
        )

        # Tạo khung viền bao quanh text_group
        # buff: khoảng cách giữa chữ và viền
        # corner_radius: độ bo góc của khung
        frame = SurroundingRectangle(
            text_group,
            color=WHITE,
            buff=0.3,
            stroke_width=2,
            corner_radius=0.1
        )

        # Thêm một lớp nền mờ phía sau khung (tùy chọn, giúp dễ đọc hơn)
        background = BackgroundRectangle(frame, color=BLACK, fill_opacity=0.5, buff=0)

        # Gộp tất cả vào một group
        group = VGroup(background, frame, text_group)

        # Căn giữa group và đưa xuống dưới cùng
        group.move_to(DOWN * 3.6)
        group.set_z_index(100)

        return group

    def construct(self):

        # ── LOGO ──
        logo = ImageMobject(
            "video_project/demo/assets/images/fami.png"
        ).scale(0.3).move_to(UP * 6)

        self.add(logo)

        # ── PATH ASSETS ──
        base_path = Path("video_project/demo/assets")
        icon_svg = base_path / "icons/user.svg"
        image_png = base_path / "images/key_insight.png"

        Y_ICONS = 3.8
        Y_STATS = 1.4
        Y_IMAGE = -1.4

        good_color = GREEN
        bad_color = PURE_RED

        # ── ICON ──
        icons = VGroup()

        for i in range(10):
            icon = SVGMobject(str(icon_svg)).scale(0.35)

            if i < 3:
                icon.set_color(good_color)
            else:
                icon.set_color(bad_color)

            icons.add(icon)

        icons.arrange_in_grid(rows=2, cols=5, buff=0.4)
        icons.move_to(UP * Y_ICONS)

        # ── TEXT ──
        percent_good = Text(
            "30% good candidate",
            font_size=48,
            weight=BOLD
        ).set_color(good_color)

        percent_bad = Text(
            "70% others",
            font_size=48,
            weight=BOLD
        ).set_color(bad_color)

        stats_group = VGroup(percent_good, percent_bad).arrange(DOWN, buff=0.3)
        stats_group.move_to(UP * Y_STATS)

        # ── IMAGE ──
        bottom_image = ImageMobject(str(image_png))
        bottom_image.scale_to_fit_width(7.5)
        bottom_image.move_to(UP * Y_IMAGE)

        # ── REALTIME SUBTITLE ──
        sub1 = self.create_realtime_sub(
            "A technology company is recruiting for the Software Engineer position.",
            "Một công ty công nghệ (IT) đang tuyển dụng vị trí Kỹ sư phần mềm."
        )

        sub2 = self.create_realtime_sub(
            "Based on many years of statistics, only about 30% are truly strong candidates.",
            "Theo thống kê nhiều năm, chỉ khoảng 30% ứng viên thực sự là ứng viên giỏi."
        )

        sub3 = self.create_realtime_sub(
            "The remaining 70% are average or weak candidates.",
            "Còn lại 70% là ứng viên trung bình hoặc yếu."
        )

        # ── INTRO ANIMATION ──
        self.play(
            FadeIn(icons, lag_ratio=0.05, run_time=1),
            FadeIn(stats_group, run_time=0.9),
            FadeIn(bottom_image, run_time=0.9),
        )

        # SUB 1
        self.play(FadeIn(sub1), run_time=0.3)
        self.wait(1.7)
        self.play(FadeOut(sub1), run_time=0.2)

        # SUB 2
        self.play(FadeIn(sub2), run_time=0.3)

        self.play(
            percent_good.animate.scale(1.2),
            icons[:3].animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1.2
        )

        self.wait(0.5)
        self.play(FadeOut(sub2), run_time=0.2)

        # SUB 3
        self.play(FadeIn(sub3), run_time=0.3)

        self.play(
            percent_bad.animate.scale(1.2),
            icons[3:].animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.1
        )

        self.wait(0.5)

        # FADE OUT
        self.play(
            FadeOut(
                Group(
                    icons,
                    stats_group,
                    bottom_image,
                    sub3
                )
            ),
            run_time=0.6
        )