import argparse
from gurobipy import Model, GRB, quicksum

COST = [2, 4, 5.2]
PRICE = [60, 40, 10]
M = [[8, 6, 1], [4, 2, 1.5], [2, 1.5, 0.5]]

DEMAND_D = [(95, 0.5), (190, 0.4), (265, 0.1)]
DEMAND_T = [(40, 0.3), (150, 0.6), (230, 0.1)]
DEMAND_C = [(140, 0.15), (210, 0.25), (365, 0.3), (390, 0.3)]
DEMAND = [DEMAND_D, DEMAND_T, DEMAND_C]

D_BAR = [sum(d[i][0] * d[i][1] for i in range(len(d))) for d in DEMAND]

OMEGA = [((DEMAND_D[i][0], DEMAND_T[j][0], DEMAND_C[k][0]), \
          DEMAND_D[i][1] * DEMAND_T[j][1] * DEMAND_C[k][1]) \
            for i in range(len(DEMAND_D)) \
                for j in range(len(DEMAND_T)) \
                    for k in range(len(DEMAND_C))]


def solve_deterministic(d):
    # Model
    model = Model("Deterministic Model")

    # 决策变量
    x = [model.addVar(name=f"x_{i}") for i in ['l', 'f', 'c']]
    y = [model.addVar(name=f"y_{i}") for i in ['d', 't', 'c']]
    s = [model.addVar(name=f"s_{i}") for i in ['d', 't', 'c']]

    # 目标函数
    model.setObjective(quicksum(-x[i] * COST[i] for i in range(len(x))) + quicksum(s[i] * PRICE[i] for i in range(len(s))), GRB.MAXIMIZE)

    # 约束条件
    for i in range(len(x)):
        model.addConstr(-x[i] + quicksum(M[i][j] * y[j] for j in range(len(y))) <= 0)
    for i in range(len(y)):
        model.addConstr(-y[i] + s[i] <= 0)
    for i in range(len(s)):
        model.addConstr(s[i] <= d[i])

    model.optimize()
    return model


def get_d_omega(idx):
    print(f"Demand scenario {idx}: {OMEGA[idx][0]}")
    return OMEGA[idx][0]


def solve_stochastic():
    # Model
    model = Model("Stochastic Model")

    # 决策变量
    x = [model.addVar(name=f"x_{i}") for i in ['l', 'f', 'c']]
    y_d = [model.addVar(name=f"y_d_{i}") for i in range(len(OMEGA))]
    y_t = [model.addVar(name=f"y_t_{i}") for i in range(len(OMEGA))]
    y_c = [model.addVar(name=f"y_c_{i}") for i in range(len(OMEGA))]

    # 目标函数
    model.setObjective(quicksum(-x[i] * COST[i] for i in range(len(x))) \
                       + quicksum((y_d[i] * PRICE[0] + y_t[i] * PRICE[1] + y_c[i] * PRICE[2]) * OMEGA[i][1] \
                                  for i in range(len(OMEGA))), GRB.MAXIMIZE)

    # 约束条件
    for i in range(len(OMEGA)):
        model.addConstr(y_d[i] <= OMEGA[i][0][0])
        model.addConstr(y_t[i] <= OMEGA[i][0][1])
        model.addConstr(y_c[i] <= OMEGA[i][0][2])

        for j in range(len(x)):
            model.addConstr(-x[j] + quicksum(M[j][k] * y for (k, y) in enumerate([y_d[i], y_t[i], y_c[i]])) <= 0)

    model.optimize()
    return model


def solve_task_i(i):
    if i == 2:
        return solve_deterministic(D_BAR)
    elif i == 3:
        return solve_deterministic(get_d_omega(0))
    elif i == 4:
        return solve_stochastic()
    else:
        raise ValueError("Invalid task number.")


def evaluate(x):
    result = 0
    for i in range(len(OMEGA)):
        # Model
        model = Model("Evaluation Model")

        # 决策变量
        y = [model.addVar(name=f"y_{i}") for i in ['d', 't', 'c']]
        # 目标函数
        model.setObjective(quicksum(-x[i] * COST[i] for i in range(len(x))) \
                           + quicksum((y[i] * PRICE[i]) for i in range(len(y))), GRB.MAXIMIZE)
        # 约束条件
        for j in range(len(y)):
            model.addConstr(y[j] <= OMEGA[i][0][j])
        for j in range(len(x)):
            model.addConstr(-x[j] + quicksum(M[j][k] * y[k] for k in range(len(y))) <= 0)
        
        model.optimize()
        current_result = model.objVal * OMEGA[i][1]
        result += current_result
    
    return result


def extract_x_from_model(model):
    x = []
    for v in model.getVars():
        if v.varName.startswith('x_'):
            x.append(v.x)
    return x


def solve_task_5():
    eval_mvp = evaluate(extract_x_from_model(solve_task_i(2)))
    eval_scenario = evaluate(extract_x_from_model(solve_task_i(3)))
    eval_dep = evaluate(extract_x_from_model(solve_task_i(4)))
    print(f"Evaluation of MVP:\t{eval_mvp}")
    print(f"Evaluation of Scenario:\t{eval_scenario}")
    print(f"Evaluation of DEP:\t{eval_dep}")


def solve_task_6():
    result = 0
    for i in range(len(OMEGA)):
        model = solve_deterministic(get_d_omega(i))
        result += model.objVal * OMEGA[i][1]
    print(f"Evaluation:\t{result}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=int, required=True, help="Specify the task number")
    args = parser.parse_args()

    if args.task == 5:
        solve_task_5()
    elif args.task == 6:
        solve_task_6()
    else:
        try:
            model = solve_task_i(args.task)
            # 输出各个变量的值
            for v in model.getVars():
                print(f"{v.varName}: {v.x}")
            # 输出目标函数值
            print(f"Maximum Profit: {model.objVal}")
        except Exception as e:
            print(f"An error occurred: {e}")
