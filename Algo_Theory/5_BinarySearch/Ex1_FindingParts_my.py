# Finding Parts
n = int(input())
store_parts = list(map(int, input().split()))
m = int(input())
customer_parts = list(map(int, input().split()))

for i in range(m):
    if customer_parts[i] in store_parts:
        print("yes", end=" ")
    else:
        print('no', end=" ")

# in 연산자는 하나하나 순회하기 때문에 O(n)으로 많은 시간이 걸린다
# 따라서 내가 구현한 코드는 결국 O(m*n)이다. (시간 초과 가능성이 있음)
# 0<n<100만, 0<m<10만
# 정렬을 한 뒤 이진탐색 알고리즘으로 구현하면 O((m+n)*log(n))으로 확연히 짧아진다.