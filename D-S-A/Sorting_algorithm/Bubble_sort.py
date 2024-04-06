def bubble_sort_max_order(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                flag = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # temp = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j + 1] = temp
        if flag == 0:
            return


if __name__ == '__main__':
    arr = [32, 4, 17, 3, 1, 20, 0, 46.5, 20]
    bubble_sort_max_order(arr)
    print("Sorted Array:", arr)
