
def printTwos(n):
    twos = []
    while n % 2 == 0 :
        n = n / 2
        twos.append(2)

    if len(twos) % 2 == 0 :
        twos.insert(len(twos) // 2, int(n))
    else:
        twos.insert(len(twos) // 2 + 1, int(n))

    return "*".join([str(i) for i in twos])

print(printTwos(32))

