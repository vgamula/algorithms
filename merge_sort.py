def merge(a, b):
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return merge(left, right)


arr = [5, 4, 7, 9, 5, 1, 2, 9, 3]

print(merge_sort(arr))
