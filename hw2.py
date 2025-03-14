# 문자열 “My name is 본인이름” 에 대해 다음 물음에 답하라
a = 'My name is Youbin Kim'

# 문자열의 문자수를 출력하라.
print(len(a))

# 문자열을 10번 반복한 문자열을 출력하라.
print(a * 10)

# 문자열의 첫 번째 문자를 출력하라.
print(a[0])

# 문자열에서 처음 4문자를 출력하라.
print(a[:4])

# 문자열에서 마지막 4문자를 출력하라.
print(a[-4:])

# 문자열의 문자를 거꾸로 출력하라.
rev_a = ''
for i in range(0, len(a)):
    rev_a += a[len(a)-i-1]
print(rev_a)

# 문자열에서 첫번째 문자와 마지막 문자를 제거한 문자열을 출력하라.
print(a[1:len(a)-1])

# 문자를 모두 대문자로 변경하여 출력하라.
print(a.upper())

# 문자를 모두 소문자로 변경하여 출력하라.
print(a.lower())

# 문자열에서 'a'를 'e'로 대체하여 출력하라.  문자열.replace('a', 'e')
print(a.replace('a', 'e'))