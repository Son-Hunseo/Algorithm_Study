h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 고칠 점
            # if문 에서의 포함 여부 in 사용 가능
            # str로 자료형 변환 활용
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)