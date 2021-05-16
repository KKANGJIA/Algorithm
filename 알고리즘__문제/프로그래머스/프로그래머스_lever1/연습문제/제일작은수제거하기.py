def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_num = min(list(set(arr)))
        index_num = arr.index(min_num)
        arr.pop(index_num)
        return arr


# arr = [4, 3, 2, 1]
arr = [10]
print(solution(arr))
