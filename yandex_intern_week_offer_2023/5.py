students_count, uni_count = map(int, input().split())

unis = list(map(int, input().split()))

students = []
for i in range(students_count):
    student = tuple(map(int, input().split()))
    rating = student[0]
    application_count = student[1]
    applications = student[2:]

    students.append((i, rating, application_count, applications))

students.sort(key=lambda x: (x[1], x[2]))

ans = []

for student in students:
    uni_enrolled = -1
    for application in student[3]:
        if unis[application-1] > 0:
            uni_enrolled = application
            unis[application-1] -= 1
            break

    ans.append((student[0], uni_enrolled))

for student in sorted(ans, key=lambda x: x[0]):
    print(student[1], end=' ')




"""
4 2
1 5
3 1 1
1 1 2
2 2 1 2
3 2 1 2
"""