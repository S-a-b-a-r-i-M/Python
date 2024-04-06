def quick_sort(arr: [], s, e):
    if s >= e:
        return
    i, j = s, e
    while i < j:
        i += 1
        while i < e and arr[i] < arr[s]:  # WE ARE TAKING START INDEX AS A PIVOT
            i += 1

        while j > s and arr[j] > arr[s]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    quick_sort(arr, s, j - 1)
    quick_sort(arr, j + 1, e)


if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(arr, 0, len(arr) - 1)
    print('sorted array : ', arr)
