i=0
while i<1:

    try:
        num1=int(input("Enter a number (or a letter to exit): "))
    except ValueError:
        break

    o=input("Enter an operation: ")
    num2=int(input("Enter another number: "))
    result=0

    if o=="+":

        result=num1+num2

    elif o=="-":

        result=num1-num2

    elif o=="*":

        result=num1*num2

    elif o=="/":

        result=num1/num2

    print(result)