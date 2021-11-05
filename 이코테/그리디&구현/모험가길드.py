# n = int(input()) # 모험가의 수
# panic = list(map(int,input().split())) # 각 공포도
# group = 0 # 그룹 수
# setGroup = list(map(int, set(panic))) # ['1','2','3'] # 중복제거한 모험가의 공포도

# # print(panic,setGroup)

# for i in setGroup:
#   if panic.count(setGroup[i-1]) >= i: # 공포도보다 크거나 같은 경우
#     group += (panic.count(setGroup[i-1]) // i)  # 그룹을 만들 수 있는 수로 나눠서 그룹 수 더하기
#   else: # 공포도 X가 X 이하인 경우에는 
#     pass # 그냥 지나가기

# print(group)


#  /********************************************************/

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도를 낮은 것부터 하나씩 확인하여
  count += 1 # 현재 그룹애 해당 모험가를 포함시키기 
  print(count, 'count')
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 # 그룹의 총 수 증가
    print(result, 'result')
    count = 0 # 현재 그룸에 포함된 모험가의 수 초기화
    print('초기화')

print(result) # 그룸의 수 출력

// 연산과정
# 1 count
# 1 result
# 초기화
# 1 count
# 2 count
# 2 result
# 초기화
# 1 count
# 2 count
# 2