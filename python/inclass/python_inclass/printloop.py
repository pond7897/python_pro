""" for i in range(4):
    print("*"*6, end = "\n") """

""" for i in range(4,0,-1):
    print("*"*i, end = "\n") """

""" quantity, cost = int(input("Enter quantity: ")), float(input("Enter quantity: "))
total = quantity*cost
print("Quantity: %d, Cost: %.2f, Total: %.2f" %(quantity,cost,total)) """

number_list = []
print("Please enter three numbers")

# input
for i in range(3):
    number = int(input())
    number_list.append(number)

# forward
print("Your numbers forward: ")
for i in range(len(number_list)):
    print(number_list[i])

# reverse
print("Your numbers reversed: ")
for i in reversed(number_list):
    print(i)



