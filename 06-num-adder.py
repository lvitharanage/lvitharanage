# This programme repeatedly reads the numbers entered by the user
# until user enters the word 'done'. It all so error checks using 'try'
# and 'except' to catch any non-integer or float values.
# at the end user are presnetd with total, count and average of numbers entered

# Sets the number counter and sum to zero before starting while loop
numCount = 0
uNumberSum = 0
while True:
    uNumber = input("Please enter a number or 'done' to end: ")
    # check to see if user input is 'done' and prints out the
    # sum, count and average before exiting the loop
    # it is possible to use Python isinstance() to verify
    # user input type here.
    # Used str.casefold() function to convert user input to lowercase
    # for caseless matching
    if uNumber.casefold() == "done":
        print("Sum of the Numbers:", uNumberSum)
        print("Number Count:", numCount)
        # try and except has been used here to manage zero division errors
        # this happens when a user type 'done' without entering any numbers
        try:
            print("Average:", uNumberSum/numCount)
        except Exception:
            print("Average: Cannot be calculated, Zero Division Error")
        break
    # this section continue the loop adding each user input and
    # counting the numbers entered. Try and except has been used
    # to manage instnaces of user inputting inccorect data type
    else:
        try:
            uNumberSum = float(uNumber) + float(uNumberSum)
            numCount = float(numCount) + 1
            # This can be used to print the running total if needed
            # print("Running Total:", uNumberSum)
        except Exception:
            print("Type Error, Integer or Float expcted recived",
                  type(uNumber))
        continue
