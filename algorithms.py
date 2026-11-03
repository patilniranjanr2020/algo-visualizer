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


def insertion_sort(arr):
    steps = [arr.copy()]
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                steps.append(arr.copy())
                j -= 1
            else:
                break
        arr[j + 1] = key

    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps
    }

def merge_sort(arr):
    steps = [arr.copy()]
    comparisons = [0]  # Using list to mutate inside recursive helper
    swaps = [0]        # Representing merge overwrites/steps as swaps for metrics

    def merge_in_place(start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = j = 0
        k = start
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            swaps[0] += 1
            steps.append(arr.copy())
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            swaps[0] += 1
            steps.append(arr.copy())
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            swaps[0] += 1
            steps.append(arr.copy())
            k += 1

    def divide(start, end):
        if start < end:
            mid = (start + end) // 2
            divide(start, mid)
            divide(mid + 1, end)
            merge_in_place(start, mid, end)

    divide(0, len(arr) - 1)
    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons[0],
        "swaps": swaps[0]
    }


def quick_sort(arr):
    steps = [arr.copy()]
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
                steps.append(arr.copy())
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        steps.append(arr.copy())
        return i + 1

    def qsort(low, high):
        if low < high:
            pi = partition(low, high)
            qsort(low, pi - 1)
            qsort(pi + 1, high)

    qsort(0, len(arr) - 1)
    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps
    }


def binary_search(arr, target):
    sorted_arr = sorted(arr)
    steps = [sorted_arr.copy()]
    comparisons = 0
    
    low = 0
    high = len(sorted_arr) - 1
    found_index = -1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        # Append state or array representation cleanly
        steps.append({
            "step_type": "inspect",
            "low": low,
            "high": high,
            "mid": mid,
            "value_at_mid": sorted_arr[mid]
        })
        
        if sorted_arr[mid] == target:
            found_index = mid
            break
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return {
        "sorted_array": sorted_arr,
        "target": target,
        "index": found_index,
        "steps": steps,
        "comparisons": comparisons
    }





if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Running Bubble Sort:")
    result = bubble_sort(numbers.copy())
    print("Result:", result)

    
    
    print("\nRunning Selection Sort:")
    result = selection_sort(numbers.copy())
    print("Result:", result)



    print("\nRunning Insertion Sort:")
    result = insertion_sort(numbers.copy())
    print("Result:", result)



    print("\nRunning Merge Sort:")
    result = merge_sort(numbers.copy())
    print("Result:", result)



    print("\nRunning Quick Sort:")
    result = quick_sort(numbers.copy())
    print("Result:", result)



    print("\nRunning Binary Search for 25:")
    result = binary_search(numbers.copy(), 25)
    print("Result:", result)

    

    
    
