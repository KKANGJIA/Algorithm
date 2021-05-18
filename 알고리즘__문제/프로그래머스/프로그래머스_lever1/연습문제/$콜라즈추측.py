# def solution(num):
#     numbers = []
#     if num == 1:
#         print(numbers)
#         return len(numbers)

#     else:
#         if num % 2 == 0:
#             num = num // 2
#             numbers.append(num)
#             solution(num)

#         else:
#             num = num * 3 + 1
#             numbers.append(num)
#             solution(num)


def solution(num):
    count = 0  # cnt 맨 위에 정의하고
    while True:  # while문으로 반복돌리면 cnt가 0이 될 일이 없음...ㅠ
        if num == 1:
            return count
        count += 1  # 마지막 1도 추가해야함

        if num % 2:
            num *= 3
            num += 1
        else:
            num /= 2
        if count == 500:
            return -1


num = 6
print(solution(num))
