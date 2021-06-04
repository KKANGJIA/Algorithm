from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    # return queue

    while queue:
        temp, idx = queue.popleft()
        print(temp, idx)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
            print(queue)
        else:
            if temp == target:
                answer += 1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 2

print(solution(numbers, target))


# # 완전탐색을 이용해서 풀 수 있고 완전탐색에 brute-force 도 있고 dfs 도 있음

# # numbers = [1, 1, 1, 1, 1]
# numbers = [1, 2, 1, 2]
# target = 2
# total = 0
# cnt = 0

# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         total += numbers[j]

#         if target < total:
#             total - numbers[j]
#         elif target > total:

#         else:
#             cnt += 1
#             total = 0

# print(cnt)
