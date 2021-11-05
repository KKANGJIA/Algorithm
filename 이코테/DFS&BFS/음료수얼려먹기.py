# 공백을 기준으로 구분하여 입력받기
N, M = map(int, input().split())

# 2차원 리스트 정보 입력받기
graph = []
for i in range(N):
  graph.append(list(map(int,input()))) 
print(graph) # [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

#dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  # 현재노드를 아직 방문하지 않았다면 
  if graph[x][y] == 0:
    #해당 노드 방문처리
    graph[x][y] = 1
    # 상하좌우 위치들도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    # 현재 위치에서 DFS 수행
    if dfs(i,j): # 첫방문시에만 아이스크림의 개수를 올림
      result += 1

# 정답출력
print(result)

# 입력
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력
# 3


# # 나의 코드 문제점 ------------------------------------------------------------
# # 로직을 너무 묶어서 처리하니까 복잡해지는 거, 분리해서 함수로 적용하기
# # for ice in iceGraph:
# #   for r in range(len(M)):
# #     for c in range(len(M)):
# #       if ice[r][c] == 0:
# #         if ice[r][c+1] == 0: # 상
# #         if ice[r][c-1] == 0: # 하
# #         if ice[r-1][c] == 0: # 좌
# #         if ice[r+1][c] == 0: # 우



