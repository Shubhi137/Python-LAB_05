def find_maximum(a,b):
    if a>b:
        return a
    else:
        return b

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

result=find_maximum(a,b)

print("The maximum number is:",result)