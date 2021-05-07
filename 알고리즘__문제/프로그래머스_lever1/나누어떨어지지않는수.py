
def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        if len(answer) == 0:
            return [-1]
    return answer

# def solution(arr, divisor):
#     answer = []
#     arr.sort()
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     return answer if len(answer)!=0 else [-1]

# def solution(arr, divisor):
#     return sorted([n for n in arr if n % divisor == 0]) or [-1]


# arr = [5, 9, 7, 10]
# divisor = 5
arr = [2, 36, 1, 3]
divisor = -1
# arr = [3, 2, 6]
# divisor = 10

print(solution(arr, divisor))

# 5분만에 해결
