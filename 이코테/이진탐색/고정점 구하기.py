def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, (start + mid-1) // 2, start, mid - 1)
    else:
        return binary_search(array, (mid+1 + end) // 2, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

answer = binary_search(array, (0+n) // 2 , 0, n-1)
print(answer)
