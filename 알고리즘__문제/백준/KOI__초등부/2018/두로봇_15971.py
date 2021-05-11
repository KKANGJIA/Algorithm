N = list(map(int, input().split()))
L = [[int(i) for i in input().split()]
     for _ in range(N[0]-1)]  # 5개의 input 이차원 리스트로 받기
print(L)  # [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4]]

n = len(L)

# 로봇의 위치에서 이동을 시작하고 길이를 비교해서 짧은 곳부터 이동 로봇이 같은 통로에서 만날 떄 까지 짧은 경로 비교해서 이동시킨다.

# 로봇의 시작 위치
robo1_loc = 1
robo2_loc = 9

cleanL = sorted(L)
print(cleanL)

# 통로의 길이를 비교해서 작은 순서대로 이동
# 로봇은 방 번호 차이가 1이 나는 곳에서 만나자
short_aisle = []  # 짧은 길이의 통로
for i in range(n):  # robo1
    for k in range(n-1, 0, -1):  # robo2

        # 각 로봇의 시작 위치의 i = 0 j = 4
        if (cleanL[i][0] == robo1_loc or cleanL[i][1] == robo1_loc) and (cleanL[k][0] == robo2_loc or cleanL[k][1] == robo2_loc):

            # for j in range(n):  # 로봇의 통로 위치를 알기 위한
            #     # 로봇 방이 통로로 연결되어 있으면
            #     for length in [int(i) for i in range(15)]:
            #         # print(length)
            #         location = [robo1_loc, robo2_loc, int(length)]
            #         # print(location)
            #         if location in cleanL[j]:
            #             break  # 반복문 종료
            #             print(short_aisle)
            #             print(sum(short_aisle))

            if cleanL[i][2] < cleanL[k][2]:  # 통로의 길이가 더 짧은 것을
                short_aisle.append(cleanL[i][2])  # 리스트에 저장한다
                robo1_loc = cleanL[i][1]
                # print(cleanL[i])

            elif cleanL[i][2] > cleanL[k][2]:
                short_aisle.append(cleanL[k][2])
                robo2_loc = cleanL[k][1]  # 5, 이동한 애를 방 번호 변경해주기
                # print(cleanL[k])


# 최소 경로 출력
print(short_aisle)
print(sum(short_aisle))

# 반복문 break 거는 거만 해결하면 끝날 듯...!!!
# 아직 미해결!!!
