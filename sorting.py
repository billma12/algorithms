from heapq import merge
import random


def bubble(lst):
    """standard bubble"""
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble2(lst):
    """short bubble"""
    exchanges = True
    for i in range(len(lst) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            exchanges = True
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not exchanges:
            break
    return lst


def selection(lst):
    for i in range(len(lst), 1, -1):
        max_index = 0
        for j in range(1, i):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i - 1], lst[max_index] = lst[max_index], lst[i - 1]

    return lst


def insertion(lst):
    for i in range(1, len(lst)):
        cur = lst[i]
        pos = i

        while pos > 0 and lst[pos - 1] > cur:
            lst[pos] = lst[pos - 1]
            pos = pos - 1
        lst[pos] = cur

    return lst


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            alist = gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2
    return alist


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue
    return alist


def merge1(alist):
    #print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge1(lefthalf)
        merge1(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    #print("Merging ", alist)


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(array1, array2):
    merged_array = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged_array.append(array1[pointer1])
            pointer1 += 1
        else:
            merged_array.append(array2[pointer2])
            pointer2 += 1
    while pointer1 < len(array1):
        merged_array.append(array1[pointer1])
        pointer1 += 1

    while pointer2 < len(array2):
        merged_array.append(array2[pointer2])
        pointer2 += 1

    return merged_array


def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
        return merge(mergeSort(left), mergeSort(right))


def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

# main func
if __name__ == '__main__':
    pass
