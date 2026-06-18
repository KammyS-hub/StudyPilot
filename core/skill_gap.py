TOPIC_SKILLS = {
    "dsa": ["arrays", "linked list", "trees", "graphs", "dynamic programming"],
    "ml": ["python", "pandas", "numpy", "statistics", "scikit-learn"],
    "web": ["html", "css", "flask", "api", "javascript"],
    "python": ["python basics", "oop", "problem solving"]
}


def find_gap(topic, user_skills):

    required = TOPIC_SKILLS.get(topic, [])
    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return {
        "required": required,
        "missing": missing
    }