# 유형 1, 3 (라이브러리를 사용하거나 정수인 것을 파악해 계수 정렬 사용)
n = int(input())

data = []
for i in range(n):
    studata = input().split()
    data.append((studata[0], int(studata[1]))) ### 튜플 방식으로 입력받는 방법

def setting(data):
    return data[1]

result = sorted(data, key=setting)
# 다른 방법
# result = sorted(data, key=lambda student: student[1])

for i in result:
    print(i[0], end=' ')
# 좀 더 직관적으로 하려면
# for student in result: print(student[0], end = ' ')

# 학생의 정보가 최대 100,000개까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘(라이브러리)을 이용하거나
# O(N)을 보장하는 계수 정렬을 이용하면 된다.
