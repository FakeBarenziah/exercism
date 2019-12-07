def convert(number):
    retStr = ""
    if number % 3 == 0:
        retStr = "Pling"
    if number % 5 == 0:
        retStr = "%sPlang" % retStr
    if number % 7 == 0:
        retStr = "%sPlong" % retStr
    if len(retStr) == 0:
        retStr = "%d" % number
    return retStr

