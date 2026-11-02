def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]

sorted_numbers = bubble_sort(numbers)

print("Sorted array:", sorted_numbers)