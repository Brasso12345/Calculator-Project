def calculator(operation):
    if operation == "a":
        print("\nMODE: NORMAL\n\"=\" = calculate\n\"**\" = \"^\"")
        calc = input("Type calculation: \n".upper())
        operation = input().upper()
        if operation == "=":
            print("Answer: " + str(eval(calc)))
        elif calc or operation == "CA":
            print("Goodbye~")
        else:
            print("Error!")
    elif operation == "b":
        print("\nMODE: SEQUENCE\nSequences: a = Arithmetic\n           b = Geometric\n           "
              "c = Fibonacci")
        type = input("Type of Sequence: ".lower())
        if type == "a":
            print("\nTYPE: ARITHMETIC CALCULATOR")
            def arithmetic_operation(ops):
                i = 1
                if ops == "a":
                    print("From a1 to an:")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    d = float(input("d = "))
                    print("From a1 to a" + str(an) + ":")
                    while i != an:
                        print("a" + str(i) + " = " + str(a1))
                        a1 += d
                        i += 1
                    return "a" + str(i) + " = " + str(a1)
                elif ops == "b":
                    print("Finding the nth term:")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    d = float(input("d = "))
                    while i != an:
                        a1 += d
                        i += 1
                    return "a" + str(i) + " = " + str(a1)
                elif ops == "c":
                    print("Finding the sum of all terms:")
                    print("Sn = ([a1 + an] / 2) n")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    print("\nS" + str(an) + " = ([(" + str(a1) + ") + a" + str(an) + "]) / 2) " + str(an))
                    a_n = float(input("a" + str(an) + " = "))
                    result = ((a1 + a_n) / 2) * an
                    return ("S" + str(an) + " = " + str(result))
                elif ops == "d":
                    print("Finding the common difference: ")
                    print("d = (ay - ax)/(y - x)")
                    y = int(input("y = "))
                    x = int(input("x = "))
                    print("d = (a" + str(y) + " - a" + str(x) + ")/(" + str(y) + " - " + str(x) + ")")
                    ay = float(input("a" + str(y) + " = "))
                    ax = float(input("a" + str(x) + " = "))
                    result = (ay - ax) / (y - x)
                    return "d = " + str(result)
                elif ops == "e":
                    print("Finding the Arithmetic Mean:")
                    print("m = (a + b) / 2")
                    a = float(input("a = "))
                    b = float(input("b = "))
                    result = (a + b) / 2
                    return "m = " + str(result)
                else:
                    return "Error!"
            print("APP: a = From 1st term to nth term\n     "
                  "b = Find the nth term\n     "
                  "c = Sum of all terms\n     "
                  "d = Find the common difference\n     "
                  "e = Arithmetic Mean\n")
            print(arithmetic_operation(input("Enter application: ").lower()))
        elif type == "b":
            print("\nTYPE: GEOMETRIC CALCULATOR")
            def geometric_operation(ops):
                i = 1
                if ops == "a":
                    print("From a1 to an:")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    r = float(input("r = "))
                    return ("From a1 to a" + str(an) + ":")
                    while i != an:
                        print("a" + str(i) + " = " + str(a1))
                        a1 *= r
                        i += 1
                    return ("a" + str(i) + " = " + str(a1))
                elif ops == "b":
                    print("Finding the nth term:")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    r = float(input("r = "))
                    while i != an:
                        a1 *= r
                        i += 1
                    return ("a" + str(i) + " = " + str(a1))
                elif ops == "c":
                    print("Finding the sum of all terms:")
                    print("Sn = (a1 [1 - r^n]) / (1 - r)")
                    a1 = float(input("a1 = "))
                    an = int(input("n = "))
                    r = float(input("r = "))
                    result = (a1 * (1 - r ** an)) / (1 - r)
                    return ("S" + str(n) + " = " + str(result))
                elif ops == "d":
                    print("Finding the common ratio: ")
                    print("r^(y - x) = ay / ax")
                    y = int(input("y = "))
                    x = int(input("x = "))
                    print("r^([" + str(y) + "] - [" + str(x) + "]) = a" + str(y) + " / a" + str(x))
                    ay = float(input("a" + str(y) + " = "))
                    ax = float(input("a" + str(x) + " = "))
                    result = (ay / ax) ** (1 / (y - x))
                    return ("r = " + str(result))
                elif ops == "e":
                    print("Finding the Geometric Mean:")
                    print("m = √a*b")
                    a = float(input("a = "))
                    b = float(input("b = "))
                    result = (a * b) ** (1 / 2)
                    return ("m = " + str(result))
                else:
                    return "Error!"
            print("APP: a = From 1st term to nth term\n     "
                  "b = Find the nth term\n     "
                  "c = Sum of all terms\n     "
                  "d = Find the common ratio\n     "
                  "e = Find the Geometric Mean\n")
            print(geometric_operation(input("Enter application: ").lower()))
        elif type == "c":
            print("\nTYPE: FIBONACCI CALCULATOR: ")
            def fibonacci_operation(ops):
                i = 0
                if ops == "a":
                    print("From f0 to fn:")
                    fn = int(input("fn = "))
                    while i <= fn:
                        result = (((1 + (5 ** (1 / 2))) ** i) - ((1 - (5 ** (1 / 2))) ** i)) / (
                                    (2 ** i) * (5 ** (1 / 2)))
                        print("f" + str(i) + " = " + str(round(result)))
                        i += 1
                    return "Done with calculation"
                elif ops == "b":
                    print("From fx to fy:")
                    fx = int(input("fx = "))
                    fy = int(input("fy = "))
                    while fx <= fy:
                        result = (((1 + (5 ** (1 / 2))) ** fx) - ((1 - (5 ** (1 / 2))) ** fx)) / (
                                    (2 ** fx) * (5 ** (1 / 2)))
                        print("f" + str(fx) + " = " + str(round(result)))
                        fx += 1
                    return "Done with calculation"
                elif ops == "c":
                    print("Finding the nth term: ")
                    fn = int(input("fn = "))
                    result = (((1 + (5 ** (1 / 2))) ** fn) - ((1 - (5 ** (1 / 2))) ** fn)) / (
                                (2 ** fn) * (5 ** (1 / 2)))
                    return ("f" + str(fn) + " = " + str(round(result)))
                elif ops == "d":
                    print("Finding the Summation of terms from f0 to fn:")
                    print("Sn = f(n+2) - 1")
                    fn = int(input("n = "))
                    while i <= fn + 2:
                        fn_plus_2 = (((1 + (5 ** (1 / 2))) ** i) - ((1 - (5 ** (1 / 2))) ** i)) / (
                                    (2 ** i) * (5 ** (1 / 2)))
                        i += 1
                    Sn = int(fn_plus_2) - 1
                    return ("S" + str(fn) + " = " + str(Sn))
                elif ops == "e":
                    print("Finding the Summation of terms from fx to fy")
                    x = int(input("fx = "))
                    y = int(input("fy = "))
                    fx = x
                    new_fx = 0
                    while x <= y:
                        prev_fx = (((1 + (5 ** (1 / 2))) ** x) - ((1 - (5 ** (1 / 2))) ** x)) / (
                                    (2 ** x) * (5 ** (1 / 2)))
                        new_fx = new_fx + prev_fx
                        x += 1
                    result = round(new_fx)
                    return ("The Summation of terms from f" + str(fx) + " to f" + str(y) + " is: " + str(result))

            print("APP: a = From 0th term to nth term\n     "
                  "b = From xth term to yth term\n     "
                  "c = Find the nth term\n     "
                  "d = Find the Summation of terms from f0 to fn\n     "
                  "e = Find the Summation of terms from fx to fy\n")
            print(fibonacci_operation(input("Enter application: ").lower()))
    elif operation == "c":
        print("\nMODE: CONVERSION")
        print("Application: a = Area\n             "
              "b = Length/ Distance\n             c = Capacity/ Volume \n             "
              "d = Speed\n             e = Energy/ Power\n             "
              "f = Temperature\n             g = Weight\n             "
              "h = Pressure\n             i = Rational Number\n             "
              "j = Data Transfer Rate\n             k = Digital Storage\n             "
              "l = Frequency\n             m = Fuel Economy\n             "
              "n = Plane Angle")
        app = input("Enter application = ")
        if app == "a":
            def area_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square kilometre (km^2) to ").lower()
                    if unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " m^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare kilometre (km^2) = ")).lower())
                    elif unit == "c":
                        x = float(input("\nSquare kilometre (km^2) = "))
                        result = x / 2.59
                        result_2 = round(result, 2)
                        unitt = " mi^2"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " sq yd"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = (int(num) * 1.196) / divider
                            result_1 = int(num) * (1.196 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare kilometre (km^2) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " ft^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = (int(num) * 1.076) / divider
                            result_1 = int(num) * (1.196 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare kilometre (km^2) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " in^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = (int(num) * 1.55) / divider
                            result_1 = int(num) * (1.55 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare kilometre (km^2) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nSquare kilometre (km^2) = "))
                        result = x * 100
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nSquare kilometre (km^2) = "))
                        result = x * 247.105
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Square kilometre (km^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square metre (m^2) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " km^2"
                            if len(num) < 3:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = int(num) * (1 * (10 ** 6))
                                return (str(num) + " km^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 3:
                                result_1 = int(num) / (1 * (10 ** 6))
                                return (str(num) + " km^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare metre (m^2) = ")).lower())
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " mi^2"
                            formula = int(num) / (2.59 * (10 ** 6))
                            if len(num) < 3:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " km^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 3:
                                result_1 = formula
                                return (str(num) + " km^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare metre (m^2) = ")).lower())
                    elif unit == "d":
                        x = float(input("\nSquare metre (m^2) = "))
                        result = x * 1.196
                        result_2 = round(result, 2)
                        unitt = " sq yd"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nSquare metre (m^2) = "))
                        result = x * 10.764
                        result_2 = round(result, 2)
                        unitt = " ft^2"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nSquare metre (m^2) = "))
                        result = x * 1550
                        result_2 = round(result, 2)
                        unitt = " in^2"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nSquare metre (m^2) = "))
                        result = x / 10000
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nSquare metre (m^2) = "))
                        result = x / 4047
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " km^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square mile (mi^2) to ").lower()
                    if unit == "a":
                        result = x * 2.59
                        result_2 = round(result, 2)
                        unitt = " km^2"
                        return (str(x) + " mi^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " m^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.59 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare mile (mi^2) = ")).lower())
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " m^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare mile (mi^2) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " ft^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.788 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare mile (mi^2) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " in^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (4.014 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi^2 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nSquare mile (mi^2) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nSquare mi (mi^2) = "))
                        result = x * 258.999
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " mi^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nSquare mi (mi^2) = "))
                        result = x * 640
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " mi^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square yard (sq yd) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " km^2"
                            formula = int(num) / (1.96 * (10 ** 6))
                            if len(num) < 3:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " sq yd = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 3:
                                result_1 = formula
                                return (str(num) + " sq yd = " + str(result_1) + unitt)

                        return (converter(input("\nSquare yard (sq yd) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nSquare yard (sq yd) = "))
                        result = x / 1.196
                        result_2 = round(result, 2)
                        unitt = " m^2"
                        return (str(x) + " sq yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " mi^2"
                            formula = int(num) / (3.098 * (10 ** 6))
                            if len(num) < 3:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " sq yd = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 3:
                                result_1 = formula
                                return (str(num) + " sq yd = " + str(result_1) + unitt)

                        return (converter(input("\nSquare yard (sq yd) = ")).lower())
                    elif unit == "e":
                        x = float(input("\nSquare yard (sq yd) = "))
                        result = x * 9
                        result_2 = round(result, 2)
                        unitt = " ft^2"
                        return (str(x) + " sq yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nSquare yard (sq yd) = "))
                        result = x * 1296
                        result_2 = round(result, 2)
                        unitt = " in^2"
                        return (str(x) + " sq yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nSquare yard (sq yd) = "))
                        result = x / 11960
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " sq yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nSquare yard (sq yd) = "))
                        result = x / 4840
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " sq yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square foot (ft^2) to ").lower()
                    if unit == "a":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x / (1.076 * (10 ** 7))
                        result_2 = round(result, 2)
                        unitt = " km^2"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x / 10.764
                        result_2 = round(result, 2)
                        unitt = " m^2"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " mi^2"
                            formula = int(num) / (2.788 * (10 ** 7))
                            if len(num) < 3:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " ft^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 3:
                                result_1 = formula
                                return (str(num) + " ft^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare foot (ft^2) = ")).lower())
                    elif unit == "d":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x / 9
                        result_2 = round(result, 2)
                        unitt = " sq yd"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x * 144
                        result_2 = round(result, 2)
                        unitt = " in^2"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x / 107639
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nSquare foot (ft^2) = "))
                        result = x / 43560
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " ft^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "f":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      "
                          "g = Hectare (ha)\n      h = Acre (ac)")
                    unit = input("Square inch (in^2) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " km^2"
                            formula = int(num) / (1.55 * (10 ** 9))
                            if len(num) < 7:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 7:
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare inch (in^2) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nSquare inch (in^2) = "))
                        result = x / 1550
                        result_2 = round(result, 2)
                        unitt = " m^2"
                        return (str(x) + " in^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " mi^2"
                            formula = int(num) / (4.014 * (10 ** 9))
                            if len(num) < 7:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 7:
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare inch (in^2) = ")).lower())
                    elif unit == "d":
                        x = float(input("\nSquare inch (in^2) = "))
                        result = x / 1296
                        result_2 = round(result, 2)
                        unitt = " sq yd"
                        return (str(x) + " in^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nSquare inch (in^2) = "))
                        result = x / 144
                        result_2 = round(result, 2)
                        unitt = " ft^2"
                        return (str(x) + " in^2 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " ha"
                            formula = int(num) / (1.55 * (10 ** 7))
                            if len(num) < 5:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= 5:
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare inch (in^2) = ")).lower())
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " ac"
                            formula = int(num) / (6.273 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " in^2 = " + str(result_1) + unitt)

                        return (converter(input("\nSquare inch (in^2) = ")).lower())
                elif ops == "g":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "h = Acre (ac)")
                    unit = input("Hectare (ha) to ").lower()
                    if unit == "a":
                        x = float(input("\nHectare (ha) = "))
                        result = x / 100
                        result_2 = round(result, 2)
                        unitt = " km^2"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nHectare (ha) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " m^2"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nHectare (ha) = "))
                        result = x / 259
                        result_2 = round(result, 2)
                        unitt = " mi^2"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nHectare (ha) = "))
                        result = x * 11960
                        result_2 = round(result, 2)
                        unitt = " sq yd"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nHectare (ha) = "))
                        result = x * 107639
                        result_2 = round(result, 2)
                        unitt = " ft^2"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " in^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.55 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " ha = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nHectare (ha) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nHectare (ha) = "))
                        result = x * 2.471
                        result_2 = round(result, 2)
                        unitt = " ac"
                        return (str(x) + " ha = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "h":
                    print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                          "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                          "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                          "g = Hectare (ha)\n      ")
                    unit = input("Acre (ac) to ").lower()
                    if unit == "a":
                        x = float(input("\nAcre (ac) = "))
                        result = x / 247
                        result_2 = round(result, 2)
                        unitt = " km^2"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nAcre (ac) = "))
                        result = x * 4047
                        result_2 = round(result, 2)
                        unitt = " m^2"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nAcre (ac) = "))
                        result = x / 640
                        result_2 = round(result, 2)
                        unitt = " mi^2"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nAcre (ac) = "))
                        result = x * 4840
                        result_2 = round(result, 2)
                        unitt = " sq yd"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nAcre (ac) = "))
                        result = x * 43560
                        result_2 = round(result, 2)
                        unitt = " ft^2"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " in^2"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (6.273 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " ac = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nAcre (ac) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nAcre (ac) = "))
                        result = x / 2.471
                        result_2 = round(result, 2)
                        unitt = " ha"
                        return (str(x) + " ac = " + str(result) + unitt + " or " + str(result_2) + unitt)
            print("UNIT: a = Square kilometre (km^2)\n      b = Square metre (m^2)\n      "
                  "c = Square mile (mi^2)\n      d = Square yard (sq yd)\n      "
                  "e = Square foot (ft^2)\n      f = Square inch (in^2)\n      "
                  "g = Hectare (ha)\n      h = Acre (ac)")
            print(area_conversion(input("Unit = ").lower()))
        elif app == "b":
            def length_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Kilometre (km) to ").lower()
                    if unit == "b":
                        x = float(input("\nKilometre (km) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilometre (km) = "))
                        result = x * 100000
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilometre (km) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " μm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilometre (km) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 12))
                            result_2 = round(result_1, 2)
                            return (str(num) + " km = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilometre (km) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nKilometre (km) = "))
                        result = x / 1.609
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nKilometre (km) = "))
                        result = x * 1094
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nKilometre (km) = "))
                        result = x * 3281
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nKilometre (km) = "))
                        result = x * 39370
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nKilometre (km) = "))
                        result = x / 1.852
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " km = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Kilometre (km)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Metre (m) to ").lower()
                    if unit == "a":
                        x = float(input("\nMetre (m) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nMetre (m) = "))
                        result = x * 100
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nMetre (m) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " mm"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " μm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " m = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMetre (m) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " m = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMetre (m) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nMetre (m) = "))
                        result = x / 1609
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nMetre (m) = "))
                        result = x * 1.094
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nMetre (m) = "))
                        result = x * 3.281
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nMetre (m) = "))
                        result = x * 39.37
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nMetre (m) = "))
                        result = x / 1852
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " m = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Centimetre (cm) to ").lower()
                    if unit == "a":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 100000
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x * 10
                        result_2 = round(result, 2)
                        unitt = " mm"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x * 10000
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " cm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nCentimetre (cm) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 160934
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 91.44
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 30.48
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 2.54
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x / 185200
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " cm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Millimetre (mm) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " km"
                            formula = int(num) / (2.59 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mm = " + str(result_1) + unitt)

                        return (converter(input("\nMillimetre (mm) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nMillimetre (mm) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nMillimetre (mm) = "))
                        result = x / 10
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nCentimetre (cm) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMillimetre (mm) = ")).lower())
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " mi"
                            formula = int(num) / (1.609 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mm = " + str(result_1) + unitt)

                        return (converter(input("\nMillimetre (mm) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nMillimetre (mm) = "))
                        result = x / 914
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nMillimetre (mm) = "))
                        result = x / 305
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nMillimetre (mm) = "))
                        result = x / 25.4
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " mm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " nmi"
                            formula = int(num) / (1.852 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mm = " + str(result_1) + unitt)

                        return (converter(input("\nMillimetre (mm) = ")).lower())
                elif ops == "e":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Micrometre (μm) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " km"
                            formula = int(num) / (1 * (10 ** 9))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μm = " + str(result_1) + unitt)

                        return (converter(input("\nMicrometre (μm) = ")).lower())
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " m"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μm = " + str(result_1) + unitt)

                        return (converter(input("\nMicrometre (μm) = ")).lower())
                    elif unit == "c":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x / 10000
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " mm"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " nm"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " mi"
                            formula = int(num) / (1.609 * (10 ** 9))
                            limit = 7
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μm = " + str(result_1) + unitt)

                        return (converter(input("\nMicrometre (μm) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x / 914400
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x / 304800
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nMicrometre (μm) = "))
                        result = x / 25400
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " μm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " nmi"
                            formula = int(num) / (1.852 * (10 ** 9))
                            limit = 7
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μm = " + str(result_1) + unitt)

                        return (converter(input("\nMicrometre (μm) = ")).lower())
                elif ops == "f":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Nanometre (nm) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " km"
                            formula = int(num) / (1 * (10 ** 12))
                            limit = 9
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " m"
                            formula = int(num) / (1 * (10 ** 9))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " cm"
                            formula = int(num) / (1 * (10 ** 7))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mm"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "e":
                        x = float(input("\nNanometre (nm) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " nm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 13
                            unitt = " mi"
                            formula = int(num) / (1.609 * (10 ** 12))
                            limit = 10
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " yd"
                            formula = int(num) / (9.144 * (10 ** 8))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " ft"
                            formula = int(num) / (3.048 * (10 ** 8))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " in"
                            formula = int(num) / (2.54 * (10 ** 7))
                            limit = 5
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                    elif unit == "k":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 13
                            unitt = " nmi"
                            formula = int(num) / (1.852 * (10 ** 12))
                            limit = 10
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " nm = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " nm = " + str(result_1) + unitt)

                        return (converter(input("\nNanometre (nm) = ")).lower())
                elif ops == "g":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Mile (mi) to ").lower()
                    if unit == "a":
                        x = float(input("\nMile (mi) = "))
                        result = x * 1.609
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nMile (mi) = "))
                        result = x * 1609.34
                        result_2 = round(result)
                        unitt = " m"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nMile (mi) = "))
                        result = x * 160934
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.609 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMile (mi) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " μm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.609 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMile (mi) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.609 * (10 ** 12))
                            result_2 = round(result_1, 2)
                            return (str(num) + " mi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nMile (mi) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nMile (mi) = "))
                        result = x * 1760
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nMile (mi) = "))
                        result = x * 5280
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nMile (mi) = "))
                        result = x * 63360
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nMile (mi) = "))
                        result = x / 1.151
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "h":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      "
                          "i = Foot (ft)\n      j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Yard (yd) to ").lower()
                    if unit == "a":
                        x = float(input("\nMile (mi) = "))
                        result = x / 1094
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " mi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nYard (yd) = "))
                        result = x / 1.094
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nYard (yd) = "))
                        result = x * 91.44
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nYard (yd) = "))
                        result = x * 914
                        result_2 = round(result, 2)
                        unitt = " mm"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nYard (yd) = "))
                        result = x * 914400
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.144 * (10 ** 8))
                            result_2 = round(result_1, 2)
                            return (str(num) + " yd = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nYard (yd) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nYard (yd) = "))
                        result = x / 1760
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nYard (yd) = "))
                        result = x * 3
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nYard (yd) = "))
                        result = x * 36
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nYard (yd) = "))
                        result = x / 2025
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " yd = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "i":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "j = Inch (in)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Feet (ft) to ").lower()
                    if unit == "a":
                        x = float(input("\nFoot (ft) = "))
                        result = x / 3281
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nFoot (ft) = "))
                        result = x / 3.281
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nFoot (ft) = "))
                        result = x * 30.48
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nFoot (ft) = "))
                        result = x * 304.8
                        result_2 = round(result)
                        unitt = " mm"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nFoot (ft) = "))
                        result = x * 304800
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (3.048 * (10 ** 8))
                            result_2 = round(result_1, 2)
                            return (str(num) + " ft = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nFoot (ft) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nFoot (ft) = "))
                        result = x / 5280
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nFoot (ft) = "))
                        result = x / 3
                        result_2 = round(result, 2)
                        unitt = " yd"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nFoot (ft) = "))
                        result = x * 12
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nFoot (ft) = "))
                        result = x / 6076
                        result_2 = round(result, 2)
                        unitt = " nm"
                        return (str(x) + " ft = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "j":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      "
                          "k = Nautical mile (nmi)")
                    unit = input("Inch (in) to ").lower()
                    if unit == "a":
                        x = float(input("\nInch (in) = "))
                        result = x / 39370
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nInch (in) = "))
                        result = x / 39.37
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nInch (in) = "))
                        result = x * 2.54
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nInch (in) = "))
                        result = x * 25.4
                        result_2 = round(result, 2)
                        unitt = " mm"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nInch (in) = "))
                        result = x * 25400
                        result_2 = round(result, 2)
                        unitt = " μm"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.54 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " in = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nInch (in) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nInch (in) = "))
                        result = x / 63360
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nInch (in) = "))
                        result = x / 36
                        result_2 = round(result, 2)
                        unitt = " in"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nInch (in) = "))
                        result = x / 12
                        result_2 = round(result, 2)
                        unitt = " ft"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nInch (in) = "))
                        result = x / 72913
                        result_2 = round(result, 2)
                        unitt = " nmi"
                        return (str(x) + " in = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "k":
                    print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                          "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                          "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                          "g = Mile (mi)\n      h = Yard (yd)\n      "
                          "i = Foot (ft)\n      j = Inch (in)")
                    unit = input("Nautical mile (nmi) to ").lower()
                    if unit == "a":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 1.852
                        result_2 = round(result, 2)
                        unitt = " km"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 1852
                        result_2 = round(result, 2)
                        unitt = " m"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 185200
                        result_2 = round(result, 2)
                        unitt = " cm"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.852 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " nmi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nNautical mile (nmi) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " μm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.852 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " nmi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nNautical mile (nmi) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " nm"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.852 * (10 ** 12))
                            result_2 = round(result_1, 2)
                            return (str(num) + " nmi = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nNautical mile (nmi) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 1.151
                        result_2 = round(result, 2)
                        unitt = " mi"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 2025.37
                        result_2 = round(result)
                        unitt = " yd"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 6076.12
                        result_2 = round(result)
                        unitt = " ft"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nNautical mile (nmi) = "))
                        result = x * 72913.4
                        result_2 = round(result)
                        unitt = " in"
                        return (str(x) + " nmi = " + str(result) + unitt + " or " + str(result_2) + unitt)

            print("UNIT: a = Kilometre (km)\n      b = Metre (m)\n      "
                  "c = Centimetre (cm)\n      d = Millimetre (mm)\n      "
                  "e = Micrometre (μm)\n      f = Nanometre (nm)\n      "
                  "g = Mile (mi)\n      h = Yard (yd)\n      "
                  "i = Foot (ft)\n      j = Inch (in)\n      "
                  "k = Nautical mile (nmi)")
            print(length_conversion(input("Unit = ")))
        elif app == "c":
            def volume_conversion(ops):
                if ops == "a":
                    print("UNIT: b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US liquid gallon (US gal) to ").lower()
                    if unit == "b":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 4
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 8
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 15.7725
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 128
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 256
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 768
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x / 264
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 3.78541
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 3785.41
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 3.331
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 6.66139
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 13.3228
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 133.228
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 213.165
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 639.494
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x / 7.481
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS liquid gallon (US gal) = "))
                        result = x * 231
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = US liquid gallon (US gal)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US liquid quart (US qt) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x / 4
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 2
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 3.94314
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 32
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 64
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 192
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x / 1057
                        result_2 = round(result)
                        unitt = " m^3"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x / 1.057
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 946.353
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x / 4.804
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x / 1.201
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 1.66535
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 3.3307
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 33.307
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 53.2911
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 159.873
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 29.922
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS liquid quart (US qt) = "))
                        result = x * 57.75
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US liquid pint (US p) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 8
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 2
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 1.97157
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 16
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 32
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 96
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 2113
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 2.113
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 473.176
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 9.608
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 2.402
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 1.201
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 1.66535
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 16.6535
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 26.6456
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 79.9367
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x / 59.844
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS liquid pint (US p) = "))
                        result = x * 28.875
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US legal cup (US c) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 15.773
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 3.943
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 1.972
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 8.11537
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 16.2307
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 48.6922
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 4167
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 4.167
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 240
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 18.942
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 4.736
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 2.368
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 1.184
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 8.44682
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 13.5149
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 40.5447
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x / 118
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS legal cup (US c) = "))
                        result = x * 14.6457
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US fluid ounce (US oz) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 128
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 32
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 16
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 8.115
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 2
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 6
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 33814
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 33.814
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 29.574
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 154
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 38.43
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 19.215
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 9.608
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 1.04084
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 1.66535
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 4.99604
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x / 958
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS fluid ounce (US oz) = "))
                        result = x * 1.80469
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "f":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US tablespoon (US tbsp) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 256
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 64
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 32
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 16.231
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 2
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x * 3
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 67628
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 67.628
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x * 14.7868
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 307
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 76.861
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 38.43
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 19.215
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 1.922
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 1.201
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x * 2.49802
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 1915
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS tablespoon (US tbsp) = "))
                        result = x / 1.108
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "g":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("US teaspoon (US tsp) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 768
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 192
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 96
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 48.692
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 6
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 3
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 202884
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 203
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x * 4.929
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 922
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 231
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 115
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 57.646
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 5.765
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 3.603
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 1.201
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 5745
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nUS teaspoon (US tsp) = "))
                        result = x / 3.325
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " US tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "h":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Cubic metre (m^3) to ").lower()
                    if unit == "a":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 264.172
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 1056.69
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 2113.38
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 4166.67
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 33814
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 67628
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 202884
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mL"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " m^3 = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nCubic metre (m^3) = ")).lower())
                    elif unit == "k":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 219.969
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 879.877
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 1759.75
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 3519.51
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 35195.1
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 56312.1
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 168936
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 35.3147
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nCubic metre (US m^3) = "))
                        result = x * 61023.7
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " m^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "i":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Litre (L) to ").lower()
                    if unit == "a":
                        x = float(input("\nLitre (L) = "))
                        result = x / 3.785
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nLitre (L) = "))
                        result = x * 1.05669
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nLitre (L) = "))
                        result = x * 2.11338
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nLitre (L) = "))
                        result = x * 4.16667
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nLitre (L) = "))
                        result = x * 33.814
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nLitre (L) = "))
                        result = x * 67.628
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nLitre (L) = "))
                        result = x * 202.884
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nLitre (L) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nLitre (L) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nLitre (L) = "))
                        result = x / 4.546
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nLitre (L) = "))
                        result = x / 1.137
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nLitre (L) = "))
                        result = x * 1.75975
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nLitre (L) = "))
                        result = x * 3.51951
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nLitre (L) = "))
                        result = x * 35.1951
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nLitre (L) = "))
                        result = x * 56.3121
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nLitre (L) = "))
                        result = x * 168.936
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nLitre (L) = "))
                        result = x / 28.317
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nLitre (L) = "))
                        result = x * 61.0237
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " L = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "j":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Millilitre (mL) to ").lower()
                    if unit == "a":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 3785
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 946
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 473
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 240
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 29.574
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 14.787
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 4.929
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " m^3"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mL = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mL = " + str(result_1) + unitt)

                        return (converter(input("\nMillilitre (mL) = ")).lower())
                    elif unit == "i":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 4546
                        result_2 = round(result)
                        unitt = " Imp. gal"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 1137
                        result_2 = round(result)
                        unitt = " Imp. qt"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 568
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 284
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 28.413
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 17.758
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 5.919
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 28317
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nMillilitre (mL) = "))
                        result = x / 16.387
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " mL = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "k":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial gallon (Imp. gal) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 4.804
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 9.608
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 18.942
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 154
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 307
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 922
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x / 220
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 4.546
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 4546
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 4
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 8
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 16
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 160
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 256
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 768
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x / 6.229
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial gallon (Imp. gal) = "))
                        result = x * 277
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. gal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "l":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial quart (Imp. qt) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x / 3.331
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 2.402
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 4.736
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 38.43
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 76.861
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 231
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x / 880
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 1.137
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 1137
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x / 4
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 2
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 4
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 40
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 64
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 192
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x / 24.915
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial quart (Imp. qt) = "))
                        result = x * 69.355
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. qt = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "m":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial pint (Imp. p) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 6.661
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 1.665
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 2.368
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 19.215
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 38.43
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 115
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 1760
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 1.76
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 568
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 8
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 2
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 2
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 20
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 32
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 96
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x / 49.831
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial pint (Imp. p) = "))
                        result = x * 34.677
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. p = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "n":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial cup (Imp. c) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 13.323
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 3.331
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 1.665
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 1.184
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 9.608
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 19.215
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 57.646
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 3520
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 3.52
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 284
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 16
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 4
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 2
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 10
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 16
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 48
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x / 99.661
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial cup (Imp. c) = "))
                        result = x * 17.339
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. c = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "o":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial fluid ounce (Imp. oz) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 133
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 33.307
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 16.653
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 8.447
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 1.041
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 1.922
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 5.765
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 35195
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 35.195
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 28.413
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 160
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 40
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 20
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 10
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 1.6
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 4.8
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x / 997
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial fluid ounce (Imp. oz) = "))
                        result = x * 1.734
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "p":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial tablespoon (Imp. tbsp) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 213
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 53.291
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 26.646
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 13.515
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 1.665
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x * 3.603
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 56312
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 56.312
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x * 17.758
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 256
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 64
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 32
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 16
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 1.6
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x * 3
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x / 1595
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial tablespoon (Imp. tbsp) = "))
                        result = x * 1.084
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. tbsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "q":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "r = Cubic foot (ft^3)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Imperial teaspoon (Imp. tsp) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 639
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 160
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 79.937
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 40.545
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 4.996
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 2.498
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x * 1.201
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 168936
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 169
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x * 5.919
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 768
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 192
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 96
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 48
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 4.8
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 3
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 4784
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nImperial teaspoon (Imp. tsp) = "))
                        result = x / 2.768
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " Imp. tsp = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "r":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      "
                          "s = Cubic inch (in^3)")
                    unit = input("Cubic foot (ft^3) to ").lower()
                    if unit == "a":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 7.481
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 29.922
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 59.844
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 118
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 958
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 1915
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 5745
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x / 35.315
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 28.317
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 28317
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 6.229
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 24.915
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 49.831
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 99.661
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 997
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 1595
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 4784
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "s":
                        x = float(input("\nCubic foot (ft^3) = "))
                        result = x * 1728
                        result_2 = round(result, 2)
                        unitt = " in^3"
                        return (str(x) + " ft^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "s":
                    print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                          "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                          "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                          "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                          "i = Litre (L)\n      j = Millilitre (mL)\n      "
                          "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                          "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                          "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                          "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      ")
                    unit = input("Cubic inch (in^3) to ").lower()
                    if unit == "a":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 231
                        result_2 = round(result, 2)
                        unitt = " US gal"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 57.75
                        result_2 = round(result, 2)
                        unitt = " US qt"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 28.875
                        result_2 = round(result, 2)
                        unitt = " US p"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 14.646
                        result_2 = round(result, 2)
                        unitt = " US c"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 1.805
                        result_2 = round(result, 2)
                        unitt = " US oz"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x * 1.108
                        result_2 = round(result, 2)
                        unitt = " US tbsp"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x * 3.325
                        result_2 = round(result, 2)
                        unitt = " US tsp"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 61024
                        result_2 = round(result, 2)
                        unitt = " m^3"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 61.024
                        result_2 = round(result, 2)
                        unitt = " L"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x * 16.387
                        result_2 = round(result, 2)
                        unitt = " mL"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "k":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 277
                        result_2 = round(result, 2)
                        unitt = " Imp. gal"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "l":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 69.355
                        result_2 = round(result, 2)
                        unitt = " Imp. qt"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "m":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 34.677
                        result_2 = round(result, 2)
                        unitt = " Imp. p"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "n":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 17.339
                        result_2 = round(result, 2)
                        unitt = " Imp. c"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "o":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 1.734
                        result_2 = round(result, 2)
                        unitt = " Imp. oz"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "p":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 1.084
                        result_2 = round(result, 2)
                        unitt = " Imp. tbsp"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "q":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x * 2.768
                        result_2 = round(result, 2)
                        unitt = " Imp. tsp"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "r":
                        x = float(input("\nCubic inch (in^3) = "))
                        result = x / 1728
                        result_2 = round(result, 2)
                        unitt = " ft^3"
                        return (str(x) + " in^3 = " + str(result) + unitt + " or " + str(result_2) + unitt)

            print("UNIT: a = US liquid gallon (US gal)\n      b = US liquid quart (US qt)\n      "
                  "c = US liquid pint (US p)\n      d = US legal cup (US c)\n      "
                  "e = US fluid ounce (US oz)\n      f = US tablespoon (US tbsp)\n      "
                  "g = US teaspoon (US tsp)\n      h = Cubic metre (m^3)\n      "
                  "i = Litre (L)\n      j = Millilitre (mL)\n      "
                  "k = Imperial gallon (Imp. gal)\n      l = Imperial quart = (Imp. qt)\n      "
                  "m = Imperial pint (Imp. p)\n      n = Imperial cup (Imp. c)\n      "
                  "o = Imperial fluid ounce (Imp. oz)\n      p = Imperial tablespoon (Imp. tbsp)\n      "
                  "q = Imperial teaspoon (Imp. tsp)\n      r = Cubic foot (ft^3)\n      "
                  "s = Cubic inch (in^3)")
            print(volume_conversion(input("Unit = ")))
        elif app == "d":
            def speed_conversion(ops):
                if ops == "a":
                    print("UNIT: a = Miles per hour (mil/hr)\n      b = Foot per second (ft/s)\n      "
                          "c = Metre per second (m/s)\n      d = Kilometre per hour (km/hr)\n      "
                          "e = Knot (kn)")
                    unit = input("Miles per hour (mil/hr) to ")
                    if unit == "b":
                        x = float(input("\nMiles per hour (mil/hr) = "))
                        result = x * 1.467
                        result_2 = round(result, 2)
                        unitt = " ft/s"
                        return (str(x) + " mil/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nMiles per hour (mil/hr) = "))
                        result = x / 2.237
                        result_2 = round(result, 2)
                        unitt = " m/s"
                        return (str(x) + " mil/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nMiles per hour (mil/hr) = "))
                        result = x * 1.609
                        result_2 = round(result, 2)
                        unitt = " km/hr"
                        return (str(x) + " mil/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nMiles per hour (mil/hr) = "))
                        result = x / 1.151
                        result_2 = round(result, 2)
                        unitt = " kn"
                        return (str(x) + " mil/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Miles per hour (mil/hr)\n      "
                          "c = Metre per second (m/s)\n      d = Kilometre per hour (km/hr)\n      "
                          "e = Knot (kn)")
                    unit = input("Foot per second (ft/s) to ")
                    if unit == "a":
                        x = float(input("\nFoot per second (ft/s) = "))
                        result = x / 1.467
                        result_2 = round(result, 2)
                        unitt = " mil/hr"
                        return (str(x) + " ft/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nFoot per second (ft/s) = "))
                        result = x / 3.281
                        result_2 = round(result, 2)
                        unitt = " m/s"
                        return (str(x) + " ft/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nFoot per second (ft/s) = "))
                        result = x * 1.097
                        result_2 = round(result, 2)
                        unitt = " km/hr"
                        return (str(x) + " ft/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nFoot per second (ft/s) = "))
                        result = x / 1.688
                        result_2 = round(result, 2)
                        unitt = " kn"
                        return (str(x) + " ft/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Miles per hour (mil/hr)\n      b = Foot per second (ft/s)\n      "
                          "d = Kilometre per hour (km/hr)\n      "
                          "e = Knot (kn)")
                    unit = input("Metre per second (m/s) to ")
                    if unit == "a":
                        x = float(input("\nMetre per second (m/s) = "))
                        result = x * 2.237
                        result_2 = round(result, 2)
                        unitt = " mil/hr"
                        return (str(x) + " m/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nMetre per second (m/s) = "))
                        result = x * 3.281
                        result_2 = round(result, 2)
                        unitt = " ft/s"
                        return (str(x) + " m/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nMetre per second (m/s) = "))
                        result = x * 3.6
                        result_2 = round(result, 2)
                        unitt = " km/hr"
                        return (str(x) + " m/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nMetre per second (m/s) = "))
                        result = x * 1.944
                        result_2 = round(result, 2)
                        unitt = " kn"
                        return (str(x) + " m/s = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = Miles per hour (mil/hr)\n      b = Foot per second (ft/s)\n      "
                          "c = Metre per second (m/s)\n      "
                          "e = Knot (kn)")
                    unit = input("Kilometre per hour (km/hr) to ")
                    if unit == "a":
                        x = float(input("\nKilometre per hour (km/hr) = "))
                        result = x / 1.609
                        result_2 = round(result, 2)
                        unitt = " mil/hr"
                        return (str(x) + " km/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nKilometre per hour (km/hr) = "))
                        result = x / 1.097
                        result_2 = round(result, 2)
                        unitt = " ft/s"
                        return (str(x) + " km/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilometre per hour (km/hr) = "))
                        result = x / 3.6
                        result_2 = round(result, 2)
                        unitt = " m/s"
                        return (str(x) + " km/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nKilometre per hour (km/hr) = "))
                        result = x / 1.852
                        result_2 = round(result, 2)
                        unitt = " km/hr"
                        return (str(x) + " km/hr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print("UNIT: a = Miles per hour (mil/hr)\n      b = Foot per second (ft/s)\n      "
                          "c = Metre per second (m/s)\n      d = Kilometre per hour (km/hr)\n      ")
                    unit = input("Knot (kn) to ")
                    if unit == "a":
                        x = float(input("\nKnot (kn) = "))
                        result = x * 1.151
                        result_2 = round(result, 2)
                        unitt = " mil/hr"
                        return (str(x) + " kn = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nKnot (kn) = "))
                        result = x * 1.688
                        result_2 = round(result, 2)
                        unitt = " ft/s"
                        return (str(x) + " kn = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKnot (kn) = "))
                        result = x / 1.944
                        result_2 = round(result, 2)
                        unitt = " m/s"
                        return (str(x) + " kn = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nKnot (kn) = "))
                        result = x * 1.852
                        result_2 = round(result, 2)
                        unitt = " km/hr"
                        return (str(x) + " kn = " + str(result) + unitt + " or " + str(result_2) + unitt)
            print("UNIT: a = Miles per hour (mil/hr)\n      b = Foot per second (ft/s)\n      "
                  "c = Metre per second (m/s)\n      d = Kilometre per hour (km/hr)\n      "
                  "e = Knot (kn)")
            print(speed_conversion(input("Unit = ").lower()))
        elif app == "e":
            def energy_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Joule (J) to ")
                    if unit == "b":
                        x = float(input("\nJoule (J) = "))
                        result = x / 1000
                        result_2 = round(result)
                        unitt = " kJ"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nJoule (J) = "))
                        result = x / 4.184
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nJoule (J) = "))
                        result = x / 4184
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nJoule (J) = "))
                        result = x / 3600
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " kWh"
                            formula = int(num) / (3.6 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " J = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " J = " + str(result_1) + unitt)

                        return (converter(input("\nJoule (J) = ")).lower())
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 18
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (6.242 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " J = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nJoule (J) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nJoule (J) = "))
                        result = x / 1055
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " thm"
                            formula = int(num) / (1.005 * (10 ** 8))
                            limit = 5
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " J = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " J = " + str(result_1) + unitt)

                        return (converter(input("\nJoule (J) = ")).lower())
                    elif unit == "j":
                        x = float(input("\nJoule (J) = "))
                        result = x / 1.356
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " J = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Joule (J)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Kilojoule (kJ) to ")
                    if unit == "a":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x * 239
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x / 4.184
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x / 3.6
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x / 3600
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 21
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kJ = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilojoule (kJ) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x / 1.055
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x / 105480
                        result_2 = round(result, 2)
                        unitt = " thm"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nKilojoule (kJ) = "))
                        result = x * 738
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " kJ = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Gram calorie (cal) to ")
                    if unit == "a":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x * 4.184
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x / 239
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x / 860
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x / 860421
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 19
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " cal = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nGram calorie (cal) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x / 252
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " thm"
                            formula = int(num) / (2.521 * (10 ** 7))
                            limit = 5
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " cal = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " cal = " + str(result_1) + unitt)

                        return (converter(input("\nGram calorie (cal) = ")).lower())
                    elif unit == "j":
                        x = float(input("\nGram calorie (cal) = "))
                        result = x * 3.086
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " cal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Kilocalorie (kcal) to ")
                    if unit == "a":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 4184
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 4.184
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 1.162
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x / 860
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 22
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kcal = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilocalorie (kcal) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 3.966
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x / 25210
                        result_2 = round(result, 2)
                        unitt = " thm"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nKilocalorie (kcal) = "))
                        result = x * 3086
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " kcal = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Watt hour (Wh) to ")
                    if unit == "a":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x * 3600
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x * 3.6
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x * 860
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x / 1.162
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 22
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " Wh = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nWatt hour (Wh) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x * 3.412
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x / 29300
                        result_2 = round(result, 2)
                        unitt = " thm"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nWatt hour (Wh) = "))
                        result = x * 2655
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " Wh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "f":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Kilowatt hour (kWh) to ")
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " J"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (3.6 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kWh = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilowatt hour (kWh) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x * 3600
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x * 860421
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x * 860
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 25
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kWh = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilowatt hour (kWh) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x * 3412
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nKilowatt hour (kWh) = "))
                        result = x / 29.3
                        result_2 = round(result, 2)
                        unitt = " thm"
                        return (str(x) + " kWh = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " ft*lb"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.655 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kWh = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilowatt hour (kWh) = ")).lower())
                elif ops == "g":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("Electronvolt (eV) to ")
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 19
                            unitt = " J"
                            formula = int(num) / (6.242 * (10 ** 18))
                            limit = 16
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 22
                            unitt = " kJ"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 19
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 20
                            unitt = " cal"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 17
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 23
                            unitt = " kcal"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 20
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 23
                            unitt = " Wh"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 20
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 26
                            unitt = " kWh"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 22
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 22
                            unitt = " Btu"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 19
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 27
                            unitt = " thm"
                            formula = int(num) / (9.223 * (10 ** 18))
                            limit = 23
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 19
                            unitt = " ft*lb"
                            formula = int(num) / (8.462 * (10 ** 18))
                            limit = 16
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " eV = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " eV = " + str(result_1) + unitt)

                        return (converter(input("\nElectronvolt (eV) = ")).lower())
                elif ops == "h":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      "
                          "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
                    unit = input("British thermal unit (Btu) to ")
                    if unit == "a":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x * 1055
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x * 1.055
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x * 252
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x / 3.966
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x / 3.412
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x / 3412
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 21
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " Btu = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nBritish thermal unit (Btu) = ")).lower())
                    elif unit == "i":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x / 99976
                        result_2 = round(result, 2)
                        unitt = " thm"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nBritish thermal unit (Btu) = "))
                        result = x * 778
                        result_2 = round(result, 2)
                        unitt = " ft*lb"
                        return (str(x) + " Btu = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "i":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "j = Foot-pound (ft*lb)")
                    unit = input("US therm (thm) to ")
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " J"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.055 * (10 ** 8))
                            result_2 = round(result_1, 2)
                            return (str(num) + " thm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS therm (thm) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nUS therm (thm) = "))
                        result = x * 105480
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " thm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " cal"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.521 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " thm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS therm (thm) = ")).lower())
                    elif unit == "d":
                        x = float(input("\nUS therm (thm) = "))
                        result = x * 25210
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " thm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nUS therm (thm) = "))
                        result = x * 29300
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " thm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        x = float(input("\nUS therm (thm) = "))
                        result = x * 29.3
                        result_2 = round(result, 2)
                        unitt = " kWh"
                        return (str(x) + " thm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 26
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.223 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " thm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS therm (thm) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nUS therm (thm) = "))
                        result = x * 99976
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " thm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " ft*lb"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (7.78 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " thm = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS therm (thm) = ")).lower())
                elif ops == "j":
                    print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                          "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                          "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                          "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                          "i = US therm (thm)\n      ")
                    unit = input("Foot-pound (ft*lb) to ")
                    if unit == "a":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x * 1.356
                        result_2 = round(result, 2)
                        unitt = " J"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x / 738
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x / 3.086
                        result_2 = round(result, 2)
                        unitt = " cal"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x / 3086
                        result_2 = round(result, 2)
                        unitt = " kcal"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x / 2655
                        result_2 = round(result, 2)
                        unitt = " Wh"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " kWh"
                            formula = int(num) / (2.655 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " ft*lb = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " ft*lb = " + str(result_1) + unitt)

                        return (converter(input("\nFoot-pound (ft*lb) = ")).lower())
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 18
                            unitt = " eV"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (8.462 * (10 ** 18))
                            result_2 = round(result_1, 2)
                            return (str(num) + " ft*lb = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nFoot-pound (ft*lb) = ")).lower())
                    elif unit == "h":
                        x = float(input("\nFoot-pound (ft*lb) = "))
                        result = x / 778
                        result_2 = round(result, 2)
                        unitt = " Btu"
                        return (str(x) + " ft*lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " thm"
                            formula = int(num) / (7.78 * (10 ** 7))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " ft*lb = " + str(result) + "x10^-" + str(
                                    expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " ft*lb = " + str(result_1) + unitt)

                        return (converter(input("\nFoot-pound (ft*lb) = ")).lower())

            print("UNIT: a = Joule (J)\n      b = Kilojoule (kJ)\n      "
                  "c = Gram calorie (cal)\n      d = Kilocalorie (kcal)\n      "
                  "e = Watt hour (Wh)\n      f = Kilowatt hour (kWh)\n      "
                  "g = Electronvolt (eV)\n      h = British thermal unit (Btu)\n      "
                  "i = US therm (thm)\n      j = Foot-pound (ft*lb)")
            print(energy_conversion(input("Unit = ").lower()))
        elif app == "f":
            def temperature_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Fahrenheit (°F)\n      c = Kelvin (K)")
                    unit = input("Celsius (°C) to ").lower()
                    if unit == "b":
                        unitt = "°F"
                        x = input("\nCelsius (°C) = ")
                        result = (float(x) * (9 / 5)) + 32
                        return (str(x) + " °C = " + str(result) + unitt)
                    elif unit == "c":
                        unitt = "K"
                        x = input("\nCelsius (°C) = ")
                        result = float(x) + 273.15
                        return (str(x) + " °C = " + str(result) + unitt)
                elif ops == "b":
                    print("UNIT: a = Celsius (°C)\n      c = Kelvin (K)")
                    unit = input("Fahrenheit (°F) to ").lower()
                    if unit == "a":
                        unitt = "°C"
                        x = input("\nFahrenheit (°F) = ")
                        result = (float(x) - 32) * (5 / 9)
                        return (str(x) + " °F = " + str(result) + unitt)
                    elif unit == "c":
                        unitt = "K"
                        x = input("\nFahrenheit (°F) = ")
                        result = (float(x) - 32) * (5 / 9) + 273.15
                        return (str(x) + " °F = " + str(result) + unitt)
                elif ops == "c":
                    print("UNIT: a = Celsius (°C)\n      b = Fahrenheit (°F)")
                    unit = input("Kelvin (K) to ").lower()
                    if unit == "a":
                        unitt = "°C"
                        x = input("\nKelvin (K) = ")
                        result = float(x) - 273.15
                        return (str(x) + " K = " + str(result) + unitt)
                    elif unit == "b":
                        unitt = "°F"
                        x = input("\nKelvin (K) = ")
                        result = (float(x) - 273.15) * (9 / 5) + 32
                        return (str(x) + " K = " + str(result) + unitt)
            print("UNIT: a = Celsius (°C)\n      b = Fahrenheit (°F)\n      c = Kelvin (K)")
            print(temperature_conversion(input("Unit = ").lower()))
        elif app == "g":
            def weight_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Tonne (t) to ").lower()
                    if unit == "b":
                        x = float(input("\nTonne (t) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " g"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nTonne (t) = ")).lower())
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " g"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nTonne (t) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 12))
                            result_2 = round(result_1, 2)
                            return (str(num) + " t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nTonne (t) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nTonne (t) = "))
                        result = x / 1.016
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nTonne (t) = "))
                        result = x * 1.102
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nTonne (t) = "))
                        result = x * 157
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nTonne (t) = "))
                        result = x * 2205
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nTonne (t) = "))
                        result = x * 35274
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Tonne (t)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Kilogram (kg) to ").lower()
                    if unit == "a":
                        x = float(input("\nKilogram (kg) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nKilogram (kg) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kg = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilogram (kg) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " kg = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nKilogram (kg) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nKilogram (kg) = "))
                        result = x / 1016
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nKilogram (kg) = "))
                        result = x / 907
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nKilogram (kg) = "))
                        result = x / 6.35
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nKilogram (kg) = "))
                        result = x * 2.205
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nKilogram (kg) = "))
                        result = x * 35.274
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " kg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Gram (g) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " J"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " g = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " g = " + str(result_1) + unitt)

                        return (converter(input("\nGram (g) = ")).lower())
                    elif unit == "b":
                        x = float(input("\nGram (g) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " kJ"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nGram (g) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " mg"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " g = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nGram (g) = ")).lower())
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " Imp. t"
                            formula = int(num) / (1.016 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " g = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " g = " + str(result_1) + unitt)

                        return (converter(input("\nGram (g) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nGram (g) = "))
                        result = x / 907185
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nGram (g) = "))
                        result = x / 6350
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nGram (g) = "))
                        result = x / 454
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nGram (g) = "))
                        result = x / 28.35
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " g = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Milligram (mg) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " J"
                            formula = int(num) / (1 * (10 ** 9))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mg = " + str(result_1) + unitt)

                        return (converter(input("\nMilligram (mg) = ")).lower())
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " kJ"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mg = " + str(result_1) + unitt)

                        return (converter(input("\nMilligram (mg) = ")).lower())
                    elif unit == "c":
                        x = float(input("\nMilligram (mg) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " mg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nMilligram (mg) = "))
                        result = x * 1000
                        result_2 = round(result, 2)
                        unitt = " μg"
                        return (str(x) + " mg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " Imp. t"
                            formula = int(num) / (1.016 * (10 ** 9))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mg = " + str(result_1) + unitt)

                        return (converter(input("\nMilligram (mg) = ")).lower())
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " US t"
                            formula = int(num) / (9.072 * (10 ** 8))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mg = " + str(result_1) + unitt)

                        return (converter(input("\nMilligram (mg) = ")).lower())
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " st"
                            formula = int(num) / (6.35 * (10 ** 6))
                            limit = 4
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " mg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " mg = " + str(result_1) + unitt)

                        return (converter(input("\nMilligram (mg) = ")).lower())
                    elif unit == "i":
                        x = float(input("\nMilligram (mg) = "))
                        result = x / 453592
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " mg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nMilligram (mg) = "))
                        result = x / 28350
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " mg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Microgram (μg) to ").lower()
                    if unit == "a":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " t"
                            formula = int(num) / (1 * (10 ** 12))
                            limit = 9
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "b":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " kg"
                            formula = int(num) / (1 * (10 ** 9))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " g"
                            formula = int(num) / (1 * (10 ** 6))
                            limit = 3
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "d":
                        x = float(input("\nMicrogram (μg) = "))
                        result = x / 1000
                        result_2 = round(result, 2)
                        unitt = " mg"
                        return (str(x) + " μg = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "f":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 13
                            unitt = " Imp. t"
                            formula = int(num) / (1.016 * (10 ** 12))
                            limit = 9
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "g":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " US t"
                            formula = int(num) / (9.072 * (10 ** 11))
                            limit = 9
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "h":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 10
                            unitt = " st"
                            formula = int(num) / (6.35 * (10 ** 9))
                            limit = 7
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "i":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " lb"
                            formula = int(num) / (4.536 * (10 ** 8))
                            limit = 6
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                    elif unit == "j":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " oz"
                            formula = int(num) / (2.835 * (10 ** 7))
                            limit = 5
                            if len(num) < limit:
                                while len(num) > x:
                                    divider *= 10
                                    expon -= 1
                                    x += 1
                                result = int(num) / divider
                                result_1 = formula
                                return (str(num) + " μg = " + str(result) + "x10^-" + str(expon) + unitt + " or " + str(
                                    result_1))
                            elif len(num) >= limit:
                                result_1 = formula
                                return (str(num) + " μg = " + str(result_1) + unitt)

                        return (converter(input("\nMicrogram (μg) = ")).lower())
                elif ops == "f":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Imperial ton (Imp. t) to ").lower()
                    if unit == "a":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 1.016
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 1016
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " g"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.016 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " Imp. t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nImperial ton (Imp. t) = ")).lower())
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " kg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.016 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " Imp. t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nImperial ton (Imp. t) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 12
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (1.016 * (10 ** 12))
                            result_2 = round(result_1, 2)
                            return (str(num) + " Imp. t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nImperial ton (Imp. t) = ")).lower())
                    elif unit == "g":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 1.12
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 160
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 2240
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nImperial ton (Imp. t) = "))
                        result = x * 35840
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " Imp. t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "g":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("US ton (US t) to ").lower()
                    if unit == "a":
                        x = float(input("\nUS ton (US t) = "))
                        result = x / 1.102
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nUS ton (US t) = "))
                        result = x * 907
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nUS ton (US t) = "))
                        result = x * 907185
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " mg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.072 * (10 ** 8))
                            result_2 = round(result_1, 2)
                            return (str(num) + " US t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS ton (US t) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 11
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (9.072 * (10 ** 11))
                            result_2 = round(result_1, 2)
                            return (str(num) + " US t = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nUS ton (US t) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nUS ton (US t) = "))
                        result = x / 1.12
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nUS ton (US t) = "))
                        result = x * 143
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nUS ton (US t) = "))
                        result = x * 2000
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nUS ton (US t) = "))
                        result = x * 32000
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " US t = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "h":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      i = Pound (lb)\n      j = Ounce (oz)")
                    unit = input("Stone (st) to ").lower()
                    if unit == "a":
                        x = float(input("\nStone (st) = "))
                        result = x / 157
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nStone (st) = "))
                        result = x * 6.35
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nStone (st) = "))
                        result = x * 6350
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 6
                            unitt = " mg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (6.35 * (10 ** 6))
                            result_2 = round(result_1, 2)
                            return (str(num) + " st = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nStone (st) = ")).lower())
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 9
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (6.35 * (10 ** 9))
                            result_2 = round(result_1, 2)
                            return (str(num) + " st = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nStone (st) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nStone (st) = "))
                        result = x / 160
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nStone (st) = "))
                        result = x / 143
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nStone (st) = "))
                        result = x * 14
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nStone (st) = "))
                        result = x * 224
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " st = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "i":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      j = Ounce (oz)")
                    unit = input("Pound (lb) to ").lower()
                    if unit == "a":
                        x = float(input("\nPound (lb) = "))
                        result = x / 2205
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nPound (lb) = "))
                        result = x / 2.205
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nPound (lb) = "))
                        result = x * 454
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nPound (lb) = "))
                        result = x * 453592
                        result_2 = round(result, 2)
                        unitt = " mg"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 8
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (4.536 * (10 ** 8))
                            result_2 = round(result_1, 2)
                            return (str(num) + " lb = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nPound (lb) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nPound (lb) = "))
                        result = x / 2240
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nPound (lb) = "))
                        result = x / 2000
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nPound (lb) = "))
                        result = x / 14
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "j":
                        x = float(input("\nPound (lb) = "))
                        result = x * 16
                        result_2 = round(result, 2)
                        unitt = " oz"
                        return (str(x) + " lb = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "j":
                    print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                          "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                          "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)")
                    unit = input("Ounce (oz) to ").lower()
                    if unit == "a":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 35274
                        result_2 = round(result, 2)
                        unitt = " t"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 35.274
                        result_2 = round(result, 2)
                        unitt = " kg"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nOunce (oz) = "))
                        result = x * 28.35
                        result_2 = round(result, 2)
                        unitt = " g"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nOunce (oz) = "))
                        result = x * 28350
                        result_2 = round(result, 2)
                        unitt = " mg"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        def converter(num):
                            divider = 1
                            x = 1
                            expon = 7
                            unitt = " μg"
                            while len(num) > x:
                                divider *= 10
                                expon += 1
                                x += 1
                            result = int(num) / divider
                            result_1 = int(num) * (2.835 * (10 ** 7))
                            result_2 = round(result_1, 2)
                            return (str(num) + " oz = " + str(result) + "x10^" + str(expon) + unitt + " or " + str(
                                result_1) + unitt
                                    + " or " + str(result_2) + unitt)

                        return (converter(input("\nOunce (oz) = ")).lower())
                    elif unit == "f":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 35840
                        result_2 = round(result, 2)
                        unitt = " Imp. t"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "g":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 32000
                        result_2 = round(result, 2)
                        unitt = " US t"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "h":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 224
                        result_2 = round(result, 2)
                        unitt = " st"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "i":
                        x = float(input("\nOunce (oz) = "))
                        result = x / 16
                        result_2 = round(result, 2)
                        unitt = " lb"
                        return (str(x) + " oz = " + str(result) + unitt + " or " + str(result_2) + unitt)

            print("UNIT: a = Tonne (t)\n      b = Kilogram (kg)\n      c = Gram (g)\n      "
                  "d = Milligram (mg)\n      e = Microgram (μg)\n      f = Imperial ton (Imp. t)\n      "
                  "g = US ton (US t)\n      h = Stone (st)\n      i = Pound (lb)\n      j = Ounce (oz)")
            print(weight_conversion(input("Unit = ").lower()))
        elif app == "h":
            def pressure_conversion(ops):
                if ops == "a":
                    print("UNIT: b = Pascal (Pa)\n      c = Pound-force per square inch (psi)\n      "
                          "d = Standard atmosphere (atm)\n      e = Torr (Torr)")
                    unit = input("Bar (bar) to ").lower()
                    if unit == "b":
                        x = float(input("\nBar (bar) = "))
                        result = x * 100000
                        result_2 = round(result, 2)
                        unitt = " Pa"
                        return (str(x) + " bar = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nBar (bar) = "))
                        result = x * 14.504
                        result_2 = round(result, 2)
                        unitt = " psi"
                        return (str(x) + " bar = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nBar (bar) = "))
                        result = x / 1.013
                        result_2 = round(result, 2)
                        unitt = " atm"
                        return (str(x) + " bar = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nBar (bar) = "))
                        result = x * 750
                        result_2 = round(result, 2)
                        unitt = " Torr"
                        return (str(x) + " bar = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "b":
                    print("UNIT: a = Bar (bar)\n      c = Pound-force per square inch (psi)\n      "
                          "d = Standard atmosphere (atm)\n      e = Torr (Torr)")
                    unit = input("Pascal (Pa) to ").lower()
                    if unit == "a":
                        x = float(input("\nPascal (Pa) = "))
                        result = x / 100000
                        result_2 = round(result, 2)
                        unitt = " bar"
                        return (str(x) + " Pa = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nPascal (Pa) = "))
                        result = x / 6895
                        result_2 = round(result, 2)
                        unitt = " psi"
                        return (str(x) + " Pa = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nPascal (Pa) = "))
                        result = x / 101325
                        result_2 = round(result, 2)
                        unitt = " atm"
                        return (str(x) + " Pa = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nPascal (Pa) = "))
                        result = x / 133
                        result_2 = round(result, 2)
                        unitt = " Torr"
                        return (str(x) + " Pa = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "c":
                    print("UNIT: a = Bar (bar)\n      b = Pascal (Pa)\n      "
                          "d = Standard atmosphere (atm)\n      e = Torr (Torr)")
                    unit = input("Pound-force per square inch (psi) to ").lower()
                    if unit == "a":
                        x = float(input("\nPound-force per square inch (psi) = "))
                        result = x / 14.504
                        result_2 = round(result, 2)
                        unitt = " bar"
                        return (str(x) + " psi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nPound-force per square inch (psi) = "))
                        result = x * 6895
                        result_2 = round(result, 2)
                        unitt = " Pa"
                        return (str(x) + " psi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nPound-force per square inch (psi) = "))
                        result = x / 14.696
                        result_2 = round(result, 2)
                        unitt = " atm"
                        return (str(x) + " psi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nPound-force per square inch (psi) = "))
                        result = x * 51.715
                        result_2 = round(result, 2)
                        unitt = " Torr"
                        return (str(x) + " psi = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "d":
                    print(
                        "UNIT: a = Bar (bar)\n      b = Pascal (Pa)\n      c = Pound-force per square inch (psi)\n      "
                        "e = Torr (Torr)")
                    unit = input("Standard atmosphere (atm) to ").lower()
                    if unit == "a":
                        x = float(input("\nStandard atmosphere (atm) = "))
                        result = x * 1.013
                        result_2 = round(result, 2)
                        unitt = " bar"
                        return (str(x) + " atm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nStandard atmosphere (atm) = "))
                        result = x * 101325
                        result_2 = round(result, 2)
                        unitt = " Pa"
                        return (str(x) + " atm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nStandard atmosphere (atm) = "))
                        result = x * 14.696
                        result_2 = round(result, 2)
                        unitt = " psi"
                        return (str(x) + " atm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "e":
                        x = float(input("\nStandard atmosphere (atm) = "))
                        result = x * 760
                        result_2 = round(result, 2)
                        unitt = " Torr"
                        return (str(x) + " atm = " + str(result) + unitt + " or " + str(result_2) + unitt)
                elif ops == "e":
                    print(
                        "UNIT: a = Bar (bar)\n      b = Pascal (Pa)\n      c = Pound-force per square inch (psi)\n      "
                        "d = Standard atmosphere (atm)")
                    unit = input("Torr (Torr) to ").lower()
                    if unit == "a":
                        x = float(input("\nTorr (Torr) = "))
                        result = x / 750
                        result_2 = round(result, 2)
                        unitt = " bar"
                        return (str(x) + " Torr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "b":
                        x = float(input("\nTorr (Torr) = "))
                        result = x * 133
                        result_2 = round(result, 2)
                        unitt = " Pa"
                        return (str(x) + " Torr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "c":
                        x = float(input("\nTorr (Torr) = "))
                        result = x / 51.715
                        result_2 = round(result, 2)
                        unitt = " psi"
                        return (str(x) + " Torr = " + str(result) + unitt + " or " + str(result_2) + unitt)
                    elif unit == "d":
                        x = float(input("\nTorr (Torr) = "))
                        result = x / 760
                        result_2 = round(result, 2)
                        unitt = " atm"
                        return (str(x) + " Torr = " + str(result) + unitt + " or " + str(result_2) + unitt)

            print("UNIT: a = Bar (bar)\n      b = Pascal (Pa)\n      c = Pound-force per square inch (psi)\n      "
                  "d = Standard atmosphere (atm)\n      e = Torr (Torr)")
            print(pressure_conversion(input("Unit = ").lower()))
        #elif app == "i":

print("MODE: a = Normal Calculator\n      "
                 "b = Sequence Calculator\n      "
      "c = Conversion Calculator\n      d = ")
calculator(input("Enter MODE: ").lower())