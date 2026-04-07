import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from skills.fami_lib import *

class Scene1_Hook(FaMIBaseScene):
    def construct(self):
        title = self.create_title("CHẤT LƯỢNG ĐƯỜNG TRUYỀN")
        
        # Mobjects
        tin_nhan = ImageMobject("assets/Bayes_Hiring/assets/icons/coding.png")
        tin_nhan.scale_to_fit_width(2.0).move_to(UP * 1.5 + LEFT * 2.0)

        van_de = ImageMobject("assets/Bayes_Hiring/assets/icons/problem.png")
        van_de.scale_to_fit_width(2.0).move_to(UP * 1.5 + RIGHT * 2.0)

        quality = ImageMobject("assets/Bayes_Hiring/assets/icons/quality.png")
        quality.scale_to_fit_width(2.5).move_to(UP * -0.5)

        with self.voiceover(text="Tin nhắn gửi đi rất dễ bị nhiễu sóng.") as tracker:
            self.update_subtitle("Tin nhắn gửi đi rất dễ bị nhiễu sóng.")
            self.play(Write(title), run_time=min(1.0, tracker.duration * 0.3))
            
            anim, r_func = skill_pop_in(tin_nhan)
            self.play(anim, rate_func=r_func, run_time=min(0.5, tracker.duration * 0.2))
            
            self.play(
                FadeIn(van_de, shift=DOWN), 
                Wiggle(tin_nhan, scale_value=1.1, rotation_angle=0.08 * PI),
                run_time=min(1.0, tracker.duration * 0.3)
            )
            
        with self.voiceover(text="Vậy lấy gì để đo lường chất lượng đường truyền?") as tracker:
            self.update_subtitle("Vậy lấy gì để đo lường chất lượng đường truyền?")
            
            self.play(FadeOut(tin_nhan, shift=LEFT), FadeOut(van_de, shift=UP), run_time=min(0.5, tracker.duration * 0.2))
            
            anim, r_func = skill_pop_in(quality)
            self.play(anim, rate_func=r_func, run_time=min(0.8, tracker.duration * 0.4))
            
            arcs = VGroup(*[
                Arc(radius=1.2 + i*0.5, angle=PI/2, start_angle=PI/4, color=SUCCESS, stroke_width=8)
                for i in range(3)
            ])
            arcs.next_to(quality, DOWN, buff=0.3)
            
            self.play(Create(arcs, lag_ratio=0.5), run_time=min(1.0, tracker.duration * 0.2))

        self.finish_scene()
