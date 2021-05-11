N = int(input())  # 9
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)

count_zero = 0
count_one = 0
count_minus = 0


def divide_paper(x, y, n):
    if n == 1:  # 더이상 나눌 수 없으몀
        if paper[x][y] == 0:
            count_zero += 1
        elif paper[x][y] == 1:
            count_one += 1
        elif paper[x][y] == -1:
            count_minus += 1

        return count_minus, count_zero, count_one

    for i in range(x, x + n):
        for j in range(y, y + n):
            if(paper[i][j] != paper[x][y]):
                divide_paper(x, y, n//3)
                divide_paper(x, y+n//3, n//3)
                divide_paper(x+n//3, y, n//3)
                divide_paper(x+n//3, y+n//3, n//3)


print(divide_paper(0, 0, N))
