
def solution(arr1, arr2):
    tmp = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
        tmp = []  # 다음 덧셈을 위해 리스트 비우기
    return answer


arr1 = [[1, 2], [2, 3]]
# arr1 = [[1], [2]]
arr2 = [[3, 4], [5, 6]]
# arr2 = [[3], [4]]
print(solution(arr1, arr2))


'''
def solution(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
'''
