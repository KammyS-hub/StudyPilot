import pandas as pd

# 🧠 store DSA progress in memory (simple version)
progress = []

def add_problem(topic, problem_name, status):
    progress.append({
        "Topic": topic,
        "Problem": problem_name,
        "Status": status
    })


def get_progress():
    return pd.DataFrame(progress)


def topic_summary():
    if not progress:
        return "No data yet"

    df = pd.DataFrame(progress)

    summary = df.groupby("Topic")["Status"].apply(
        lambda x: (x == "Solved").sum()
    )

    return summary