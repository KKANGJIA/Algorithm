def solution(s):
    arr_s = list(s)
    if len(arr_s) == 0:
        return 1
    else:
        for i in range(len(arr_s) - 1):
            if arr_s[i] == arr_s[i+1]:
                arr_s = arr_s[:i] + arr_s[i+2:]
                print(arr_s)
                # 맨 앞으로 가서 탐색하는 걸 하지 못하니까...


s = 'baabaa'
print(solution(s))
