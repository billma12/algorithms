def binary_search(sorted_list, val):
    l, r = 0, len(sorted_list)
    mid = (l + r) // 2

    if len(sorted_list) is 1 and sorted_list[0] is not val:
        return False
    if sorted_list[mid] is val:
        return True
    elif sorted_list[mid] > val:
        return binary_search(sorted_list[:mid], val)
    elif sorted_list[mid] < val:
        return binary_search(sorted_list[mid:], val)

l = [1, 2]
val = 1

print(binary_search(l, val))
