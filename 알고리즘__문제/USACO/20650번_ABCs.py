nums = list(map(int, input().split()))  # 7개 정수받기


def find_ABC(nums):
    sortNums = sorted(nums)
    # A, B를 제일 작은 수
    A = sortNums[0]
    B = sortNums[1]
    C = sortNums[-1] - (A+B)

    return A, B, C


A = find_ABC(nums)
a, b, c = A
print(a, b, c)

# 위의 코드 간략하게
# nums = list(sorted(map(int,input().split())))
# a,b = nums[0],nums[1]
# c = nums[-1]-a-b
# print(a,b,c)

# 풀이 방법은 비슷했으나 문법에 문제가 있다.
