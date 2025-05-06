import argparse
from gurobipy import Model, GRB, quicksum

C = [2.5, 3.75, 5.0, 3.0]
L = [400, 400, 400]
G = [[2.6, 3.4, 3.4, 2.5], [1.5, 2.3, 2.0, 3.6], [4.0, 3.8, 3.5, 3.2]]
H = [500, 500, 500, 500]
T = [0.08, 0.04, 0.03, 0.01]
TT = 100
U = [2000, 2000, 3000, 3000]
A = [[0.6, 0.6, 0.9, 0.8], [0.1, 0.9, 0.6, 0.8], [0.05, 0.2, 0.5, 0.8]]
DEMAND_I = [(0, 1/6), (600, 1/6), (1200, 1/6), (1800, 1/6), (2400, 1/6), (3000, 1/6)]
DEMAND = [DEMAND_I, DEMAND_I, DEMAND_I]

N = len(C)
M = len(L)

D_BAR = [sum(d[i][0] * d[i][1] for i in range(len(d))) for d in DEMAND]

OMEGA = [((DEMAND_I[i][0], DEMAND_I[j][0], DEMAND_I[k][0]), \
          DEMAND_I[i][1] * DEMAND_I[j][1] * DEMAND_I[k][1]) \
            for i in range(len(DEMAND_I)) \
                for j in range(len(DEMAND_I)) \
                    for k in range(len(DEMAND_I))]


def solve_deterministic(d):
    # Model
    model = Model("Deterministic Model")

    # 决策变量
    x = [model.addVar(name=f"x_{j}") for j in range(1, N + 1)]
    z = [model.addVar(name=f"z_{j}") for j in range(1, N + 1)]
    y = [model.addVar(name=f"y_{i}_{j}") for i in range(1, M + 1) for j in range(1, N + 1)]
    s = [model.addVar(name=f"s_{i}") for i in range(1, M + 1)]

    # 目标函数
    model.setObjective(quicksum(C[j] * x[j] for j in range(N))
                       + quicksum(G[i][j] * y[i * N + j] for i in range(M) for j in range(N))
                       + quicksum(L[i] * s[i] for i in range(M)), GRB.MINIMIZE)
    # 约束条件
    for j in range(N):
        model.addConstr(-x[j] + z[j] <= H[j])
    model.addConstr(quicksum(T[j] * z[j] for j in range(len(z))) <= TT)
    for j in range(N):
        model.addConstr(z[j] <= U[j])
    for i in range(M):
        model.addConstr(quicksum(A[i][j] * y[i * N + j] for j in range(N)) + s[i] >= d[i])
    for j in range(N):
        model.addConstr(quicksum(y[i * N + j] for i in range(M)) - z[j] <= 0)
    
    model.optimize()
    return model


def get_d_omega(idx):
    print(f"Demand scenario {idx}: {OMEGA[idx][0]}")
    return OMEGA[idx][0]


def solve_stochastic():
    # Model
    model = Model("Stochastic Model")

    # 决策变量
    x = [model.addVar(name=f"x_{j}") for j in range(1, N + 1)]
    z = [model.addVar(name=f"z_{j}") for j in range(1, N + 1)]
    y = []
    s = []
    for k in range(len(OMEGA)):
        y.append([model.addVar(name=f"y_{i}_{j}_{k}") for i in range(1, M + 1) for j in range(1, N + 1)])
        s.append([model.addVar(name=f"s_{i}_{k}") for i in range(1, M + 1)])

    # 目标函数
    model.setObjective(quicksum(C[j] * x[j] for j in range(N))
                       + quicksum((quicksum(G[i][j] * y[k][i * N + j] for i in range(M) for j in range(N))
                                   + quicksum(L[i] * s[k][i] for i in range(M))) * OMEGA[k][1]
                                  for k in range(len(OMEGA))), GRB.MINIMIZE)

    # 约束条件
    for j in range(N):
        model.addConstr(-x[j] + z[j] <= H[j])
    model.addConstr(quicksum(T[j] * z[j] for j in range(len(z))) <= TT)
    for j in range(N):
        model.addConstr(z[j] <= U[j])
    for k in range(len(OMEGA)):
        for i in range(M):
            model.addConstr(quicksum(A[i][j] * y[k][i * N + j] for j in range(N)) + s[k][i] >= OMEGA[k][0][i])
        for j in range(N):
            model.addConstr(quicksum(y[k][i * N + j] for i in range(M)) - z[j] <= 0)

    model.optimize()
    return model


def solve_task_i(i):
    if i == 3:
        return solve_deterministic(D_BAR)
    elif i == 4:
        return solve_deterministic(get_d_omega(len(OMEGA) // 2 - 1))
    elif i == 5:
        return solve_stochastic()
    else:
        raise ValueError("Invalid task number.")


def evaluate(xz):
    x, z = xz
    result = 0
    for k in range(len(OMEGA)):
        # Model
        model = Model("Evaluation Model")

        # 决策变量
        y = [model.addVar(name=f"y_{i}_{j}") for i in range(1, M + 1) for j in range(1, N + 1)]
        s = [model.addVar(name=f"s_{i}") for i in range(1, M + 1)]
        
        # 目标函数
        model.setObjective(quicksum(C[j] * x[j] for j in range(N))
                           + quicksum(G[i][j] * y[i * N + j] for i in range(M) for j in range(N))
                           + quicksum(L[i] * s[i] for i in range(M)), GRB.MINIMIZE)

        # 约束条件
        for j in range(N):
            model.addConstr(-x[j] + z[j] <= H[j])
        model.addConstr(quicksum(T[j] * z[j] for j in range(len(z))) <= TT)
        for j in range(N):
            model.addConstr(z[j] <= U[j])
        for i in range(M):
            model.addConstr(quicksum(A[i][j] * y[i * N + j] for j in range(N)) + s[i] >= OMEGA[k][0][i])
        for j in range(N):
            model.addConstr(quicksum(y[i * N + j] for i in range(M)) - z[j] <= 0)
        
        model.optimize()
        current_result = model.objVal * OMEGA[k][1]
        result += current_result
    
    return result


def extract_x_z_from_model(model):
    x = []
    z = []
    for v in model.getVars():
        if v.varName.startswith('x_'):
            x.append(v.x)
        if v.varName.startswith('z_'):
            z.append(v.x)
    return x, z


def solve_task_6():
    eval_mvp = evaluate(extract_x_z_from_model(solve_task_i(3)))
    eval_scenario = evaluate(extract_x_z_from_model(solve_task_i(4)))
    eval_dep = evaluate(extract_x_z_from_model(solve_task_i(5)))
    print(f"Evaluation of MVP:\t{eval_mvp}")
    print(f"Evaluation of Scenario:\t{eval_scenario}")
    print(f"Evaluation of DEP:\t{eval_dep}")


def solve_task_8():
    result = 0
    for i in range(len(OMEGA)):
        model = solve_deterministic(get_d_omega(i))
        result += model.objVal * OMEGA[i][1]
    print(f"Evaluation:\t{result}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=int, required=True, help="Specify the task number")
    args = parser.parse_args()

    if args.task == 6:
        solve_task_6()
    elif args.task == 7:
        pass
    elif args.task == 8:
        solve_task_8()
    else:
        try:
            model = solve_task_i(args.task)
            # 输出各个变量的值
            for v in model.getVars():
                print(f"{v.varName}: {v.x}")
            # 输出目标函数值
            print(f"Minimum Cost: {model.objVal}")
        except Exception as e:
            print(f"An error occurred: {e}")
