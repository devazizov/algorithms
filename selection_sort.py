def find_max_index(arr):
    """Return the index of the maximum element in the array."""
    max_value = arr[0]  # Initial maximum value
    max_index = 0  # Index of the maximum value
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    return max_index

def selection_sort_desc(arr):
    """Sort the array in descending order using selection sort."""
    sorted_arr = []
    temp_arr = arr.copy()  # Copy to avoid modifying the original array
    for _ in range(len(arr)):
        max_index = find_max_index(temp_arr)
        sorted_arr.append(temp_arr.pop(max_index))  # Remove and append the largest element
    return sorted_arr

if __name__ == '__main__':
    array = [3, 4, 1, 6, 10, 20, 9, 8]
    sorted_array = selection_sort_desc(array)
    print(sorted_array)
