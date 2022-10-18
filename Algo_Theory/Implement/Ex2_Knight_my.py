# 주어진 좌표에서 기사가 이동할 수 있는 경우의 수

location = input()

count = 0

# 좌표를 숫자로 바꿈
# str은 바꿀 수 없으므로 새로운 문자열을 정의해야함 location[0] = 1 과 같은 형태 불가
if location[0] == 'a':
    coordinate_str = '1' + location[1]
elif location[0] == 'b':
    coordinate_str = '2' + location[1]
elif location[0] == 'c':
    coordinate_str = '3' + location[1]
elif location[0] == 'd':
    coordinate_str = '4' + location[1]
elif location[0] == 'e':
    coordinate_str = '5' + location[1]
elif location[0] == 'f':
    coordinate_str = '6' + location[1]
elif location[0] == 'g':
    coordinate_str = '7' + location[1]
elif location[0] == 'h':
    coordinate_str = '8' + location[1]


# check 1
if int(coordinate_str[0]) < 3:
    x1 = 1
elif 3 <= int(coordinate_str[0]) <= 6:
    x1 = 2
elif 6 < int(coordinate_str[0]):
    x1 = 1

if int(coordinate_str[1]) == 1:
    y1 = 1
elif 2 <= int(coordinate_str[1]) <= 7:
    y1 = 2
elif int(coordinate_str[1]) == 8:
    y1 = 1

# check 2
if int(coordinate_str[1]) < 3:
    y2 = 1
elif 3 <= int(coordinate_str[1]) <= 6:
    y2 = 2
elif 6 < int(coordinate_str[1]):
    y2 = 1

if int(coordinate_str[0]) == 1:
    x2 = 1
elif 2 <= int(coordinate_str[0]) <= 7:
    x2 = 2
elif int(coordinate_str[0]) ==8:
    x2 = 1

# result
result = x1*y1 + y2*x2

print(result)





