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

#************************************************************************#

# bisect 모듈을 사용해서 이진 탐색을 해결하는 방식

from bisect import bisect_left, bisect_right

# 값이 [bisect_left, bisect_right]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index, left_index
  
N, x = map(int, input().split()) # 정수의 개수, 찾는 값
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
  print(-1)
#  값이 x인 원소가 존재한다면
else:
  print(count)

