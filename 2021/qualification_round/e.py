"""Cheating Detection."""


def reader():
    Q = []
    for _ in range(100):
        Q.append(input())
    return Q


def solver(Q):
    # Since P is low (10%) on Test Set 1, and the cheater cheats on 50% of the
    # questsions the cheater is likely the player with the highest score.
    p_max = 0
    i_max = None
    for i, q in enumerate(Q):
        p = q.count("1") / len(q)
        if p > p_max:
            p_max = p
            i_max = i + 1
    return i_max


T = int(input())
P = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solver(reader())))
