# 성적이 낮은 순서로 학생 츨력하기
# chap6. 180 page

# N명의 학생 
# 이후로 수 -> 범위는 1 이상 100,000 이하의 자연수

N = int(input())
students = []

for i in range(N):
    name, score = input().split()
    score = int(score)
    students.append((name, score))

students.sort(key=lambda x: x[1])

for i in students:
    print(i[0], end=' ')
    # end= ' ' 없으면 new line 
