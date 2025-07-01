# 모험가 길드
# chap3. 311 page 

# N = 모험가의 수 
# X = 공포도 

N = int(input())
fears = list(map(int, input().split()))
fears.sort(reverse=True) 

count = 0

while(len(fears) > 0):
    fears = fears[max(fears):]
    count += 1 

print(count)