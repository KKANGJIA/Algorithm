def solution(x, n):

    if x == 0:
        return [0]*n

    return list(range(x, x*n+1, x)) if x > 0 else list(range(x, x*n-1, x))


print(solution(0, 5))
