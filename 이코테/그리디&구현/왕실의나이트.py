# 현재의 나이트의 위치 입략빋기
input_data = input()
row = int(input_data[1])
# 문자열로 들어온 위치를 아스키 코드로 바꾸고
column = int(ord(input_data[0])) - int(ord('a')) + 1 # a=1 b=2 c=3
# print(row, column)

# 나이트가 이동할 수 있는 8가지 방향의 정의(방향 백터를 사용)
steps = [(-2, -1), (-1, -2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)] 

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result) 

