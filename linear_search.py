def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
print("Element found at index:", result)
