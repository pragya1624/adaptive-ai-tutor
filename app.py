"""
app.py — Adaptive AI Tutor Web App
====================================
Run this to open the tutor in your browser.

Usage:
    py app.py
Then open: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
import random
from tutor import AdaptiveAITutor, TOPICS, PERSONALITIES

app = Flask(__name__)
app.secret_key = "adaptive_ai_tutor_secret"
SAVE_FOLDER = "student_data"


def get_all_students():
    """Load all saved students."""
    if not os.path.exists(SAVE_FOLDER):
        return []
    students = []
    for file in os.listdir(SAVE_FOLDER):
        if file.endswith(".json"):
            with open(os.path.join(SAVE_FOLDER, file)) as f:
                students.append(json.load(f))
    students.sort(
        key=lambda s: sum(s["knowledge"].values()) / len(s["knowledge"]),
        reverse=True
    )
    return students


def get_student(name):
    """Load one student by name."""
    path = os.path.join(
        SAVE_FOLDER,
        f"{name.lower().replace(' ', '_')}.json"
    )
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None


def overall_score(student):
    return round(
        sum(student["knowledge"].values()) / len(student["knowledge"]) * 100, 1
    )


def mastered_count(student):
    return sum(1 for v in student["knowledge"].values() if v >= 0.9)


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Landing / login page."""
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    """Handle login or new student creation."""
    name = request.form.get("name", "").strip()
    personality = request.form.get("personality", "curious")

    if not name:
        return redirect(url_for("index"))

    os.makedirs(SAVE_FOLDER, exist_ok=True)
    student = get_student(name)

    if not student:
        # Create new student
        tutor = AdaptiveAITutor(student_name=name, personality=personality)
        tutor.save()

    session["student_name"] = name
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    """Main student dashboard."""
    name = session.get("student_name")
    if not name:
        return redirect(url_for("index"))

    student = get_student(name)
    if not student:
        return redirect(url_for("index"))

    # Build topic data for template
    topics_data = []
    for topic in TOPICS:
        score = student["knowledge"].get(topic, 0)
        topics_data.append({
            "name": topic.replace("_", " ").title(),
            "key": topic,
            "score": round(score * 100),
            "status": (
                "mastered"    if score >= 0.9 else
                "learning"    if score >= 0.5 else
                "beginner"    if score >= 0.1 else
                "not_started"
            )
        })

    return render_template(
        "dashboard.html",
        student=student,
        topics=topics_data,
        overall=overall_score(student),
        mastered=mastered_count(student),
    )


@app.route("/study", methods=["POST"])
def study():
    """Auto study or manual study."""
    name = session.get("student_name")
    if not name:
        return redirect(url_for("index"))

    mode = request.form.get("mode", "auto")
    tutor = AdaptiveAITutor(student_name=name)

    results = []

    if mode == "auto":
        sessions = int(request.form.get("sessions", 5))
        for _ in range(sessions):
            next_topic = tutor.suggest_next()
            if next_topic is None:
                break
            report = tutor.teach(next_topic)
            results.append(report)

    elif mode == "manual":
        topic = request.form.get("topic")
        if topic in TOPICS:
            report = tutor.teach(topic)
            results.append(report)

    tutor.save()

    student = get_student(name)
    topics_data = []
    for topic in TOPICS:
        score = student["knowledge"].get(topic, 0)
        topics_data.append({
            "name": topic.replace("_", " ").title(),
            "key": topic,
            "score": round(score * 100),
            "status": (
                "mastered"    if score >= 0.9 else
                "learning"    if score >= 0.5 else
                "beginner"    if score >= 0.1 else
                "not_started"
            )
        })

    return render_template(
        "study_result.html",
        student=student,
        results=results,
        topics=topics_data,
        overall=overall_score(student),
        mastered=mastered_count(student),
    )


@app.route("/leaderboard")
def leaderboard():
    """Leaderboard of all students."""
    students = get_all_students()
    ranked = []
    for i, s in enumerate(students, 1):
        ranked.append({
            "rank": i,
            "name": s["name"],
            "personality": s["personality"],
            "sessions": s["sessions"],
            "overall": overall_score(s),
            "mastered": mastered_count(s),
            "last_saved": s.get("last_saved", "—"),
        })
    return render_template("leaderboard.html", students=ranked)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("\n🎓 Adaptive AI Tutor Web App")
    print("=" * 35)
    print("Open your browser and go to:")
    print("👉 http://localhost:5000")
    print("=" * 35 + "\n")
    app.run(debug=True)
