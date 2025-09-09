#Q.2 Implement if-elif-else conditions and loops (for, while) with real-world examples (e.g., student grades).

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F (Fail)"
    
    
students = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 65,
    "David": 35
}

print("Student Grades (using for loop):")
for name, marks in students.items():
    grade = calculate_grade(marks)
    print(f"{name}: {marks} -> {grade}")