# Program to find the character that occurs most frequently in a string

def maxctr(string):
    occ = {}
    for s in string:
        occ[string.count(s)] = s
    return occ[max(occ.keys())]


def main():
    if __name__ == '__main__':
        print(maxctr("oxymoxytoxy"))


main()
