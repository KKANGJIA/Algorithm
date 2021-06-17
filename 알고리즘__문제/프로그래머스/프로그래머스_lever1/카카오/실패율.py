# import collections


# def solution(N, stages):
#     challengers = len(stages)  # 도전자의 수
#     failure_rate = []  # 실패율
#     answer = []

#     # {2: 3, 1: 1, 6: 1, 4: 1, 3: 2}
#     now_stages = dict(collections.Counter(stages))

#     for stage in range(1, N+1):
#         if stage in now_stages:
#             failure_rate.append(now_stages[stage] / challengers)
#             challengers -= now_stages[stage]  # 이미 계산한 도전자 수를 제외
#         else:
#             now_stages[stage] = 0  # key가 없는 경우 keyError가 발생하기 때문
#             failure_rate.append(now_stages[stage] / challengers)

#     # 정렬: 키 함수를 사용해서 정렬하기
#     descending = [(idx, rate) for idx, rate in enumerate(failure_rate)]
#     sorted_descending = sorted(
#         descending, key=lambda des: des[1], reverse=True)
#     for i in range(len(descending)):
#         answer.append(sorted_descending[i][0] + 1)

#     return answer


# # stages = [2, 1, 2, 6, 2, 4, 3, 3]
# # N = 5
# stages = [4, 4, 4, 4, 4]
# N = 4
# print(solution(N, stages))
# # 답이 나오기는 하는데 런타임에러가 발생한다...


# 다른 사람의 풀이
def solution(N, stages):
    result = {}  # 실패율을 저장할 딕셔너리
    num = len(stages)  # 도전자 수

    for stage in range(1, N+1):
        if num != 0:  # 도전자 수가 0명이 아니면
            count = stages.count(stage)  # 도전자의 수를 세서
            result[stage] = count / num  # 전체 도전자에서 해당 스테이지에 있는 도전자의수를 나눈다
            num -= count  # 이미 계산한 도전자는 제외
        else:
            result[stage] = 0  # 도전자가 0명이면 0으로 계산

    # 키값만 가지고 나오도록 정렬
    return sorted(result, key=lambda x: result[x], reverse=True)


# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 5
stages = [4, 4, 4, 4, 4]
N = 4
print(solution(N, stages))
