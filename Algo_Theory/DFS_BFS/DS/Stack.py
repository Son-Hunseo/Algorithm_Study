# stack
# LIFO : Last In First Out

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력

### 슬라이싱
### [1:4] 두 번째 원소부터 네 번째 원소 까지 (인덱스 1부터 3까지)
### [::-1] 처음의 원소부터 -1씩 인덱스를 증가시키며 슬라이스 (따라서 역순)
print(stack[::-1]) # 최상단 원소부터 출력



