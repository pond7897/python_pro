def calgrade(score):
    if score >= 80:
        return "A"
    elif 70 <= score < 80:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 50 <= score < 60:
        return "D"
    else:
        return "F"
def main():
    score = int(input("Score: "))
    grade = calgrade(score)
    print(grade)
main()
