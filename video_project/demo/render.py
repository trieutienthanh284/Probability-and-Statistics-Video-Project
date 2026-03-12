import os

if __name__ == "__main__":
    # Render chất lượng preview (nhanh)
    os.system("manim -pql scenes/decision_tree_scene.py DecisionTreeScene")
    
    # Render chất lượng cao (khi xong)
    # os.system("manim -qh scenes/decision_tree_scene.py DecisionTreeScene")