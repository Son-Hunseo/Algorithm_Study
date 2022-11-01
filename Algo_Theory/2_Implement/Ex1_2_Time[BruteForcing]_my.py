# N시 59분 59초까지 3이 하나라도 포함되는 모든 경우의 수를 구하기

n = int(input())

count = 0

for i in range(n+1):
# count hour include 3
    if i == 3 or i == 13:
        count += 3600
    # count minute include 3
    else:
        for j in range(60):
            if j == 3 or j == 13 or j == 23 or 30 <= j <= 39 or j == 43 or j == 53:
                count += 60
            # count second include 3
            else:
                for k in range(60):
                    if k == 3 or k == 13 or k == 23 or 30 <= k <= 39 or k == 43 or k == 53:
                        count += 1

print(count)