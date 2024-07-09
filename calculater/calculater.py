x=float(input("Enter the first number\n"))
y=float(input("ENter the second number\n"))
z=input("Enter the operataor\n")
match z:
    case "+":
        w=x+y
        print(w,"the sum of two number")
    case "-":
        w=x-y
        print(w,"Difference of two number")
    case "*":
        w=x*y
        print(w,"multiply of two number")
    case "/":
        w=x/y
        print(w,"division of given number")
    case "%":
        w=x%y
        print(w,"Get remainder of given number")
    case "//":
        w=x//y
        print(w,"floor division of given number")
    case _:
        print("wrong choice")
