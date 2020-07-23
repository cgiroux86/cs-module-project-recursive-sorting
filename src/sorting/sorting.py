# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged = []
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            merged.append(arrA[0])
            arrA.pop(0)
        else:
            merged.append(arrB[0])
            arrB.pop(0)
    merged.extend(arrA[:])
    merged.extend(arrB[:])

    # Your code here

    return merged

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    mid = len(arr) // 2
    if len(arr) > 1:
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)
    return arr


def quick_sort(arr, l, h):
    if l <= h:
        p = partition(arr, l, h)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, h)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    s = mid + 1
    print('s', s)
    if arr[mid] <= arr[s]:
        return
    while start <= mid and s <= end:
        if arr[start] <= arr[s]:
            start += 1
        else:
            val = arr[s]
            idx = s
            while idx != start:
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[start] = val
            start += 1
            mid += 1
            s += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
        print(arr)
    return arr
    # return arr


a = [4, 14, 9, 1, 5, 4, 7, 8, 2, 3]

print(merge_sort_in_place(a, 0, len(a) - 1))
