def calculate_gpa(grades:dict) -> float:
    """Calculate GPA"""
    total = 0
    for grade, counts in grades.items():
        if grade == "A":
            total += counts * 5 * 3
        elif grade == "B":
            total += counts * 4 * 3
        elif grade == "C":
            total += counts * 3 * 3
        elif grade == "D":
            total += counts * 2 * 3

    return total / (sum(grades.values()) * 3)

def honours(gpa:float) -> str:
    """Check if honours

    1st class: 4.4-5.0
    2nd class(upper division): 3.60 -  4.39
    2nd class (lower division): 2.80 - 3.59
    Pass: 2.2 - 2.79 """
    if gpa >= 4.4:
        return "1st class honours"
    elif gpa >= 3.6:
        return "2nd class (Upper Division)"
    elif gpa >= 2.8:
        return "2nd class (Lower Division)"
    else:
        return "PASS"

if __name__ == "__main__":
    years = int(input("How many years of data? "))
    grades = {}
    for year in range(1, years + 1):
        print("Year {}".format(year))
        for grade in "ABCD":
            count = int(input("How many {}'s in year {}? ".format(grade, year)))
            grades[grade] = grades.get(grade, 0) + count
    
    print(f"""Your GPA is: {calculate_gpa(grades)}
    Your honours status is: {honours(calculate_gpa(grades))}""")