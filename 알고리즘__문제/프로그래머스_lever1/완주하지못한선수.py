def solution(participant, completion):
    for i in participant:
        if i not in completion:
            answer = i
            return answer


# ''' counter함수를 사용하면 객체끼리 뺄셈가능
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # print(collections.Counter(participant),
    #       ' = ', collections.Counter(completion)) # Counter({'marina': 1, 'josipa': 1, 'nikola': 1, 'vinko': 1, 'filipa': 1})  =  Counter({'josipa': 1, 'filipa': 1, 'marina': 1, 'nikola': 1})
    # print(answer) # Counter({'vinko': 1})
    # print(answer.keys()) # dict_keys(['vinko'])
    # print(list(answer.keys())) # ['vinko']
    return list(answer.keys())[0] # vinko
# '''


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))
