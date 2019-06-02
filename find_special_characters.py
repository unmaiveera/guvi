x=input()
count=0
for c in x:
  if c.isdigit()!=True and c.isalpha()!=True :
    count=count+1
print(count)
