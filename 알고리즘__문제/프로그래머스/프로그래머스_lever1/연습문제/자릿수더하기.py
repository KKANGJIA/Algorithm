def solution(n):
    sum = 0
    for i in list(str(n)):
        sum += int(i)
    return sum


n = 123
n = 987
print(solution(n))
