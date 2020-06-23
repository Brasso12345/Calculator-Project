def rational_numbers_conversion(ops):
    if ops == "a":
        print("FORM: d = Decimals\n      "
            "e = Ratio\n      f = Percentage")
        unit = input("Proper Fraction to ").lower()
        if unit == "d":
            x = input("Fraction = ")
            result = eval(x)
            result_2 = round(result, 2)
            return x + " = " + str(result) + " or " + str(result_2)
        elif unit == "e":
            x = input("Fraction = ")
            result = x.replace("/", ":")
            return x + " = " + str(result)
        elif unit == "f":
            x = input("Fraction = ")
            result = eval(x)
            fin_result = result * 100
            fin_result_2 = round(fin_result, 2)
            return x + " = " + str(fin_result) + "%" + " or " + str(fin_result_2) + "%"
    elif ops == "b":
        print("FORM: c = Mixed Fraction\n      d = Decimals\n      "
            "e = Ratio\n      f = Percentage")
        unit = input("Improper Fraction to ").lower()
        if unit == "c":
            x = input("Fraction = ")
            j = x.index("/")
            new_blah = ""
            while j != len(x):
                blah = x[j]
                new_blah += str(blah)
                j += 1
            new_x = x.replace("/", "%")
            result = eval(x)
            num = eval(new_x)
            if num == 0:
                return str(x) + " = " + str(int(result))
            else:
                return str(x) + " = " + str(int(result)) + " " + str(num) + str(new_blah)
        elif unit == "d":
            x = input("Fraction = ")
            result = eval(x)
            result_2 = round(result, 2)
            return x + " = " + str(result) + " or " + str(result_2)
        elif unit == "e":
            x = input("Fraction = ")
            result = x.replace("/", ":")
            return x + " = " + str(result)
        elif unit == "f":
            x = input("Fraction = ")
            result = eval(x)
            fin_result = result * 100
            fin_result_2 = round(fin_result, 2)
            return x + " = " + str(fin_result) + "%" + " or " + str(fin_result_2) + "%"
    elif ops == "c":
        print("FORM: b = Improper Fraction\n      d = Decimals\n      "
              "e = Ratio\n      f = Percentage")
        unit = input("Mixed Fraction to ").lower()
        if unit == "b":
            x = input("Fraction = ")
            j = x.index(" ")
            j_2 = j
            d = x.index("/")
            d_2 = d
            i = 0
            whole_num = ""
            denominator = ""
            numerator = ""
            while j != 0:
                blah = x[i]
                whole_num += str(blah)
                i += 1
                j -= 1
            while d != len(x):
                bitch = x[d]
                denominator += str(bitch)
                d += 1
            while j_2 < d_2:
                new_bitch = x[j_2]
                numerator += str(new_bitch)
                j_2 += 1
            new_numerator = numerator.replace("/", "")
            new_denominator = denominator.replace("/", "")
            result = int(whole_num) * int(new_denominator) + int(new_numerator)
            return x + " = " + str(result) + str(denominator)
        elif unit == "d":
            x = input("Fraction = ")
            j = x.index(" ")
            j_2 = j
            d = x.index("/")
            d_2 = d
            i = 0
            whole_num = ""
            denominator = ""
            numerator = ""
            while j != 0:
                blah = x[i]
                whole_num += str(blah)
                i += 1
                j -= 1
            while d != len(x):
                bitch = x[d]
                denominator += str(bitch)
                d += 1
            while j_2 < d_2:
                new_bitch = x[j_2]
                numerator += str(new_bitch)
                j_2 += 1
            new_numerator = numerator.replace("/", "")
            new_denominator = denominator.replace("/", "")
            result = int(whole_num) * int(new_denominator) + int(new_numerator)
            peyk_result = str(result) + str(denominator)
            fin_result = eval(peyk_result)
            fin_result_2 = round(fin_result, 2)
            if fin_result_2 != fin_result:
                return x + " = " + str(fin_result) + " or " + str(fin_result_2)
            else:
                return x + " = " + str(fin_result)
        elif unit == "e":
            x = input("Fraction = ")
            j = x.index(" ")
            j_2 = j
            d = x.index("/")
            d_2 = d
            i = 0
            whole_num = ""
            denominator = ""
            numerator = ""
            while j != 0:
                blah = x[i]
                whole_num += str(blah)
                i += 1
                j -= 1
            while d != len(x):
                bitch = x[d]
                denominator += str(bitch)
                d += 1
            while j_2 < d_2:
                new_bitch = x[j_2]
                numerator += str(new_bitch)
                j_2 += 1
            new_numerator = numerator.replace("/", "")
            new_denominator = denominator.replace("/", "")
            result = int(whole_num) * int(new_denominator) + int(new_numerator)
            peyk_result = str(result) + str(denominator)
            fin_result = peyk_result.replace("/", ":")
            return x + " = " + str(fin_result)
        elif unit == "f":
            x = input("Fraction = ")
            j = x.index(" ")
            j_2 = j
            d = x.index("/")
            d_2 = d
            i = 0
            whole_num = ""
            denominator = ""
            numerator = ""
            while j != 0:
                blah = x[i]
                whole_num += str(blah)
                i += 1
                j -= 1
            while d != len(x):
                bitch = x[d]
                denominator += str(bitch)
                d += 1
            while j_2 < d_2:
                new_bitch = x[j_2]
                numerator += str(new_bitch)
                j_2 += 1
            new_numerator = numerator.replace("/", "")
            new_denominator = denominator.replace("/", "")
            result = int(whole_num) * int(new_denominator) + int(new_numerator)
            peyk_result = str(result) + str(denominator)
            new_peyk_result = eval(peyk_result)
            fin_result = float(new_peyk_result) * 100
            fin_result_2 = round(fin_result, 2)
            if fin_result_2 != fin_result:
                return x + " = " + str(fin_result) + "%" + " or " + str(fin_result_2) + "%"
            else:
                return x + " = " + str(fin_result) + "%"
    elif ops == "d":
        print("FORM: a/b/c = Fraction\n      "
            "e = Ratio\n      f = Percentage")
        unit = input("Decimal to ").lower()
        if unit == "a" or "b" or "c":
            x = input("Number = ")
            j = x.index(".")
            d = j
            i = 0
            whole_num = ""
            dec = ""
            denominator = 1
            b = len(x) - j
            v = j
            while j != 0:
                blah = x[i]
                whole_num += str(blah)
                i += 1
                j -= 1
            while d != len(x):
                bitch = x[d]
                dec += str(bitch)
                d += 1
            new_dec = dec.replace(".", "")
            denominator = 10 ** len(new_dec)
            def lowest_term(nume, denome):
                while int(nume) != 1 and int(denome) != 1:
                    if int(nume) % 10 == 0 and int(denome) % 10 == 0:
                        nume = int(nume) / 10
                        denome = int(denome) / 10
                    elif int(nume) % 9 == 0 and int(denome) % 9 == 0:
                        nume = int(nume) / 9
                        denome = int(denome) / 9
                    elif int(nume) % 8 == 0 and int(denome) % 8 == 0:
                        nume = int(nume) / 8
                        denome = int(denome) / 8
                    elif int(nume) % 7 == 0 and int(denome) % 7 == 0:
                        nume = int(nume) / 7
                        denome = int(denome) / 7
                    elif int(nume) % 6 == 0 and int(denome) % 6 == 0:
                        nume = int(nume) / 6
                        denome = int(denome) / 6
                    elif int(nume) % 5 == 0 and int(denome) % 5 == 0:
                        nume = int(nume) / 5
                        denome = int(denome) / 5
                    elif int(nume) % 4 == 0 and int(denome) % 4 == 0:
                        nume = int(nume) / 4
                        denome = int(denome) / 4
                    elif int(nume) % 3 == 0 and int(denome) % 3 == 0:
                        nume = int(nume) / 3
                        denome = int(denome) / 3
                    elif int(nume) % 2 == 0 and int(denome) % 2 == 0:
                        nume = int(nume) / 2
                        denome = int(denome) / 2
                    else:
                        break
                nume = int(nume)
                denome = int(denome)
                answer = str(whole_num) + " " + str(nume) + "/" + str(denome)
                return answer
            return lowest_term(new_dec, denominator)
print("FORM: a = Proper fraction\n      b = Improper Fraction\n      c = Mixed Fraction\n      d = Decimals\n      "
      "e = Ratio\n      f = Percentage")
print(rational_numbers_conversion(input("Unit = ").lower()))