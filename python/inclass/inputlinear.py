import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# รับค่าจากผู้ใช้สำหรับ Objective Function
c = [-float(input('Enter the coefficient for x: ')), -float(input('Enter the coefficient for y: '))]

# รับค่าจากผู้ใช้สำหรับ Constraints
A = [[float(input('Enter the coefficient for x in Constraint 1: ')), float(input('Enter the coefficient for y in Constraint 1: '))],
     [float(input('Enter the coefficient for x in Constraint 2: ')), float(input('Enter the coefficient for y in Constraint 2: '))]]
b = [float(input('Enter the RHS value for Constraint 1: ')), float(input('Enter the RHS value for Constraint 2: '))]

# กำหนดเงื่อนไข (Constraints)
bounds = [(0, None), (0, None)]

# แก้ปัญหาการปรับ
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
print('ค่า x และ y ที่ทำให้ Objective Function มีค่าสูงสุดคือ:')
print(f'x = {result.x[0]}')
print(f'y = {result.x[1]}')
print(f'ค่าสูงสุดของ Objective Function คือ {result.fun}')

# สร้างกราฟ
x_values = np.linspace(0, 50, 100)
y1_values = (b[0] - x_values * A[0][0]) / A[0][1]
y2_values = (b[1] - x_values * A[1][0]) / A[1][1]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=f'Constraint 1: {A[0][0]}x + {A[0][1]}y <= {b[0]}')
plt.plot(x_values, y2_values, label=f'Constraint 2: {A[1][0]}x + {A[1][1]}y <= {b[1]}')
plt.axhline(0, color='g', linestyle='--', label=r'$y \geq 0$')
plt.axvline(0, color='g', linestyle='--', label=r'$x \geq 0$')

# เติมสีในพื้นที่ใต้กราฟ
plt.fill_between(x_values, np.minimum(y1_values, y2_values), color='gray', alpha=0.5)

# พล็อตจุดที่ทำให้ Objective Function มีค่าสูงสุด
plt.scatter(result.x[0], result.x[1], color='red', marker='*', label='Maximize Point')

# แสดงจุดที่ละเอียด
for i in range(0, int(b[0])+1, 20):
    plt.scatter(i, (b[0] - i * A[0][0]) / A[0][1], color='blue')  # ใส่จุดที่ละเอียด
for i in range(0, int(b[1])+1, 20):
    plt.scatter(i, (b[1] - i * A[1][0]) / A[1][1], color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Programming: Maximize Objective Function')
plt.legend()
plt.grid(True)
plt.show()
