'''
입력 데이터 개수 많음 -> input() 함수 시간 초과 
sys 라이브러리 readline() 이용하기
ex) input_data = sys.stdin.readline().rstrip() -> enter 제거 
'''

# 부품 찾기 
# chap6. 197 page

# 부품 N개, 손님이 M개 부품번호 요청

N = int(input())
things = list(map(int, input().split()))

M = int(input())
wants = list(map(int, input().split()))

# result = set(wants).issubset(things)
# print(result) # 부품 별로 no, yes

for i in wants:
    if i in things:
        print("yes")
    else:
        print("no")