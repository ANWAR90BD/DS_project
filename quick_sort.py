# implementation of quick_sort
def partition(L, low, high):
    pivot = L[high]
    i = low -1
    for j in range(low, high):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]

    L[i+1], L[high] = L[high], L[i+1]
    return i+1

def quick_sort(L, low, high):
    if low >= high:
        return
    pivot_index = partition(L, low, high)
    quick_sort(L, low, pivot_index - 1)
    quick_sort(L, pivot_index + 1, high)


if __name__ == "__main__":
    number = [1, 5, 6, 3, 8]
    print("unsorted list:", number)
    quick_sort(number, 0, len(number)-1)
    print("sorted list:", number)
