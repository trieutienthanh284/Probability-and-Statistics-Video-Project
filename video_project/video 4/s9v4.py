from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class PossessionTwist(TikTokBaseScene):
    def construct(self):
        # 1. Header chính phân cảnh
        self.add_header("TỶ LỆ CẦM BÓNG")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            # Chuẩn màn hình dọc ban đầu
            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            # Neo phụ đề ở đáy với buff=1.0
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: ĐẶT CÂU HỎI VÀ ICON QUẢ BÓNG XOAY TRÒN (TRÊN CÙNG)
        # ======================================================================
        q_txt = Text("Nhưng nếu xét tỷ lệ Cầm bóng?", font="Arial", font_size=20, color=WHITE, weight=BOLD).move_to(
            UP * 2.5)

        # Icon quả bóng
        ball_outer = Circle(radius=0.25, color=WHITE, stroke_width=2)
        ball_inner = RegularPolygon(n=5, radius=0.1, color=WHITE, fill_opacity=1).move_to(ball_outer.get_center())
        ball_lines = VGroup(
            *[Line(ball_inner.get_vertices()[i], ball_outer.get_all_points()[i * 6], color=WHITE, stroke_width=1.5) for
              i in range(5)])
        ball_icon = VGroup(ball_outer, ball_inner, ball_lines).next_to(q_txt, RIGHT, buff=0.25)

        # ======================================================================
        # PHẦN 2: THẺ CARD TÓM TẮT CHỈ SỐ CẦM BÓNG & KIỂM ĐỊNH (GIỮA MÀN HÌNH)
        # ======================================================================
        card_box = RoundedRectangle(corner_radius=0.2, width=6.4, height=2.4, color=GRAY, fill_color=BLACK,
                                    fill_opacity=0.5, stroke_width=2).move_to(UP * 0.4)

        # Số liệu thực tế
        d1 = Text("Đội thắng: 50.38%  |  Đội thua: 49.62%", font="Arial", font_size=15, color=WHITE).shift(UP * 1.0)
        d2 = Text("Chênh lệch hiệu số: chỉ 0.76%", font="Arial", font_size=14, color=GRAY, slant=ITALIC).next_to(d1,
                                                                                                                 DOWN,
                                                                                                                 buff=0.1)

        # Kết quả Paired T-test
        t1 = MathTex("T = 0.60", font_size=30, color=WHITE)
        t2 = MathTex(r"p\text{-value} = 0.55", font_size=30, color=WHITE)
        t3 = MathTex(r"t_{\text{critical}} = \pm 1.97", font_size=30, color=GRAY)

        stats_group = VGroup(t1, t2, t3).arrange(RIGHT, buff=0.4).next_to(d2, DOWN, buff=0.3)
        full_card = Group(card_box, d1, d2, stats_group)

        # ======================================================================
        # PHẦN 3: ĐỒ THỊ PHÂN PHỐI T-DISTRIBUTION (DƯỚI CÙNG)
        # ======================================================================
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 0.25, 0.05], x_length=6.4, y_length=1.5,
                    axis_config={"color": GRAY, "stroke_width": 2}).move_to(DOWN * 2.3)
        curve = axes.plot(lambda x: 0.15 * np.exp(-0.25 * x ** 2), color=YELLOW, stroke_width=2.5)

        t_crit = 1.97
        left_tail = axes.get_area(curve, x_range=[-4, -t_crit], color="#FF4B4B", opacity=0.7)
        right_tail = axes.get_area(curve, x_range=[t_crit, 4], color="#FF4B4B", opacity=0.7)

        line_crit_l = DashedLine(axes.c2p(-t_crit, 0), axes.c2p(-t_crit, 0.18), color=WHITE, stroke_width=2)
        line_crit_r = DashedLine(axes.c2p(t_crit, 0), axes.c2p(t_crit, 0.18), color=WHITE, stroke_width=2)

        lbl_crit_l = MathTex("-1.97", font_size=15, color=WHITE).next_to(line_crit_l, UP, buff=0.08)
        lbl_crit_r = MathTex("1.97", font_size=15, color=WHITE).next_to(line_crit_r, UP, buff=0.08)

        # Tracker cho con trỏ
        tracker = ValueTracker(0)
        pointer = Arrow(UP, DOWN, color=WHITE, buff=0).scale(0.5)
        val_label = Text("T = 0.00", font="Arial", font_size=14, color=WHITE, weight=BOLD)
        pointer_group = VGroup(pointer, val_label)

        def update_pointer(mob):
            val = tracker.get_value()
            mob[0].put_start_and_end_on(axes.c2p(val, 0.16), axes.c2p(val, 0.02))
            mob[1].become(
                Text(f"T = {val:.2f}", font="Arial", font_size=14, color=WHITE, weight=BOLD).next_to(mob[0], UP,
                                                                                                     buff=0.05))

        pointer_group.add_updater(update_pointer)

        # ======================================================================
        # PHẦN 4: CON DẤU ĐỎ ĐẬM (ĐÃ PHÓNG TO GẤP ĐÔI, MAX SIZE)
        # ======================================================================
        # ĐÃ SỬA: Tăng kích thước font chữ gấp đôi (từ 22/28 lên 40/50)
        stamp_txt1 = Text("KHÔNG THỂ BÁC BỎ", font="Arial", font_size=40, color=WHITE, weight=BOLD)
        stamp_txt2 = MathTex("H_0", font_size=50, color=WHITE)
        stamp_content = VGroup(stamp_txt1, stamp_txt2).arrange(RIGHT, buff=0.2)

        # ĐÃ SỬA: Tăng border box cho phù hợp với font khổng lồ
        stamp_bg = RoundedRectangle(corner_radius=0.2, width=stamp_content.width + 0.8,
                                    height=stamp_content.height + 0.5,
                                    fill_color="#C0392B", fill_opacity=0.95, stroke_color=WHITE, stroke_width=3.5)

        stamp_group = VGroup(stamp_bg, stamp_content).move_to(card_box.get_center()).rotate(-PI / 12).set_z_index(5)

        # ======================================================================
        # DIỄN HOẠT ĐỒNG BỘ (GIỮ NGUYÊN THỜI GIAN 100%)
        # ======================================================================

        sync_subtitle(
            "Now for the surprise. Football fans often believe that:",
            "Bây giờ đến phần bất ngờ. Người hâm mộ bóng đá thường tin rằng:",
            [FadeIn(q_txt, shift=UP * 0.2), Create(ball_icon)], total_time=3.5
        )

        sync_subtitle(
            "the team that holds the ball more controls the game and is more likely to win.",
            "đội nào cầm bóng nhiều hơn thì kiểm soát trận đấu và dễ thắng hơn.",
            [Rotate(ball_icon, angle=TAU * 2, run_time=2.0)], total_time=4.0
        )

        sync_subtitle(
            "Let's test this with the same process. Winners average 50.38% possession,",
            "Hãy kiểm định điều này bằng cùng quy trình. Đội thắng cầm bóng trung bình 50.38%,",
            [FadeIn(card_box), FadeIn(d1, shift=UP * 0.1)], total_time=4.5
        )

        sync_subtitle(
            "while losers average 49.62%. The difference is only 0.76 percent.",
            "đội thua là 49.62%. Chênh lệch chỉ 0.76 phần trăm.",
            [FadeIn(d2, shift=UP * 0.1)], total_time=3.5
        )

        sync_subtitle(
            "Applying the Paired T-test: T equals 0.60, p-value equals 0.55.",
            "Áp dụng Paired T-test: T bằng 0.60, p-value bằng 0.55.",
            [
                FadeIn(stats_group, shift=UP * 0.15),
                FadeIn(axes), Create(curve),
                Create(line_crit_l), Create(line_crit_r), Write(lbl_crit_l), Write(lbl_crit_r),
                FadeIn(left_tail, right_tail), FadeIn(pointer_group)
            ], total_time=4.5
        )

        sync_subtitle(
            "The T-value lies right in the middle of the distribution — not in the rejection region.",
            "Giá trị T nằm ngay giữa phân phối — không vào vùng bác bỏ.",
            [tracker.animate.set_value(0.60)], total_time=4.5
        )
        pointer_group.clear_updaters()

        # Hiệu ứng phóng to mượt mà: Bắt đầu từ scale 0.5 bung ra scale 1.0 (kích thước siêu to khổng lồ)
        sync_subtitle(
            "Conclusion: we CANNOT reject the null hypothesis.",
            "Kết luận: KHÔNG thể bác bỏ giả thuyết không.",
            [
                FadeIn(stamp_group, scale=0.5),
                Wiggle(stamp_group, scale_value=1.05, rotation_angle=0.04),
                Indicate(t2, color=YELLOW)
            ], total_time=3.5
        )

        sync_subtitle(
            "Ball possession — in this 24-25 Premier League data —",
            "Tỷ lệ cầm bóng — trong dữ liệu Premier League 24-25 này —",
            [Circumscribe(stamp_group, color=WHITE, time_width=2.0)], total_time=3.5
        )

        sync_subtitle(
            "has NO statistically significant difference between winning and losing teams.",
            "KHÔNG có sự khác biệt có ý nghĩa thống kê giữa đội thắng và đội thua.",
            [], total_time=4.5
        )

        self.wait(1)