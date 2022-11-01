# 유형 1 : 가장 기본적인 정렬을 할 수 있는지 물어보는 문제
n = int(input())
data = [int(input()) for i in range(n)] ### 리스트 컴프리핸션
# 또는
# array = [] 이후 for문과 array.append(int(input()))를 사용해도 된다.

data.sort(reverse=True)
# 또는
# data = sorted(data, reverse = True)

for i in range(n):
    print(data[i], end=' ')
# 또는
# for i in data:
#     print(i, end=' ')