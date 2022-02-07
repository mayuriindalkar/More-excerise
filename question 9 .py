# Harshad number

def number(n):
    sum=0
    a=n
    while a>0:
        b=a%10
        sum=sum+b
        a=a//10
    if n%sum==0:
        print(n,"is harshad number")
    else:
        print(n,"is not harshad number")
number(4)