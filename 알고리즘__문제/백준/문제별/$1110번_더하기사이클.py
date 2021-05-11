n = input()


def plus_cycle(n):

    listN = list(n)  # ['2', '6']
    intN = int(n)  # 26
    cnt = 0  # 사이클 횟수
    newNum = 0

    a = []
    a.append(n)
    # print(a, end='/')
    # print(a[0])

    while (a[0] != newNum):
        if intN < 10:
            n = str(0) + n
        else:
            result = list(str(int(listN[0]) + int(listN[1])))
            # print(result)
            if int(listN[0]) + int(listN[1]) < 10:
                result = str(0) + str(result[0])
                # print(result) # 08

            newNum = listN[1] + result[1]  # 68
            # print(newNum, end='//')

            cnt += 1  # 새로운 수가 만들어질 때 1을 증가
            # print(cnt)

            if a[0] == newNum:  # 처음 입력한 숫자와 새로운 숫자가 일치하면 함수 종료
                break
                return cnt
            else:
                return plus_cycle(newNum)


print(plus_cycle(n))
