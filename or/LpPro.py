import pulp as p
import matplotlib.pyplot as plt
import numpy as np
import math as m

def getMax(constraint_coefficients_list, rhs_values):
    cut_x,cut_y = [], []
    for i in range(len(constraint_coefficients_list)):
        if (constraint_coefficients_list[i][0] == 0): # x = 0
            cut_x.append(0)
            cut_y.append(rhs_values[i]/constraint_coefficients_list[i][1])
        elif (constraint_coefficients_list[i][1] == 0): # y = 0
            cut_x.append(rhs_values[i]/constraint_coefficients_list[i][0])
            cut_y.append(0)
        else:
            cut_x.append(rhs_values[i]/constraint_coefficients_list[i][0])
            cut_y.append(rhs_values[i]/constraint_coefficients_list[i][1])
    
    return m.ceil(max(cut_x)), m.ceil(max(cut_y))
                
def plot_lp_problem(constraint_coefficients_list, relations, rhs_values):
    
    
    # Plot constraints
    x = np.arange(0, 100, 0.1)
    for i in range(len(constraint_coefficients_list)):
        
        y_expression = (rhs_values[i]/constraint_coefficients_list[i][1]) - (constraint_coefficients_list[i][0]/constraint_coefficients_list[i][1])*x
        if relations[i] == "<=": 
            plt.plot(x, y_expression, label=f'Constraint {i + 1}: {constraint_coefficients_list[i]} <= {rhs_values[i]}')
        elif relations[i] == "=":
            plt.plot(x, y_expression, label=f'Constraint {i + 1}: {constraint_coefficients_list[i]} = {rhs_values[i]}')
        elif relations[i] == ">=":
            plt.plot(x, y_expression, label=f'Constraint {i + 1}: {constraint_coefficients_list[i]} >= {rhs_values[i]}')
            
    max_x, max_y = getMax(constraint_coefficients_list, rhs_values)
        
    # Plot the feasible region using the common condition
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('LP Problem: Graphical Solution')
    
    plt.axis([0,max_x,0,max_y])
    plt.legend()
    plt.grid(True)
    plt.show()


# max Z = num1*x1 + num2*x2
print("Enter 'max' for Maximization or 'min' for Minimization:", end=" ")
objective_type = input()
Lp_prob = p.LpProblem('Problem', p.LpMaximize if objective_type == 'max' else p.LpMinimize)

num_vars = 2
variables = [p.LpVariable(f"x{i}", lowBound=0) for i in range(1, num_vars + 1)] # 1,2

print(f"Enter coefficients for {variables} (separated by space):", end=" ")
coefficients = list(map(float, input().split()))
objective_function = sum(coefficients[i] * variables[i] for i in range(num_vars))
Lp_prob += objective_function

print("Enter the number of constraints:", end=" ")
num_constraints = int(input())

constraint_coefficients_list = []
relations = []
rhs_values = []

for i in range(num_constraints):
    print(f"Enter coefficients for {variables} (separated by space):", end=" ")
    constraint_coefficients = list(map(float, input().split()))
    constraint_coefficients_list.append(constraint_coefficients)

    print(f"Enter the relation for constraint {i + 1} (<=, =, >=):", end=" ")
    relation = input()
    relations.append(relation)

    print(f"Enter the RHS value for constraint {i + 1}:", end=" ")
    rhs_value = float(input())
    rhs_values.append(rhs_value)

    constraint_expression = sum(constraint_coefficients[j] * variables[j] for j in range(num_vars))

    if relation == "<=":
        Lp_prob += constraint_expression <= rhs_value
    elif relation == "=":
        Lp_prob += constraint_expression == rhs_value
    elif relation == ">=":
        Lp_prob += constraint_expression >= rhs_value
        
print(Lp_prob)
status = Lp_prob.solve()
print(p.LpStatus[status])


for i in range(num_vars):
    print(f"{variables[i].name}: {p.value(variables[i])}")

print(f"Objective Value: {p.value(Lp_prob.objective)}")

# plot graph
plt.annotate(f'Optimal \n solution\n({p.value(variables[0])}, {p.value(variables[1])})', xy = (p.value(variables[0]), p.value(variables[1])),arrowprops=dict(arrowstyle='o'))
plot_lp_problem(constraint_coefficients_list, relations, rhs_values)

