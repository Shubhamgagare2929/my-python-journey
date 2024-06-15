
# calciulator using for loop

a=int(input("enter value of a :"))
b=int(input("enter value of b :"))
print("select 1 for addition")
print("select 2 for substraction")
print("select 3 for multiplication")
print("select 4 for division")

x=int(input())
if (x==1):
    print(a+b)
elif (x == 2):
    print(a-b)
elif (x==3):
    print(a*b)
elif (x==4):
    print(a/b)
else:
    print("invalid operation")

