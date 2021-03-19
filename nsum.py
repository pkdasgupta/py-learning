n = int(input("Enter Value of n : "))


def nsum(lt):
    s = 1 if lt==1 else lt + nsum(lt-1)
    return s


print(f"Sum of first {n} natural numbers is : {nsum(n)}.")
