# 🎓 Adaptive AI Tutor

A personal AI tutor that teaches you math step by step — remembers your progress, adapts to how you learn, and never gets tired.

---

## 📁 Project Structure

```
adaptive-ai-tutor/
├── tutor.py          ← brain of the project (do not edit)
├── main.py           ← run this to study as a student
├── analysis.py       ← compare all students in tables (needs Pandas)
├── charts.py         ← visual progress charts (needs Matplotlib)
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

## 📊 Student Analysis — Tables (analysis.py)

Compare all students side by side using Pandas.

**Install once:**
```bash
pip install pandas
```

**Run:**
```bash
py analysis.py
```

**4 tables you get:**

| Table | What it shows |
|---|---|
| Summary | Sessions, overall %, mastered topics per student |
| Knowledge Breakdown | Every topic score for every student |
| Strongest & Weakest | Best and worst topic per student |
| Leaderboard | Students ranked by overall score |

Also exports a CSV file → open in Excel!

---

## 📈 Visual Charts (charts.py)

See your progress as beautiful colourful charts.

**Install once:**
```bash
pip install matplotlib
```

**Run:**
```bash
py charts.py
```

**4 charts you get:**

| Chart | What it shows |
|---|---|
| Progress Bar Chart | One student's score per topic — colour coded |
| All Students Comparison | Everyone side by side per topic |
| Leaderboard Chart | Horizontal bars ranked by overall score |
| Radar / Spider Chart | Web shape showing knowledge spread |

Charts are saved as PNG images in your `student_data` folder automatically.

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
Only Pandas and Matplotlib for analysis and charts.
Everything else runs on pure Python.

```bash
pip install pandas matplotlib
```

**How to add a new student?**
Just enter a new name in main.py — done automatically.

**Forgot your name?**
Pick option 4 in main.py to see all saved students.

**Want to start fresh?**
Delete your file from the `student_data` folder.

**How do I compare all students?**
Run `py analysis.py` for tables or `py charts.py` for visuals.

---

## 🛠️ Requirements

```
Python 3.11+
pandas>=2.0.0      (for analysis.py)
matplotlib>=3.7.0  (for charts.py)
```

Install everything at once:
```bash
pip install pandas matplotlib
```

---

## 📦 Coming Soon

Flask web app · Claude AI explanations · Online deployment

---

## 📄 License
MIT
