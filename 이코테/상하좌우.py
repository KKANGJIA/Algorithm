# 파이썬에서 Switch문은 존재 x

# 시간복잡도 O(N)
# 조건문으로 풀기
N = int(input()) # 5
directions = list(input().split()) # R R R U D D
start_x = 1  
start_y = 1

for direction in directions:
  if direction == 'L':
    start_y -= 1
    if start_y < 1:
      start_y += 1
  elif direction == 'R':
    start_y += 1
    if start_y < 1:
      start_y += 1
  elif direction == 'U':
    start_x -= 1
    if start_x < 1 :
        start_x += 1
  elif direction == 'D':
    start_x += 1
    if start_x < 1 :
        start_x += 1
    # print(start_x, start_y)
    
print(start_x, start_y) # 3 4
