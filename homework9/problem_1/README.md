# Problem 1

## Definition of the Key Elements

### State

设 $S_t$ 表示在 period $t$ 的开始，inventory 为 $S_t$ units。

### Decision

设 $x_t$ 表示在 period $t$，生产的 inventory 为 $x_t$ units。约束条件是 $0 \le x_t \le 4$。

### Exogenous Information

$W_t$ 表示 pertiod $t$ 的 demand，其分布为：

$$
P(W_t = 1) = P(W_t = 2) = \frac{1}{2}
$$

由此，对 $x_t$ 有约束条件：$S_t + x_t - W_t \le 3$ 恒成立，此即 $S_t + x_t - 1 \le 3$。

### Transition Function

$$
S_{t + 1} = \max\{S_t + x_t - W_t, 0\}
$$

### One-period Cost Function

设 $t = 1, 2, \cdots, T - 1$，则

$$
\hat{C}_t(S_t, x_t, W_t) = c(x_t) + \begin{cases}
    S_t + x_t - W_t, & S_t + x_t \ge W_t, \\
    3(W_t - S_t - x_t), & S_t + x_t < W_t.
\end{cases}
$$

若 $t = T$，则

$$
\hat{C}_t(S_t, x_t, W_t) = c(x_t) + \begin{cases}
    W_t -S_t - x_t, & S_t + x_t \ge W_t, \\
    3(W_t - S_t - x_t), & S_t + x_t < W_t.
\end{cases}
$$

记 $C_t(S_t, x_t) = \mathbb{E}[\hat{C}_t(S_t, x_t, W_t)]$。

### Objective Function

Value Function 为

$$
V_t(S_t) = \min_{0 \le x_t \le 4 - S_t}\{C_t(S_t, x_t) + \mathbb{E}[V_{t + 1}(S_{t + 1})]\},
$$

边界条件为 $V_T(S_T) = \min_{0 \le x_T \le 4 - S_T}\{C_T(S_T, x_T)\}$。Objective Function 即为 $V_1(1)$。

## Solution

经计算，得到 $V_t(S_t)$ 的值如下：

| $V_t(S_t)$ | $S_t = 0$ | $S_t = 1$ | $S_t = 2$ | $S_t = 3$ |
| :--------: | :-------: | :-------: | :-------: | :-------: |
|  $t = 3$   |   $4.5$   |   $1.5$   |  $-0.5$   |  $-1.5$   |
|  $t = 2$   |   $9.0$   |   $6.0$   |   $3.5$   |   $2.0$   |
|  $t = 1$   |           |  $10.5$   |           |           |

$x_t^*(S_t)$ 的值如下：

| $x_t^*(S_t)$ | $S_t = 0$ | $S_t = 1$ | $S_t = 2$ | $S_t = 3$ |
| :----------: | :-------: | :-------: | :-------: | :-------: |
|   $t = 3$    |    $0$    |    $0$    |    $0$    |    $0$    |
|   $t = 2$    |    $0$    |    $0$    |    $0$    |    $0$    |
|   $t = 1$    |           |    $0$    |           |           |

### 附录

```bash
python3 main.py
```

可以检验结果的正确性：

```bash
V_3(0) = 4.5,    x_3^*(0) = [0]
V_3(1) = 1.5,    x_3^*(1) = [0]
V_3(2) = -0.5,   x_3^*(2) = [0]
V_3(3) = -1.5,   x_3^*(3) = [0]
V_2(0) = 9.0,    x_2^*(0) = [0]
V_2(1) = 6.0,    x_2^*(1) = [0]
V_2(2) = 3.5,    x_2^*(2) = [0]
V_2(3) = 2.0,    x_2^*(3) = [0]
V_1(1) = 10.5,   x_1^*(1) = [0]
```
