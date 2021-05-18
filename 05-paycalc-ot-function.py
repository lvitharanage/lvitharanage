# Gets the user to input number of hours and payrate calculate pay
# Where the the hours are above 40, 1.5 multiplier is applied to
# add overtime caluclation using a function
# Function to carry out the calcualtions
def payCompute(hoursWorked, payRate):
    # The try and except has been used to capture data type errors.
    # Important to note that 'execept requires an actual"exception" to
    # catch the exception and comply with coding style guidance.
    try:
        # Converts the input to float for use later and prevent errors
        hoursWorkedFloat = float(hoursWorked)
        payRateFloat = float(payRate)
        # Check if the hours are less than 40 and worksout
        # the pay rate if that is the case
        if hoursWorkedFloat <= 40:
            nonOvertimePay = float(hoursWorkedFloat) * float(payRateFloat)
            print("Regular Pay (No Overtime): ", nonOvertimePay)
        # workout the Base Pay and Overtime Pay for instances where
        # hours are over 40
        elif hoursWorkedFloat > 40:
            overtimeHours = float(hoursWorkedFloat - 40)
            overtimeRate = float(payRateFloat * 1.5)
            basePay = float(40 * payRateFloat)
            overtimePay = float(overtimeHours * overtimeRate)
            print("Regular Pay:", basePay)
            print("Overtime Pay:", overtimePay)
            print("Total Pay:", basePay + overtimePay)
    # prints out a message and a data type if user input is not an int or float
    except Exception:
        typeHoursWorked = type(hoursWorked)
        typePayRate = type(payRate)
        print("incorrect data type/s:", "Hours", typeHoursWorked,
              "Pay Rate", typePayRate)


# Takes user input for hours and pay rates
eHours = input("Enter Hours: ")
eRate = input("Enter Pay Rate: ")

# function recall to compute the pay rates based on user input
payCompute(eHours, eRate)
