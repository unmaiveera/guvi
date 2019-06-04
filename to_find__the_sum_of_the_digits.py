given_number = int(input())
sum = 0
while given_number > 0 :
  remainder = given_number % 10
  sum += remainder
  given_number //= 10
print(sum)
