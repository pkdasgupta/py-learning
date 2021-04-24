

def add_commas(mystr):
    l = list(mystr)
    l.reverse()

    for i in range(1, len(l)):
        if i % 3 == 0:
            l.insert(i, ",")

    l.reverse()
    return ("".join(l))


print(add_commas("1154392"))
