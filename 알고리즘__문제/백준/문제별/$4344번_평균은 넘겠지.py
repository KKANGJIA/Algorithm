T = int(input())  # 테스트 케이스 수

TestCase = [list(map(int, input().split())) for i in range(T)]

# print(T, TestCase, end='') 5 [[5, 50, 50, 70, 80, 100], [7, 100, 95, 90, 80, 70, 60, 50], [3, 70, 90, 80], [3, 70, 90, 81], [9, 100, 99, 98, 97, 96, 95, 94, 93, 91]]

total = []  # 각 줄의 점수의 총합
average = []  # 각 줄의 점수의 평균
for i in range(T):
    total.append(sum(TestCase[i][1:]))
    average.append(total[i] // TestCase[i][0])
# print(average) # [70, 77, 80, 80, 95]
# print(total) # [350, 545, 240, 241, 863]

filterScore = []
for i in range(T+1):
    for j in range(1, TestCase[i][0]+1):
        if TestCase[i][j] > average[i]:
            filterScore.append(TestCase[i][j])
    print('/')
print(filterScore)
