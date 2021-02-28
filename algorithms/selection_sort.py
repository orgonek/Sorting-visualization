def selection_sort(arr):
    length = len(arr)

    for i in range(length - 1):
        min = i
        
        for j in range(i+1, length):
            if arr[j] < arr[min]:
                min = j
        
        if min != i: 
            arr[min], arr[i] = arr[i], arr[min]

        yield arr

