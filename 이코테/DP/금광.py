# 테스트 케이스 입력(여러개가 반복되며 들어오니까 반복문)
for tc in range(int(input())):
  # 금광 정보 입력
  n, m = map(int, input()) # N X M
  gold_number = map(int, input().split()) # 열의 금의 개수
  array = list(gold_number);

  # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
  dp = []
  index = 0
  for i in range(n): 
    dp.append(array[index : index + m]) # 인덱스 슬라이싱해서 2차원 배열을 만듬
    index += m
    
  # 다이나믹 프로그래밍 진행
  for j in range(1, m): # 열, 1부터 진행
    for j in range(n): # 행
      # 왼쪽 위에서 오는 경우(인덱스를 벗어나는 지 확인)
      if i == 0: left_up = 0
      else: left_up = dp[i-1][j-1]
      # 왼쪽 아래에서 오는 경우(인덱스를 벗어나는 지 확인)
      if i == n-1: left_down = 0
      else: left_down = dp[i+1][j-1]
      # 왼쪽에서 오는 경우
      left = dp[i][j-1]

      dp[i][j] = array[i][j] + max(left_up, left, left_down)
  
  result = 0
  # 가장 오른쪽 열에 값들 중 큰 값을 찾아 출력하도록 만든다
  for i in range(n):
    result = max(result, dp[i][m-1])
  print(result)