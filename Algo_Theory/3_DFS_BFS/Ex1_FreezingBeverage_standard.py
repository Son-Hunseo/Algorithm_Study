n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input()))) ### 띄워지지 않은채 입력되는 경우 .split()을 붙이지 않으면 된다

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x>= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

### 범위 이탈 return False
### 범위 안에 있으면서 0의 위치일 경우 모든곳을 1로 채우고 return True
### 범위 안에 있으면서 1의 위치일 경우 return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result +=1

print(result)
