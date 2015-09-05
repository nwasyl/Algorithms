__author__ = 'nickwasy'

import random
import math

best = 1000000      # initialize closest distance to something impossibly large given possible inputs
best_pair = None    # currently no best pair

# merges two sorted lists of points into a list sorted by the [index] coord
def merge_tuple(list1, list2, index):
    merged = []
    i, j = 0, 0
    for k in range(len(list1) + len(list2)):
        if i < len(list1) and j < len(list2):
            if list1[i][index] <= list2[j][index]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        elif i == len(list1):
            merged.append(list2[j])
            j += 1
        else:
            merged.append(list1[i])
            i += 1
    return merged

# sorts a list of points by the [index] coord
def merge_sort_tuple(alist, index):
    if len(alist) <= 1:
        return alist
    list1 = alist[:len(alist) // 2]
    list2 = alist[len(alist) // 2:]
    list1 = merge_sort_tuple(list1, index)
    list2 = merge_sort_tuple(list2, index)
    return merge_tuple(list1, list2, index)

# Euclidean distance between p[i] and p[j]
def d(p, i, j):
    return math.sqrt((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2)

# returns the closest pair of and the minimum distance between points where exactly one is in the left half of p
def closest_split_pair(p_x, p_y, delta):    # list sorted by first coord, by second, and smallest
    best_split_pair = None
    best_split = delta

    x_bar = p_x[len(p_x) // 2][0]           # biggest first coord in left half of p
    s_y = []                                # points whose first coord within delta of p, sorted by second coord
    for item in p_y:
        if abs(item[0] - x_bar) < delta:
            s_y.append(item)
    for i in range(len(s_y) - 1):
        for j in range(i + 1, min(7, len(s_y) - i)):    # only need to consider pairs that are sufficiently close
            if d(s_y, i, j) < best_split:
                best_split_pair = [s_y[i], s_y[j]]
                best_split = d(s_y, i, j)
    return (best_split_pair, best_split)


def closest_pair(p):
    global best
    global best_pair

    if len(p) == 2:                 # if there are two points, return the list and the distance
        return (p, d(p, 0, 1))
    elif len(p) == 3:               # just do brute force if there are three
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                distance = d(p, i, j)
                if distance < best:
                    best = distance
                    best_pair = [p[i], p[j]]
        return (best_pair, best)
    else:
        p_x = (merge_sort_tuple(p, 0))      # list sorted by first coord
        p_y = (merge_sort_tuple(p, 1))      # list sorted by second coord
        q = [p_x[i] for i in range(len(p) // 2)]            # the points in the left half of p_x
        r = [p_x[i] for i in range(len(p) // 2, len(p))]    # the points in the right half of p_x

        (point_q, distance_q) = closest_pair(q)
        (point_r, distance_r) = closest_pair(r)
        if distance_q < distance_r:
            best_pair = point_q
        else:
            best_pair = point_r
        delta = min(distance_q, distance_r)     # minimum distance of pairs either both in q or both in r
        best_split_pair, best_split = closest_split_pair(p_x, p_y, delta)   # closest pair and dist where one point is
        if best_split < delta:                                              # in q and the other is in r
            best = best_split
            best_pair = best_split_pair
        return (best_pair, best)

# computes the closest pair and their distance by comparing every pair
def brute_force_closest_pair(p):
    closest = d(p, 0, 1)
    closest_pair = None
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            distance = d(p, i, j)
            if distance < closest:
                closest = distance
                closest_pair = [p[i], p[j]]
    return (closest_pair, closest)

# tests closest_pair against the brute force method
def test():
    alist = [(random.randrange(0, 10000), random.randrange(0, 10000)) for _ in range(100)]
    print(brute_force_closest_pair(alist))
    print(closest_pair(alist))
    assert closest_pair(alist)[1] == brute_force_closest_pair(alist)[1]     # only check distance--order may be flipped
