x_val = []
y_val = []
x = 0
y = 0


def make_rectangular(v):
    for i in range(3):
        x_val.append(v[i][0])

    for i in range(4):
        if x_val.count(i) == 1:
            x = i

    for i in range(3):
        y_val.append(v[i][1])

    for i in range(11):
        if y_val.count(i) == 1:
            y = i

    return [x, y]


# v = [[1, 4], [3, 4], [3, 10]]
v = [1, 1], [2, 2], [1, 2]
print(make_rectangular(v))

# 한시간 왜...?
