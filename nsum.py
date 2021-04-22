n = int(input("Enter Value of n : "))


def nsum(lt):
    # s = 1 if lt==1 else lt + nsum(lt-1)
    slist = [0, 1]
    for i in range(2, lt+1):
        slist.insert(i, i + slist[i-1])

    return slist[lt]


print(f"Sum of first {n} natural numbers is : {nsum(n)}.")
