#Program to Print Fibonacci Series upto a said number of terms
# Eg. Series for 8 No. of terms : 0 1 1 2 3 5 8 13

def fibo(term):
    if term == 0 or term == 1:
        return term
    else:
        return (fibo(term-2) + fibo(term - 1))

print(" ************* Fibonacci Series ******************")

nt = int(input("\n Please enter no. of terms for Series : "))

print(f"\n Fibonacci Series upto {nt} Terms goes as : ", end="")

for k in range(nt):
    print(f"{fibo(k)}",end=", ")

print("\n\n**************************************************")