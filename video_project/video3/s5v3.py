from base_scene import TikTokBaseScene
from manim import *


class InsuranceRisk(TikTokBaseScene):
    def construct(self):
        # 1. Header phân đoạn
        self.add_header("ỨNG DỤNG THỰC TẾ")

        asset_path = "video_project/video3/assets/"

        # ======================================================================
        # PHẦN 1: NHÂN VẬT & DẤU HỎI (Đã thu nhỏ)
        # ======================================================================
        try:
            # Thu nhỏ nhân vật bằng với kích thước dấu hỏi chấm (1.2)
            customer = ImageMobject(asset_path + "customer.png").scale_to_fit_height(1.2)
            customer.move_to(UP * 1.5)

            qm = ImageMobject(asset_path + "question-mark.png").scale_to_fit_height(1.2)
            qm.next_to(customer, UP, buff=0.4)

            self.play(FadeIn(customer, shift=UP * 0.3), run_time=0.8)

            # Tách sub 1 (Vế A)
            self.play_subtitle(
                "Imagine you are an insurance company,",
                "Hãy tưởng tượng bạn là một công ty bảo hiểm,",
                duration=2
            )

            # Tách sub 1 (Vế B)
            self.play_subtitle(
                "selling a policy to a customer.",
                "vừa bán hợp đồng bảo hiểm xe cho một khách hàng.",
                duration=2
            )

            self.play(FadeIn(qm, scale=0.5), run_time=0.6)
            self.play(Indicate(qm, color=YELLOW))
        except Exception as e:
            print("Lỗi tải ảnh nhân vật/dấu hỏi:", e)

        # ======================================================================
        # PHẦN 2: CÂY XÁC SUẤT (Nhánh trái - Nhánh phải)
        # ======================================================================

        node_origin = customer.get_bottom() + DOWN * 0.3

        # Nhánh trái
        left_target = node_origin + LEFT * 2.5 + DOWN * 2.5
        line_left = Arrow(node_origin, left_target, buff=0, color=WHITE, stroke_width=4)

        # Nhánh phải
        right_target = node_origin + RIGHT * 2.5 + DOWN * 2.5
        line_right = Arrow(node_origin, right_target, buff=0, color=WHITE, stroke_width=4)

        prob_95 = Text("95%", font="Arial", font_size=32, color=GREEN, weight=BOLD)
        prob_95.move_to(line_left.get_center() + LEFT * 0.6 + UP * 0.3)

        prob_5 = Text("5%", font="Arial", font_size=32, color=RED, weight=BOLD)
        prob_5.move_to(line_right.get_center() + RIGHT * 0.6 + UP * 0.3)

        # Hiện nhánh
        self.play(Create(line_left), Create(line_right), run_time=1)

        # Tách sub 2 (Vế A)
        self.play_subtitle(
            "According to historical data,",
            "Theo dữ liệu lịch sử,",
            duration=2
        )

        # Hiện tỷ lệ
        self.play(Write(prob_95), Write(prob_5))

        # Tách sub 2 (Vế B)
        self.play_subtitle(
            "the probability of an accident is 5%.",
            "xác suất người này gặp tai nạn trong năm là 5%.",
            duration=2.5
        )

        # ======================================================================
        # PHẦN 3: ICONS KẾT QUẢ & CHI PHÍ
        # ======================================================================
        try:
            safety = ImageMobject(asset_path + "safety.png").scale_to_fit_height(1.5)
            safety.move_to(left_target + DOWN * 1.0)
            label_safe = Text("An toàn", font="Arial", font_size=24, color=GREEN).next_to(safety, DOWN, buff=0.2)

            breakdown = ImageMobject(asset_path + "car-breakdown.png").scale_to_fit_height(1.5)
            breakdown.move_to(right_target + DOWN * 1.0)

            cost_text = Text("–50 triệu", font="Arial", font_size=36, color=RED, weight=BOLD)
            cost_text.next_to(breakdown, DOWN, buff=0.2)

            # Tách sub 3 (Vế A)
            self.play_subtitle(
                "With only one customer, the result is unpredictable",
                "Nhưng với duy nhất một khách hàng, bạn hoàn toàn không biết kết quả",
                duration=2.5
            )

            # Hiện kết quả
            self.play(FadeIn(safety), Write(label_safe))
            self.play(FadeIn(breakdown), Write(cost_text))

            # Tách sub 3 (Vế B)
            self.play_subtitle(
                "like a single coin flip.",
                "giống như không thể đoán được kết quả của một lần tung đồng xu.",
                duration=2.5
            )

            self.play(Circumscribe(cost_text, color=RED))

        except Exception as e:
            print("Lỗi tải ảnh safety/breakdown:", e)

        self.wait(1)