year = int(input("Please enter a year: "))  # Enter a year

months = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a Leap year.")
                return True
            else:
                print("This is NOT a leap year.")
                return False
        else:
            print("This is a Leap year.")
            return True
    else:
        print("This is NOT a leap year.")
        return False

leap = is_leap(year)
print(f"Leap is {leap}")
if leap:
    print("Verified: It is definitely a leap year.")
    counter = 1
elif not leap:
    print("Verified: It is definitely NOT a leap year.")
    counter = 0

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(f"Normally, {months[month]} has {(int(month_days[month-1]))} days in it.")
    if leap and month == 2:
        print(f"But because it's a leap year, {months[month]} has {(int(month_days[month - 1] + counter))} days in it that year.")


days_in_month(year, int(input("Please enter a month (1-12): ")))
													  # Enter a month