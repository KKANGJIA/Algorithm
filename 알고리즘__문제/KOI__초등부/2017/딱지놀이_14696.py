# 입력
import sys
L = int(input())  # 총 라운드 수
round = []
for i in range(2*L):
    # A 카드모양 수 , 모양번호 # B 카드모양 수 , 모양번호
    A = [int(i) for i in list(map(int, input().split()))]
    round.append(A)  # 라운드마다 A, B의 카드

# 카드의 모양에 번호를 지정
# star = 4
# circle = 3
# square = 2
# triangle = 1

print(round)
# a = round[0][1:].count(4)
# print(a)


def Battle_AB(round):  # 별 개수 비교
    for i in range(0, L):
        if round[i][1:].count(4) != round[i + 1][1:].count(4):  # 별 개수가 다르다면
            if round[0][1:].count(4) > round[i + 1][1:].count(4):
                result = 'A'
                print(result)
            else:
                result = 'B'
                print(result)
        elif round[i][1:].count(4) == round[i + 1][1:].count(4):  # 별 개수가 같다면
            if round[i][1:].count(3) > round[i + 1][1:].count(3):
                result = 'A'
                print(result)
            elif round[i][1:].count(3) == round[i + 1][1:].count(3):
                return
            else:
                result = 'B'
                print(result)

                if round[i][1:].count(3) == round[i + 1][1:].count(3):  # 동그라미 개수가 같다면
                    if round[i][1:].count(2) > round[i + 1][1:].count(2):
                        result = 'A'
                    elif round[i][1:].count(2) == round[i + 1][1:].count(2):
                        return
                    else:
                        result = 'B'
                        print(result)

                    if round[i][1:].count(2) == round[i + 1][1:].count(2):  # 네모 개수가 같다면
                        if round[i][1:].count(1) > round[i + 1][1:].count(1):
                            result = 'A'
                            print(result)
                        elif round[i][1:].count(1) == round[i + 1][1:].count(1):
                            result = 'D'
                            print(result)
                        else:
                            result = 'B'
                            print(result)
        i += 2

    return result
# 모든 라운드에 함수적용


ab = Battle_AB(round)
print(ab)


# -------------------------------------------------------------------------------------------------------------------
sys.stdin = open("input.txt", 'r')

# a,b를 따로 만들어서 비교하는 전략
N = int(input())
a = [0]
b = [0]
state = True
for _ in range(N*2):
    data = input().split()
    cnt = [0, 0, 0, 0, 0]
    if state:
        for i in range(1, len(data)):
            cnt[int(data[i])] += 1
        a.append(cnt)
        state = False
    else:
        for i in range(1, len(data)):
            cnt[int(data[i])] += 1
        b.append(cnt)
        state = True

for i in range(1, N+1):
    for j in range(4, 0, -1):
        if a[i][j] > b[i][j]:
            print('A')
            break
        elif a[i][j] < b[i][j]:
            print('B')
            break
    else:
        print('D')
