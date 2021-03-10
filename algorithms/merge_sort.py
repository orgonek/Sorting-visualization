def merge_sort(list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(list, start, mid)
        yield from merge_sort(list, mid , end)
        yield from merge(list, start, mid, end)

def merge(list, start, mid, end):
    result = []
    left = list[start:mid]
    right = list[mid:end]

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1

    for index, value in enumerate(result):
        list[start + index] = value
        yield list
