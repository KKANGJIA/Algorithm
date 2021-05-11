def solution(n):
    # if n % 2 == 0:
    #     return '수박' * int(n//2)
    # else:
    #     return '수박' * int(n//2) + '수'

    return '수박' * int(n//2) if n % 2 == 0 else '수박' * int(n//2) + '수'


# n = 3
# n = 4
print(solution(n))


'''다른사람풀이: 문자열슬라이싱
# def water_melon(n):
#     return ("수박"*n)[0:n]
'''
