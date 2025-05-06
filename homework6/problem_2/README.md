# Problem 2

## 配置环境

首先，新建虚拟环境：

```bash
python3 -m venv .venv
```

然后，激活虚拟环境。在 Windows 下，使用如下命令：

```bash
.venv\Scripts\activate
```

在 Linux 或者 macOS 下，使用如下命令：

```bash
source .venv/bin/activate
```

进入虚拟环境后，安装依赖：

```bash
pip install -r requirements.txt
```
## 问题回答

### (1)

将 Problem 1 中的描述具体化为如下 DEP 方程（$m = 3, n = 4$）：

$$
\begin{align*}
\min \quad & c_1x_1 + c_2x_2 + c_3x_3 + c_4x_4 + \sum_{\omega \in \Omega}p_{\omega}\left(\sum_{i = 1}^{3}\sum_{j = 1}^{4}g_{ij}y_{ij}(\omega) + \sum_{i = 1}^{3}l_i s_i(\omega)\right) \\
\text{s.t.} \quad & -x_1 + z_1 \le h_1, \\
& -x_2 + z_2 \le h_2, \\
& -x_3 + z_3 \le h_3, \\
& -x_4 + z_4 \le h_4, \\
& t_1z_1 + t_2z_2 + t_3z_3 + t_4z_4 \le T, \\
& z_1 \le u_1, \\
& z_2 \le u_2, \\
& z_3 \le u_3, \\
& z_4 \le u_4, \\
& \sum_{j = 1}^{4}a_{ij}y_{ij}(\omega) + s_i(\omega) \ge d_i(\omega), \forall i \in \{1, 2, 3\}, \\
& \sum_{i = 1}^{3}y_{ij} - z_j \le 0, \forall j \in \{1, 2, 3, 4\}, \\
& x_j, z_j, y_{ij}(\omega), s_i(\omega) \ge 0, \forall i \in \{1, 2, 3\}, \forall j \in \{1, 2, 3, 4\}.
\end{align*}
$$

在以上表示中，对于 $y_{ij}$ 和 $s_i$ 而言，它们可以看作是以 scenario $\omega$ 作为自变量的函数。

为了方便区分，这里不使用 Problem 1 中的 $\omega_i$，而是使用 $d_i(\omega)$ 来表示在 scenario $\omega$ 情形下的 demand。同时，将原来的 penalty $p_i$ 改名为 $l_i$（意为 **L**ost Penalty），以和 scenario $\omega$ 出现的概率 $p_\omega$ 区分。

列：

- `COL1_1`、`COL1_2`、`COL1_3`、`COL1_4` 对应 $x_1, x_2, x_3, x_4$。
- `COL1_5`、`COL1_6`、`COL1_7`、`COL1_8` 对应 $z_1, z_2, z_3, z_4$。
- `COL2_1`、`COL2_2`、`COL2_3`、`COL2_4`、`COL2_5`、`COL2_6`、`COL2_7`、`COL2_8`、`COL2_9`、`COL2_10`、`COL2_11`、`COL2_12` 对应 $y_{ij}(\omega), \quad(i \in \{1, 2, 3\}, j \in \{1, 2, 3, 4\})$。
- `COL2_13`、`COL2_14`、`COL2_15` 对应 $s_1(\omega), s_2(\omega), s_3(\omega)$。

行：

- `ROW1_1`、`ROW1_2`、`ROW1_3`、`ROW1_4` 对应 $-x_j + z_j \le h_j, \quad (j = 1, 2, 3, 4)$。
- `ROW1_5` 对应 $\sum_{j = 1}^{4} t_j z_j \le T$。
- `ROW1_6`、`ROW1_7`、`ROW1_8`、`ROW1_9` 对应 $z_j \le u_j, \quad (j = 1, 2, 3, 4)$。
- `ROW2_1`、`ROW2_2`、`ROW2_3` 对应 $\sum_{j = 1}^{4} a_{ij} y_{ij} + s_i \ge \omega_i, \quad (i = 1, 2, 3)$。
- `ROW2_4`、`ROW2_5`、`ROW2_6`、`ROW2_7` 对应 $\sum_{i = 1}^{3} y_{ij} - z_j \le 0, \quad (j = 1, 2, 3, 4)$。

### (2)

由 [cep1.sto](../assets/cep1.sto) 可知 $\Omega$ 中元素 $\omega$ 是等概率的：

$$
p_{\omega} = \frac{1}{216}, \quad \omega = (d_1, d_2, d_3) \in \Omega,
$$

其中 $d_1, d_2, d_3 \in \{0, 600, 1200, 1800, 2400, 3000\}$。

### (3)

运行

```bash
python3 main.py --task=3
```

输出为

```bash
x_1: 0.0
x_2: 0.0
x_3: 1166.6666666666667
x_4: 2500.0
z_1: 0.0
z_2: 500.0
z_3: 1666.6666666666667
z_4: 3000.0
y_1_1: 0.0
y_1_2: 0.0
y_1_3: 1666.6666666666665
y_1_4: 0.0
y_2_1: 0.0
y_2_2: 500.0
y_2_3: 0.0
y_2_4: 1125.0
y_3_1: 0.0
y_3_2: 0.0
y_3_3: 0.0
y_3_4: 1875.0
s_1: 0.0
s_2: 150.0
s_3: 0.0
Minimum Cost: 90200.0
```

由输出可知，此时最佳方案需要花费 $90200$ 美元。

### (4)

假设解决的是 $\omega = (1200， 3000， 3000)$ 这个 scenario。

运行

```bash
python3 main.py --task=4
```

输出为

```bash
x_1: 0.0
x_2: 250.0
x_3: 833.3333333333335
x_4: 2500.0
z_1: 0.0
z_2: 750.0
z_3: 1333.3333333333335
z_4: 3000.0
y_1_1: 0.0
y_1_2: 0.0
y_1_3: 1333.3333333333333
y_1_4: 0.0
y_2_1: 0.0
y_2_2: 750.0
y_2_3: 0.0
y_2_4: 0.0
y_3_1: 0.0
y_3_2: 0.0
y_3_3: 0.0
y_3_4: 3000.0
s_1: 0.0
s_2: 2325.0
s_3: 600.0
Minimum Cost: 1198462.5
```

由输出可知，此时最佳方案需要花费 $1198462.5$ 美元。

### (5)

将 Problem 1 中的描述具体化为 (1) 中所述 DEP 方程。

运行

```bash
python3 main.py --task=5
```

输出为

```bash
x_1: 0.0
x_2: 0.0
x_3: 1833.3333333333335
x_4: 2500.0
z_1: 0.0
z_2: 0.0
z_3: 2333.3333333333335
z_4: 3000.0
y_1_1_0: 0.0
y_1_2_0: 0.0
y_1_3_0: 0.0
...
y_3_2_215: 0.0
y_3_3_215: 0.0
y_3_4_215: 1875.0
s_1_215: 0.0
s_2_215: 3000.0
s_3_215: 1500.0
Minimum Cost: 355159.9537037038
```

由输出可知，此时最佳方案需要花费 $355159.95$ 美元。

### (6)

运行

```bash
python3 main.py --task=6
```

输出为

```bash
Evaluation of MVP:      366897.4845679012
Evaluation of Scenario: 377057.1341306584
Evaluation of DEP:      355159.95370370365
```

由输出可知，三种解在随机的情形下分别需要花费的金额（单位：美元）如下表所示：

| MVP | (4) 中的 scenario | DEP |
|:-:|:-:|:-:|
| $366897.48$ | $377057.13$ | $355159.95$ |

### (7)

Higle (2005) 的式 (15) 如下：

$$
\begin{align*}
c\bar{x} + h(\bar{x}, \mathbb{E}[\tilde{\omega}]) \le c x^* + \mathbb{E}[h(x^*, \tilde{\omega})] \le c\bar{x} + \mathbb{E}[h(\bar{x}, \tilde{\omega})]
\end{align*}
$$

可以看出，

- Lower bound 是 MVP 的解对应的目标函数值。由 (3) 知，值为 $90200$。
- Upper bound 是 MVP 的解在随机情况下的 evaluation 值。由 (6) 知，值为 $366897.48$。

### (8)

对于每一个 $\omega \in \Omega$，都进行一遍 evaluation，并求出期望 $\mathbb{E}[\hat{f}_\omega(\hat{x}_\omega)]$。

运行

```bash
python3 main.py --task=8
```

输出为

```bash
Evaluation:     339991.1848976582
```

- 由输出可知 $\mathbb{E}[\hat{f}_\omega(\hat{x}_\omega)] = 339991.18$，
- 由 (5) 知 $f(x^*) = 355159.95$，
- 由 (6) 知 $f(\bar{x}) = 366897.48$。

因此，

$$
\begin{align*}
\text{EVPI} & = f(x^*) - \mathbb{E}[\hat{f}_\omega(\hat{x}_\omega)] \\
& = 355159.95 - 339991.18 \\
& = 15168.77, \\
\text{VSS} & = f(\bar{x}) - f(x^*)\\
& = 366897.48 - 355159.95 \\
& = 11737.53.
\end{align*}
$$
