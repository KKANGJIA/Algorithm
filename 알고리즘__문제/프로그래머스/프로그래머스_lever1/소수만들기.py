from itertools import combinations


def solution(nums):
    nums_sum = [sum(i) for i in list(combinations(nums, 3))]

    sosu = []
    for j in nums_sum:
        for k in range(2, j):
            if j % k == 0:
                sosu.append(j)

    not_sosu = list(set(sosu))

    result = [x for x in nums_sum if x not in not_sosu]
    return len(result)


nums = [1, 2, 3, 4]
# nums = [1, 2, 7, 6, 4]
print(solution(nums))
