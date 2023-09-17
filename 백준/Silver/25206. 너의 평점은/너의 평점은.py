total_grade = 0
scores = 0
grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

for i in range(20):
    subject, score, grade = input().split()
    score = float(score)
    if grade in grades:
        total_grade += grades[f"{grade}"] * score
        scores += score
    else:
        scores - score

print(total_grade / scores)
