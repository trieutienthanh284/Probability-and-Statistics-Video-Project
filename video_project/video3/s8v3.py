from base_scene import TikTokBaseScene
from manim import *


class InsuranceCalculationExample(TikTokBaseScene):
    def construct(self):
        self.add_header("VÍ DỤ TÍNH PHÍ THỰC TẾ")
        asset_path = "video_project/video3/assets/"

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
        # CĂN LỀ TEXT VÀ CỐ ĐỊNH CHIỀU DÀI ĐƯỜNG KẺ
        # ======================================================================

        # Gộp các dòng thành 3 nhóm (để chữ nhỏ lại một chút cho vừa vặn)
        n_line = Text("N = 100.000 khách hàng", font="Arial", font_size=26, color=WHITE)
        p_line = Text("p = 5% (xác suất tai nạn)", font="Arial", font_size=26, color="#00FFFF")
        c_line = Text("c = 50.000.000đ (bồi thường/ca)", font="Arial", font_size=26, color=GREEN)
        g1 = VGroup(n_line, p_line, c_line).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        cases_line = Text("→ Số ca dự kiến = 5.000 vụ", font="Arial", font_size=28, color=ORANGE, weight=BOLD)
        total_line = Text("→ Tổng chi phí = 250 tỷ đồng", font="Arial", font_size=28, color=ORANGE, weight=BOLD)
        g2 = VGroup(cases_line, total_line).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        risk_line = Text("Phí rủi ro = 2,5 triệu đ/người", font="Arial", font_size=28, color=WHITE)
        final_line = Text("Phí thực tế (+20% margin) = 3 triệu đ", font="Arial", font_size=30, color=YELLOW,
                          weight=BOLD)
        g3 = VGroup(risk_line, final_line).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # Căn cho mép trái của 3 khối bằng nhau tăm tắp
        g2.align_to(g1, LEFT)
        g3.align_to(g1, LEFT)

        # Đường phân cách có độ rộng cố định (width=6.0)
        line1 = Line(LEFT, RIGHT, color=GRAY).set_width(6.0)
        line2 = Line(LEFT, RIGHT, color=GRAY).set_width(6.0)

        # Trộn tất cả vào 1 VGroup và đặt thẳng vào giữa màn hình
        table_group = VGroup(g1, line1, g2, line2, g3).arrange(DOWN, buff=0.4)
        table_group.move_to(UP * 0.8)  # Dịch lên trên một chút để chừa chỗ cho easy.png

        # ======================================================================
        # DIỄN HOẠT
        # ======================================================================
        sync_subtitle("Example: with 100,000 customers, 5% accident rate,",
                      "Lấy ví dụ cụ thể: với 100.000 khách hàng, xác suất tai nạn 5%,",
                      [FadeIn(VGroup(n_line, p_line), shift=RIGHT * 0.3)], 4.0)
        sync_subtitle("and 50 million VND average cost per accident—", "và chi phí trung bình mỗi vụ 50 triệu đồng—",
                      [FadeIn(c_line, shift=RIGHT * 0.3)], 3.5)

        sync_subtitle("the company predicts 5,000 accidents, total 250 billion VND.",
                      "công ty dự đoán khoảng 5.000 vụ, tổng chi phí khoảng 250 tỷ.",
                      [Create(line1), FadeIn(g2, shift=RIGHT * 0.3)], 4.5)

        sync_subtitle("Divided by 100,000 customers, each pays 2.5 million VND.",
                      "Chia đều cho 100.000 khách, mỗi người đóng 2,5 triệu phí rủi ro.",
                      [Create(line2), FadeIn(risk_line, shift=RIGHT * 0.3)], 4.0)

        sync_subtitle("Plus 20% margin, the actual premium is 3 million VND per year.",
                      "Cộng thêm 20% margin, mức phí thực tế là 3 triệu đồng mỗi năm.", [FadeIn(final_line, scale=1.2)],
                      4.5)

        # Highlight dòng cuối
        highlight_rect = SurroundingRectangle(final_line, color=YELLOW, buff=0.15, stroke_width=3)
        self.play(Create(highlight_rect), final_line.animate.set_color(YELLOW))
        self.play(Indicate(final_line))
        self.wait(1)

        # Ẩn bảng để lấy chỗ cho kết luận
        self.play(FadeOut(table_group), FadeOut(highlight_rect))

        try:
            easy_icon = ImageMobject(asset_path + "easy.png").scale_to_fit_height(3.5)
            easy_icon.move_to(UP * 0.5)
            self.play(FadeIn(easy_icon, scale=0.5, shift=UP * 0.5), run_time=1)
            self.play(Wiggle(easy_icon))

            sync_subtitle("This is a simple illustration of how Insurance works.",
                          "Đây là ví dụ minh họa đơn giản nhất để hiểu ngành Bảo hiểm.", [], 4.5)
        except Exception as e:
            print("Lỗi tải easy.png:", e)

        self.wait(1.5)