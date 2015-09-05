__author__ = 'nickwasy'

import random

total = 0    # number of inversions

# merges two lists and counts the number of inversions
def merge_and_count(list1, list2):
    merged = []
    global total    # is this dangerous?
    i, j = 0, 0
    for k in range(len(list1) + len(list2)):
        if i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
                total += len(list1) - i
        elif i == len(list1):
            merged.append(list2[j])
            j += 1
        else:
            merged.append(list1[i])
            i += 1
    return merged


def mergesort(alist):
    if len(alist) <= 1:
        return alist
    list1 = alist[:len(alist) // 2]
    list2 = alist[len(alist) // 2:]
    list1 = mergesort(list1)
    list2 = mergesort(list2)
    return merge_and_count(list1, list2)

# tests with a randomly-generated 10000-element list
def test():
    alist = [random.randrange(0, 10000) for _ in range(10000)]
    assert mergesort(alist) == sorted(alist)
    
