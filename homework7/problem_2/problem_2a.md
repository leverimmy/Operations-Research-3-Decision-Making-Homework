# Problem 2a

由题知

$$
L = (p_1, r_1; p_2, r_2; \cdots),
$$

其中 $p_k = 2^{-k}, r_k = \$2^k$。

由于决策者是 risk-neutral 的，因此 $u(x)$ 为线性函数。不妨设 $u(x) = x$，因此，

$$
\begin{align*}
E(U \text{ for } L) & = \sum_{i = 1}^{+\infty}p_k u(r_k) \\
& = \sum_{i = 1}^{+\infty}\frac{1}{2^k} \times 2^k \\
& = \sum_{i = 1}^{+\infty}1 \\
& = +\infty
\end{align*}
$$

而，

$$
\begin{align*}
\text{CE}(L) & = u^{-1}(E(U \text{ for } L)) \\
& = E(U \text{ for } L) \\
& = +\infty
\end{align*}
$$

这显然是不合理的，因为实际中**没有人会为这种彩票支付无限多的钱**。这就是 The St. Petersburg Paradox 的核心所在，说明了期望值在某些情况下的局限性。
