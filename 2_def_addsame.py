def addsame():
    a=int(input("Enter 1st no.="))
    b=int(input("Enter 2nd no.="))
    c=int(input("Enter 3rd no.="))
    if a==b==c:
        return("same")
    else:
        return(a+b+c)
d=addsame()
if d=="same":
    print("Entered three numbers are same")
else:
    print("Addition of three numbers=",d)
