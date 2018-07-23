def quick_sort_with_comparisons(arr, sub=False):
    if len(arr) <= 1:
        return arr, 1
    # total += len(arr) - 1
    pivot = arr[-1]
    left, lx = quick_sort_with_comparisons([x for x in arr if x < pivot], True)
    right, tx = quick_sort_with_comparisons([x for x in arr if x > pivot], True)
    if sub:
        r = lx + tx + len(arr) - 1
    else:
        r = lx + tx
    return (left + [pivot] + right), r


def quick_sort(arr):
    return quick_sort_with_comparisons(arr)[0]


def comparisons(arr):
    return quick_sort_with_comparisons(arr)[1]


if __name__ == '__main__':
    arr = [5, 4, 7, 8, 9, 1, 3, 6, 2]

    print(quick_sort(arr))
    print(comparisons(arr))
    # print(total)


# 154575
# 162330
