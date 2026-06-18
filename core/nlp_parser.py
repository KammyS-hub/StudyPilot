import re

def extract_intent(text):
    text = text.lower()

    if "interview" in text:
        intent = "interview_prep"
    elif "project" in text:
        intent = "project_building"
    elif "exam" in text:
        intent = "exam_prep"
    else:
        intent = "general_learning"

    return intent


def extract_topic(text):

    text = text.lower()

    topics = {
        "dsa": ["dsa", "data structures", "algorithms"],
        "ml": ["machine learning", "ml", "ai"],
        "web": ["web development", "flask", "django", "frontend"],
        "python": ["python"]
    }

    for key, keywords in topics.items():
        for kw in keywords:
            if kw in text:
                return key

    return "general"


def analyze_input(text):

    return {
        "intent": extract_intent(text),
        "topic": extract_topic(text)
    }