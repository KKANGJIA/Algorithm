N = int(input())
answer = []

for _ in range(N):
    answer.append(list(input()))

# [['O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O'], ['O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O'], ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X']]
# print(answer)

score = []  # 점수
cnt = 0  # 연속횟수


for i in range(N):
    for j in range(i):
        if answer[i][j] == 'O':
            print(1)
            if answer[i][j] and answer[i][j+1] == 'O':
                print(answer[i][j], answer[i][j+1])
                cnt += 1
                print(cnt)
                score.append(cnt)
            else:
                print(0)

        else:
            score.append(0)


print(score)
print(sum(score))
