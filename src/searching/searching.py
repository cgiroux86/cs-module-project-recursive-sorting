# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target, count=0):
    # Your code here
    pivot = (len(arr)) // 2
    print('pivot', pivot)
    if arr[pivot] == target:
        return pivot
    elif arr[pivot] < arr[0]:
        if arr[pivot] < target:
            return pivot + agnostic_binary_search(arr[pivot:], target)
        else:
            return agnostic_binary_search(arr[:pivot], target)
    elif arr[pivot] > arr[0]:
        if arr[pivot] > target:
            return pivot + agnostic_binary_search(arr[:pivot], target)
        else:
            return agnostic_binary_search(arr[pivot:], target)
    else:
        return -1


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# arr = [2, 3, 4, 10, 40]

print(agnostic_binary_search(arr1, 2))
