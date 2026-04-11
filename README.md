# 🎓 Adaptive AI Tutor

A smart Python tutoring system that teaches a student math topics
step by step — adapting to their personality, respecting topic order,
simulating memory decay, and saving progress automatically.

---

## 📁 Project Structure

```
adaptive-ai-tutor/
├── tutor.py          ← brain of the entire project
├── main.py           ← run this to see everything working
├── requirements.txt  ← no external libraries needed
├── README.md         ← you are here
└── student_data/     ← auto-created, stores student JSON files
    ├── rahul.json
    ├── priya.json
    └── ...
```

---

## 🚀 How to Run

```bash
python main.py
```

No installs needed — runs on pure Python 3.11+

---

## 💡 How to Use in Your Own Code

```python
from tutor import AdaptiveAITutor

# ── Create a new student ──────────────────────────
tutor = AdaptiveAITutor(student_name="Rahul", personality="curious")
# First time → creates a new student
# Next time  → automatically loads saved progress!

# ── Teach a topic ─────────────────────────────────
tutor.teach("arithmetic")
tutor.teach("fractions")

# ── Get a smart suggestion ────────────────────────
tutor.suggest_next()
# Suggests topic with: prerequisites met + lowest score

# ── See full progress report ──────────────────────
tutor.progress_report()

# ── Auto study for N sessions ─────────────────────
tutor.auto_study(sessions=20)
# Automatically picks the best topic each session

# ── Save progress to file ─────────────────────────
tutor.save()
# Saves to student_data/rahul.json

# ── Delete save file (fresh start) ───────────────
tutor.delete_save()

# ── See all saved students ────────────────────────
AdaptiveAITutor.list_students()
```

---

## 📚 Topics & Learning Order

Topics must be learned in the right order.
You cannot learn advanced topics without mastering the basics first.

```
arithmetic
    ├── fractions
    │     ├── algebra_basics
    │     │     ├── linear_equations
    │     │     │     └── quadratics ──────────────┐
    │     │     └── trigonometry (needs geometry)  │
    │     └── probability (needs statistics too)   │
    └── geometry                                   │
          └── trigonometry ──────────────► calculus_intro
    └── statistics
          └── probability
```

| # | Topic | Prerequisite |
|---|---|---|
| 1 | Arithmetic | None |
| 2 | Fractions | Arithmetic |
| 3 | Algebra Basics | Arithmetic + Fractions |
| 4 | Geometry | Arithmetic |
| 5 | Statistics | Arithmetic + Fractions |
| 6 | Linear Equations | Algebra Basics |
| 7 | Quadratics | Linear Equations |
| 8 | Trigonometry | Geometry + Algebra Basics |
| 9 | Probability | Statistics + Fractions |
| 10 | Calculus Intro | Quadratics + Trigonometry |

---

## 🎭 Student Personalities

| Personality | Learn Rate | Forget Rate | Behaviour |
|---|---|---|---|
| **Curious** | Fast (0.18) | Slow (0.005) | Learns and retains well |
| **Lazy** | Slow (0.10) | Fast (0.015) | Learns slowly, forgets quickly |
| **Anxious** | Medium (0.12) | Medium (0.008) | Struggles without prerequisites |

---

## 🧠 Key Features

### 1. Knowledge Graph (Prerequisites)
Topics have dependencies — just like real school.
Teaching calculus before algebra gives almost no benefit.

### 2. Memory Decay
Students forget a little after every session.
The tutor must balance teaching new topics vs. revising old ones.

### 3. Student Personalities
Three different student types with different learning behaviours.

### 4. Smart Suggestions
`suggest_next()` always recommends the best topic:
- Prerequisites must be met
- Picks the topic with the biggest knowledge gap

### 5. Save & Load (JSON)
Progress is saved to `student_data/name.json`.
Loading is automatic — just use the same student name next time.

---

## 💾 Save File Format

```json
{
    "name": "Rahul",
    "personality": "curious",
    "knowledge": {
        "arithmetic": 0.72,
        "fractions": 0.45,
        "algebra_basics": 0.10
    },
    "sessions": 12,
    "history": ["arithmetic", "arithmetic", "fractions"],
    "last_saved": "2026-04-04 18:25:21"
}
```

---

## 📊 Knowledge Score Guide

| Score | Meaning |
|---|---|
| 0.0 | Not started |
| 0.1 – 0.4 | Beginner |
| 0.5 – 0.7 | Intermediate |
| 0.8 – 0.89 | Advanced |
| 0.9 – 1.0 | ✅ Mastered |

---

## 🛠️ Requirements

- Python 3.11 or higher
- No external libraries needed

---

## 📦 What's Coming Next

- 📊 Matplotlib — visual progress charts
- 🗃️ Pandas — compare multiple students
- 🌐 Flask — web interface
- 🤖 Claude AI — real explanations when student is stuck


