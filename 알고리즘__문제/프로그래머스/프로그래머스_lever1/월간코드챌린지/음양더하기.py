def solution(absolutes, signs):
    result = []
    for i in range(len(absolutes)):
        result.append(
            absolutes[i]) if signs[i] == True else result.append(-absolutes[i])
    return sum(result)


# absolutes = [4, 7, 12]
absolutes = [1, 2, 3]
# signs = [true, false, true]
signs = [false, false, true]

print(solution(absolutes, signs))
