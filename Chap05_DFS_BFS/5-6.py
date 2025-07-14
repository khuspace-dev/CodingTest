# 괄호 변환 
# chap5. 346 page 
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def isGood(string): # 스택에 넣었다 빼면 이거 구현할 수 있음
    stack = [] 
    
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    
    return True

def reversedStr(string):
    output = ''

    for i in string:
        if i == '(' :
            output += ')'
        else:
            output += '('

    return output

def split(string):
    lparen = 0
    rparen = 0

    for i in range(len(string)):
        if string[i] == '(':
            lparen += 1
        else:
            rparen += 1 
        if lparen == rparen :
            return string[:i+1], string[i+1:]

def recursive(string):
    if string == '':
        return ''
    
    u, v = split(string)
    
    if isGood(u) == True:
        return u + recursive(v)
    else: 
        # 앞 뒤 끝 제거하고 넣어주기 
        return '(' + recursive(v) + ')' + reversedStr(u[1:-1])
        

def solution(p):
    answer = recursive(p)
    return answer