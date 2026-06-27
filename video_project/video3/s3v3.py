from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class LLNSimulationGraph(TikTokBaseScene):
    def construct(self):
        # 1. Tiêu đề phụ
        self.add_header("XÁC SUẤT HỘI TỤ")

        # ======================================================================
        # PHẦN 1: PHÁT BIỂU LUẬT SỐ LỚN & CÔNG THỨC TOÁN HỌC
        # ======================================================================

        # Tạo nhóm công thức: Trung bình mẫu -> Kỳ vọng (Sử dụng mã màu HEX #00FFFF thay cho CYAN)
        f_left = MathTex(r"\frac{1}{n} \sum_{i=1}^{n} X_i").scale(1.3).set_color("#00FFFF")
        f_arrow = MathTex(r"\xrightarrow{n \to \infty}").scale(1.2)
        f_right = MathTex(r"\mu").scale(1.5).set_color(YELLOW)
        formula = VGroup(f_left, f_arrow, f_right).arrange(RIGHT, buff=0.4).move_to(UP * 1.5)

        # Chú thích công thức
        note_left = Text("Trung bình mẫu", font="Arial", font_size=20, color="#00FFFF").next_to(f_left, DOWN, buff=0.3)
        note_right = Text("Kỳ vọng lý thuyết", font="Arial", font_size=20, color=YELLOW).next_to(f_right, DOWN,
                                                                                                 buff=0.3)

        # Lời thoại 1
        self.play_subtitle(
            "The Law of Large Numbers states:",
            "Luật số lớn được phát biểu như sau:",
            duration=2
        )

        # Lời thoại 2 + Hiện nửa đầu công thức
        self.play(FadeIn(f_left, shift=UP * 0.5), Write(note_left))
        self.play_subtitle(
            "As the number of independent trials increases significantly,",
            "Khi số lần thực hiện một phép thử ngẫu nhiên độc lập tăng lên rất lớn,",
            duration=4
        )

        # Lời thoại 3 + Hiện mũi tên và nửa sau công thức
        self.play(Write(f_arrow), FadeIn(f_right, shift=LEFT * 0.5), Write(note_right))
        self.play_subtitle(
            "the average of observed results converges to the expected value.",
            "giá trị trung bình của các kết quả quan sát sẽ tiến gần đến giá trị kỳ vọng.",
            duration=4
        )

        # Lời thoại 4 (Chuyển cảnh)
        self.play_subtitle(
            "To simplify, let's look at the graph below.",
            "Để đơn giản hóa, bạn hãy nhìn về đồ thị dưới đây.",
            duration=3
        )

        # Xóa công thức để nhường chỗ cho đồ thị
        self.play(FadeOut(VGroup(formula, note_left, note_right)))

        # ======================================================================
        # PHẦN 2: THIẾT LẬP DỮ LIỆU & HỆ TRỤC (Làm đậm nét)
        # ======================================================================
        np.random.seed(42)
        log_n = np.linspace(0, 5, 500)
        n_values = np.unique(np.round(10 ** log_n).astype(int))

        ratios = []
        for n in n_values:
            if n == 1:
                r = 0.2
            elif n == 2:
                r = 0.8
            elif n == 3:
                r = 0.33
            elif n == 4:
                r = 0.75
            else:
                # Thuật toán tiệm cận mạnh
                base_noise = np.random.uniform(-0.45, 0.45)
                noise = base_noise / (n ** 0.35)
                r = 0.5 + noise
            ratios.append(max(0, min(1, r)))  # Giữ trong khoảng 0-1

        # Hệ trục: Tăng stroke_width lên 4 để đường kẻ dày và rõ
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 1, 0.2],
            x_length=6.0, y_length=4.5,
            axis_config={"color": GRAY, "stroke_width": 4}
        ).move_to(DOWN * 0.5 + RIGHT * 0.2)

        # Trục X Labels (Bôi đậm: weight=BOLD)
        x_labels = VGroup()
        for pos, txt in zip([0, 1, 2, 3, 4, 5], ["1", "10", "100", "1K", "10K", "100K"]):
            lbl = Text(txt, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            lbl.next_to(axes.c2p(pos, 0), DOWN, buff=0.2)
            x_labels.add(lbl)

        # Trục Y Labels (Bôi đậm)
        y_labels = VGroup()
        for pos in [0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]:
            color = YELLOW if pos == 0.5 else WHITE
            lbl = Text(f"{pos}", font="Arial", font_size=18, color=color, weight=BOLD)
            lbl.next_to(axes.c2p(0, pos), LEFT, buff=0.2)
            y_labels.add(lbl)

        x_title = Text("Số lần tung n", font="Arial", font_size=20, color=GRAY, weight=BOLD).next_to(axes, DOWN,
                                                                                                     buff=0.8)
        y_title = Text("Tỷ lệ mặt Ngửa", font="Arial", font_size=20, color=GRAY, weight=BOLD).next_to(axes, UP,
                                                                                                      buff=0.3).shift(
            LEFT * 1.5)

        # Đường Kỳ Vọng: Màu Vàng, Dày hơn
        dashed_line = DashedLine(axes.c2p(0, 0.5), axes.c2p(5, 0.5), color=YELLOW, stroke_width=4)

        # Chữ kỳ vọng: Đẩy lên cao hơn (buff=0.35) để không bị đè
        label_05 = Text("Kỳ vọng (0.5)", font="Arial", font_size=18, color=YELLOW, weight=BOLD)
        label_05.next_to(dashed_line, UP, buff=0.35).to_edge(RIGHT, buff=0.8)

        self.play(FadeIn(axes, x_labels, y_labels, x_title, y_title, dashed_line, label_05), run_time=1.5)

        # ======================================================================
        # PHẦN 3: VẼ ĐỒ THỊ ĐỘNG VÀ KHỚP LỜI THOẠI MỚI
        # ======================================================================
        tracker = ValueTracker(0.0)

        # Cục Counter n: Dời xuống ngay trên trục tọa độ bên phải
        counter_text = always_redraw(lambda:
                                     Text(f"n = {int(10 ** tracker.get_value()):,}", font="Arial", font_size=32,
                                          color=WHITE, weight=BOLD)
                                     .next_to(axes, UP, buff=0.1).align_to(axes, RIGHT)
                                     )
        self.add(counter_text)

        # Đường xác suất: Màu Xanh lơ HEX, Nét dày (stroke_width=4)
        def get_curve():
            t = tracker.get_value()
            valid_points = [(n, r) for n, r in zip(n_values, ratios) if np.log10(n) <= t]
            if len(valid_points) < 2: return VMobject()
            points_coords = [axes.c2p(np.log10(n), r) for n, r in valid_points]
            return VMobject(color="#00FFFF", stroke_width=4).set_points_as_corners(points_coords)

        curve = always_redraw(get_curve)
        self.add(curve)

        # --- Subtitle Helper Function (Đóng khung cho lúc vẽ đồ thị) ---
        def show_sync_subtitle(eng, vie):
            e_sub = Text(eng, font="Arial", font_size=22, color=WHITE, weight=BOLD).scale_to_fit_width(7.2)
            v_sub = Text(vie, font="Arial", font_size=18, color=YELLOW, slant=ITALIC).scale_to_fit_width(7.2)
            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.8, height=g.height + 0.5, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)
            return VGroup(bg, g).to_edge(DOWN, buff=1.2)

        # Đồng bộ 1: n chạy từ 1 -> 100 (Dao động mạnh)
        sub1 = show_sync_subtitle("Observe this Heads ratio curve. Initially, it fluctuates wildly.",
                                  "Hãy quan sát đường biểu diễn tỷ lệ mặt Ngửa này. Ban đầu, nó dao động rất mạnh.")
        self.play(FadeIn(sub1, run_time=0.4))
        self.play(tracker.animate.set_value(2.0), run_time=4.0, rate_func=linear)
        self.play(FadeOut(sub1, run_time=0.4))

        # Đồng bộ 2: n chạy từ 100 -> 10.000 (Phẳng dần)
        sub2 = show_sync_subtitle("But later on, as the number of flips increases, the curve flattens out",
                                  "Nhưng càng về sau, khi số lần tung tăng lên, đường này càng phẳng dần")
        self.play(FadeIn(sub2, run_time=0.4))
        self.play(tracker.animate.set_value(4.0), run_time=4.5, rate_func=linear)
        self.play(FadeOut(sub2, run_time=0.4))

        # Đồng bộ 3: n chạy từ 10.000 -> 100.000 (Tiến sát 0.5)
        sub3 = show_sync_subtitle("and tightly approaches 0.5 — this is exactly what the LLN is about.",
                                  "và tiến sát về đúng giá trị 0.5 — đây chính là điều Luật số lớn đang nói tới.")
        self.play(FadeIn(sub3, run_time=0.4))
        self.play(tracker.animate.set_value(5.0), run_time=4.5, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(sub3, run_time=0.4))

        self.wait(1)