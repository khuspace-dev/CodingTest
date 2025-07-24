# 가사 검색
# chap7. 370 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

def binarySearch(words, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if words[mid] == target:
            return mid 
        elif words[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def solution(words, queries):
    words.sort()
    length = len(words)
    answer = []
    
    for query in queries:
        binarySearch(words, query, 0, length)
    
    return answer