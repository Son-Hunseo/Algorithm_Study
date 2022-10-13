# Input datas

##########################################

# List

# Input the number of datas
# Ex) 5
n = int(input())

# Input splited datas by blanks
# list(map(function, list))
# Ex) 65 90 75 34 99
data = list(map(int, input().split()))

# Sorting reverse
data.sort(reverse = True)
print(data)
# Ex Result) [99, 90, 75, 65, 34]

##########################################

# Non-list
# Ex) 3, 5, 7
n, m, k = map(int, input().split())

print(n, m, k)
# Ex Result) 3, 5, 7
