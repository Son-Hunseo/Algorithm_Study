n, m = input().split()

data = list(map(int, input().split()))

map = [list(map(int, input().split())) for _ in range(int(n))] # List Comprehension

location = [data[0], data[1]]

direction = data[2] # 0:north, 1:east, 2:south, 3:west

# 1은 바다 0은 육지 2는 가본 곳

count = 1

break_condition = 0

map[location[0]][location[1]] = 2 # 현재 위치는 가본 칸이기 때문

while True:
    # direction 0 : north
    if direction == 0:
       if map[location[0]][location[1]-1] == 0:
           direction = 3
           location[1] = location[1]-1
           map[location[0]][location[1]] = 2
           count += 1
           break_condition = 0
       else :
           direction = 3
           break_condition += 1
           if break_condition == 4 and map[location[0]+1][location[1]] == 2:
               location[0] = location[0]+1
               direction = 0
           elif break_condition == 4 and map[location[0]+1][location[1]] == 1:
               break
    # direction 3 : west
    elif direction == 3:
        if map[location[0]+1][location[1]] == 0:
            direction = 2
            location[0] = location[0]+1
            map[location[0]][location[1]] = 2
            count += 1
            break_condition = 0
        else :
            direction = 2
            break_condition += 1
            if break_condition == 4 and map[location[0]][location[1]+1] == 2:
                location[1] = location[1]+1
                direction = 3
            elif break_condition == 4 and map[location[0]][location[1]+1] == 1:
                break
    # direction 2 : south
    elif direction == 2:
        if map[location[0]][location[1]+1] == 0:
            direction = 1
            location[1] = location[1]+1
            map[location[0]][location[1]] = 2
            count += 1
            break_condition = 0
        else :
            direction = 1
            break_condition += 1
            if break_condition == 4 and map[location[0]-1][location[1]] == 2:
                location[0] = location[0]-1
                direction = 2
            elif break_condition == 4 and map[location[0]-1][location[1]] == 1:
                break
    # direction 1 : east
    elif direction == 1:
        if map[location[0]-1][location[1]] == 0:
            direction = 0
            location[0] = location[0]-1
            map[location[0]][location[1]] = 2
            count += 1
            break_condition = 0
        else :
            direction = 0
            break_condition += 1
            if break_condition == 4 and map[location[0]][location[1]-1] == 2:
                location[1] = location[1]-1
                direction = 1
            elif break_condition == 4 and map[location[0]][location[1]-1] == 1:
                break

print(count)


