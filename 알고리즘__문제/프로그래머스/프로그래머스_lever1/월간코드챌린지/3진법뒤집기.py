def solution(n):
    rev_base = ''
    answer = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    answer = [int(num) * (3**idx) for idx, num in enumerate(rev_base[::-1])]
    
    # 형변환을 위한 int()
    # answer = int(rev_base, 3)

    return sum(answer)


n = 45
# n = 125

print(solution(n))
