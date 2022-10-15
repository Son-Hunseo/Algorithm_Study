# 동전의 개수를 가장 적게하여 거스름돈을 거슬러주어라

# n is the amount of change
n = 1260
count = 0

# types of coins
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # counting coins
    n %= coin

print(count)
# Result : 6