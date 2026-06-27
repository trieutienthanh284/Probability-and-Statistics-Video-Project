from base_scene import TikTokBaseScene
from manim import *


class SummaryScene(TikTokBaseScene):
    def construct(self):
        self.add_header("TỔNG KẾT")

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

        def create_summary_node(num, txt_mobject, icon_mobject, color_theme):
            bg = RoundedRectangle(corner_radius=0.15, width=6.8, height=0.95, fill_color=color_theme, fill_opacity=0.2,
                                  stroke_color=color_theme, stroke_width=3)
            lbl_num = Text(str(num), font="Arial", font_size=24, color=color_theme, weight=BOLD)
            bg_num = Circle(radius=0.3, fill_color=color_theme, fill_opacity=0.2, stroke_width=2.5,
                            stroke_color=color_theme)
            num_group = VGroup(bg_num, lbl_num)

            icon_mobject.scale_to_fit_height(0.45).set_color(WHITE)
            content = Group(num_group, icon_mobject, txt_mobject).arrange(RIGHT, buff=0.3).move_to(
                bg.get_center()).align_to(bg.get_left(), LEFT).shift(RIGHT * 0.2)
            return Group(bg, content)

        t1 = VGroup(Text("Xác định câu hỏi nghiên cứu,", font="Arial", font_size=18),
                    VGroup(Text("thiết lập giả thuyết", font="Arial", font_size=18), MathTex("H_0", font_size=22),
                           Text("&", font="Arial", font_size=18), MathTex("H_1", font_size=22)).arrange(RIGHT,
                                                                                                        buff=0.1)).arrange(
            DOWN, aligned_edge=LEFT, buff=0.08)
        t2 = Text("Lựa chọn phương pháp kiểm định\nphù hợp với bản chất dữ liệu.", font="Arial", font_size=18,
                  line_spacing=1.1)
        t3 = VGroup(
            VGroup(Text("Ngưỡng ý nghĩa", font="Arial", font_size=18), MathTex(r"\alpha = 0.05", font_size=24)).arrange(
                RIGHT, buff=0.15),
            Text("là quy ước, không phải quy luật tự nhiên.", font="Arial", font_size=18)).arrange(DOWN,
                                                                                                   aligned_edge=LEFT,
                                                                                                   buff=0.08)
        t4 = VGroup(MathTex("p < 0.05", font_size=24, color=YELLOW),
                    Text("là bằng chứng thực nghiệm mạnh,\nluôn cần xem xét CI & Effect Size.", font="Arial",
                         font_size=18, line_spacing=1.1)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        t5 = Text("Dữ liệu thống kê có sức mạnh\nbác bỏ trực giác cảm tính.", font="Arial", font_size=18,
                  line_spacing=1.1)

        boxes = [create_summary_node(i + 1, t, MathTex(["?", "T", r"\alpha", "p", "!"][i], font_size=35), c)
                 for i, (t, c) in
                 enumerate(zip([t1, t2, t3, t4, t5], ["#74B9FF", "#A29BFE", "#FDCB6E", "#FF7675", "#55E6C1"]))]

        summary_list = Group(*boxes).arrange(DOWN, buff=0.15).move_to(UP * 0.1)

        sync_subtitle("Let's summarize five key points.", "Tổng kết 5 điểm quan trọng trong tư duy Thống kê học.", [],
                      2.5)

        lessons_eng = [
            "One: always start with a clear question, state H0 and H1 before looking at data.",
            "Two: choose the appropriate test—paired data uses Paired T-test.",
            "Three: alpha 0.05 is convention, not a law of nature.",
            "Four: small p-value does not mean large effect, just strong evidence.",
            "Five: data can debunk intuition — this is the power of statistical thinking."
        ]
        lessons_vie = [
            "Một: Luôn bắt đầu từ câu hỏi, thiết lập H0 và H1 trước khi thu thập dữ liệu.",
            "Hai: Lựa chọn phép kiểm định phù hợp (vd: Paired T-test cho dữ liệu cặp).",
            "Ba: Alpha = 0.05 là quy ước khoa học, không phải quy tắc bất biến.",
            "Bốn: p-value nhỏ chỉ thể hiện bằng chứng mạnh, không phản ánh quy mô hiệu ứng.",
            "Năm: Dữ liệu thực chứng có khả năng bác bỏ mọi trực giác cảm tính."
        ]

        for i in range(5):
            sync_subtitle(lessons_eng[i], lessons_vie[i], [FadeIn(boxes[i], shift=DOWN * 0.1)], 7.5 if i < 4 else 5.5)

        self.wait(1)