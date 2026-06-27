from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class HistogramOverlap(TikTokBaseScene):
    def construct(self):
        # 1. Header chính của phân cảnh
        self.add_header("PHÂN PHỐI SỐ CÚ SÚT")

        # --- Helper: Phụ đề cố định size 18/16 & Khóa giới hạn chiều rộng ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)

            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)

            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)

            # Neo phụ đề ở đáy với buff=0.4 an toàn
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=0.4)

            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: GIỚI THIỆU SỐ LƯỢNG MẪU (287 Trận)
        # ======================================================================
        text_287 = Text("287 trận", font="Arial", font_size=65, color=YELLOW, weight=BOLD)
        text_desc = Text("Có kết quả thắng/thua rõ ràng", font="Arial", font_size=24, color=WHITE)
        group_287 = VGroup(text_287, text_desc).arrange(DOWN, buff=0.3).move_to(UP * 0.5)

        sync_subtitle(
            "I filtered 287 matches with clear results (excluding draws).",
            "Tôi đã lọc ra 287 trận có kết quả rõ ràng (tức loại bỏ trận hòa).",
            [Write(group_287)], total_time=4.5
        )
        self.play(FadeOut(group_287), run_time=0.5)

        # ======================================================================
        # PHẦN 2: THIẾT LẬP 2 BIỂU ĐỒ TÁCH BIỆT (Hạ thấp chống đè chữ)
        # ======================================================================
        win_freq = [0, 2, 8, 18, 32, 48, 52, 42, 32, 22, 14, 8, 5, 2, 1, 1, 0]
        lose_freq = [8, 25, 50, 60, 48, 35, 25, 15, 10, 6, 3, 2, 0, 0, 0, 0, 0]

        ax_config = {
            "x_range": [0, 16, 2], "y_range": [0, 65, 20],
            "x_length": 6.0, "y_length": 1.8,
            "axis_config": {"color": GRAY, "stroke_width": 2}
        }

        # --- Biểu đồ Đội Thắng (UP * 1.6) ---
        axes_win = Axes(**ax_config).move_to(UP * 1.6)
        win_x_nums = VGroup(
            *[Text(str(x), font="Arial", font_size=12).next_to(axes_win.c2p(x, 0), DOWN, buff=0.2) for x in
              range(0, 17, 2)])
        win_y_nums = VGroup(
            *[Text(str(y), font="Arial", font_size=12).next_to(axes_win.c2p(0, y), LEFT, buff=0.2) for y in
              range(20, 61, 20)])
        lbl_w_x = Text("Số cú sút trúng đích (Đội thắng)", font="Arial", font_size=14, color="#3498db",
                       weight=BOLD).next_to(win_x_nums, DOWN, buff=0.1)
        lbl_w_y = Text("Số trận", font="Arial", font_size=12, color=GRAY).next_to(axes_win.y_axis, UP, buff=0.1).shift(
            LEFT * 0.3)

        # --- Biểu đồ Đội Thua (DOWN * 1.2) ---
        axes_lose = Axes(**ax_config).move_to(DOWN * 1.2)
        lose_x_nums = VGroup(
            *[Text(str(x), font="Arial", font_size=12).next_to(axes_lose.c2p(x, 0), DOWN, buff=0.2) for x in
              range(0, 17, 2)])
        lose_y_nums = VGroup(
            *[Text(str(y), font="Arial", font_size=12).next_to(axes_lose.c2p(0, y), LEFT, buff=0.2) for y in
              range(20, 61, 20)])
        lbl_l_x = Text("Số cú sút trúng đích (Đội thua)", font="Arial", font_size=14, color="#e74c3c",
                       weight=BOLD).next_to(lose_x_nums, DOWN, buff=0.1)
        lbl_l_y = Text("Số trận", font="Arial", font_size=12, color=GRAY).next_to(axes_lose.y_axis, UP, buff=0.1).shift(
            LEFT * 0.3)

        win_bars_top = VGroup()
        lose_bars_bottom = VGroup()
        step_x = axes_win.x_axis.unit_size

        for x in range(17):
            if win_freq[x] > 0:
                bw = Rectangle(width=step_x * 0.95, height=win_freq[x] * axes_win.y_axis.unit_size,
                               fill_color="#3498db", fill_opacity=0.8, stroke_width=0).move_to(
                    axes_win.c2p(x + 0.5, win_freq[x] / 2))
                win_bars_top.add(bw)
            if lose_freq[x] > 0:
                bl = Rectangle(width=step_x * 0.95, height=lose_freq[x] * axes_lose.y_axis.unit_size,
                               fill_color="#e74c3c", fill_opacity=0.8, stroke_width=0).move_to(
                    axes_lose.c2p(x + 0.5, lose_freq[x] / 2))
                lose_bars_bottom.add(bl)

        sync_subtitle(
            "Looking at the distributions: blue is winning teams, red is losing teams.",
            "Nhìn vào phân phối của hai nhóm: xanh là đội thắng, đỏ là đội thua.",
            [
                FadeIn(Group(axes_win, win_x_nums, win_y_nums, lbl_w_x, lbl_w_y, win_bars_top)),
                FadeIn(Group(axes_lose, lose_x_nums, lose_y_nums, lbl_l_x, lbl_l_y, lose_bars_bottom))
            ], total_time=5.0
        )

        peak_win = axes_win.c2p(6.5, 52)
        peak_lose = axes_lose.c2p(3.5, 60)
        arrow_win = Arrow(start=peak_win + UP * 0.4 + RIGHT * 0.5, end=peak_win + UP * 0.05, color=YELLOW, buff=0,
                          stroke_width=4)
        arrow_lose = Arrow(start=peak_lose + UP * 0.4 + RIGHT * 0.5, end=peak_lose + UP * 0.05, color=YELLOW, buff=0,
                           stroke_width=4)

        sync_subtitle(
            "We clearly see the two peaks are shifted—winning teams tend to shoot more.",
            "Chúng ta thấy rõ hai đỉnh phân phối lệch nhau — đội thắng có xu hướng sút nhiều hơn.",
            [GrowArrow(arrow_win), GrowArrow(arrow_lose)], total_time=5.5
        )
        self.play(FadeOut(arrow_win), FadeOut(arrow_lose), run_time=0.5)

        # ======================================================================
        # PHẦN 3: HỢP NHẤT VÀ KHOANH VÙNG CỘT ĐỎ CAO NHẤT BẰNG KHUNG ĐỨT NÉT
        # ======================================================================
        axes_merged = Axes(**ax_config).move_to(UP * 0.2)
        merged_x_nums = VGroup(
            *[Text(str(x), font="Arial", font_size=12).next_to(axes_merged.c2p(x, 0), DOWN, buff=0.2) for x in
              range(0, 17, 2)])
        merged_y_nums = VGroup(
            *[Text(str(y), font="Arial", font_size=12).next_to(axes_merged.c2p(0, y), LEFT, buff=0.2) for y in
              range(20, 61, 20)])
        lbl_m_x = Text("Số cú sút trúng đích / trận", font="Arial", font_size=15, color=WHITE, weight=BOLD).next_to(
            merged_x_nums, DOWN, buff=0.1)
        lbl_m_y = Text("Số trận đấu", font="Arial", font_size=13, color=GRAY).next_to(axes_merged.y_axis, UP,
                                                                                      buff=0.1).shift(LEFT * 0.3)

        win_bars_merged = VGroup()
        lose_bars_merged = VGroup()
        overlap_bars = VGroup()

        # Biến lưu trữ cột ĐỎ cao nhất để khoanh vùng
        max_lh = 0
        highest_red_bar = None

        for x in range(17):
            w_h, l_h = win_freq[x], lose_freq[x]
            o_h = min(w_h, l_h)

            if w_h > 0:
                bwm = Rectangle(width=step_x * 0.95, height=w_h * axes_merged.y_axis.unit_size, fill_color="#3498db",
                                fill_opacity=0.5, stroke_width=0).move_to(axes_merged.c2p(x + 0.5, w_h / 2))
                win_bars_merged.add(bwm)
            if l_h > 0:
                blm = Rectangle(width=step_x * 0.95, height=l_h * axes_merged.y_axis.unit_size, fill_color="#e74c3c",
                                fill_opacity=0.5, stroke_width=0).move_to(axes_merged.c2p(x + 0.5, l_h / 2))
                lose_bars_merged.add(blm)
                # Tự động tìm cột ĐỎ có chiều cao lớn nhất
                if l_h > max_lh:
                    max_lh = l_h
                    highest_red_bar = blm
            if o_h > 0:
                bom = Rectangle(width=step_x * 0.95, height=o_h * axes_merged.y_axis.unit_size, fill_color="#f1c40f",
                                fill_opacity=1.0, stroke_width=0).move_to(axes_merged.c2p(x + 0.5, o_h / 2))
                overlap_bars.add(bom)

        old_labels = Group(axes_win, win_x_nums, win_y_nums, lbl_w_x, lbl_w_y, axes_lose, lose_x_nums, lose_y_nums,
                           lbl_l_x, lbl_l_y)

        sync_subtitle(
            "But notice this yellow overlapping area:",
            "Nhưng chú ý vùng vàng chồng lấp này:",
            [
                ReplacementTransform(old_labels, Group(axes_merged, merged_x_nums, merged_y_nums, lbl_m_x, lbl_m_y)),
                ReplacementTransform(win_bars_top, win_bars_merged),
                ReplacementTransform(lose_bars_bottom, lose_bars_merged),
                FadeIn(overlap_bars)
            ], total_time=2.5
        )

        # Đẩy chữ tản sang góc PHẢI trên cùng để không che khuất đỉnh đồ thị
        overlap_note = Text("Vùng chồng lấp: 57 trận (Gần 20%)", font="Arial", font_size=18, color=YELLOW,
                            weight=BOLD).move_to(UP * 2.5 + RIGHT * 1.5)

        # Mũi tên thẳng, chỉ chéo từ chữ sang hông phải của CỘT ĐỎ CAO NHẤT
        overlap_arrow = Arrow(start=overlap_note.get_left() + LEFT * 0.1, end=highest_red_bar.get_right() + RIGHT * 0.1,
                              color=YELLOW, buff=0, stroke_width=3)

        # Khung đứt nét ôm sát cột ĐỎ cao nhất
        box = SurroundingRectangle(highest_red_bar, color=YELLOW, buff=0.1, corner_radius=0.05, stroke_width=3)
        highlight_box = DashedVMobject(box, num_dashes=15)

        self.play(Write(overlap_note), Create(overlap_arrow))
        # Hiện khung viền nét đứt và nhấp nháy làm nổi bật
        self.play(Create(highlight_box), Indicate(highest_red_bar, color=YELLOW, scale_factor=1.05), run_time=1.5)

        sync_subtitle(
            "In 287 matches, there are 57 matches — almost 20% —",
            "trong 287 trận có kết quả rõ ràng, có đến 57 trận — tức gần 20% —",
            [], total_time=3.0
        )

        sync_subtitle(
            "where the losing team had more shots on target than the winner.",
            "mà đội thua lại có cú sút trúng đích nhiều hơn đội thắng.",
            [], total_time=4.0
        )

        sync_subtitle(
            "This shows shots on goal is not an absolute factor.",
            "Điều này cho thấy shots on goal không phải yếu tố tuyệt đối.",
            [Circumscribe(overlap_note, color=YELLOW, time_width=2)], total_time=3.5
        )

        # ======================================================================
        # PHẦN 4: DẪN DẮT VÀO LÝ THUYẾT KIỂM ĐỊNH GIẢ THUYẾT
        # ======================================================================
        self.play(FadeOut(
            Group(axes_merged, merged_x_nums, merged_y_nums, lbl_m_x, lbl_m_y, win_bars_merged, lose_bars_merged,
                  overlap_bars, overlap_note, overlap_arrow, highlight_box)))

        sys_text = Text("KIỂM ĐỊNH GIẢ THUYẾT", font="Arial", font_size=36, color=GREEN, weight=BOLD).move_to(UP * 0.5)
        sys_box = SurroundingRectangle(sys_text, color=GREEN, buff=0.3, stroke_width=3)

        sync_subtitle(
            "This is exactly where hypothesis testing comes into play:",
            "Đây chính xác là lúc kiểm định giả thuyết phát huy tác dụng:",
            [Write(sys_text), Create(sys_box)], total_time=4.0
        )

        sync_subtitle(
            "instead of intuition, we need a systematic process to evaluate.",
            "thay vì nhìn cảm tính, ta cần một quy trình có hệ thống để đánh giá.",
            [sys_box.animate.set_fill(GREEN, opacity=0.2)], total_time=4.5
        )

        self.wait(1)