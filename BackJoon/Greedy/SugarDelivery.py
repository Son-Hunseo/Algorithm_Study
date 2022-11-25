data = int(input())

# case 1
bag5_1 = data//5
bag3_1 = (data - bag5_1*5)//3
result_1 = data - (bag5_1*5) - (bag3_1*3)

# case 2
bag3_2 = data//3
bag5_2 = (data - bag3_2*3)//5
result_2 = data - (bag3_2*3) - (bag5_2*5)

if result_1 != 0 and result_2 != 0:
    print(-1)
elif result_1 == 0 and result_2 != 0:
    print(bag5_1+bag3_1)
elif result_2 == 0 and result_1 != 0:
    print(bag3_2+bag5_2)
elif result_2 == 0 and result_1 == 0:
    bagnumber = bag5_1+bag3_1
    if bag5_1+bag3_1 > bag5_2+bag3_2:
        bagnumber = bag5_2+bag3_2
    print(bagnumber)
