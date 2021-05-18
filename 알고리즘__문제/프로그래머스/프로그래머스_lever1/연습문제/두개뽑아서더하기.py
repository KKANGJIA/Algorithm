def twoNumPlus(numbers):
    new_arr = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            new_arr.append(numbers[i] + numbers[j])
    return sorted(set(new_arr))


# numbers = [2, 1, 3, 4, 1]
numbers = [5, 0, 2, 7]
print(twoNumPlus(numbers))


'''조합 모듈 사용하기
from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))
'''
