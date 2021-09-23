e=0
a=0
n=int(input("nombre de note : "))
for k in range(n):
    i=int(input("note : "))
    c=int(input("coef : "))
    a=i*c+a
    e=e+c
print(a/e)
