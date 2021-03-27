"""Reversort."""


def reader():
    N = int(input())
    L = [int(l) for l in input().split(" ")]
    return N, L


def solver(N, L):
    C = 0
    for i in range(N - 1):
        j = L.index(min(L[i:]))
        L[i : j + 1] = L[i : j + 1][::-1]
        C += j - i + 1
    return C


T = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solver(*reader())))
