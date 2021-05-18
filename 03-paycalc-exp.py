# Gets the user to input number of hours and payrate calculate pay
eHours = input("Enter Hours: ")
eRate = input("Enter Rate: ")
# The try and except has been used to capture data type errors.
# Important to note that 'execept requires an actual"exception" to
# catch the exception and comply with coding style guidance.
try:
    print("Pay:", float(eHours)*float(eRate))
except Exception:
    print("Incorrect data type")
