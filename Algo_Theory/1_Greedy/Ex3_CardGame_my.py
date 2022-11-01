# 각 행에서 가장 작은 수 선택
# 각 행에서 가장 작은 수 중 큰 수 선택

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    # data를 sort 해서 찾는 방법 보다는 min() max() 함수를 쓰는 것이 더 적절할 것 같다.
    # min_value = min(data)
    # result = max(result, min_value)
    if data[0] >= result:
        result = data[0]
    i += 1

print(result)


