# Problem 2

画出决策树如下：

```mermaid
graph LR
A[ ] -->|operate now| B((EV_1))
A -->|wait for 12 hours| C((EV_2))
B -->|**28%**, appendicitis| D([p = 0.0009])
B -->|**72%**, nonspecific abdominal pains| E([p = 0.0004])
C -->|**6%**, perforated appendix| F([p = 0.0064])
C -->|**22%**, appendicitis| G([p = 0.0009])
C -->|**72%**, nonspecific abdominal pain| H([p = 0.0000])
```

由图知，若选择立即做手术，则患者死亡概率为

$$
\text{EV}_1 = 28\% \times 0.0009 + 72\% \times 0.0004 = 5.4 \times 10^{-4}
$$

若选择等待 $12$ 小时后再做手术，则患者死亡概率为

$$
\text{EV}_2 = 6\% \times 0.0064 + 22\% \times 0.0009 + 72\% \times 0.0000 = 5.82 \times 10^{-4}
$$

由于 $5.4 \times 10^{-4} < 5.82 \times 10^{-4}$，故应当选择立即做手术。
