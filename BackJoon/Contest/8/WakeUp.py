from sys import stdin
import math

a, b = map(int, input().split())
data = [0]*a
number = 0
for i in range(a):
    data[i] = list(map(int, stdin.readline().split()))

for i in range(len(data)):
    for j in range(len(data)):
        alarm = 0

        if i == j:
            continue

        else:
            # i
            if data[i][0] == 0:
                alarm = alarm + (b//data[i][1]+1)
            else:
                alarm = alarm + ((b//data[i][1]+1)-(data[i][0]//data[i][1]))

            # j
            if data[j][0] == 0:
                alarm = alarm + (b // data[j][1] + 1)
            else:
                alarm = alarm + ((b//data[j][1]+1)-(data[j][0]//data[j][1]))

            # 최소공배수 구하고 빼기
            lcm = math.lcm(data[i][1], data[j][1])

            if data[i][0] >= data[j][0]:
                if data[i][0] == 0:
                    alarm = alarm - (b//lcm+1)
                else:
                    if lcm>data[i][0]:
                        alarm = alarm - ((b//lcm+1)-1)
                    else:
                        alarm = alarm - ((b//lcm+1)-(data[i][0]//lcm))
            else:
                if data[j][0] == 0:
                    alarm = alarm - (b//lcm)
                else:
                    if lcm > data[j][0]:
                        alarm = alarm - ((b//lcm+1)-1)
                    else:
                        alarm = alarm - ((b//lcm+1)-(data[j][0]//lcm))

            if alarm > number:
                number = alarm
                ni = i+1
                nj = j+1

print(ni, end=' ')
print(nj)
print(number)