n=int(input(""))

l=list(input(""))
l=l[:2*n-1:2]

temp=0
even=0
odd=0

for k in l:
    k=int(k)
    if k%2==0:
        even+=1
    else:
        odd+=1
    if k>temp:
        temp=k
print("Largest: ", temp)

for m in l:
    m=int(m)
    if m<temp:
        temp=m
print("Largest: ", temp)

summ=0
for n in l:
    n=int(n)
    summ+=n
print("Sum: ", summ)

print("Even count: ", even)
print("Odd count: ", odd)

for o in l[::-1]:
    print(o, end=" ")
print("")
