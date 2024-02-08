N, D = map(int, input().split())
students = list(map(int, input().split()))
sort_students = sorted(students)

variants = []
variants_count = 0

ans = {}
for student in sort_students:
    for i in range(variants_count):
        if student - variants[i] > D:
            variants[i] = student
            ans[student] = i + 1
            break

    if student not in ans:
        variants.append(student)
        variants_count += 1
        ans[student] = variants_count

print(variants_count)
for student in students:
    print(ans[student], end=' ')

