def genArray(size):
    arr = [0 for x in range(size)]
    return arr


def genMatrix(w, h):
    mat = [[0 for x in range(w)] for y in range(h)]
    return mat


if __name__ == '__main__':
    size = 6

    a = input("Input a:")
    a = int(a)
    b = input("Input b:")
    b = int(b)

    alpha = 0
    beta = 1
    i = 0

    k = genArray(size)

    formatA = genArray(size)
    formatB = genArray(size)

    formatST = genMatrix(2, size)

    formatA[0] = a
    formatB[0] = b

    while a > 0:
        k[i] = b // a
        i += 1
        rest = b % a
        b = a
        a = rest
        formatA[i] = a
        formatB[i] = b

    formatST[i][0] = alpha
    formatST[i][1] = beta
    for j in range(0, i):
        newA = alpha
        alpha = beta - k[i - j - 1] * alpha
        beta = newA
        formatST[i - j - 1][0] = alpha
        formatST[i - j - 1][1] = beta

    print("a b k alpha beta")

    for j in range(0, i + 1):
        print("%d  %d  %d  %d  %d" % (formatA[j], formatB[j], k[j], formatST[j][0], formatST[j][1]))
