def bubble_sort(arr):
    n = len(arr)
    steps = [arr.copy()]  # Save initial state
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                steps.append(arr.copy())  # Save state after swap

    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps
    }



def selection_sort(arr):
    n = len(arr)
    steps = [arr.copy()]
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            steps.append(arr.copy())

    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps
    }



if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    result = bubble_sort(numbers)
    print("Result:", result)

    print("\nRunning Selection Sort:")
    
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    result = selection_sort(numbers)
    print("Result:", result)
