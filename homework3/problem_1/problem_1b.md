# Problem 1b

## Primal Model

$$
\begin{align*}
\max \quad & x_{OA} + x_{OB} - x_{BO} \\
\text{s.t.} \quad & x_{AB} + x_{AD} - x_{OA} - x_{BA} - x_{DA} = 0, \quad(W_A) \\
& x_{BA} + x_{BD} + x_{BO} - x_{OB} - x_{AB} = 0, \quad(W_B) \\
& x_{OA} \le u_{OA}, \quad(V_{OA}) \\
& x_{OB} \le u_{OB}, \quad(V_{OB}) \\
& x_{AB} \le u_{AB}, \quad(V_{AB}) \\
& x_{AD} \le u_{AD}, \quad(V_{AD}) \\
& x_{BO} \le u_{BO}, \quad(V_{BO}) \\
& x_{BA} \le u_{BA}, \quad(V_{BA}) \\
& x_{BD} \le u_{BD}, \quad(V_{BD}) \\
& x_{DA} \le u_{DA}, \quad(V_{DA}) \\
& x_{OA}, x_{OB}, x_{AB}, x_{AD}, x_{BO}, x_{BA}, x_{BD}, x_{DA} \ge 0.
\end{align*}
$$

## Dual Model

$$
\begin{align*}
\min \quad & u_{OA}V_{OA} + u_{OB}V_{OB} + u_{AB}V_{AB} + u_{AD}V_{AD} + u_{BO}V_{BO} + u_{BA}V_{BA} + u_{BD}V_{BD} + u_{DA}V_{DA} \\
\text{s.t.} \quad & V_{OA} - W_A \ge 1, \\
& V_{OB} - W_B \ge 1, \\
& V_{AB} + W_A - W_B \ge 0, \\
& V_{AD} + W_A \ge 0, \\
& V_{BO} + W_B \ge -1, \\
& V_{BA} - W_A + W_B \ge 0, \\
& V_{BD} + W_B \ge 0, \\
& V_{DA} - W_A \ge 0, \\
& V_{OA}, V_{OB}, V_{AB}, V_{AD}, V_{BO}, V_{BA}, V_{BD}, V_{DA} \ge 0, \\
& W_A, W_B \;\text{urs}.
\end{align*}
$$
