# 주어진 수 들을 더해 가장 큰 숫자를 생성
# n개의 자연수가 주어지며 m번 더하여 가장 큰 숫자를 생성한다
# 같은 숫자는 최대 k번까지만 더해질 수 있다
# m은 항상 k보다 크거나 같다

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)