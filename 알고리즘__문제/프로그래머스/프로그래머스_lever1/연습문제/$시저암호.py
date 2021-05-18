def code(s, n):
    alpa = 'abcdefghijklmnopqrstuvWxyz'
    up_alpa = alpa.upper()
    if s.isupper():
        return up_alpa[up_alpa.rindex(s)+n: up_alpa.rindex(s) + len(s) + 1].upper()
        if alpa.rindex(s) >= len(s)-1:
            s = 'a'
            return up_alpa[up_alpa.rindex(s)]
    elif s.islower():
        return alpa[alpa.rindex(s)+n: alpa.rindex(s) + len(s) + 1]
        if alpa.rindex(s) >= len(s)-1:
            s = 'a'
            return alpa[alpa.rindex(s)]


'''
def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ind = low.find(char)+n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
        elif char in up:
            ind = up.find(char)+n
            answer += up[ind%26]
        else: # 공백일 경우도 고려
            answer += " "
    return answer
     
solution("a B z E", 4) # 'e F d I'
'''


'''아스키 코드를 사용한 풀이(문자와 숫자가 대응하는 관계를 가진 함수, ord()와 chr())
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)
 
print(caesar("a B z", 4)) # 'e F d'
 
'''


s = 'z'
# s = 'abcd'
# s = "AB"
# s = "a B z"
n = 1
print(code(s, n))
