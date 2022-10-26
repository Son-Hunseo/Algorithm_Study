# Queue
# FIFO : Fist In First Out
from collections import deque
# 파이썬에서 큐를 구현할 때는 deque 사용
# deque는 스택과 큐의 장점을 모두 채택한 자료구조이다
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 간단하다

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# popleft : stack과 다르게 먼저들어온 요소를 pop
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
