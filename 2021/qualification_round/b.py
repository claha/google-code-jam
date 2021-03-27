"""Moons and Umbrellas."""


def reader():
    X, Y, S = input().split(" ")
    return int(X), int(Y), S


def solver(X, Y, S):
    S = list(S)
    for i, s in enumerate(S):
        if i == 0:
            if s == "?":
                j = i + 1
                while j < len(S) and S[j] == "?":
                    j += 1
                if j == len(S):
                    S[i] = "C"
                else:
                    S[i] = S[j]
        elif i == len(S) - 1:
            if s == "?":
                j = i - 1
                while j >= 0 and S[j] == "?":
                    j -= 1
                if j == -1:
                    S[i] = "C"
                else:
                    S[i] = S[j]
        else:
            if S[i] == "?":
                if S[i + 1] == "?":
                    S[i] = S[i - 1]
                elif S[i - 1] == S[i + 1]:
                    S[i] = S[i - 1]
                else:
                    if S[i - 1] == "C":
                        if X <= Y:
                            S[i] = "J"
                        else:
                            S[i] = "C"
                    else:
                        if Y <= X:
                            S[i] = "C"
                        else:
                            S[i] = "J"
    S = "".join(S)
    return S.count("CJ") * X + S.count("JC") * Y


T = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solver(*reader())))
