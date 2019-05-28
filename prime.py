a=int(input(""))
x=1
for i in range (2,a):
    if((a%i)==0):
        x=0
        break
    else:
        continue
if(x==0):
    print("no")
else:
    print("yes")
