def is_prime(n):
    '''
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
    '''
    for j in range(2,n+1):
        for k in range(2,j):
            if j%k==0:
                break
        else:
            print(j, end=" ")
    print()
        
n=int(input())
is_prime(n)
