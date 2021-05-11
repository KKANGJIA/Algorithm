def solution(strings, n):
    string = []
    for i in range(len(strings)):
        string.append(list(sorted(strings))[i][n])
    return sorted(string)


strings = ["sun", "bed", "car"]
# strings = ["abce", "abcd", "cdx"]
print(solution(strings, 1))
