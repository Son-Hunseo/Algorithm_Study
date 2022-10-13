# What is the least number of coins for change?

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