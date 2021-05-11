# def solution(a, b):
#     numbers = []
#     if a < b :
#         for i in range(a, b+1):
#             numbers.append(i)
#     else:
#         a, b = b, a
#         for i in range(a, b+1):
#             numbers.append(i)

#     return sum(numbers)


#  간결하게 줄여보기
def solution(a, b):
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))


def solution(a, b):
    return sum([i for i in range(a, b+1)]) if a < b else sum([i for i in range(b, a+1)])


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

'''다른 사람 풀이
def solution(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

print( adder(3, 5))

# 수열 이용
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
'''
