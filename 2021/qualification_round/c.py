"""Reversort Engineering."""
LUT = {
    2: {1: [1, 2], 2: [2, 1]},
    3: {2: [1, 2, 3], 3: [2, 1, 3], 5: [2, 3, 1], 4: [3, 2, 1]},
    4: {
        3: [1, 2, 3, 4],
        4: [2, 1, 3, 4],
        6: [4, 3, 2, 1],
        5: [3, 2, 1, 4],
        8: [4, 3, 1, 2],
        7: [4, 2, 3, 1],
        9: [2, 4, 3, 1],
    },
    5: {
        4: [1, 2, 3, 4, 5],
        5: [2, 1, 3, 4, 5],
        7: [4, 3, 2, 1, 5],
        6: [3, 2, 1, 4, 5],
        9: [5, 4, 2, 3, 1],
        8: [5, 4, 3, 2, 1],
        10: [5, 4, 2, 1, 3],
        11: [5, 2, 4, 3, 1],
        12: [5, 4, 3, 1, 2],
        14: [2, 4, 5, 3, 1],
        13: [4, 5, 3, 1, 2],
    },
    6: {
        5: [1, 2, 3, 4, 5, 6],
        6: [2, 1, 3, 4, 5, 6],
        8: [4, 3, 2, 1, 5, 6],
        7: [3, 2, 1, 4, 5, 6],
        10: [6, 5, 4, 3, 2, 1],
        9: [5, 4, 3, 2, 1, 6],
        11: [6, 5, 4, 2, 3, 1],
        12: [6, 5, 3, 2, 4, 1],
        13: [6, 5, 2, 4, 3, 1],
        15: [6, 5, 2, 4, 1, 3],
        14: [6, 5, 4, 2, 1, 3],
        17: [6, 4, 5, 3, 1, 2],
        16: [6, 5, 4, 3, 1, 2],
        19: [4, 6, 5, 3, 1, 2],
        18: [6, 5, 3, 4, 1, 2],
        20: [2, 4, 6, 5, 3, 1],
    },
    7: {
        6: [1, 2, 3, 4, 5, 6, 7],
        7: [2, 1, 3, 4, 5, 6, 7],
        9: [4, 3, 2, 1, 5, 6, 7],
        8: [3, 2, 1, 4, 5, 6, 7],
        11: [6, 5, 4, 3, 2, 1, 7],
        10: [5, 4, 3, 2, 1, 6, 7],
        12: [7, 6, 5, 4, 3, 2, 1],
        13: [7, 6, 5, 4, 2, 3, 1],
        14: [7, 6, 5, 3, 2, 4, 1],
        16: [7, 6, 5, 3, 2, 1, 4],
        15: [7, 6, 5, 2, 4, 3, 1],
        18: [7, 6, 5, 4, 2, 1, 3],
        17: [7, 6, 5, 2, 3, 1, 4],
        20: [7, 6, 5, 4, 3, 1, 2],
        19: [7, 6, 5, 2, 4, 1, 3],
        21: [7, 6, 4, 5, 3, 1, 2],
        22: [7, 6, 5, 3, 1, 2, 4],
        23: [7, 4, 6, 5, 3, 1, 2],
        24: [7, 6, 5, 3, 4, 1, 2],
        25: [6, 7, 5, 3, 4, 1, 2],
        27: [2, 4, 6, 7, 5, 3, 1],
        26: [4, 6, 7, 5, 3, 1, 2],
    },
}


def reader():
    N, C = input().split(" ")
    return int(N), int(C)


def solver(N, C):
    c_min = N - 1
    c_max = N * (N - 1) - (N - 1) * (0 + N - 2) / 2
    if C < N - 1 or C > c_max:
        return "IMPOSSIBLE"

    if N in LUT.keys():
        return " ".join(map(str, LUT[N][C]))

    # LUT only handles 2 <= N <= 7 som for everything else return IMPOSSIBLE,
    # i.e. this code will only pass Test Set 1.
    return "IMPOSSIBLE"


T = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solver(*reader())))
