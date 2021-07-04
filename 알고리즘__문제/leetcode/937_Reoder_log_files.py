# def reorderLogFiles(logs):
#     lets = sorted([i[5:] for i in logs if i[:3] == 'let'])
#     digits = sorted([i[3:] for i in logs if i[:3] == 'dig'])
#     result = []  # 정렬 후 결과 담는 곳

#     # ['art can', 'art zero', 'own kit dig', '1 8 1 5 1', '2 3 6']
#     reorder = lets + digits


# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
#         "let2 own kit dig", "let3 art zero"]
# print(reorderLogFiles(logs))


'''
# split()을 이용해서 쉽게풀이할 수있음 굳이 슬라이싱으로 결과내지 않아도 된다!
1. 람다와 + 연산자를 이용
def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            # print(log.split()[1])  # 8 3
            digits.append(log)
        else:
            # print(log.split()[1])  # art art own
            letters.append(log)

    # 문자열 split()
    # 두 개의 키를 람다 표현식으로 정렬
    # 식별자를 제외한 문자열 [1:]을 키로하여 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록 람다 표현식울 사용해 정렬
    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
'''
