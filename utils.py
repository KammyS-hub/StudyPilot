import dsa_tracker as d


# 🧠 Smart suggestion engine
def get_suggestions():
    df = d.get_progress()

    if df.empty:
        return ["Start solving DSA problems"]

    suggestions = []

    topic_counts = df.groupby("Topic")["Status"].apply(
        lambda x: (x == "Solved").sum()
    )

    for topic, count in topic_counts.items():
        if count == 0:
            suggestions.append(f"Focus on {topic} — no problems solved yet")
        elif count < 2:
            suggestions.append(f"Improve {topic} — low practice")
        else:
            suggestions.append(f"Good progress in {topic}")

    return suggestions