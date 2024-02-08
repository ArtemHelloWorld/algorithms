N = int(input())

students = []
all_languages = set()

for _ in range(N):
    student = set()

    M = int(input())
    for _ in range(M):
        lang = input()
        student.add(lang)
        all_languages.add(lang)
    students.append(student)
all_students = students[0]
for student in students[1:]:
    all_students &= student

print(len(all_students))
for lang in all_students:
    print(lang)
print(len(all_languages))
for lang in all_languages:
    print(lang)

