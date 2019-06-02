a=int(input())
if(a<60):
  print(0,a)
else:
  hr=a//60
  min=a%60
  print(hr,min)
