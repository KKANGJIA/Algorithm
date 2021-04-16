# 문제해석 잘못 접근... 풀이전략부터 다시짜기
# 입력값 리스트 내포한 거 반복학습하기

import sys

N = int(input())  # 점들의 개수

point_arr = []  # 입력을 저장할 리스트
for _ in range(N):
    # 리스트 컴프리헨션을 이용 ★★입력 패턴 기억하기★★
    point_arr.append([int(i) for i in sys.stdin.readline().split()])
# print(point_arr)

# 리스트 ★안과 밖★에서 정렬
# print(sorted(point_arr))
points = sorted(point_arr)  # 점들을 리스트로 정렬

# first_list = []
# second_list = []
# for i in range(0, N):  # 점들의 색깔 별로 개수 나누기
#     if points[i][1] == 1:
#         first_list.append(points[i][1])
#     elif points[i][1] == 2:
#         second_list.append(points[i][1])

# print(first_list, second_list)
