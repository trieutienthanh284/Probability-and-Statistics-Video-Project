from base_scene import TikTokBaseScene
from manim import *


class CoinTossLLN(TikTokBaseScene):
    def construct(self):
        # 1. Header cho phân cảnh
        self.add_header("MÔ PHỎNG LUẬT SỐ LỚN")

        # Định nghĩa đường dẫn chung để code gọn gàng
        asset_path = "video_project/video3/assets/"

        # ==========================================
        # LỜI THOẠI 1 & 2: Giới thiệu tung đồng xu
        # ==========================================
        try:
            coin = ImageMobject(asset_path + "coin.png").scale_to_fit_height(2.0)
            coin.move_to(UP * 2)
            self.play(FadeIn(coin, shift=UP * 0.5), run_time=0.8)
        except:
            print("Thiếu ảnh coin.png")

        self.play_subtitle(
            "Let's review what the Law of Large Numbers is.",
            "Chúng ta cùng nhau ôn lại xem luật số lớn là gì nhé.",
            duration=3
        )

        # Hiệu ứng nảy lên văng xuống mô phỏng tung đồng xu
        self.play(coin.animate.shift(UP * 1.5).scale(1.2), run_time=0.4, rate_func=there_and_back)
        self.play(coin.animate.shift(DOWN * 1.5).scale(0.8), run_time=0.4, rate_func=there_and_back)

        self.play_subtitle(
            "Let's start with a familiar example: flipping a coin.",
            "Hãy bắt đầu bằng một ví dụ quen thuộc: tung một đồng xu.",
            duration=3
        )
        self.play(FadeOut(coin))

        # ==========================================
        # LỜI THOẠI 3: 4 lần tung (3 Sấp - 1 Ngửa)
        # ==========================================
        try:
            # Load và copy ảnh để tạo chuỗi
            img_sap = ImageMobject(asset_path + "matsap.png").scale_to_fit_height(1.3)
            img_ngua = ImageMobject(asset_path + "matngua.png").scale_to_fit_height(1.3)

            s1 = img_sap.copy()
            n1 = img_ngua.copy()
            s2 = img_sap.copy()
            s3 = img_sap.copy()

            # Gom lại thành hàng ngang
            coins_group = Group(s1, n1, s2, s3).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
            self.play(FadeIn(coins_group, shift=UP * 0.5), run_time=1)

            # Chuỗi text dưới ảnh
            seq_text = Text("S – N – S – S", font="Arial", font_size=40, color=WHITE)
            seq_text.next_to(coins_group, DOWN, buff=0.4)
            self.play(Write(seq_text))
        except:
            print("Thiếu ảnh matsap.png hoặc matngua.png")

        self.play_subtitle(
            "If flipped only 4 times, you might get 3 Heads and 1 Tail",
            "Nếu chỉ tung 4 lần, bạn có thể nhận được 3 mặt Sấp và 1 mặt Ngửa",
            duration=4
        )

        # ==========================================
        # LỜI THOẠI 4: So sánh 75% và 50%
        # ==========================================
        # Text 75%
        ratio_75 = Text("75% Sấp", font="Arial", font_size=55, color=RED).next_to(seq_text, DOWN, buff=1.0)
        self.play(FadeIn(ratio_75, scale=1.5))

        # Text 50% (Kỳ vọng)
        ratio_50 = Text("50% (Kỳ vọng)", font="Arial", font_size=40, color=GREEN).next_to(ratio_75, DOWN, buff=2.0)

        # Mũi tên 2 chiều và chữ thể hiện sự chênh lệch
        arrow = DoubleArrow(ratio_75.get_bottom(), ratio_50.get_top(), color=YELLOW)
        gap_text = Text("Lệch rất xa", font="Arial", font_size=30, color=YELLOW, slant=ITALIC)
        gap_text.next_to(arrow, RIGHT, buff=0.3)

        self.play(FadeIn(ratio_50), GrowArrow(arrow), Write(gap_text))

        self.play_subtitle(
            "a 75% ratio, far off from the 50% we usually expect.",
            "tỷ lệ 75%, lệch rất xa so với 50% mà chúng ta thường nghĩ tới.",
            duration=4
        )

        # ==========================================
        # LỜI THOẠI 5: Tăng số lần tung lên 100, 1000, 100.000
        # ==========================================
        # Xóa các đối tượng cũ đi để lấy chỗ
        try:
            self.play(FadeOut(Group(coins_group, seq_text, ratio_75, ratio_50, arrow, gap_text)))
        except:
            pass  # Bỏ qua nếu lỗi nạp ảnh ở trên

        # Tạo các con số (Đã giảm 20% size: 90->72, 110->88, 120->96)
        # Đặt ở UP * 1.5 để chừa khoảng trống rộng rãi cho dấu hỏi bên dưới
        num_100 = Text("100", font="Arial", font_size=72, color="#40E0D0").move_to(UP * 1.5)
        num_1000 = Text("1.000", font="Arial", font_size=88, color="#40E0D0").move_to(UP * 1.5)
        num_100k = Text("100.000", font="Arial", font_size=96, color="#40E0D0").move_to(UP * 1.5)

        # 100 hiện lên rồi mờ đi
        self.play(FadeIn(num_100, scale=0.5), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(num_100, scale=1.5), run_time=0.5)

        # 1.000 hiện lên rồi mờ đi
        self.play(FadeIn(num_1000, scale=0.5), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(num_1000, scale=1.5), run_time=0.5)

        # 100.000 hiện lên
        self.play(FadeIn(num_100k, scale=0.5), run_time=0.8)

        # Dấu hỏi chấm thu nhỏ hiện ra NGAY BÊN DƯỚI
        try:
            qm = ImageMobject(asset_path + "question-mark.png").scale_to_fit_height(1.8)
            # Căn vị trí ngay dưới số 100.000
            qm.next_to(num_100k, DOWN, buff=0.8)
            self.play(FadeIn(qm, scale=0.3, shift=UP * 0.5), run_time=0.6)
        except:
            print("Thiếu ảnh question-mark.png")

        self.play_subtitle(
            "But what if we flip this coin 100, 1,000, or 100,000 times?",
            "Nhưng điều gì sẽ xảy ra nếu chúng ta tung 100, 1.000, hay 100.000 lần?",
            duration=4
        )

        self.wait(1)