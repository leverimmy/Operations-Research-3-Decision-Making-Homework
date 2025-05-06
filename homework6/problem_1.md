# Problem 1

## TS-SP Model

The TS-SP model of CEP1 is as follows:

$$
\begin{align*}
\min \quad & \sum_{j = 1}^{n}c_jx_j + \mathbb{E}[h(z, \tilde{\omega})] \\
\text{s.t.} \quad & -x_j + z_j \le h_j, \forall j \in \{1, 2, \cdots, n\}, \\
& \sum_{j = 1}^{n}t_jz_j \le T, \\
& 0 \le z_j \le u_j, \forall j \in \{1, 2, \cdots, n\}, \\
& 0 \le x_j, \forall j \in \{1, 2, \cdots, n\}.
\end{align*}
$$

where

$$
\begin{align*}
h(z, \omega) = \min \quad & \sum_{i = 1}^{m}\sum_{j = 1}^{n}g_{ij}y_{ij} + \sum_{i = 1}^{m}p_is_i \\
\text{s.t.} \quad & \sum_{j = 1}^{n}a_{ij}y_{ij} + s_i \ge \omega_i, \forall i \in \{1, 2, \cdots, m\}, \\
& \sum_{i = 1}^{m}y_{ij} \le z_j, \forall j \in \{1, 2, \cdots, n\}, \\
& y_{ij} \ge 0, \forall i \in \{1, 2, \cdots, m\}, \forall j \in \{1, 2, \cdots, n\}, \\
& s_i \ge 0, \forall i \in \{1, 2, \cdots, m\}.
\end{align*}
$$
