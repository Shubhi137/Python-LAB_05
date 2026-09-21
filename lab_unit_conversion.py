def convert(C):
    F=(C*9/5)+32
    return F

C=float(input("Enter temperature in Celsius:"))

F=convert(C)
print("Temperature in Fahrenheit:",F,"F")