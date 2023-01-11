def mulval(*x):
    print("Multiple values stored in one formal parameter=",x)
    print("Perticuler value(last value)=",x[-1],type(x))
mulval('man',20,'cat',True,34.89,False)