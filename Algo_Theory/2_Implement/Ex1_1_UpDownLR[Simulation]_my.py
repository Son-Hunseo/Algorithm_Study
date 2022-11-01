# 명령대로 이동하는 알고리즘
# break 는 모든 반복문 빠져나감
# 그냥 넘어가고 싶다면 continue

N = int(input())

data = list(map(str, input().split()))

start = [1, 1]

for i in range(len(data)) :
    if data[i] == "U" :
        if start[0] <= 1 :
            continue
        else :
            start[0] -= 1
    ######################
    elif data[i] == "D" :
        if start[0] >= N :
            continue
        else :
            start[0] += 1
    ######################
    elif data[i] == "L" :
        if start[1] <= 1 :
            continue
        else :
            start[1] -= 1
    ######################
    elif data[i] == "R" :
        if start[1] >= N :
            continue
        else :
            start[1] += 1
    ######################

print(start)

