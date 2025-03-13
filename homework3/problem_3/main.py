from gurobipy import Model, GRB, quicksum
import argparse
import pandas as pd


def read_data_from_excel(file_path):
    df = pd.read_excel(file_path, header=None)

    n = int(df.iloc[0, 1])
    m = int(df.iloc[1, 1])
    L = int(df.iloc[2, 1])
    N = int(df.iloc[3, 1])
    t = df.iloc[7:7+n, 1].values.tolist()
    l = df.iloc[7:7+n, 2].values.tolist()

    return n, m, L, N, t, l


def solve(n, m, L, N, l, t):
    # Model
    model = Model("Laboring Problem")

    # 决策变量
    x = []
    for i in range(m):
        x.append(model.addVar(name=f"x_S_M{i}"))
    for i in range(n):
        x.append(model.addVar(name=f"x_P{i}_T"))
        for j in range(t[i]):
            x.append(model.addVar(name=f"x_M{j}_P{i}"))

    # 目标函数
    model.setObjective(quicksum(x[i] for i in range(m + sum(t), m + sum(t) + n)), GRB.MINIMIZE)

    # 约束条件
    for i in range(m):
        model.addConstr(x[i] == L)
    for i in range(sum(t)):
        model.addConstr(x[m + i] == N)
    for i in range(n):
        model.addConstr(x[m + sum(t) + i] == t[i])

    model.optimize()
    return model.objVal == sum(t)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve a laboring problem.")
    parser.add_argument("-i", "--input", required=True, help="Input Excel file path")
    args = parser.parse_args()

    input_file = args.input

    n, m, L, N, t, l = read_data_from_excel(input_file)
    print(solve(n, m, L, N, t, l))
