def merge_and_count_split_inv(B, C):
    i = 0
    j = 0
    res = []
    inv_count = 0
    b_remaining = len(B)
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            res.append(B[i])
            i += 1
            b_remaining -= 1
        else:
            if C[j] < B[i]:
                inv_count += b_remaining
            res.append(C[j])
            j += 1

    while i < len(B):
        res.append(B[i])
        i += 1

    while j < len(C):
        res.append(C[j])
        j += 1

    return res, inv_count


def merge_and_count_inv(A):
    if len(A) <= 1:
        return A, 0
    m = len(A) // 2
    B, x = merge_and_count_inv(A[:m])
    C, y = merge_and_count_inv(A[m:])
    D, z = merge_and_count_split_inv(B, C)
    return D, x + y + z


def count_inversions(A):
    _, count = merge_and_count_inv(A)
    return count


print(count_inversions([1, 3, 5, 2, 4, 7, 6]))
