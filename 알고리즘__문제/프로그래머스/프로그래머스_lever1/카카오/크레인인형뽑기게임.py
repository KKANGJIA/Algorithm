def solution(board, moves):
    answer = []
    bucket = []  # 인형 담을 바구니

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0  # 인형을 뺀 곳은 0으로 인형 제거
                if bucket[-1:] == bucket[-2:-1]:  # 바구니에 담긴 요소들이 밑에서부터 동일하다면
                    answer += bucket[-1:]  # 임시위치에 중복요소를 하나만 저장하고
                    bucket = bucket[:-2]  # 중복된 앞의 두 요소를 제외하고 바구니에 요소 저장
                break  # break를 걸어서 찾으면 그 다음을 찾지 않게 해줌 (가장 위에 것만 뽑아가니까)
    return len(answer)*2


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
