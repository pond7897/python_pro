def num_to_month(num):
    switcher ={
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
    }
    return switcher.get(num,"None")

num = int(input("Enter number of Month (1 = January): "))

print(num_to_month(num))