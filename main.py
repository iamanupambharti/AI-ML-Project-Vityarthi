import csv
import os

class HostelAllocator:
    def __init__(self):
        self.students = []
        self.allocations = {}
        
        self.rooms = {
            'Boys_AC': [101, 102, 103],
            'Boys_NonAC': [201, 202, 203],
            'Girls_AC': [301, 302, 303],
            'Girls_NonAC': [401, 402, 403]
        }
        self.room_capacity = 2

    def load_data(self, filename):
        """Perception: Reading the environment data from CSV"""
        if not os.path.exists(filename):
            print(f"Error: {filename} not found.")
            return False
        
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.students.append(row)
        
        print(f"--- Data Loaded: {len(self.students)} students found ---")
        return True

    def calculate_compatibility(self, student_a, student_b):
        """Heuristic Function: Calculates a match score (Module 2)"""
        score = 0
        if student_a['major'] == student_b['major']:
            score += 1
        if student_a['study_habit'] == student_b['study_habit']:
            score += 2
        return score

    def allocate(self):
        """The Search Process: Finding the best room for each student"""
        for student in self.students:
            gender_type = "Boys" if student['gender'] == 'Male' else "Girls"
            ac_type = "AC" if student['prefers_ac'] == 'Yes' else "NonAC"
            required_category = f"{gender_type}_{ac_type}"
            
            is_placed = False
            
            for room_no in self.rooms[required_category]:
                
                if room_no not in self.allocations:
                    self.allocations[room_no] = [student]
                    is_placed = True
                    break
                
                elif len(self.allocations[room_no]) < self.room_capacity:
                    existing_student = self.allocations[room_no][0]
                    match_score = self.calculate_compatibility(student, existing_student)
                    
                    if match_score >= 2:
                        self.allocations[room_no].append(student)
                        is_placed = True
                        break
            
            if not is_placed:
                for room_no in self.rooms[required_category]:
                    if len(self.allocations.get(room_no, [])) < self.room_capacity:
                        if room_no not in self.allocations:
                            self.allocations[room_no] = []
                        self.allocations[room_no].append(student)
                        is_placed = True
                        break

    def display_results(self):
        """Output: Showing the final decisions of the Intelligent Agent"""
        print("\n======================================")
        print("   FINAL HOSTEL ALLOCATION RESULTS")
        print("======================================\n")
        
        for room_no in sorted(self.allocations.keys()):
            occupants = self.allocations[room_no]
            names = " & ".join([person['name'] for person in occupants])
            habit = occupants[0]['study_habit'] if len(occupants) > 0 else ""
            
            print(f"Room {room_no} [{habit} Section]: {names}")
            
        print("\n======================================")

if __name__ == "__main__":

    agent = HostelAllocator()
    
    if agent.load_data('students.csv'):
        agent.allocate()
        agent.display_results()