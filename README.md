# Git Assignment – Hero Vired  
This repository documents the complete workflow for three separate Git exercises:

1. Versioning and releasing the CalculatorPlus Python application.
2. Integrating Git LFS for large binary file handling.
3. Using Git stash to manage work across multiple feature branches for a Geometry Calculator project.

Each section below outlines the exact Git workflow used, with branching strategy, stashing, merging, reviews, and releases.

---

# Part 1 – CalculatorPlus Application

## Overview
The CalculatorPlus application provides basic arithmetic operations. Features were developed using `main`, `dev`, and feature branches. Bug fixes, feature updates, and code reviews followed a real-world Git workflow.

## Steps Completed

### 1. Repository Setup
Repository created: `git_assignment_HeroVired`  
Local setup:
```bash
git clone <repo-url>
git checkout -b dev
````

### 2. Implement Square Root Feature

A new branch was created to implement `square_root`:

```bash
git checkout -b feature/sqrt
```

Updated `CalculatorPlus.py` with:

* `square_root()` function
* Tests in the `__main__` block

### 3. Bug Fix During Feature Work

A bug was reported in `divide()`.
Fix applied on `dev`:

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

Then merged back into the feature branch.

### 4. Unit Tests Added

`test_calculator.py` added with tests for:

* Addition
* Square root
* Divide-by-zero

### 5. Pull Request & Merge

PR created: `feature/sqrt → dev`
After review → merged.

### 6. Release Version 1 & Version 2

After merging into `main`, version tags were created:

```bash
git tag -a v1.0.0 -m "Release v1"
git push origin v1.0.0

git tag -a v2.0.0 -m "Release v2"
git push origin v2.0.0
```

---

# Part 2 – Git LFS Integration

## Overview

A large binary file (`access_log.gz`, >200MB) was added using Git LFS to prevent large-file pollution in Git history.

## Steps Completed

### 1. Install Git LFS (WSL Ubuntu)

```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
```

### 2. Create LFS Branch

```bash
git checkout dev
git checkout -b lfs
```

### 3. Track `.gz` Files with Git LFS

```bash
git lfs track "*.gz"
git add .gitattributes
git commit -m "track .gz files with Git LFS"
```

### 4. Add & Commit Large File

```bash
git add access_log.gz
git commit -m "add large file using Git LFS"
git push -u origin lfs
```

### 5. Merge LFS Branch into Dev & Main

```bash
git checkout dev
git merge lfs
git push origin dev

git checkout main
git merge dev
git push origin main
```

### 6. Verified LFS on Fresh Clone

```bash
git clone <repo>
git lfs pull
ls -lh access_log.gz
```

LFS successfully downloaded the full file.

---

# Part 3 – Geometry Calculator (Git Stash Workflow)

## Overview

A new Python module (`GeometryCalculator.py`) was developed while practicing `git stash` to manage incomplete work across two feature branches:

* `feature/circle-area`
* `feature/rectangle-area`

The objective was to stash partial implementations, switch tasks, and resume work safely.

## Steps Completed

### A. Create Circle Feature Branch

```bash
git checkout dev
git checkout -b feature/circle-area
```

Added **incomplete** circle code → stashed:

```bash
git stash push -u -m "WIP: circle area implementation"
```

### B. Create Rectangle Feature Branch

```bash
git checkout dev
git checkout -b feature/rectangle-area
```

Added **incomplete** rectangle code → stashed:

```bash
git stash push -u -m "WIP: rectangle area implementation"
```

### C. Restore Circle Stash and Complete Feature

```bash
git checkout feature/circle-area
git stash pop stash@{circle_index}
```

Implemented full circle + rectangle code.
Committed & pushed:

```bash
git add GeometryCalculator.py
git commit -m "feat(circle): complete circle area implementation"
git push -u origin feature/circle-area
```

### D. Restore Rectangle Stash and Complete Feature

```bash
git checkout feature/rectangle-area
git stash pop stash@{rectangle_index}
```

Completed rectangle implementation.
Committed & pushed:

```bash
git add GeometryCalculator.py
git commit -m "feat(rectangle): complete rectangle area implementation"
git push -u origin feature/rectangle-area
```

### E. Pull Requests to Dev

Two PRs were created:

* `feature/circle-area → dev`
* `feature/rectangle-area → dev`

After review, both were merged.

### F. Merge into Main

```bash
git checkout main
git merge dev
git push origin main
```

Geometry Calculator is now fully implemented and released.

---

# Final Project Structure

```
.
├── CalculatorPlus.py
├── GeometryCalculator.py
├── test_calculator.py
├── access_log.gz (LFS-tracked)
├── .gitattributes
├── .gitignore
└── README.md
```

---

# Summary

This repository demonstrates complete mastery of:

* Branching strategies (`dev`, feature branches, release tagging)
* Git LFS configuration and verification
* Git stash for managing multiple parallel features
* Pull requests, reviews, and merges
* Full Git workflow mirroring real-world team development