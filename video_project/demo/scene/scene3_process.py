from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0


class ProcessScene(Scene):
    def construct(self):

        pipeline_x = -1.8
        good_color = "#2ecc71"
        bad_color = "#e74c3c"
        note_font_size = 24

        # ICONS
        group_people = SVGMobject(
            "video_project/demo/assets/icons/crowd-of-users.svg"
        ).scale_to_fit_width(1.5).move_to(UP * 5 + RIGHT * pipeline_x)

        cv_icon = ImageMobject(
            "video_project/demo/assets/icons/cv.png"
        ).scale_to_fit_width(1.5).move_to(UP * 1.8 + RIGHT * pipeline_x)

        interview_icon = ImageMobject(
            "video_project/demo/assets/icons/interview.png"
        ).scale_to_fit_width(1.5).move_to(DOWN * 1.4 + RIGHT * pipeline_x)

        coding_icon = ImageMobject(
            "video_project/demo/assets/icons/coding.png"
        ).scale_to_fit_width(1.5).move_to(DOWN * 4.6 + RIGHT * pipeline_x)

        group_people.set_color(WHITE)

        # ARROWS
        arrow1 = Arrow(group_people.get_bottom(), cv_icon.get_top(), buff=0.2, stroke_width=3)
        arrow2 = Arrow(cv_icon.get_bottom(), interview_icon.get_top(), buff=0.2, stroke_width=3)
        arrow3 = Arrow(interview_icon.get_bottom(), coding_icon.get_top(), buff=0.2, stroke_width=3)

        # NOTES
        def create_note(mobject, good_val, bad_val):
            return MarkupText(
                f"<span foreground='{good_color}'>Pro: {good_val}%</span> | "
                f"<span foreground='{bad_color}'>Non-Pro: {bad_val}%</span>",
                font_size=note_font_size,
                font="sans-serif"
            ).next_to(mobject, RIGHT, buff=0.6)

        note_cv = create_note(cv_icon, 80, 50)
        note_interview = create_note(interview_icon, 85, 40)
        note_coding = create_note(coding_icon, 90, 30)

        # SUBTEXT
        sub_style = {"font_size": 36, "color": WHITE, "font": "sans-serif"}
        sub1 = Text("Round 1: CV Screening", **sub_style)
        sub2 = Text("Round 2: Technical Interview", **sub_style)
        sub3 = Text("Round 3: Coding Skill Test", **sub_style)

        for s in [sub1, sub2, sub3]:
            s.to_edge(DOWN, buff=1.2)

        # --- ANIMATION ---

        # INTRO (~4s)
        self.play(FadeIn(group_people), run_time=2)
        self.wait(2)

        # ROUND 1 CV (~9s)
        self.play(
            FadeIn(cv_icon),
            GrowArrow(arrow1),
            Write(note_cv),
            Write(sub1),
            run_time=2
        )

        self.play(
            cv_icon.animate.scale(1.1),
            note_cv.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=2
        )

        self.wait(5)

        # ROUND 2 INTERVIEW (~9s)
        self.play(
            FadeIn(interview_icon),
            GrowArrow(arrow2),
            Write(note_interview),
            ReplacementTransform(sub1, sub2),
            run_time=2
        )

        self.play(
            interview_icon.animate.scale(1.1),
            note_interview.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=2
        )

        self.wait(5)

        # ROUND 3 CODING (~9s)
        self.play(
            FadeIn(coding_icon),
            GrowArrow(arrow3),
            Write(note_coding),
            ReplacementTransform(sub2, sub3),
            run_time=2
        )

        self.play(
            coding_icon.animate.scale(1.1),
            note_coding.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=2
        )

        self.wait(5)

        # OUTRO (~2s)
        self.play(FadeOut(Group(*self.mobjects)), run_time=2)