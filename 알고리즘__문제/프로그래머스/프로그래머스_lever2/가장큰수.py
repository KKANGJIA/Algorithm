from itertools import permutations, combinations  # 순열 모듈
# 최대 값을 구하는거기 때문에 permutation은 필요 없다는 결과...
# 모듈없이 푸는 방법 생각해보기
numbers = [6, 10, 2]
print(list(permutations(numbers)))
print(list(combinations(numbers, 2)))

# def solution(numbers):
#     arr = []

#     for i in list(permutations(list(map(str, numbers)))):
#         arr.append((''.join(i)))
#     return max(arr)


# # numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
# print(solution(numbers))
