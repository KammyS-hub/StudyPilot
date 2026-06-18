def generate_plan(topic, intent):

    if topic == "dsa":
        return [
            "Start with arrays and strings",
            "Practice basic problems",
            "Move to trees and graphs",
            "Solve LeetCode medium problems"
        ]

    if topic == "ml":
        return [
            "Learn Python basics",
            "Study Pandas & NumPy",
            "Understand statistics",
            "Start ML models with sklearn"
        ]

    if topic == "web":
        return [
            "Learn HTML/CSS",
            "Build Flask app",
            "Create APIs",
            "Deploy project"
        ]

    return [
        "Define your goal clearly",
        "Start with basics",
        "Build small projects"
    ]