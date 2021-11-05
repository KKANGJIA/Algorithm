n, m = map(int, input().split()) # 화폐의 개수, 총 금액
array = [] # 화폐가치 배열

# N개의 줄에 화폐가치가 나오게 하기
for i in range(n):
  array.append(int(input())) 

#화폐개수를 출력할 곳
#(화폐개수의 단위가 0,1,2,3... 이니까 화폐 개수로 만들 수 없도록 10001의 임의의 큰 수를 넣어준 것)
d = [10001] * (m + 1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0 # 화폐개수 0개
for i in range(n):
  for j in range(array[i], m + 1): # 2부터 15 # 3부터 15
    if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j - array[i]] +  1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])
  




