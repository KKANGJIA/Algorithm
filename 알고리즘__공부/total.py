# 1부터 n까지의 합을 구하는 기본 알고리즘
a = list(range(1, n+1))

for _ in a:
    result = sum(a)

print(result)


# 1부터 n까지의 합을 구하는 피타고라스의 식을 이용해서 (n*(n+1)) // 2
pitagoras = (n*(n+1)) // 2
print(pitagoras)
