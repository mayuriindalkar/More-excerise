a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))
if a>b and a>c:
    print(a, "a is maximum number")
elif b>c and b>a:
    print(b, "b is maximum number")
elif c>b and c>a:
    print(c, "c is a maximum number")
else:
    print("invalid number")