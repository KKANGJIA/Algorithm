# DP로 푸는 문제
# 다음에 다시 풀기

def rectangular(board):
    for i in range(len(board)-1):  # 행
        for j in range(len(board[i])):  # 열
            if board[i][j] == board[i+1][j]:
                print(i, j, i+1)

    # return min(board[i].count(1))**2


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
# board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(rectangular(board))
