def selection_sort(list):
    length = len(list)

    for i in range(length - 1):
        min = i
        
        for j in range(i+1, length):
            if list[j] < list[min]:
                min = j
            yield 
        
        if min != i: 
            list[min], list[i] = list[i], list[min]
            yield list
