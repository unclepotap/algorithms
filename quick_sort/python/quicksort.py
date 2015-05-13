def quicksort(data):
    if len(data) <= 1:
        return data

    op_elem = data[0]
    less, pivot, more = [], [], []
    for el in data:
        if el > op_elem:
            more.append(el)
        elif el < op_elem:
            less.append(el)
        else:
            pivot.append(el)
    data = quicksort(less) + pivot + quicksort(more)
    return data

def partition(data, pivot_index, first_index, last_index):
    pivot_value = data[pivot_index]
    left_index = first_index
    right_index = last_index

    print pivot_value

    while True:
        while left_index <= right_index and data[left_index] < pivot_value:
            left_index += 1

        while left_index <= right_index and data[right_index] > pivot_value:
            right_index -= 1

        if right_index <= left_index:
            break

        data[left_index], data[right_index] = data[right_index], data[left_index]

    return data


if __name__ == '__main__':
    data = [1, 5, 3, 7, 2, 9, 6]
    print quicksort(data)
    print partition(data, 1, 0, len(data) - 1)
