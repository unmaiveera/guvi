s,k=list(map(int,input().split()))
s=s^k
k=s^k
s=s^k
print(s,end=" ")
print(k)
