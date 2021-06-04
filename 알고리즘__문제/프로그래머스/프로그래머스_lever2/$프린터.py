# def solution(priorities, location):
#     priorities1 = [c for c in range(len(priorities))]  # index 위치 저장
#     priorities2 = priorities.copy()  # 값 저장 (출력되는 값)

#     i = 0  # for 문처럼 정해진 변수가 없으니까 선언 초기화 변수증가까지 지정하기
#     while True:
#         if priorities2[i] < max(priorities2[i+1:]):
#             priorities1.append(priorities1.pop(i))
#             priorities2.append(priorities2.pop(i))
#         else:
#             i += 1

#         if priorities2 == sorted(priorities2, reverse=True):
#             break

#     return priorities1.index(location) + 1


# '''deque를 활용하면 약 절반정도 빠름'''
from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])
    print(d)  # deque([(1, 0), (1, 1), (9, 2), (1, 3), (1, 4), (1, 5)])

    while len(d):
        item = d.popleft()
        print(item)
        if d and max(d)[0] > item[0]:
            d.append(item)
            print(d)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
