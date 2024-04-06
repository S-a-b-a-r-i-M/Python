def binary_search(s, e, val, arr):
    mid = (s + e) // 2
    if arr[mid] < val:
        return binary_search(mid + 1, e, val, arr)
    elif arr[mid] > val:
        return binary_search(s, mid - 1, val, arr)
    else:
        return mid


if __name__ == '__main__':
    arr = [1, 3, 5, 9, 13, 17, 21, 47, 69, 73, 81, 85, 87, 89, 91, 93]
    print("index of 91 : ", binary_search(0, len(arr) - 1, 91, arr))
    print("index of 93 : ", binary_search(0, len(arr) - 1, 93, arr))
    print("index of 13 : ", binary_search(0, len(arr) - 1, 13, arr))
