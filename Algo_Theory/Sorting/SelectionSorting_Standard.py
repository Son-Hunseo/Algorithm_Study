# 선택 정렬(Selection Sorting)
# 1. 가장 작은 데이터를 선택 해 맨 앞에있는 데이터와 바꾼다.
# 2. 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾼다.
# 3. 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    ### 가장 작은 원소 찾기

    array[i], array[min_index] = array[min_index], array[i]
    # 파이썬의 Swap : 다른 언어의 경우 임시 저장용 변수를 만들어야 하지만 파이썬은 이렇게 편하게 구현 가능

print(array)

# 선택 정렬(Selection Sorting)
# 시간 복잡도 : O(N^2)
# 다른 알고리즘과 비교했을 때 비효율적
# 하지만 특정한 리스트에서 가장 작은 데이터를 찾는 로직이 자주 사용되므로 이 코드를 반복작성하며 기억할 필요성이 있다