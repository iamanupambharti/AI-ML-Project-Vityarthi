# OptiHostel: Heuristic-Based Room Allotment


## Project Overview
OptiHostel is an intelligent system designed to solve the real-world problem of college hostel room allocation. Instead of random assignment, this project uses **Heuristic Search** and **Constraint Satisfaction** to pair students based on gender, facility preference, and lifestyle compatibility.

## Project Structure
```text
OptiHostel/
├── main.py          # The core AI engine with search logic
├── students.csv     # Dataset of student features and preferences
├── README.md        # Setup and execution instructions
└── report.md        # Project documentation 
```
## Concepts Applied
- **Intelligent Agents :** The system acts as a rational agent that perceives student data and acts to maximize compatibility.
- **Problem-Solving Agents :** Defined as a goal-based search where the "Goal State" is 100% allocation with high compatibility.
- **Heuristic Search :** Uses a weighted scoring system (Study Habits + Degree) to find optimal roommates.
- **Constraint Satisfaction:** Enforces hard constraints (Gender/AC) before processing soft preferences.


## 🛠️ Setup & Installation
1. **Install Python:**
   - Ensure you have Python 3.10 or higher installed.
   - If not installed, download it from [python.org](https://www.python.org/downloads/).
   - During installation on Windows, **critically check the box** that says "Add Python to PATH".
   - 
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/iamanupambharti/AI-ML-Project-Vityarthi.git
   cd OptiHostel