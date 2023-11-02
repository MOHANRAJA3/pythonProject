#Building a calculator
num1 = input("Enter your first number")
num2 = input("Enter your second number")
sum = float(num1)+float(num2)
sub = float(num1)-float(num2)
multiply = float(num1)*float(num2)
div = float(num1)/float(num2)
modular = float(num1)%float(num2)
print(num1)
print(num2)

op= input("What Do you want to calculate ? " + "ENTER + for sum, - for subtraction, * for multiplication, / for division, % for remainder = ")
print(op)
if op=="+":
    print(sum)

elif op=="-":
    print(sub)

elif op=="*":
    print(multiply)
elif op=="%":
    print(modular)
else:
    print(div)
print("Thank you")