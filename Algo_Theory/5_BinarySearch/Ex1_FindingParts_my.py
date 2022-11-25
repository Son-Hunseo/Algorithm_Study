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