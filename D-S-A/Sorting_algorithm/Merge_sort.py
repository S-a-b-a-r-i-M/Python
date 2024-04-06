def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])  # IT WONT AFFECT THE ORIGINAL ARRAY
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    joined_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            joined_arr.append(left[i])
            i += 1
        else:
            joined_arr.append(right[j])
            j += 1

    while i < len(left):
        joined_arr.append(left[i])
        i += 1
    while j < len(right):
        joined_arr.append(right[j])
        j += 1

    return joined_arr


def merge_in_place(arr, start, mid, end):
    joined = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            joined.append(arr[i])
            i += 1
        else:
            joined.append(arr[j])
            j += 1

    while i <= mid:
        joined.append(arr[i])
        i += 1

    while j <= end:
        joined.append(arr[j])
        j += 1

    for i in range(len(joined)):
        arr[start + i] = joined[i]


def merge_sort_in_place(arr, start, end):
    if (end - start) < 1:
        return

    mid = (start + end) // 2

    merge_sort_in_place(arr, start, mid)
    merge_sort_in_place(arr, mid + 1, end)

    merge_in_place(arr, start, mid, end)


if __name__ == '__main__':
    arr = [8, 5, 3, 1, 7, 6, 2, 0]
    print("Sorted Array:", merge_sort(arr))
    merge_sort_in_place(arr, 0, len(arr)-1)
    print("Sorted array in place :", arr)
