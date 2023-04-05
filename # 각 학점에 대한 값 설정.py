# 각 학점에 대한 값 설정
grades = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

# 사용자로부터 수강과목 수를 입력받음
num_courses = int(input("수강 과목 수를 입력하세요: "))

# 수강과목 수만큼 반복하면서 학점, 평점을 입력받음
submit_grades = []
view_grades = []
for i in range(num_courses):
    name = input(f"{i+1}번째 과목명을 입력하세요: ")
    credit = int(input(f"{name}의 학점을 입력하세요: "))
    grade = input(f"{name}의 평점을 입력하세요(A+, A, B+, B, C+, C, D+, D, F): ")
    submit_grades.append((credit, grade))
    view_grades.append((credit, grade))

# 제출용 학점 계산
submit_total_credits = 0
submit_total_grade_points = 0
for credit, grade in submit_grades:
    if grade != "F":
        submit_total_credits += credit
        submit_total_grade_points += credit * grades[grade]

submit_gpa = submit_total_grade_points / submit_total_credits

# 열람용 학점 계산
view_total_credits = 0
view_total_grade_points = 0
for credit, grade in view_grades:
    view_total_credits += credit
    view_total_grade_points += credit * grades[grade]

view_gpa = view_total_grade_points / view_total_credits

# 제출용 학점과 학점평균 출력
print("제출용 학점:")
print(f"총 학점: {submit_total_credits}")
print(f"GPA: {submit_gpa:.2f}")

# 열람용 학점과 학점평균 출력
print("열람용 학점:")
print(f"총 학점: {view_total_credits}")
print(f"GPA: {view_gpa:.2f}")