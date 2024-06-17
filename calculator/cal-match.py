a=float(input("enter value of a :"))
b=float(input("enter value of b :"))
operators = input("select operator +,-,*,/ :")

match operators :
    case '+':
        result = a + b
        print(result)
    case '-':
        result = a - b
        print(result)
    case '*':
        result = a * b
        print(result)
    case '/':
        result = a / b
        print(result)