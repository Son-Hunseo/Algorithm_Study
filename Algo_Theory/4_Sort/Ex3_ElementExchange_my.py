# 유형 2
n, k = input().split()
### n, k = map(int, input().split()) 벌써 까먹었냐..

List_A = list(map(int, input().split()))
List_B = list(map(int, input().split()))

for i in range(int(k)):
    min_index_A = 0
    max_index_B = 0

    for j in range(int(n)):
        if List_A[min_index_A] >= List_A[j]:
            min_index_A = j
        if List_B[max_index_B] <= List_B[j]:
            max_index_B = j

    List_A[min_index_A], List_B[max_index_B] = List_B[max_index_B], List_A[min_index_A]

result = 0

### 내가 구현한 코드는 O(N^2)이다 하지만 문제에서 N과 K의 범위가 10만이므로 이는 너무 느린 알고리즘이다
### 따라서 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야한다.

for i in List_A:
    result += i

print(result)


