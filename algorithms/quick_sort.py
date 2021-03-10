
def quick_sort(list, start, end):
    if start >= end:
        return
    
    pivot = list[end]
    index = start

    for i in range(start, end):
        if list[i] < pivot:
            list[i], list[index] = list[index], list[i]
            index += 1
        yield list
    
    list[index], list[end] = list[end], list[index]
    yield list

    yield from quick_sort(list, start, index - 1)
    yield from quick_sort(list, index + 1, end)
