def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z += y
        y = y << 1
        x = x >> 1
    return z


if __name__ == '__main__':
    assert russian(2, 2) == 4
    assert russian(13, 13) == 169
