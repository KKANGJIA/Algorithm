def solution(x):
    temp = list(str(x))
    sum = 0

    for i in range(len(temp)):
        sum += int(temp[i])

    return True if x % sum == 0 else False


x = 106
print(solution(x))
