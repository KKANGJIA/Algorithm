# def solution(array, commands):
#     answer = []

#     for i in range(3):
#         cut_arr = array[commands[i][0] - 1: commands[i][1]]
#         sort_arr = sorted(cut_arr)
#         find_num = sort_arr[commands[i][2]-1]
#         answer.append(find_num)

#     return answer


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


'''
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
'''

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
