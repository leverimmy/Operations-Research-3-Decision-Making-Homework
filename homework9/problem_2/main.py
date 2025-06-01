T = 3

l = [
    [(-1, -1), (1, 4), (2, 5), (3, 4)],
    [(-1, -1), (2, 6), (4, 6), (5, 5)],
    [(-1, -1), (3, 7), (5, 6), (6, 7)],
    [(-1, -1), (4, 8), (6, 6), (7, 7)],
]

A = [[-1 for _ in range(6)] for _ in range(T + 1)]


def r(t, x):
    return 0.7 * l[x][t][0] + 0.3 * l[x][t][1]


def S(t, s, x):
    if t == T:
        return r(t, x)
    else:
        return r(t, x) + S(t + 1, s - x, A[t + 1][s - x])


if __name__ == "__main__":
    for i in range(T, 0, -1):
        for j in range(6):
            for k in range(min(j, 3) + 1):
                if A[i][j] == -1 or S(i, j, k) > S(i, j, A[i][j]):
                    A[i][j] = k
            print(f"V_{i}({j}) = {S(i, j, A[i][j]):.1f}, \t x_{i}^*({j}) = {A[i][j]}")
        print()
