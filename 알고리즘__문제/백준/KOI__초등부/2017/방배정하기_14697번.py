
A, B, C, N = map(int, input().split())  # 각 방의 침대 수 # 총 학생 수
# print(A, B, C, N)


def div_room(A, B, C, N):
    cnt = 0
    # 한 종류의 방에 배정이 가능한 경우 N//A니까
    for i in range(N//A+1):
        for j in range(N//B+1):
            for k in range(N//C+1):
                if (A * i) + (B * j) + (C * k) == N:  # 3개 방에 나눠 넣기
                    cnt = 1
    if cnt == 1:
        return 1
    else:
        return 0


print(div_room(A, B, C, N))
