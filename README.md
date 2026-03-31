# 🏠 OptiHostel: Smart Room Allotment System

Welcome to **OptiHostel**! If you've ever dealt with the chaos of hostel room assignments, you know that random allocation often leads to mismatched roommates and lifestyle clashes. This project is a Python-based solution that uses **Heuristic Search** to pair students based on their habits, majors, and facility preferences.

## 🌟 What does it do?
OptiHostel isn't just a spreadsheet; it's a "Problem-Solving Agent" that:
- **Prioritizes Compatibility:** Matches "Night Owls" with "Night Owls" and "Early Birds" with "Early Birds."
- **Respects Preferences:** Ensures students who need AC get AC rooms, while keeping gender-specific wings separate.
- **Optimizes Space:** Efficiently fills rooms to capacity while maintaining the highest possible compatibility score.

## 🚀 Getting Started

### 1. Prerequisites
You’ll need **Python 3.x** installed on your machine. You can grab it from [python.org](https://www.python.org/).

### 2. Setup
Clone this repository or download the files into a folder:
```bash
git clone https://github.com/iamanupambharti/AI-ML-Project-Vityarthi.git
cd OptiHostel
```

### 3. Data Preparation
The system reads student data from `students.csv`. You can open this file in Excel or any text editor to add your own data. Make sure to follow this format:
- `name`: Student's name
- `gender`: Male / Female
- `major`: Field of study (e.g., CSE, ECE)
- `study_habit`: Night Owl / Early Bird
- `prefers_ac`: Yes / No

### 4. Running the Allotment
Simply run the script using your terminal or command prompt:
```bash
python main.py
```
The system will process the list and print a clean report of which students were paired together in which rooms.

## 🧠 How it Works (The "AI" Bit)
Under the hood, OptiHostel follows a logical flow:
1. **Perception:** It reads the `students.csv` file to understand the "environment."
2. **Hard Constraints:** It first filters students by Gender and AC preference (you can't put a student in a Non-AC room if they paid for AC!).
3. **Heuristic Matching:** It calculates a "Match Score." For example, if two students share the same Major and Study Habits, they get a higher priority to be roommates.
4. **Allocation:** It places students in rooms (capacity of 2) based on the best available matches.

## 📂 Project Structure
- `main.py`: The brain of the project containing the allocation logic.
- `students.csv`: Your database of student preferences.
- `project-report.docx`: A detailed breakdown of the project's academic concepts.

---
