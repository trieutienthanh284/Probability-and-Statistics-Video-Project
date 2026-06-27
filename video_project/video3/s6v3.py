from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class InsuranceScale(TikTokBaseScene):
    def construct(self):
        # Header của phân cảnh
        self.add_header("ỨNG DỤNG THỰC TẾ")

        asset_path = "video_project/video3/assets/"
        np.random.seed(42)

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            # Khóa chiều rộng tối đa (Max Width) để không bị tràn màn hình dọc
            max_width = 6.8

            if e_sub.width > max_width:
                e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width:
                v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)

            bg = RoundedRectangle(
                corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4,
                color=BLACK, fill_opacity=0.85, stroke_width=2, stroke_color=WHITE
            )
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time, rate_func=linear)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: ICON VÀ SỐ LƯỢNG N
        # ======================================================================
        tracker = ValueTracker(0.0)

        try:
            rating_icon = ImageMobject(asset_path + "rating.png").scale_to_fit_height(0.6)
            x_sign = Text("×", font="Arial", font_size=28, color=WHITE)

            fixed_part = Group(rating_icon, x_sign).arrange(RIGHT, buff=0.15).move_to(UP * 2.2 + LEFT * 0.8)

            n_val_text = always_redraw(lambda:
                                       Text(f"{int(10 ** tracker.get_value()):,}", font="Arial", font_size=32,
                                            color=YELLOW, weight=BOLD)
                                       .next_to(fixed_part, RIGHT, buff=0.2)
                                       )
            self.add(fixed_part, n_val_text)
        except Exception as e:
            print("Thiếu rating.png:", e)

        # ======================================================================
        # PHẦN 2: THIẾT LẬP BIỂU ĐỒ
        # ======================================================================
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 0.4, 0.1],
            x_length=6.5, y_length=4.5,
            axis_config={"color": GRAY, "stroke_width": 3}
        ).move_to(DOWN * 1.0 + RIGHT * 0.2)

        x_labels = VGroup(
            *[Text(txt, font="Arial", font_size=16, color=WHITE, weight=BOLD).next_to(axes.c2p(pos, 0), DOWN, buff=0.2)
              for pos, txt in zip([0, 1, 2, 3, 4, 5], ["1", "10", "100", "1K", "10K", "100K"])])
        y_labels = VGroup(*[
            Text(f"{pos}", font="Arial", font_size=16, color=WHITE, weight=BOLD).next_to(axes.c2p(0, pos), LEFT,
                                                                                         buff=0.2) for pos in
            [0, 0.1, 0.2, 0.3, 0.4]])

        dashed_line = DashedLine(axes.c2p(0, 0.05), axes.c2p(5, 0.05), color=YELLOW, stroke_width=4)
        lbl_05 = Text("5% Dự báo", font="Arial", font_size=16, color=YELLOW, weight=BOLD)
        lbl_05.next_to(dashed_line, UP, buff=0.4).align_to(axes.x_axis, RIGHT)

        y_title = Text("Tỷ lệ tai nạn thực tế", font="Arial", font_size=16, color=GRAY, weight=BOLD)
        y_title.next_to(axes.c2p(0, 0.4), UP, buff=0.2).align_to(axes.y_axis, LEFT)

        x_title = Text("Số lượng khách hàng (N)", font="Arial", font_size=16, color=GRAY, weight=BOLD)
        x_title.next_to(axes, DOWN, buff=0.7)

        self.play(FadeIn(axes, x_labels, y_labels, dashed_line, lbl_05, x_title, y_title), run_time=1)

        # ======================================================================
        # PHẦN 3: ĐƯỜNG XÁC SUẤT ĐỘNG (Đã sửa logic dao động cho N<=10)
        # ======================================================================
        log_n = np.linspace(0, 5, 500)
        n_values = np.unique(np.round(10 ** log_n).astype(int))
        ratios = []
        for n in n_values:
            if n <= 10:
                # Dao động ngẫu nhiên nhảy liên tục từ 0 đến 0.3 (0% - 30%)
                r = np.random.uniform(0.0, 0.3)
            else:
                noise = np.random.uniform(-0.4, 0.4) / (n ** 0.4)
                r = 0.05 + noise
            ratios.append(max(0, min(0.4, r)))  # Ép giới hạn từ 0 đến 0.4

        def get_curve():
            t = tracker.get_value()
            pts = [axes.c2p(np.log10(n), r) for n, r in zip(n_values, ratios) if np.log10(n) <= t]
            if len(pts) < 2: return VMobject()
            return VMobject(color="#00FFFF", stroke_width=4).set_points_as_corners(pts)

        curve = always_redraw(get_curve)
        self.add(curve)

        # ======================================================================
        # CHẠY PHÂN CẢNH & SUBTITLE
        # ======================================================================
        sync_subtitle(
            "Insurance companies have millions of customers.",
            "Công ty bảo hiểm có hàng triệu khách hàng độc lập.",
            [tracker.animate.set_value(1.0)], total_time=2.5
        )

        sync_subtitle(
            "With 10 customers, the rate is unpredictable (0-30%).",
            "Với 10 khách hàng, tỷ lệ tai nạn là không thể đoán trước.",
            [], total_time=3.0
        )

        sync_subtitle(
            "As N grows, the rate flattens towards 5%.",
            "Khi N tăng lên, tỷ lệ thực tế phẳng dần về mức 5%.",
            [tracker.animate.set_value(3.5)], total_time=3.5
        )

        sync_subtitle(
            "The Law of Large Numbers makes the business stable.",
            "Luật số lớn giúp việc kinh doanh trở nên ổn định.",
            [tracker.animate.set_value(5.0)], total_time=3.0
        )

        sync_subtitle(
            "They need to know HOW MANY, not WHO.",
            "Họ không cần biết AI bị nạn, chỉ cần biết BAO NHIÊU người.",
            [], total_time=3.5
        )

        self.play(Circumscribe(dashed_line, color=YELLOW, time_width=1.5), run_time=1.5)

        sync_subtitle(
            "And that's how they avoid bankruptcy.",
            "Và đó là cách họ đảm bảo không bao giờ phá sản.",
            [], total_time=3.0
        )

        self.wait(1)