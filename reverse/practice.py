def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if item_list[mid] == item :
            return True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False