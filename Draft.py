print("FORM: a = Proper fraction\n      b = Improper Fraction\n      c = Mixed Fraction\n      d = Decimals\n      "
      "e = Ratio\n      f = Percentage")
unit = input("Fraction to ").lower()


#____________________________
# multiply with x10
def converter(num):
    divider = 1
    x = 1
    expon = 6
    unitt = " m"
    while len(num) > x:
        divider *= 10
        expon += 1
        x += 1
    result = int(num) / divider
    result_1 = int(num) * (1 * (10 ** 6))
    result_2 = round(result_1, 2)
    return (str(num) + " Torr = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(result_1) + unitt
            + " or " + str(result_2) + unitt)
return (converter(input("\nTorr (Torr) = ")).lower())

#------------------------------
# Simple
x = float(input("\nTorr (Torr) = "))
            result = x * 100
            result_2 = round(result, 2)
            unitt = " ha"
            return (str(x) + " Torr = " + str(result) + unitt + " or " + str(result_2) + unitt)

#--------------------------------
# divide with x10
def converter(num):
    divider = 1
    x = 1
    expon = 7
    unitt = " mi"
    formula = int(num) / (1 * (10 ** 6))
    limit = 3
    if len(num) < limit:
        while len(num) > x:
            divider *= 10
            expon -= 1
            x += 1
        result = int(num) / divider
        result_1 = formula
        return (str(num) + " psi = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
            result_1))
    elif len(num) >= limit:
        result_1 = formula
        return (str(num) + " psi = " + str(result_1) + unitt)
return (converter(input("\nPound-force per square inch (psi) = ")).lower())