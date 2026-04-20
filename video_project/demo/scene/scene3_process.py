from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ProcessScene(Scene):
    def construct(self):
        # ── CẤU HÌNH TỌA ĐỘ & MÀU SẮC ──
        pipeline_x = -1.5
        good_color = "#2ecc71"
        bad_color = "#e74c3c"
        note_font_size = 22
        icon_scale = 1.0

        # ── LOGO ──
        logo = ImageMobject("video_project/demo/assets/images/fami.png").scale(0.3).move_to(UP * 6)
        self.add(logo)

        # ── HÀM TẠO SUBTITLE CÓ KHUNG VIỀN (ĐÃ CẬP NHẬT) ──
        def create_dual_sub(en, vi):
            max_w = config.frame_width - 1.5

            en_text = Paragraph(
                en, font="Arial", font_size=22, weight=BOLD,
                alignment="center", width=max_w
            ).set_color(WHITE)

            vi_text = Paragraph(
                vi, font="Arial", font_size=18,
                alignment="center", width=max_w
            ).set_color(YELLOW)

            # Gộp text trước để tính toán kích thước khung
            text_group = VGroup(en_text, vi_text).arrange(DOWN, buff=0.2)

            # Tạo khung viền bao quanh chữ
            # buff=0.3 tạo khoảng cách giữa chữ và viền
            frame = SurroundingRectangle(
                text_group,
                color=WHITE,
                buff=0.3,
                stroke_width=2,
                corner_radius=0.1
            )

            # Tạo nền đen mờ phía sau để dễ đọc
            background = BackgroundRectangle(
                frame,
                color=BLACK,
                fill_opacity=0.5,
                buff=0
            )

            # Gộp tất cả thành một nhóm duy nhất
            full_sub = VGroup(background, frame, text_group)
            full_sub.move_to(DOWN * 3.8)
            full_sub.set_z_index(100)

            return full_sub

        # ── ICONS ──
        # Lưu ý: Đảm bảo đường dẫn file svg/png của bạn là chính xác
        group_people = SVGMobject(
            "video_project/demo/assets/icons/crowd-of-users.svg"
        ).scale_to_fit_width(icon_scale).move_to(UP * 4.2 + RIGHT * pipeline_x)

        cv_icon = ImageMobject(
            "video_project/demo/assets/icons/cv.png"
        ).scale_to_fit_width(icon_scale).move_to(UP * 1.8 + RIGHT * pipeline_x)

        interview_icon = ImageMobject(
            "video_project/demo/assets/icons/interview.png"
        ).scale_to_fit_width(icon_scale).move_to(DOWN * 0.4 + RIGHT * pipeline_x)

        coding_icon = ImageMobject(
            "video_project/demo/assets/icons/coding.png"
        ).scale_to_fit_width(icon_scale).move_to(DOWN * 2.6 + RIGHT * pipeline_x)

        group_people.set_color(WHITE)

        # ── ARROWS ──
        arrow_style = {"buff": 0.15, "stroke_width": 4}
        arrow1 = Arrow(group_people.get_bottom(), cv_icon.get_top(), **arrow_style)
        arrow2 = Arrow(cv_icon.get_bottom(), interview_icon.get_top(), **arrow_style)
        arrow3 = Arrow(interview_icon.get_bottom(), coding_icon.get_top(), **arrow_style)

        # ── NOTES ──
        def create_note(mobject, good_val, bad_val):
            return MarkupText(
                f"<span foreground='{good_color}'>Pro: {good_val}%</span>\n"
                f"<span foreground='{bad_color}'>Non-Pro: {bad_val}%</span>",
                font_size=note_font_size, font="Arial", line_spacing=0.2
            ).next_to(mobject, RIGHT, buff=0.4)

        note_cv = create_note(cv_icon, 80, 50)
        note_interview = create_note(interview_icon, 85, 40)
        note_coding = create_note(coding_icon, 90, 30)

        # ── ĐỊNH NGHĨA NỘI DUNG SUBTITLE ──
        sub_intro = create_dual_sub(
            "The recruitment process consists of 3 rounds:",
            "Quy trình tuyển dụng bao gồm 3 vòng:"
        )
        sub1 = create_dual_sub(
            "Round 1: CV Screening. Pro: 80% pass rate | Non-Pro: 50%.",
            "Vòng 1: Lọc CV. Nếu giỏi xác suất chọn là 80%, không giỏi là 50%."
        )
        sub2 = create_dual_sub(
            "Round 2: Interview. Pro: 85% pass rate | Non-Pro: 40%.",
            "Vòng 2: Phỏng vấn. Nếu giỏi xác suất vượt qua là 85%, không giỏi là 40%."
        )
        sub3 = create_dual_sub(
            "Round 3: Coding Skill Test. Pro: 90% pass rate | Non-Pro: 30%.",
            "Vòng 3: Test lập trình. Nếu giỏi xác suất vượt qua là 90%, không giỏi là 30%."
        )

        # ── ANIMATION ──
        # Intro
        self.play(FadeIn(group_people), FadeIn(sub_intro), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(sub_intro), run_time=0.5)

        # Round 1
        self.play(FadeIn(cv_icon), GrowArrow(arrow1), Write(note_cv), FadeIn(sub1))
        self.play(cv_icon.animate.scale(1.1), rate_func=there_and_back)
        self.wait(4)

        # Round 2 (Sử dụng ReplacementTransform để chuyển đổi mượt cả khung và chữ)
        self.play(FadeIn(interview_icon), GrowArrow(arrow2), Write(note_interview), ReplacementTransform(sub1, sub2))
        self.play(interview_icon.animate.scale(1.1), rate_func=there_and_back)
        self.wait(4)

        # Round 3
        self.play(FadeIn(coding_icon), GrowArrow(arrow3), Write(note_coding), ReplacementTransform(sub2, sub3))
        self.play(coding_icon.animate.scale(1.1), rate_func=there_and_back)
        self.wait(4)

        # Outro
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)