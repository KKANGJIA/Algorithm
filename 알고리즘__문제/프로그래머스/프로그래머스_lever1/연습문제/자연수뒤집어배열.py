
def solution(n):
    arr = list(str(n))
    arr.reverse()  # 리스트 리버스 함수 ☆

    return list(map(int, arr))


n = 12345
print(solution(n))
