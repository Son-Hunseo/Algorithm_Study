# 퀵 정렬(Quick Sorting)
# 가장 많이 사용되는 정렬 알고리즘
# 퀵 정렬과 비슷하게 빠른 알고리즘으로는 병합 정렬(Merge Sorting)이 있다
# 기준(Pivot)을 설정한 후 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
# 피벗과 리스트를 분할하는 방법에는 여러가지가 있는데 대표적인 호어 분할(Hoare Partition)을 사용
# Part 1
# 1. 첫번째 원소를 Pivot으로 설정
# 2. 이후 Pivot을 제외한 리스트에서 왼쪽에서부터 Pivot보다 큰 데이터 선택, 오른쪽에서부터 Pivot보다 작은 데이터 선택한 후 두 데이터 위치 변경
# 3. 반복하다가 위치가 엇갈리는(교차함) 때 작은 데이터와 Pivot의 위치를 변경
# 4. 이 과정이 되면 Pivot 왼쪽에는 Pivot보다 작은 데이터 오른쪽에는 Pivot보다 큰 데이터가 위치하고 이 과정을 분할(Divide) 또는 파티션(Partition)이라고 함
# Part 2 (재귀적)
# 왼쪽 리스트에서 Part 1을 반복
# 오른쪽 리스트에서 Part 1을 반복
# Part 3
# 이 과정을 분할 된 리스트의 데이터 개수가 1개일 때 까지 반복 (종료 조건)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start # Pivot은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면(교차) 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할(파티션) 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 (재귀)
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 시간 복잡도 : O(NlogN)
# Worst Case : O(N^2) [이미 데이터가 정렬 되어있는 경우] 이 경우 Insertion Sorting이 좋다


