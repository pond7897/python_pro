def inchtoCenti(inch):
    centi = inch * 2.54
    return centi
def main():
    inch = int(input("Enter inch: "))
    centi = inchtoCenti(inch)
    print("Inch: %d, Centimeters: %.2f" %(inch,centi))
main()
