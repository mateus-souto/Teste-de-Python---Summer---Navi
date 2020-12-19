c=0
n=0

while n<=5000000:
    if n%2 != 1 and n%49 ==0 and n%37 ==0:
        c=c+1
    n=n+1

print (c)
