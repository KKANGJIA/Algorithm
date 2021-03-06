# X = int(input()) # 정수
# cnt = 0 # 연산 횟수

# d = [0] * X

# while(X > 1):
#   if X == 2 or X == 5 or X == 3:
#     X -= 1
#   if X == 1:
#     break

#   if X % 5 == 0: # 제일 큰 수로 나누기
#     X // 5
#     cnt += 1
#   elif X % 5 != 0 : 
#     if X % 3 == 0: # 다음 큰 수로 나누기 
#       X // 3
#       cnt += 1
#     elif X % 3 != 0 : 
#       if X % 2 == 0: # 다음 큰 수로 나누기
#         X // 2 # 13
#         cnt += 1
#       elif X % 2 != 0 : # 나누기가 안되면 
#         X -= 1 # 1 빼기 
#         cnt += 1

# print(cnt)

#--------------------------------------------------------------

x = int(input()) # 정수
# 앞서 계산된 결과(최소연산횟수)를 저장하기 위한 DP 테이블 초기화
# d[0]는 필요없어서 1부터 시작하고자 30001개로 설정한 것임
d = [0] * 30001 # x가 3만까지 가능하다고 나왔기 때문임

# 다이나믹 프로그래밍 진행(바텀업) => 반대로 계산해서 올라가면서 계산 횟수를 구하는 과정
for i in range(2, x + 1):
  d[i] = d[i-1] + 1 # d[2] = d[1]+1 => 1
  #현재의 수가 2로 나누어 떨어지는 경우
  if i % 2 == 0: 
    d[i] = min(d[i], d[i//2] + 1) #d[2] = min(d[2], d[1]+1)
  #현재의 수가 3로 나누어 떨어지는 경우
  if i % 3 == 0: 
    d[i] = min(d[i], d[i//3] + 1) #d[3] = min(d[3], d[1]+1)
  #현재의 수가 5로 나누어 떨어지는 경우
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)
  print(d)
  # [0, 0, 1, 1, 2, 1, 2, 3, 3, 2, 2, 3, 3, 4, 4, 2, 3, 4, 3, 4, 3, 4, 4, 5, 4, 2, 3]

print(d[x])




