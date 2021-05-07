answers = [1, 3, 2, 4, 2]

supoja1 = [1, 2, 3, 4, 5]
supoja2 = [2, 1, 2, 3, 2]
supoja3 = [3, 3, 1, 1, 2]


# n = len(answer)
# print(answer)
a = []
b = []
c = []


def correct(answers):
    for i in range(5):
        if supoja1[i] == answers[i]:
            a.append(supoja1[i])
        if supoja2[i] == answers[i]:
            b.append(supoja2[i])
        if supoja3[i] == answers[i]:
            c.append(supoja3[i])
    print(a, b, c)

    if len(a) > len(b):
        if len(a) > len(c):
            return [1]
        elif len(a) < len(c):
            return [3]
    elif len(a) == len(b) == len(c):
        return [1, 2, 3]
    else:
        return [2]


print(correct(answers))
