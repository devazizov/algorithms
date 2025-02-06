def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return index if found
        elif arr[mid] < target:
            left = mid + 1  # Search in right half
        else:
            right = mid - 1  # Search in left half
            
    return -1  # Return -1 if not found

arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
print("Element found at index:", result)
