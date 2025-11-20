
# Python Visitor Logging Assignment

## Overview
You will build a Python program that logs visitors into a file while enforcing:
- No duplicate consecutive visitors
- A mandatory 5‑minute wait between different visitors

This repo contains:
- `main.py` → Scaffold you must complete
- Tests → Used for automatic grading
- GitHub Actions → Runs your tests on every push

---

# 📌 Part 1 — Setting Up Git & GitHub (Beginner-Friendly)

### 1. Install Git
Download Git here: https://git-scm.com/downloads  
During installation, use default settings.

### 2. Create a GitHub Account
Go to https://github.com and sign up.

### 3. Clone your assignment repo
After accepting the GitHub Classroom link, run:

```
git clone <your-repo-url>
```

### 4. Open the folder in VS Code
```
code <folder-name>
```

---

# 📌 Part 2 — Branching Requirement

You **must** use at least 2 branches.

### Step 1 — Work on the main branch
Implement duplicate‑visitor logic.

```
git add .
git commit -m "duplicate visitor done"
git push
```

### Step 2 — Create a new branch for the 5‑minute rule

```
git checkout -b feature/wait-time
```

Implement the 5‑minute rule.

```
git add .
git commit -m "added 5 minute waiting rule"
git push --set-upstream origin feature/wait-time
```

### Step 3 — Create a Pull Request
On GitHub:
1. Go to your repo
2. Click **Pull Requests**
3. Click **New Pull Request**
4. Compare `feature/wait-time` → `main`
5. Submit PR

### Step 4 — Merge the PR
Click **Merge Pull Request**.

---

# 📌 Part 3 — Submitting the Assignment

Your submission is valid ONLY if:

✔ All tests pass  
✔ You used 2 branches  
✔ You created a Pull Request  
✔ You merged it yourself  
✔ Your final code is on `main` branch  

---

# 📺 Recommended Video for Beginners  
**Git & GitHub for Beginners – Full Course (free):**  
https://www.youtube.com/watch?v=RGOj5yH7evk

---

Good luck, and code responsibly 😄
