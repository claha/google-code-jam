"""Roaring Years."""


def reader():
    return int(input())


def check_n(Y, n):
    if len(Y) == n:
        return True
    A = Y[-n:]
    Y = Y[:-n]
    if A[0] == "0":
        return False
    A = int(A)
    if len(str(A - 1)) != n:
        n -= 1
    if len(Y) < n:
        return False
    B = int(Y[-n:])
    if B == A - 1:
        return check_n(Y, n)
    return False


def check(Y):
    Y = str(Y)
    N = len(Y)
    for n in range(int((N + 1) / 2), 0, -1):
        if check_n(Y, n):
            return True
    return False


def solver(Y):
    Y += 1
    if Y < 10:
        Y = 12
    while True:
        if check(Y):
            return Y
        Y += 1


T = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solver(reader())))
