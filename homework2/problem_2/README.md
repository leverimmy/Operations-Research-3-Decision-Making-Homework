# Problem 2

## 安装与运行

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

最后，指定输入文件与输出文件后，运行程序：

```bash
python3 main.py -i <input-file> -o <output-file>
```

## 输入格式与输出格式

在 `data` 目录下有 `input.xlsx` 和 `output.xlsx` 两个文件，分别是输入和输出示例。

### 输入格式

输入的格式如下图所示，是一个 Excel 文件，需要填写 $n$ 和 $m$ 的值，以及 $c_{ij}$、各个 Supply 和 Demand 的值，其中 $n$ 是 Supply 的数量，$m$ 是 Demand 的数量。

![输入示例](./assets/input.png)

### 输出格式

输出的格式如下图所示，是一个 Excel 文件，包含了 $x_{ij}$ 的值，以及目标函数的值。

![输出示例](./assets/output.png)

## Gurobi 与 Problem 1 中 optimal dual variables 的对比

在使用 Gurobi 进行求解时，我发现其 objective function 的最优值与 Problem 1 中的结果相同，并且各个 optimal decision variable $x_{ij}$ 的值也一致。然而，optimal dual variable $V_i$ 和 $W_j$ 的值均存在差异。

我先开始认为这是因为有自由变量，所以 $V_i$ 和 $W_j$ 的值不唯一。但是，我发现按照 Problem 1 中的表格检查，它并不自洽。然而，当我将 Gurobi 求得的 $V_i$ 取相反数后，经验证，此时的 $V_i$ 和 $W_j$ 构成的是合理且自洽的解。

这个结果并非偶然，它与课上对 Transportation Problem 的 dual model 做的修改一致：课上我们形式化地将 dual model 的标准形式，通过令 $V_i \gets -V_i$ 来得到与 Shortest Path Problem 一致的形式，而 Gurobi 并没有这么做，所以 **Gurobi 得到的 $V_i$ 与我们的符号相反**。
