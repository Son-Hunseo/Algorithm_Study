# N(가게의 부품 개수)를 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)를 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 내가 구현한 코드와의 차이점은 list는 순서가 존재하는 데이터 타입이지만 set은 순서가 존재하지 않는 데이터 타입이다.
# 따라서 List는 in에서 O(n)이고 Set은 in O(1)이므로 set을 사용하는 것이 맞다.