e=0
n=int(input("nb de nb : "))
k=10**(n+1)
for i in range(n):
    a=int(input("nombre : "))
    e=a*k+e
    k=k/10
print(e)
    