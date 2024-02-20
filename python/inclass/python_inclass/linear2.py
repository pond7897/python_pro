import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# กำหนดฟังก์ชันการเปลี่ยนแปลง (Objective Function)
c = [-5, -4]

# กำหนดเงื่อนไข (Constraints)
A = [[1, 3], [4, 2]]
b = [200, 140]
bounds = [(0, None), (0, None)]

# แก้ปัญหาการปรับ
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
print('ค่า x และ y ที่ทำให้ 5x + 4y มีค่าสูงสุดคือ:')
print(f'x = {result.x[0]}')
print(f'y = {result.x[1]}')
print(f'ค่าสูงสุดของ 5x + 4y คือ {result.fun}')

# สร้างกราฟ
x_values = np.linspace(0, 50, 100)
y1_values = (200 - x_values) / 3
y2_values = (140 - 4*x_values) / 2



plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$x + 3y \leq 200$')
plt.plot(x_values, y2_values, label=r'$4x + 2y \leq 140$')
plt.axhline(0, color='g', linestyle='--', label=r'$y \geq 0$')
plt.axvline(0, color='g', linestyle='--', label=r'$x \geq 0$')

# เติมสีในพื้นที่ใต้กราฟ
plt.fill_between(x_values, np.minimum(y1_values, y2_values), color='gray', alpha=0.5)

# พล็อตจุดที่ทำให้ฟังก์ชันเป้าหมายมีค่าสูงสุด
plt.scatter(result.x[0], result.x[1], color='red', marker='*', label='Maximize Point')

# แสดงจุดที่ละเอียด
for i in range(0, 201, 20):
    plt.scatter(i, (200 - i) / 3, color='blue')  # ใส่จุดที่ละเอียด
    plt.scatter(i, (140 - 4*i) / 2, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Programming: Maximize 5x + 4y')
plt.legend()
plt.grid(True)
plt.show()
