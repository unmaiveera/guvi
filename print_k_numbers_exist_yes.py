x=0
f,s=map(int,input().split())
a=list(map(int,input().split()))[:f]
for i in a:
  if i==s:
    x+=1
if(x!=0):
  print("yes")
else:
  print("no")
