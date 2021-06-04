def solution(left, right):
    divisor = []  # 약수
    result = []  # 결과 값

    for j in range(left, right+1):
        for i in range(1, right+1):
            if j % i == 0:
                divisor.append(i)
        if len(divisor) % 2 == 0:
            result.append(j)
        else:
            result.append(-j)
        divisor = []

    return sum(result)


left = 13
right = 17
print(solution(left, right))
