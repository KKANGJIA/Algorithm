from collections import Counter
# Counter(array) # ({2: 4, 1: 2, 3: 1})

N, x = map(int, input().split()) # 정수의 개수, 찾는 값
array = list(map(int, input().split())) # [1,1,2,2,2,2,3]

mid = array[len(array) // 2] # 2
def findX(array, mid, N, x):
  if mid == x:
    print(dict(Counter(array)).get(x))
  elif mid > x:
    mid -= 1
    return findX(array, mid, N, x)
  elif mid < x:
    mid += 1
    return findX(array, mid, N, x)

findX(array, mid, N, x)

# 15~ 20분 소요

