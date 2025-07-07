
# basic algorithms for testing purposes
def linear_search(arr, target):
    """
    Perform a linear search for the target in the array.
    
    :param arr: List of elements to search in.
    :param target: Element to search for.
    :return: Index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def binary_search(arr, target):
    """
    Perform a binary search for the target in the sorted array.
    
    :param arr: Sorted list of elements to search in.
    :param target: Element to search for.
    :return: Index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(arr):
    """
    Perform bubble sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    """
    Perform selection sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    """
    Perform insertion sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    """
    Perform quick sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Perform merge sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays.
    
    :param left: Left sorted array.
    :param right: Right sorted array.
    :return: Merged sorted array.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def heapify(arr, n, i):
    """
    Helper function to maintain the heap property.
    
    :param arr: List of elements to heapify.
    :param n: Size of the heap.
    :param i: Index of the element to heapify.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heap_sort(arr):
    """
    Perform heap sort on the array.
    
    :param arr: List of elements to sort.
    :return: Sorted list of elements.
    """
    n = len(arr)
    
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
    return arr

def counting_sort(arr, max_val):
    """
    Perform counting sort on the array.
    
    :param arr: List of elements to sort.
    :param max_val: Maximum value in the array.
    :return: Sorted list of elements.
    """
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
        
    # Update count[i] to contain the actual position of this element in output[]
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        
    return output

# main function to test the algorithms
if __name__ == "__main__":
    # Example usage of the algorithms
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Heap Sort:", heap_sort(arr.copy()))
    
    target = 22
    print("Linear Search for", target, ":", linear_search(arr, target))
    
    sorted_arr = sorted(arr)
    print("Binary Search for", target, "in sorted array:", binary_search(sorted_arr, target))
    
    max_val = max(arr)
    print("Counting Sort:", counting_sort(arr.copy(), max_val))