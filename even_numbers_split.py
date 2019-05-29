upper,lower = input().split()
x = int(upper)
y = int(lower)
for i in range(x+1,y):
  if(i % 2 == 0):
    print(i,end=" ")
