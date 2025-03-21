# Merge implementation for calculating inversions in an array

def count_inversions(arr):
    temp_arr = arr.copy()
    inversions = _merge_sort_and_count(temp_arr, 0, len(temp_arr) - 1)
    return inversions, temp_arr

def _merge_sort_and_count(arr, start, end):
    # Base case: subarray has 0 or 1 elements
    if start >= end:
        return 0
    
    # Divide the array and count inversions in each half
    mid = (start + end) // 2
    inversions = 0
    
    # Count inversions in left and right halves
    inversions += _merge_sort_and_count(arr, start, mid)
    inversions += _merge_sort_and_count(arr, mid + 1, end)
    
    # Count inversions while merging the two halves
    inversions += _merge_and_count(arr, start, mid, end)
    
    return inversions

def _merge_and_count(arr, start, mid, end):
    
    # Create temporary arrays for the two halves
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    
    i = j = 0  
    k = start  
    inversions = 0
    
    # Compare and merge while counting inversions
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            # When right[j] is smaller than left[i], it forms inversions with all remaining elements in the left array
            arr[k] = right[j]
            j += 1
            inversions += len(left) - i
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return inversions

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        user_array = list(map(int, user_input.strip().split()))
        
        # Count inversions and get sorted array
        inversion_count, sorted_array = count_inversions(user_array)
        
        # Print results
        print(f"\nOriginal array: {user_array}")
        print(f"Number of inversions: {inversion_count}")
        print(f"Sorted array: {sorted_array}")
        
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")

    # Test cases
    """
    test_arrays = [
        [1, 20, 6, 4, 5],  # Some inversions
        [1, 2, 3, 4, 5],   # Sorted (0 inversions)
        [5, 4, 3, 2, 1],   # Completely reversed (maximum inversions)
        [2, 4, 1, 3, 5]    # A few inversions
    ]
    
    for arr in test_arrays:
        inversion_count, sorted_arr = count_inversions(arr)
        print(f"Array: {arr}")
        print(f"Number of inversions: {inversion_count}")
        print(f"Sorted array: {sorted_arr}")
        print()
    """
    
# Lotus Kshetri