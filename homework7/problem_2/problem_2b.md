# Problem 2b

由题知

$$
L = (p_1, r_1; p_2, r_2; \cdots),
$$

其中 $p_k = 2^{-k}, r_k = \$2^k$。

因此，

$$
\begin{align*}
E(U \text{ for } L) & = \sum_{i = 1}^{+\infty}p_k u(r_k) \\
& = \sum_{i = 1}^{+\infty}\frac{1}{2^k} \times \log_22^k \\
& = \sum_{i = 1}^{+\infty}\frac{k}{2^k} \\
& = \lim_{n \to +\infty}\frac{2^{n + 1} - n - 2}{2^n} \\
& = 2
\end{align*}
$$

所以，

$$
\begin{align*}
\text{CE}(L) & = u^{-1}(E(U \text{ for } L)) \\
& = 2^2 \\
& = 4
\end{align*}
$$
