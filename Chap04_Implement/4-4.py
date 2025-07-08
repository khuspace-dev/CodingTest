# 문자열 재정렬
# chap4. 322 page

# S = 주어진 문자열

S = input()

text = []
count = 0

for i in S:
    if i.isalpha():
        text.append(i)
    else:
        count += int(i)

text.sort()
result = ""
for i in range(len(text)):
    result = result + text[i]

result = result + str(count)
print(result)

# 이걸 ''.join(text) + str(count)로 줄일 수 있음 