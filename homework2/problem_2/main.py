from gurobipy import Model, GRB, quicksum
import argparse
import pandas as pd


def read_data_from_excel(file_path):
    df = pd.read_excel(file_path, header=None)

    n = int(df.iloc[0, 1])
    m = int(df.iloc[1, 1])

    c = df.iloc[2:n+2, 1:m+1].values.tolist()
    s = df.iloc[2:n+2, m+1].values.tolist()
    d = df.iloc[n+2, 1:m+1].values.tolist()

    return c, s, d


def solve(c, s, d):
    # Supply 和 Demand 的数量
    n = len(s)
    m = len(d)

    # Model
    model = Model("Transportation Problem")

    # 决策变量
    x = [[model.addVar(name=f"x_{i}_{j}") for j in range(m)] for i in range(n)]

    # 目标函数
    model.setObjective(quicksum(c[i][j] * x[i][j] for i in range(n) for j in range(m)), GRB.MINIMIZE)

    # Supply 对应的约束
    supply_constrs = []
    for i in range(n):
        supply_constrs.append(model.addConstr(quicksum(x[i][j] for j in range(m)) == s[i], name=f"Supply_{i}"))

    # Demand 对应的约束
    demand_constrs = []
    for j in range(m):
        demand_constrs.append(model.addConstr(quicksum(x[i][j] for i in range(n)) == d[j], name=f"Demand_{j}"))

    # 非负约束
    for i in range(n):
        for j in range(m):
            model.addConstr(x[i][j] >= 0, name=f"NonNeg_{i}_{j}")

    model.optimize()

    
    if model.status == GRB.OPTIMAL:
        # 得到结果
        xs = []
        v = []
        w = []
        for i in range(n):
            xs.append([])
            for j in range(m):
                xs[i].append(x[i][j].X)

        # 对偶变量
        for i, constr in enumerate(supply_constrs):
            v.append(constr.Pi)
        for j, constr in enumerate(demand_constrs):
            w.append(constr.Pi)
        return xs, v, w, model.ObjVal
    else:
        return None


def write_data_to_excel(file_path, x, v, w, obj):
    n = len(v)
    m = len(w)

    df = pd.DataFrame()
    
    df.loc[0, 0] = "obj="
    df.loc[0, 1] = obj

    df.loc[1, 0] = "x="
    for i in range(n):
        for j in range(m):
            df.loc[1 + i, 1 + j] = x[i][j] if x[i][j] != 0 else None
    
    df.loc[0, m + 1] = "V"
    for i in range(n):
        # 注意这里 v[i] 和上课讲的对偶变量 v[i] 的符号是相反的
        df.loc[1 + i, m + 1] = -v[i]

    df.loc[2 + n, 0] = "W"
    for j in range(m):
        df.loc[2 + n, 1 + j] = w[j]

    df.to_excel(file_path, index=False, header=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve a transportation problem.")
    parser.add_argument("-i", "--input", required=True, help="Input Excel file path")
    parser.add_argument("-o", "--output", required=True, help="Output Excel file path")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    c, s, d = read_data_from_excel(input_file)
    if solve(c, s, d) is None:
        print("The model is infeasible.")
    else:
        x, v, w, obj = solve(c, s, d)
        write_data_to_excel(output_file, x, v, w, obj)
