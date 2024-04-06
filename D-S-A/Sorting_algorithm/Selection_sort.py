"""IN EVERY ITERATION FIND THE MINIMUM NUMBER IN THE UNSORTED ARRAY,
   AND MOVE IT TO THE NEXT SORTING POSITION"""


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i + 1, len(arr)):  # SIMPLY IN THIS LOOP WE ARE TAING THE MIN OF UNSORTED ARRAY
            if arr[min_index] > arr[j]:
                index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    arr = [17, 30, 4, 7, 9, 5, 11, 5, 0]
    selection_sort(arr)
    print('sorted array:', arr)
