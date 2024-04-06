def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


if __name__ == '__main__':
    arr = [2, 1, 7, 5, 11, 0]
    insertion_sort(arr)
    print('sorted array:',arr)
