def solution(s):
    if len(s) % 2 == 0:
        return list(s)[(len(s) // 2) - 1]+list(s)[len(s) // 2]
    else:
        return list(s)[(len(s) // 2)]


s = "qwer"
print(solution(s))
