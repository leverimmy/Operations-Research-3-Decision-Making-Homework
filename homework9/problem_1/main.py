T = 3


def c(x):
    return 0 if x == 0 else 3 + 2 * x


def C_hat(t, S, x, W):
    if t == T:
        if S + x >= W:
            return c(x) + W - S - x
        else:
            return c(x) + 3 * (W - S - x)
    else:
        if S + x >= W:
            return c(x) + S + x - W
        else:
            return c(x) + 3 * (W - S - x)


def C(t, S, x):
    return 0.5 * C_hat(t, S, x, 1) + 0.5 * C_hat(t, S, x, 2)


VV = [{}, {}, {}, {}]


def TF(S, x):
    return max(S + x - 1, 0)


# 返回 (V(S_t), [x_t*(S_t)])
def V(t, S):
    if VV[t].get(S) is not None:
        return VV[t][S]
    V_star = -1
    x_t_star = []
    if t == T:
        for x_t in range(0, 5 - S):
            if len(x_t_star) == 0 or C(t, S, x_t) < V_star:
                x_t_star = [x_t]
                V_star = C(t, S, x_t)
            elif C(t, S, x_t) == V_star:
                x_t_star.append(x_t)
    else:
        for x_t in range(0, 5 - S):
            V_next = 0.5 * V(t + 1, max(S + x_t - 1, 0))[0] + 0.5 * V(t + 1, max(S + x_t - 2, 0))[0]
            if len(x_t_star) == 0 or C(t, S, x_t) + V_next < V_star:
                x_t_star = [x_t]
                V_star = C(t, S, x_t) + V_next
            elif C(t, S, x_t) + V_next == V_star:
                x_t_star.append(x_t)
    print(f"V_{t}({S}) = {V_star}, \t x_{t}^*({S}) = {x_t_star}")
    VV[t][S] = (V_star, x_t_star)
    return V_star, x_t_star


if __name__ == "__main__":
    _, _ = V(1, 1)
