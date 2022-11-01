# 1이 될 때 까지 1을 빼거나 k로 나눔
# 연산의 횟수 세기

n, k = map(int, input().split())

result = n
count = 0

while result != 1 :
    if result%k != 0 :
        result -= 1
        count += 1
    else :
        result /= k
        count += 1

print(count)

