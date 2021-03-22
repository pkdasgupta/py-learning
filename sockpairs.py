# Complete the sockMerchant function below.

def sockMerchant(n, ar):
    return sum([ar.count(i) // 2 for i in set(ar)])


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)


