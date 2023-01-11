base=int(input('Enter base='))
power=int(input('Enter power='))
ans=1
pow=power
while(power>0):
    ans=ans*base
    power-=1
print('Base',base,'to the power',pow,'=',ans)