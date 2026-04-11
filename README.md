# 🎓 Adaptive AI Tutor

A personal AI tutor that teaches you math step by step — remembers your progress, adapts to how you learn, and never gets tired.

---

## 📁 Project Structure

```
adaptive-ai-tutor/
├── tutor.py          ← brain of the project (do not edit)
├── main.py           ← run this to study as a student
├── analysis.py       ← run this to compare all students (needs Pandas)
├── requirements.txt  ← libraries needed
├── README.md         ← you are here
└── student_data/     ← auto-created, stores every student's progress
    ├── rahul.json
    ├── priya.json
    └── ...
```

---

## 🚀 How to Run

**Step 1** — Open your Adaptive AI Tutor folder in File Explorer

**Step 2** — Click the address bar → type `powershell` → press Enter

**Step 3** — Type and press Enter:
```bash
py main.py
```

---

## 👤 First Time (New Student)

```
Enter your name: Pragya

👋 Welcome Pragya! You are a new student.

What kind of learner are you?
  1. Curious  — learns fast, remembers well
  2. Lazy     — learns slowly, forgets quickly
  3. Anxious  — struggles without proper order
```

Your profile is created and saved automatically.

---

## 🔄 Returning Student

Just enter the same name — everything loads automatically:

```
Enter your name: Pragya
👋 Welcome back, Pragya!
📖 Sessions done: 10
```

---

## 📋 The Menu (main.py)

```
  1. Auto study        → tutor picks best topic for you
  2. Study a topic     → you choose which topic to focus on
  3. Progress report   → see your scores across all topics
  4. See all students  → list everyone saved on this computer
  5. Exit              → saves and closes
```

---

## 📊 Student Analysis (analysis.py)

Run this separately to compare all students using Pandas:

**Step 1 — Install Pandas (one time only):**
```bash
pip install pandas
```

**Step 2 — Run:**
```bash
py analysis.py
```

**What you get — 4 tables:**

| Table | What it shows |
|---|---|
| 📊 Summary | All students — sessions, overall %, mastered topics |
| 📚 Knowledge Breakdown | Every topic score for every student side by side |
| 💪 Strongest & Weakest | Best and worst topic per student |
| 🏆 Leaderboard | Students ranked by overall score |

Plus a **CSV file** exported to `student_data/all_students.csv` — open it in Excel!

---

## 📚 Topics & Learning Order

| # | Topic | Needs First |
|---|---|---|
| 1 | Arithmetic | Nothing — start here |
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

## 🎭 Personalities

| | Curious | Lazy | Anxious |
|---|---|---|---|
| Learns | Fast | Slow | Medium |
| Forgets | Slowly | Quickly | Medium |
| Weakness | None | Needs repetition | Panics without prerequisites |

---

## 💾 How Saving Works

- Progress saves **automatically** after every session
- Each student gets their own file in `student_data/`
- Same name = loads your progress. New name = fresh start
- Delete your `.json` file to start over

---

## ❓ Quick FAQ

**Need to install anything?**
Only Pandas for analysis.py — run `pip install pandas` once.
Everything else runs on pure Python.

**How to add a new student?**
Just enter a new name in main.py — done automatically.

**Forgot your name?**
Pick option 4 in main.py to see all saved students.

**Want to start fresh?**
Delete your file from the `student_data` folder.

**How do I see all students compared?**
Run `py analysis.py` after installing Pandas.

---

## 🛠️ Requirements

```
Python 3.11+
pandas >= 2.0.0   (only for analysis.py)
```

Install with:
```bash
pip install pandas
```

---

## 📦 Coming Soon

Matplotlib charts · Flask web app · Claude AI explanations

---

## 📄 License
MIT
