def solution(s):
    # return s.isdigit()
    for i in range(len(s)):
        if s[i] in range(1, 9):
            continue
        else:
            return False
    return True


# s = "a234"
s = "1234"

print(solution(s))
