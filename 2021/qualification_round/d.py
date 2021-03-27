"""Median Sort."""


def solver(N, Q):
    if Q <= 0:
        return Q
    print("1 2 3", flush=True)
    Q -= 1
    judge = int(input())
    if judge == 1:
        solution = [2, 1, 3]
    elif judge == 2:
        solution = [1, 2, 3]
    else:
        solution = [1, 3, 2]

    for n in range(4, N + 1):
        high_prev = None
        low_prev = None
        low = 0
        high = len(solution) - 1
        while low < high:
            mid = (high + 1 + low) // 2
            test = [solution[low], solution[mid], n]
            print(" ".join(map(str, test)), flush=True)
            Q -= 1
            judge = int(input())
            if judge == -1:
                return Q
            if judge == solution[low]:
                solution.insert(low, n)
                break
            if judge == solution[mid]:
                low = mid
            elif judge == n:
                high = mid

            if low_prev == low and high_prev == high:
                solution.insert(high, n)
                break

            if low == high:
                solution.insert(low + 1, n)
                break

            low_prev = low
            high_prev = high

    print(" ".join(map(str, solution)), flush=True)
    judge = int(input())
    return Q


T, N, Q = map(int, input().split(" "))
for t in range(1, T + 1):
    Q = solver(N, Q)
