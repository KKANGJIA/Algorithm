s_slicing = []
unit = []  # 문자열나누는단위


def solution(s):
    for i in range(1, len(s)):
        if s[0] != s[i:i+1]:  # 앞의 문자열로 압축불가능한 경우
            return len(s)
        else:
            for i in range(len(s)):  # 앞의 문자열로 압축가능한 경우
                if s[:i] == s[i:i*2]:  # 앞의 수부터 같은 게 반복되는 범위찾기
                    if i != len(s) and i != 0:
                        unit.append(i)
                        print('unit:', list(set(unit)))

                        for i in unit:
                            if len(s) % 2 != 0:
                                if s[0:i] == s[i:i*2]:
                                    print('2'+s[0:i]+s[i*2:])
                            else:
                                print('2'+s[:i])


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"

print(solution(s))
