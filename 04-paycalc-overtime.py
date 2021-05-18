# Gets the user to input number of hours and payrate calculate pay
# Where the the hours are above 40, 1.5 multiplier is applied to
# add overtime caluclation
eHours = input("Enter Hours: ")
eRate = input("Enter Pay Rate: ")
# The try and except has been used to capture data type errors.
# Important to note that 'execept requires an actual"exception" to
# catch the exception and comply with coding style guidance.
try:
    # Converts the input to float for use later and prevent errors
    eHoursFloat = float(eHours)
    eRateFloat = float(eRate)
    # Check if the hours are less than 40 and worksout
    # the pay rate if that is the case
    if eHoursFloat <= 40:
        print("Regular Pay (No Overtime):", float(eHours) * float(eRate))
    # worksout the Base Pay and Overtime Pay for instances where hours are
    # over 40
    elif eHoursFloat > 40:
        overtimeHours = float(eHoursFloat - 40)
        overtimeRate = float(eRateFloat * 1.5)
        basePay = float(40 * eRateFloat)
        overtimePay = float(overtimeHours * overtimeRate)
        print("Regular Pay:", basePay)
        print("Overtime Pay:", overtimePay)
        print("Total Pay:", basePay + overtimePay)
# prints out a message and a data type if user input is not an int or float
except Exception:
    print("incorrect data type/s:", " Hours", type(eHours),
          " Pay Rate", type(eRate))
