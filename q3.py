def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
        
n=int(input())
for j in range(2,n+1):
    if is_prime(j)==True:
        print(j, end=" ")
print()
