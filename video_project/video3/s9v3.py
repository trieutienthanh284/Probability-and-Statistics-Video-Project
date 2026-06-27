from base_scene import TikTokBaseScene
from manim import *
import numpy as np


class LLNFailure(TikTokBaseScene):
    def construct(self):
        # 1. Header phân đoạn
        self.add_header("KHI LUẬT SỐ LỚN THẤT BẠI")

        asset_path = "video_project/video3/assets/"

        # --- Helper: Phụ đề chuẩn ---
        def sync_subtitle(eng, vie, anims, total_time):
            e_sub = Text(eng, font="Arial", font_size=18, color=WHITE, weight=BOLD)
            v_sub = Text(vie, font="Arial", font_size=16, color=YELLOW, slant=ITALIC)
            max_width = 6.8
            if e_sub.width > max_width: e_sub.scale_to_fit_width(max_width)
            if v_sub.width > max_width: v_sub.scale_to_fit_width(max_width)
            g = VGroup(e_sub, v_sub).arrange(DOWN, buff=0.15)
            bg = RoundedRectangle(corner_radius=0.15, width=g.width + 0.6, height=g.height + 0.4, color=BLACK,
                                  fill_opacity=0.85, stroke_width=2, stroke_color=WHITE)
            full_sub = VGroup(bg, g).to_edge(DOWN, buff=1.0)
            anim_time = max(0.1, total_time - 0.8)
            self.play(FadeIn(full_sub, run_time=0.4))
            if anims:
                self.play(*anims, run_time=anim_time)
            else:
                self.wait(anim_time)
            self.play(FadeOut(full_sub, run_time=0.4))

        # ======================================================================
        # PHẦN 1: TÁI HIỆN LƯỚI NGƯỜI ĐỘC LẬP
        # ======================================================================
        grid_pos = UP * 0.5

        # Tạo lưới khách hàng (Dot) để xử lý hiệu ứng sóng mượt mà
        rows, cols = 20, 30
        customers = VGroup(*[Dot(radius=0.06, color=GREEN) for _ in range(rows * cols)])
        customers.arrange_in_grid(rows=rows, cols=cols, buff=0.12).move_to(grid_pos)

        # Một vài đốm đỏ ngẫu nhiên (độc lập) ban đầu
        for i in np.random.choice(len(customers), 30, replace=False):
            customers[i].set_color(RED)

        self.add(customers)

        sync_subtitle(
            "However, this formula only works if risks are independent—",
            "Tuy nhiên, công thức này chỉ đúng khi rủi ro của các khách hàng độc lập—",
            [FadeIn(customers)], total_time=3.5
        )

        sync_subtitle(
            "as required by the Law of Large Numbers.",
            "đúng điều kiện ta đã nhắc ở Luật số lớn.",
            [], total_time=3.0
        )

        # ======================================================================
        # PHẦN 2: THẢM HỌA XẢY RA (HIỆU ỨNG SÓNG)
        # ======================================================================

        # Chữ Overlay cảnh báo
        warning_text = Text("KHI RỦI RO KHÔNG ĐỘC LẬP...", font="Arial", font_size=28, color=RED, weight=BOLD)
        warning_text.move_to(grid_pos).set_z_index(10)
        bg_warning = BackgroundRectangle(warning_text, color=BLACK, fill_opacity=0.8, buff=0.2)
        warning_group = VGroup(bg_warning, warning_text)

        # Load các icon thảm họa
        try:
            quake = ImageMobject(asset_path + "earthquake.png").scale_to_fit_height(1.2).move_to(LEFT * 2.5 + UP * 2.5)
            storm = ImageMobject(asset_path + "storm.png").scale_to_fit_height(1.2).move_to(RIGHT * 2.5 + UP * 2.5)
            virus = ImageMobject(asset_path + "coronavirus.png").scale_to_fit_height(1.2).move_to(
                LEFT * 2.5 + DOWN * 1.5)
            flood = ImageMobject(asset_path + "flooded-house.png").scale_to_fit_height(1.2).move_to(
                RIGHT * 2.5 + DOWN * 1.5)
        except Exception as e:
            print("Lỗi tải ảnh:", e)
            quake = storm = virus = flood = Dot()  # Fallback an toàn

        # --- Diễn hoạt Động đất ---
        sync_subtitle(
            "What if an earthquake, a storm, or a pandemic occurs,",
            "Điều gì xảy ra nếu một trận động đất, một cơn bão, hay một đại dịch...",
            [
                FadeIn(quake, shift=DOWN),
                Flash(quake, color=RED),
                customers.animate.set_color(GREEN)  # Reset về xanh trước khi sóng đỏ tới
            ], total_time=4.0
        )

        # --- Hiệu ứng SÓNG LAN TỎA ---
        # Tính toán khoảng cách từ tâm (quake) đến từng dot
        center_point = quake.get_center()

        def get_dist(mob):
            return np.linalg.norm(mob.get_center() - center_point)

        # Sắp xếp các dot theo thứ tự xa dần tâm chấn
        sorted_customers = sorted(customers, key=get_dist)
        wave_anim = LaggedStart(
            *[c.animate.set_color(RED).scale(1.5).set_color(RED).scale(1 / 1.5) for c in sorted_customers],
            lag_ratio=0.005,
            run_time=3
        )

        sync_subtitle(
            "causing mass risks at the same time?",
            "khiến hàng loạt khách hàng cùng gặp rủi ro vào một thời điểm?",
            [
                FadeIn(storm, shift=LEFT),
                FadeIn(flood, shift=UP),
                FadeIn(virus, scale=0.5),
                wave_anim,
                Write(warning_group)
            ], total_time=5.0
        )

        # ======================================================================
        # PHẦN 3: KẾT LUẬN
        # ======================================================================

        sync_subtitle(
            "Then, risks are no longer independent—",
            "Khi đó, rủi ro không còn độc lập nữa —",
            [
                Indicate(warning_text, color=WHITE),
                quake.animate.scale(1.2), storm.animate.scale(1.2)
            ], total_time=3.5
        )

        sync_subtitle(
            "and the LLN no longer protects the insurance company.",
            "và Luật số lớn không còn bảo vệ công ty bảo hiểm như trước.",
            [
                # SỬA LỖI Ở ĐÂY: Dùng Group thay vì VGroup cho ImageMobject
                Group(quake, storm, virus, flood).animate.set_opacity(0.3),
                customers.animate.set_opacity(0.3)
            ], total_time=4.5
        )

        self.wait(1.5)