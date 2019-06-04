n=input()
a=int(n)
x=list(map(int,input().split()))
count=0
for i in x:
  count=i+count
  average=count//a
print(average)
