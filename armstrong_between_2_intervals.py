x,y= input().split()
lower=int(x)
upper=int(y) 
for num in range(lower,upper + 1):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num,end=" ")
