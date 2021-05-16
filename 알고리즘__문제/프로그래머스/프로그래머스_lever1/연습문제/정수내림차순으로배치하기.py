def solution(n):
    sort_num = []
    for i in sorted(str(n), reverse=True):
        sort_num.append(int(i))
    return "".join(map(str, sort_num))


n = 118372
print(solution(n))

# TypeError: sequence item 0: expected str instance, int found
# 에러가 발생하는 이유는 리스트안에 요소가 문자가 아닌 정수, 실수이기때문 따라서 요소를 문자로 바꿔주면 에러가 해결된다.

# sort와 sorted쓰는 방법은 다르다!
# ls.sort(reverse = True)
