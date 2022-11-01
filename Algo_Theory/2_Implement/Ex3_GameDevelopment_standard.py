n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 캐릭터의 좌표, 방향 입력 받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보를 입력받기
### 나의 구현과 다른 점
### 나는 맵만 입력 받아서 맵에서 가본 곳 자체를 2로 바꾸는 작업을 했지만
### 정답에서는 맵과 방문한 위치를 따로 기록하였다
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
# 오답정리 : 방향에 대한 정의가 나올 경우 dx dy로 나누는 것이 좋다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1: # 오답정리 : 순환하는 구조일 경우의 처리를 이렇게 하면 되구나
        direction = 3

# 시뮬레이션 시작
### nx ny를 정의 해 두고 조건이 맞을 경우에 x y를 nx ny로 바꾸고 아닐경우 적용 x
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction] # - 로 뒤로 가는 것을 표현
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
