import pandas as pd

# 🧠 Generate study plan
def generate_plan(subjects, hours_per_day):
    plan = []

    total_subjects = len(subjects)

    if total_subjects == 0:
        return pd.DataFrame()

    hours_each = hours_per_day / total_subjects

    for subject in subjects:
        plan.append({
            "Subject": subject,
            "Hours Allocated": round(hours_each, 2),
            "Priority Task": f"Revise {subject} + practice questions"
        })

    return pd.DataFrame(plan)