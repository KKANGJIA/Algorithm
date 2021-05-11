def solution(s):
    print(s.upper())
    return True if list(s.upper()).count('P') == list(s.upper()).count('Y') else False


# s = "pPoooyY"
s = "Pyy"
print(solution(s))
