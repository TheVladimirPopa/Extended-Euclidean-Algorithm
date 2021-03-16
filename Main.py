def generate_array(length):
    arr = [0 for x in range(length)]
    return arr


def generate_matrix(w, h):
    mat = [[0 for x in range(w)] for y in range(h)]
    return mat


def print_stuff(collection, s):
    for t in range(0, s + 1):
        print("%d " % collection[t], end='')


if __name__ == '__main__':
    size = 6  # chosen at random

    a = input("Input a:")
    a = int(a)
    b = input("Input b:")
    b = int(b)
    print()

    if a > b:
        c = a
        a = b
        b = c
        print("(Note: a and b have been swapped because a < b)")
        print()

    alpha = 0
    beta = 1
    i = 0

    k = generate_array(size)

    formatA = generate_array(size)
    formatB = generate_array(size)

    formatST = generate_matrix(2, size)

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

    print("As table:")
    print("a\tb\tk\talpha\tbeta")

    for j in range(0, i + 1):
        print("%d  %d  %d  %d  %d" % (formatA[j], formatB[j], k[j], formatST[j][0], formatST[j][1]))

    print()

    print("Greatest common divisor(%d,%d) = %d * %d + %d * %d = %d" % (formatA[0], formatB[0],
                                                                       formatA[0], formatST[0][0], formatB[0],
                                                                       formatST[0][1],
                                                                       formatA[0] * formatST[0][0] + formatB[0] *
                                                                       formatST[0][1]))

    print()
    print("As lists:")
    print("a: ", end='')
    print_stuff(formatA, i)

    print()
    print("b: ", end='')
    print_stuff(formatB, i)

    print()
    print("k: ", end='')
    print_stuff(k, i)

    print()
    print("alpha: ", end='')
    for j in range(0, i + 1):
        print("%d " % formatST[j][0], end='')

    print()
    print("beta: ", end='')
    for j in range(0, i + 1):
        print("%d " % formatST[j][1], end='')
    print()
