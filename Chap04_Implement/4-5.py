# 문자열 압축
# chap4. 323 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# S = 압축할 문자열

def solution(s):
    min_length = len(s)
    
    for i in range(1, len(s)//2 + 1):
        temp_length = 0
        comp = 1
        first = s[0:i] # 기준
        
        for j in range(i, len(s), i):
            if s[j:j+i] == first:
                comp += 1
            else:
                if comp == 1:
                    temp_length = len(first) 
                else:
                    temp_length += 1 + len(first)
                
                first = s[j : j+i]
                comp = 1

        if comp == 1:
            temp_length = len(first) 
        else:
            temp_length += 1 + len(first)     

        min_length = min(temp_length, min_length)
    return min_length