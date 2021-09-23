s=int(input("somme initiale : "))
t=float(input("taux d'intéret : "))
n=int(input("nombres d'années: "))


for i in range(n):
    print(s*t/100)
    s=s+s*t/100
print(s)    

    




    
    