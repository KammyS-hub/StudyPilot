import dsa_tracker as d
import pandas as pd


# 📊 DSA analytics
def dsa_topic_analysis():
    df = d.get_progress()

    if df.empty:
        return "No DSA data"

    summary = df.groupby("Topic")["Status"].apply(
        lambda x: (x == "Solved").sum()
    )

    return summary


# 📈 completion rate
def completion_rate():
    df = d.get_progress()

    if df.empty:
        return 0

    total = len(df)
    solved = len(df[df["Status"] == "Solved"])

    return round((solved / total) * 100, 2)
    