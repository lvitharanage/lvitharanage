# this script extracts the portion of the string 'X-DSPAM-Confidence:0.8475'
# after the colon character and then use the float function to convert
# the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475 '
startPos = str.find('0')
endPos = str.find('5')
print(startPos, endPos)
# there is a quite accurate start and end posistion that accounts for
# spaces, however this is not required as float method could handle spaces.
numfloat = str[startPos:endPos+1]
print(type(numfloat))
numfloat = float(numfloat)
print(numfloat)
print(type(numfloat))
