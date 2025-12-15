students = [
    {"id": 1, "name": "Rohan"},
    {"id": 2, "name": "Amit"},
    {"id": 3, "name": "Sneha"}
]

marks = [
    {"student_id": 1, "marks": 85},
    {"student_id": 2, "marks": 90},
    {"student_id": 3, "marks": 88}
]

marks_map = {m["student_id"] : m["marks"] for m in marks }
result = [ ]

for student in students:
    student_data = student.copy()
    student_data["marks"] = marks_map.get(student["id"])
    result.append(student_data)
    
print(result)
