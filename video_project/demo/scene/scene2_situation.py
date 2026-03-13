from manim import *
from pathlib import Path

# ── CẤU HÌNH VIDEO DỌC 9:16 ──
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class SituationScene(Scene):

    # ── HÀM TẠO SUBTITLE TỰ ĐỘNG ──
    def create_subtitle(self, text):
        sub = MarkupText(
            text,
            font_size=26,
            weight=BOLD,
            justify=True
        )

        # giới hạn chiều rộng để tránh tràn màn hình
        sub.set_max_width(config.frame_width - 1)

        # luôn nằm dưới cùng màn hình
        sub.to_edge(DOWN, buff=2.2)

        # luôn nằm trên các object khác
        sub.set_z_index(10)

        return sub

    def construct(self):

        self.wait(0.5)

        # ── PATH ASSETS ──
        base_path = Path("video_project/demo/assets")
        icon_svg = base_path / "icons/user.svg"
        image_png = base_path / "images/key_insight.png"

        # ── BỐ CỤC ──
        Y_ICONS = 3.8
        Y_STATS = 1.4
        Y_IMAGE = -1.4

        good_color = GREEN
        bad_color = PURE_RED

        # ── ICON NGƯỜI ──
        icons = VGroup()

        for i in range(10):
            icon = SVGMobject(str(icon_svg)).scale(0.65)

            if i < 3:
                icon.set_color(good_color)
            else:
                icon.set_color(bad_color)

            icons.add(icon)

        icons.arrange_in_grid(rows=2, cols=5, buff=0.4)
        icons.move_to(UP * Y_ICONS)

        # ── TEXT PHẦN TRĂM ──
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

        # ── SUBTITLE ──
        subtitle1 = self.create_subtitle(
            "A technology company is recruiting\n"
            "for the Software Engineer position."
        )

        subtitle2 = self.create_subtitle(
            "According to statistics over many years, \n"
            "only about <span foreground='green'>30%</span> \n"
            "of candidates are truly excellent."
        )

        subtitle3 = self.create_subtitle(
            "while the remaining "
            "<span foreground='red'>70%</span>\n"
            "are average or weak."
        )

        # ── ANIMATION ──
        self.play(
            FadeIn(icons, lag_ratio=0.06, run_time=1.2),
            FadeIn(stats_group, run_time=1.0),
            FadeIn(bottom_image, run_time=1.0),
        )

        # subtitle 1
        self.play(Write(subtitle1), run_time=1.6)
        self.wait(2)
        self.play(FadeOut(subtitle1))

        # subtitle 2
        self.play(Write(subtitle2), run_time=1.8)

        self.play(
            percent_good.animate.scale(1.2),
            icons[:3].animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1.5
        )

        self.wait(1.5)
        self.play(FadeOut(subtitle2))

        # subtitle 3
        self.play(Write(subtitle3), run_time=1.6)

        self.play(
            percent_bad.animate.scale(1.2),
            icons[3:].animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.5
        )

        self.wait(1)

        # fade out toàn bộ
        self.play(
            FadeOut(
                Group(
                    icons,
                    stats_group,
                    bottom_image,
                    subtitle3
                )
            )
        )