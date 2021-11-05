# 두 개의 정수를 받음
N,M = map(int, input().split())

# 미로의 정보, 공백없이 붙이므로 split는 붙아면 안된당
graph = []
for i in range(N):
  graph.append(list(map(int,input())))

def dfs(x, y):
  # 범위를 벗어나는 곳은 갈 수 없으니까 제외한다
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  # 1인 곳은 괴물이 없으니까 방문 가능
  if graph[x][y] == 1:
    if dfs(x, y-1) == 1: # 하
       graph[x][y-1] = graph[x][y] + 1
    elif dfs(x+1, y) == 1: # 우
       graph[x+1][y] = graph[x][y] + 1
    return True
  # 0인 곳은 괴물이 있으니까 방문 불가
  return False

move = 0
for i in range(N):
  for j in range(M):
    bfs(i,j)

print(move)



