import math


def solution(n):
    x = math.sqrt(n)
    if n % x == 0:
        return math.trunc(x+1)**2
    else:
        return -1


n = 121
print(solution(n))
