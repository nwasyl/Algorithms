__author__ = 'nickwasy'

import random

# partitions the list so that left of the pivot are all the points smaller than it
# and right of the pivot are all the points greater than it
def partition(list1, p):
    list1[0], list1[p[1]] = list1[p[1]], list1[0]   # switches the pivot point to the beginning for ease
    i = 0                                           # i = divide between greater than p and less than p
    for j in range(i + 1, len(list1)):              # j = divide between partitioned and unpartitioned
        if list1[j] < list1[0]:
            list1[i + 1], list1[j] = list1[j], list1[i + 1]
            i += 1
    list1[i], list1[0] = list1[0], list1[i]         # put pivot in its place
    return (list1, i)  # have to return the index too because there may be repeats


# randomly chooses a pivot and returns the number and its index
def choose_pivot(list1):
    index = random.randrange(len(list1))
    p = list1[index]
    return (p, index)


# conducts quick sort on list1
def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        p = choose_pivot(list1)  # (pivot number, index)
        list1 = partition(list1, p)
        alist = list1[0]
        index = list1[1]
        left_half = [alist[i] for i in range(index)]
        right_half = [alist[i] for i in range(index + 1, len(alist))]
        list1 = quick_sort(left_half) + [p[0]] + quick_sort(right_half)
        return list1


# tests quick_sort for a randomly-generated 10000-element list
def test():
    alist = [random.randrange(0, 10000) for _ in range(10000)]
    assert quick_sort(alist) == sorted(alist)
