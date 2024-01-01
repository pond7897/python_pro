import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# รับค่าจากผู้ใช้สำหรับการเลือก Maximize หรือ Minimize
optimization_direction = input('Maximize or Minimize (max | min): ')

def get_coefficients(prompt):
    return [float(val) for val in input(prompt).split()]

# รับค่าจากผู้ใช้สำหรับ Objective Function
c = [-val for val in get_coefficients('ใส่ค่าสัมประสิทธิ์หน้าสมการ เช่น (4x+2y ให้ใส่ 4 2) : ')]

# รับค่าจากผู้ใช้สำหรับจำนวนข้อจำกัด
num_constraints = int(input('มีกี่ข้อจำกัด: '))

# รับค่าจากผู้ใช้สำหรับ Constraints
A = []
b = []
for i in range(num_constraints):
    constraint = get_coefficients(f'ใส่สัมประสิทธิ์หน้าสมการของ x และ y ในข้อจำกัดที่ {i + 1} เช่น (2x+y ให้ใส่ 2 1) : ')
    rhs = float(input(f'ใส่ค่าตัวเลขขอบเขตของสัมประสิทธิ์ตัวที่ {i + 1} เช่น ( (... <= 3) ให้ใส่ 3 ) : '))
    A.append(constraint)
    b.append(rhs)


# กำหนดเงื่อนไข (Constraints)
bounds = [(0, None), (0, None)]

# แก้ปัญหาการปรับ
if optimization_direction == 'max':
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
elif optimization_direction == 'min':
    result = linprog([-coefficient for coefficient in c], A_ub=A, b_ub=b, bounds=bounds, method='highs')
else:
    raise ValueError('กรุณาระบุแค่ "max" หรือ "min".')

print(f'ค่า x และ y ที่ทำให้ Objective Function มีค่า{optimization_direction}คือ:')
print(f'x = {result.x[0]}')
print(f'y = {result.x[1]}')
print(f'ค่า{optimization_direction}ของ Objective Function คือ {-result.fun}')

# สร้างกราฟ
x_values = np.linspace(0, 50, 100)
y_values = [(b[i] - x_values * A[i][0]) / A[i][1] for i in range(num_constraints)]

plt.figure(figsize=(8, 6))

# พล็อตข้อจำกัด
for i in range(num_constraints):
    plt.plot(x_values, y_values[i], label=f'Constraint {i + 1}: {A[i][0]}x + {A[i][1]}y <= {b[i]}')

plt.axhline(0, color='g', linestyle='--', label=r'$y \geq 0$')
plt.axvline(0, color='g', linestyle='--', label=r'$x \geq 0$')

# เติมสีในพื้นที่ใต้กราฟ
min_y_values = np.min(y_values, axis=0)
plt.fill_between(x_values, min_y_values, color='gray', alpha=0.5)

# พล็อตจุดที่ทำให้ Objective Function มีค่า{optimization_direction}
plt.scatter(result.x[0], result.x[1], color='red', marker='*', label=f'{optimization_direction.capitalize()} Point')

# แสดงจุดที่ละเอียด
for i in range(0, int(np.max(b))+1, 20):
    for j in range(num_constraints):
        plt.scatter(i, (b[j] - i * A[j][0]) / A[j][1], color='blue')  # ใส่จุดที่ละเอียด

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Linear Programming: {optimization_direction.capitalize()}imize Objective Function')
plt.legend()
plt.grid(True)
plt.show()
