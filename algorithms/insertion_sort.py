def insertion_sort(list):
    for i in range(1, len(list)):
        current_item = list[i]
        position = i

        while(list[position - 1] > current_item and position > 0):
            list[position] = list[position - 1]
            position -= 1

        list[position] = current_item

        yield list