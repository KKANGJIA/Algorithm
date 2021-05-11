def solution(arr):

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
            print(arr)
        else:
            pass

    return arr


arr = [1, 1, 3, 3, 0, 1, 1]
# arr = [4, 4, 4, 3, 3]

print(solution(arr))

# print(dir(collections.Counter))
