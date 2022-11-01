# AdjacencyList는 LinkedList를 이용하여 구현
# Java나 C++에서는 표준 라이브러리를 제공하지만
# Python에서는 리스트 자료형이 append()와 메소드를 제공하므로
# 배열과 연결 리스트의 기능을 모두 기본으로 제공한다

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리(엣지))
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리(엣지))
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리(엣지))
graph[2].append((0, 5))

print(graph)

### [] 리스트 () 튜플 {} 딕셔너리