def c_to_f(degC):
    degF = (degC * 9/5) + 32
    return degF

temperatures = [10, -20, -289, 100]

for c in temperatures:
    if c > -273.15:
        with open("example.txt", "a+ ") as file:
            file.write(str(c_to_f(c))+"\n")
    else:
        print("yous a foo")
