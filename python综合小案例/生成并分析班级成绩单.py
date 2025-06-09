import random

# 1. 生成随机成绩数据
students = []
for i in range(1, 31):
    student = {
        "name": f"学生{i}",
        "math": random.randint(50, 100),
        "chinese": random.randint(50, 100),
        "english": random.randint(50, 100)
    }
    students.append(student)

# 2. 计算平均分
def calculate_average(students, subject):
    total = sum(student[subject] for student in students)
    return total / len(students)

avg_math = calculate_average(students, "math")
avg_chinese = calculate_average(students, "chinese")
avg_english = calculate_average(students, "english")

# 3. 找出总分最高的学生
for student in students:
    student["total"] = student["math"] + student["chinese"] + student["english"]

top_student = max(students, key=lambda s: s["total"])

# 4. 排名前 5 的学生
students_sorted = sorted(students, key=lambda s: s["total"], reverse=True)
top_5 = students_sorted[:5]

# 5. 输出结果
print("各科平均分：")
print(f"数学：{avg_math:.2f}, 语文：{avg_chinese:.2f}, 英语：{avg_english:.2f}\n")
print(f"总分最高的学生是：{top_student['name']}，总分为 {top_student['total']}\n")
print("成绩排名前 5 的学生：")
for rank, student in enumerate(top_5, start=1):
    print(f"第{rank}名：{student['name']} - 总分：{student['total']}")
