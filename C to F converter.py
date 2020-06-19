def c_to_f(degC):
    degF = (degC * 9/5) + 32
    return degF

degC = float(input("Gimme a temperature in celsius: "))

if degC > -273.15:
    print(c_to_f(degC))
else:
    print("yous a foo")
