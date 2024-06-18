import time # type: ignore
a = time.strftime('%H:%M:%S')
print(a)
a =int(time.strftime('%H'))
print(a)

if (a<=12):
    print("good morning")
else :
    print("good aftrnoon")
 # type: ignore