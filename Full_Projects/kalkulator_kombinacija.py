from math import factorial

print("---Kalkulator kombinacija.---")
print("PRIMJER. Loto 7/39. 7=k, 39=n")
print("-----------------------------")
n = int(input("Unesi broj opcija: "))
k = int(input("Unesi broj clanova kombinacije: "))

if n > 0 and k > 0:
    comb = factorial(n)//(factorial(k)*factorial(n-k))
    print("Broj mogucih kombinacija:", comb)
