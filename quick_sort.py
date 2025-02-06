from random import randrange

def quick_sort(arr):
    """Sort the array using the quicksort algorithm."""
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(randrange(len(arr)))  # Select a random pivot
        smaller = [i for i in arr if i <= pivot]  # Elements smaller or equal to pivot
        larger = [i for i in arr if i > pivot]  # Elements greater than pivot
        return quick_sort(smaller) + [pivot] + quick_sort(larger)

if __name__ == '__main__':
    array1 = [1, 5, 12, 0, -5, 66]
    print("Original array:", array1)
    print("Sorted array:", quick_sort(array1))
    
    array2 = list(range(20))
    print("Original array:", array2)
    print("Sorted array:", quick_sort(array2))
