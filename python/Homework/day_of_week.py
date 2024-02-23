def day_of_week(day):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    return switcher.get(day,"Invalid day")
def main():
    day = int(input("Enter day [0-6]: "))
    dow = day_of_week(day)
    print(dow)
main()
