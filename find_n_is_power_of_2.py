a=int(input(""))
b=0
c=1
while(c<a):
    b+=1
    c=2**b
if(c==a):
    print("yes")
else:
    print("no")
