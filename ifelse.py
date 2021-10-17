#short rev for if else n nested if
gradeslist = ["A","A-","B+","B","B-","C","D","F"]
while(True):
    marks = int(input("Enter marks: "))
    if marks > 90 and marks <= 100:
        print(f"Grade is {gradeslist[0]}")
        if marks == 100:
            print("Outstanding effort!!")
            break
    elif marks >= 85 and marks <= 90:
        print(f"Grade is {gradeslist[1]}")
        if marks == 90:
            print("Better luck for A next time!!")
            break
    elif marks >= 80 and marks < 85:
        print(f"Grade is {gradeslist[2]}")
    elif marks >= 70 and marks < 80:
        print(f"Grade is {gradeslist[3]}")
    elif marks >= 60 and marks < 70:
        print(f"Grade is {gradeslist[4]}")
    elif marks >= 50 and marks < 60:
        print(f"Grade is {gradeslist[5]}")
    elif marks >= 40 and marks < 50:
        print(f"Grade is {gradeslist[6]}")
    else:
        print(f"Grade is {gradeslist[7]}")

