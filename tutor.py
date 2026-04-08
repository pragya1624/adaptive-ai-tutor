"""
Adaptive AI Tutor
==================
A smart tutoring system that teaches a student math topics
step by step, respecting prerequisites and adapting to the
student's learning pace and personality.
"""

import random
import json
import os
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, List


# ── All Topics in Learning Order ──────────────────────────────────────────────
TOPICS = [
    "arithmetic",
    "fractions",
    "algebra_basics",
    "geometry",
    "statistics",
    "linear_equations",
    "quadratics",
    "trigonometry",
    "probability",
    "calculus_intro",
]

# You must know these topics before learning the next one
PREREQUISITES = {
    "arithmetic":       [],
    "fractions":        ["arithmetic"],
    "algebra_basics":   ["arithmetic", "fractions"],
    "geometry":         ["arithmetic"],
    "statistics":       ["arithmetic", "fractions"],
    "linear_equations": ["algebra_basics"],
    "quadratics":       ["linear_equations"],
    "trigonometry":     ["geometry", "algebra_basics"],
    "probability":      ["statistics", "fractions"],
    "calculus_intro":   ["quadratics", "trigonometry"],
}

TOPIC_INDEX = {t: i for i, t in enumerate(TOPICS)}


# ── Student Personalities ──────────────────────────────────────────────────────
PERSONALITIES = {
    "curious": {
        "learn_rate":  0.18,
        "decay_rate":  0.005,
        "description": "Learns fast and remembers well",
    },
    "lazy": {
        "learn_rate":  0.10,
        "decay_rate":  0.015,
        "description": "Learns slowly and forgets quickly",
    },
    "anxious": {
        "learn_rate":  0.12,
        "decay_rate":  0.008,
        "description": "Struggles when topics are too advanced",
    },
}


@dataclass
class Student:
    name: str
    personality: str
    knowledge: Dict[str, float] = field(default_factory=dict)
    sessions: int = 0
    history: List[str] = field(default_factory=list)

    def __post_init__(self):
        # Every student starts with zero knowledge
        if not self.knowledge:
            self.knowledge = {topic: 0.0 for topic in TOPICS}


class AdaptiveAITutor:
    """
    Adaptive AI Tutor

    Teaches a student math topics one session at a time.
    Adapts to the student's personality, respects topic
    prerequisites, and simulates memory decay over time.
    """

    SAVE_FOLDER = "student_data"  # folder where all student files are saved

    def __init__(self, student_name: str, personality: str = None):
        # Make sure the save folder exists
        os.makedirs(self.SAVE_FOLDER, exist_ok=True)

        save_file = self._save_path(student_name)

        # If a save file exists for this student → load it
        if os.path.exists(save_file):
            self._load(student_name)
            print(f"\n👋 Welcome back, {student_name}!")
            print(f"🎭 Personality  : {self.student.personality.capitalize()}")
            print(f"📖 Sessions done: {self.student.sessions}")
            print(f"📂 Progress loaded from: {save_file}\n")

        # Otherwise → create a new student
        else:
            personality = personality or random.choice(list(PERSONALITIES.keys()))
            assert personality in PERSONALITIES, \
                f"Personality must be one of: {list(PERSONALITIES.keys())}"

            self.student = Student(
                name=student_name,
                personality=personality,
            )
            print(f"\n👋 Welcome, {student_name}! (New student created)")
            print(f"🎭 Student type: {personality.capitalize()} "
                  f"— {PERSONALITIES[personality]['description']}")
            print(f"📚 Topics to master: {len(TOPICS)}\n")

    # ── Core Teaching Method ───────────────────────────────────────────────────

    def teach(self, topic: str) -> dict:
        """
        Teach the student a specific topic.
        Returns a report of what happened this session.
        """
        assert topic in TOPICS, f"Unknown topic. Choose from: {TOPICS}"

        s = self.student
        p = PERSONALITIES[s.personality]

        # 1. Memory decay — student forgets a little each session
        for t in TOPICS:
            s.knowledge[t] = max(0.0, s.knowledge[t] - p["decay_rate"])

        # 2. Check if prerequisites are met
        prereqs = PREREQUISITES[topic]
        prereqs_met = all(s.knowledge[pre] >= 0.5 for pre in prereqs)
        missing_prereqs = [p for p in prereqs if s.knowledge[p] < 0.5]

        # 3. Calculate how much the student learns
        gain = p["learn_rate"] * random.uniform(0.8, 1.2)

        if not prereqs_met:
            gain *= 0.3  # learns very little without prerequisites

        prev = s.knowledge[topic]
        s.knowledge[topic] = min(1.0, s.knowledge[topic] + gain)
        actual_gain = round(s.knowledge[topic] - prev, 3)

        # 4. Update session info
        s.sessions += 1
        s.history.append(topic)

        # 5. Build report
        report = {
            "topic":          topic,
            "knowledge_before": round(prev, 3),
            "knowledge_after":  round(s.knowledge[topic], 3),
            "gain":           actual_gain,
            "prereqs_met":    prereqs_met,
            "missing_prereqs": missing_prereqs,
            "mastered":       s.knowledge[topic] >= 0.9,
            "session_number": s.sessions,
        }

        self._print_session_report(report)
        return report

    # ── Smart Suggestion ───────────────────────────────────────────────────────

    def suggest_next(self) -> str:
        """
        Suggests the best topic to study next based on:
        - Prerequisites being met
        - Lowest current knowledge score
        """
        s = self.student
        candidates = []

        for topic in TOPICS:
            prereqs = PREREQUISITES[topic]
            prereqs_met = all(s.knowledge[pre] >= 0.5 for pre in prereqs)
            not_mastered = s.knowledge[topic] < 0.9

            if prereqs_met and not_mastered:
                candidates.append((topic, s.knowledge[topic]))

        if not candidates:
            return None

        # Suggest topic with lowest knowledge (biggest gap)
        candidates.sort(key=lambda x: x[1])
        best = candidates[0][0]
        print(f"\n💡 Suggested next topic: '{best}' "
              f"(current score: {round(self.student.knowledge[best], 2)})")
        return best

    # ── Progress Report ────────────────────────────────────────────────────────

    def progress_report(self):
        """Prints a full progress report for the student."""
        s = self.student
        mastered = [t for t in TOPICS if s.knowledge[t] >= 0.9]
        in_progress = [t for t in TOPICS if 0.1 <= s.knowledge[t] < 0.9]
        not_started = [t for t in TOPICS if s.knowledge[t] < 0.1]

        overall = round(sum(s.knowledge.values()) / len(TOPICS) * 100, 1)

        print(f"\n{'='*50}")
        print(f"  📊 Progress Report — {s.name}")
        print(f"{'='*50}")
        print(f"  Personality   : {s.personality.capitalize()}")
        print(f"  Total sessions: {s.sessions}")
        print(f"  Overall score : {overall}%\n")

        print("  📚 Topic Breakdown:")
        for topic in TOPICS:
            score = s.knowledge[topic]
            bar = self._progress_bar(score)
            status = "✅" if score >= 0.9 else "🔄" if score >= 0.1 else "⬜"
            print(f"  {status} {topic:<20} {bar} {round(score*100)}%")

        print(f"\n  ✅ Mastered    : {len(mastered)} topics")
        print(f"  🔄 In Progress : {len(in_progress)} topics")
        print(f"  ⬜ Not Started : {len(not_started)} topics")
        print(f"{'='*50}\n")

    # ── Auto Study Session ─────────────────────────────────────────────────────

    def auto_study(self, sessions: int = 10):
        """
        Automatically studies the best topic for N sessions.
        Great for seeing how the student progresses over time.
        """
        print(f"\n🤖 Auto-studying for {sessions} sessions...\n")
        for _ in range(sessions):
            next_topic = self.suggest_next()
            if next_topic is None:
                print("🎉 All topics mastered!")
                break
            self.teach(next_topic)

    # ── Save & Load (JSON) ─────────────────────────────────────────────────────

    def save(self):
        """Save the student's progress to a JSON file."""
        s = self.student
        data = {
            "name":        s.name,
            "personality": s.personality,
            "knowledge":   s.knowledge,
            "sessions":    s.sessions,
            "history":     s.history,
            "last_saved":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        path = self._save_path(s.name)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Progress saved → {path}")

    def _load(self, student_name: str):
        """Load a student's progress from their JSON file."""
        path = self._save_path(student_name)
        with open(path, "r") as f:
            data = json.load(f)
        self.student = Student(
            name=data["name"],
            personality=data["personality"],
            knowledge=data["knowledge"],
            sessions=data["sessions"],
            history=data["history"],
        )

    def delete_save(self):
        """Delete the student's save file (fresh start)."""
        path = self._save_path(self.student.name)
        if os.path.exists(path):
            os.remove(path)
            print(f"🗑️  Save file deleted for {self.student.name}")
        else:
            print("No save file found.")

    def _save_path(self, student_name: str) -> str:
        """Returns the file path for a student's save file."""
        safe_name = student_name.lower().replace(" ", "_")
        return os.path.join(self.SAVE_FOLDER, f"{safe_name}.json")

    @staticmethod
    def list_students():
        """Show all saved students."""
        folder = AdaptiveAITutor.SAVE_FOLDER
        if not os.path.exists(folder):
            print("No students saved yet.")
            return

        files = [f for f in os.listdir(folder) if f.endswith(".json")]
        if not files:
            print("No students saved yet.")
            return

        print(f"\n📋 Saved Students ({len(files)} found):")
        print("-" * 40)
        for file in files:
            path = os.path.join(folder, file)
            with open(path, "r") as f:
                data = json.load(f)
            overall = round(
                sum(data["knowledge"].values()) / len(data["knowledge"]) * 100, 1
            )
            mastered = sum(1 for v in data["knowledge"].values() if v >= 0.9)
            print(f"  👤 {data['name']:<15} "
                  f"| {data['personality']:<8} "
                  f"| Sessions: {data['sessions']:<4} "
                  f"| Overall: {overall}% "
                  f"| Mastered: {mastered}/10 topics"
                  f"\n     Last saved: {data.get('last_saved', 'unknown')}")
        print("-" * 40 + "\n")

    # ── Helpers ────────────────────────────────────────────────────────────────

    def _print_session_report(self, r: dict):
        print(f"📖 Session {r['session_number']} — Teaching: {r['topic']}")
        if not r["prereqs_met"]:
            print(f"   ⚠️  Missing prerequisites: {r['missing_prereqs']}")
            print(f"   (Student struggles without these foundations)")
        print(f"   Knowledge: {r['knowledge_before']} → {r['knowledge_after']} "
              f"(+{r['gain']})")
        if r["mastered"]:
            print(f"   🏆 Topic MASTERED!")
        print()

    def _progress_bar(self, score: float, width: int = 15) -> str:
        filled = int(score * width)
        return "[" + "█" * filled + "░" * (width - filled) + "]"
