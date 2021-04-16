
N = int(input())

score = list(map(int, input().split()))

# print(score)


def minus_max_min(score):
    n = len(score)
    sortList = sorted(score)
    return sortList[n-1] - sortList[0]


# score = [85, 42, 79, 95, 37, 11, 72, 32]
print(minus_max_min(score))
