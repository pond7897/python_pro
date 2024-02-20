sold_computer = int(input("How many Computer were sold? ")) 
sold_monitor = int(input("How many Monitors were sold? ")) 
sold_printer = int(input("How many Printers were sold? ")) 

price_computer, price_moniter, price_printer = 30,8,12
sum = (price_computer*sold_computer)+(price_moniter*sold_monitor)+(price_printer*sold_printer)
tax = sum*0.7

print("%s %5s %12s" %("QTY", "DESCRIPTIONUNIT PRICE", "TOTAL PRICE"))
print("%s %5s %12s" %("-"*3, "-"*21, "-"*11))
print("%d %11s %11.2f %12.2f" %(sold_computer, "Computer", price_computer, (price_computer*sold_computer)))
print("%d %10s %12.2f %12.2f" %(sold_monitor, "Moniter", price_moniter, (price_moniter*sold_monitor)))
print("%d %10s %12.2f %12.2f" %(sold_printer, "Printer", price_printer, (price_printer*sold_printer)))
print("%39s" %("-"*7))
print("%28s %9.2f" %("SUBTOTAL", sum))
print("%23s %14.2f" %("TAX", sum*0.07))
print("%25s %12.2f" %("TOTAL", sum*0.93))
