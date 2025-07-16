# 국영수
# chap6. 359 page

# 학생 수 N명 
# 국어 점수 내림차순 -> 영어 점수 오름차순 -> 수학 점수 내림차순 -> 이름 사전 순

N = int(input())
students = []

for i in range(N):
    name, kor, eng, mat = input().split()
    students.append((name, int(kor), int(eng), int(mat)))

students.sort(key=lambda x: (-x[1],x[2],-x[3],x[0])) # 국어로 정렬된 상태

for i in students:
    print(i[0])

""" 
12 
Junkyu 50 60 100 
Sangkeun 80 60 50 
Sunyoung 80 70 100 
Soong 50 60 90 
Haebin 50 60 100 
Kangsoo 60 80 100
Donghyuk 80 60 100 
Sei 70 70 70 
Wonseob 70 70 90 
Sanghyun 70 70 80 
nsj 80 80 80
Taewhan 50 60 90
 """