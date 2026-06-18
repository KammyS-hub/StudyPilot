from flask import Flask, render_template, request

from core.nlp_parser import analyze_input
from core.recommender import generate_plan
from core.skill_gap import find_gap

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    analysis = None
    plan = []
    gap = None

    topic = ""
    intent = ""

    if request.method == "POST":

        user_input = request.form.get("goal_text", "")

        # ---------- NLP ANALYSIS ----------
        analysis = analyze_input(user_input)

        topic = analysis["topic"]
        intent = analysis["intent"]

        # ---------- RECOMMENDATION ENGINE ----------
        plan = generate_plan(topic, intent)

        # ---------- SKILL GAP ANALYSIS ----------
        gap = find_gap(topic, user_skills=[])

    return render_template(
        "index.html",
        analysis=analysis,
        topic=topic,
        intent=intent,
        plan=plan,
        gap=gap
    )


if __name__ == "__main__":
    app.run(debug=True)