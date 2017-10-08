temperatures = [10, -20, -289, 100]

def c_to_f(degC):
    degF = (degC * 9/5) + 32
    return degF

for degC in temperatures:
    if degC > -273.15:
        print(c_to_f(degC))
    else:
        print("That temperature doesn't make sense!")
