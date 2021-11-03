N = int(input()) # 식량창고 개수
K = list(map(int, input().split())) # 식량 창고에 저장된 식량의 개수

total= [0] * (N-2) #[2,8,6]
result = 0 # 최대값

for i in range(N-2): # 0~N
  # 두개면 더할 수가 없으니까 큰 값을 고르기
  if N <= 2:
    result = max(K[i])  
  
  # 계산
  total[i] = K[i] + K[i + 2]

  # 현재값이 더 크면 result 할당
  if total[i-1] < total[i]:
    result = total[i]

# 식량의 최대값을 구하기
print(result)




#-----------------------------------------------------------------

n = int(input()) # 식량창고 개수
array = list(map(int, input().split())) # 식량 창고에 저장된 식량의 개수

# 앞서 계산된 결과를 저장하기 위해나 DP테이블 초기화
d = [0] * 100 # N은 100까지 가능하다고 문제 조건에 주어졌음

#다이나믹 프로그래밍 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

# 계산된 결과 출력
print(d[n-1])