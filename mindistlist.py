# The distance between two array values is the number of indices between them.
# Given an array A, find the minimum distance between any pair of equal elements in the array.
# If no such value exists, return -1.

def mindistlist(a):
    d = {}
    mindist = len(a)

    for i in range(len(a)):
        try:
            mindist = min(abs(d[a[i]] - i), mindist)

            d[a[i]] = i

            if mindist == 1:
                break
        except:
            d[a[i]] = i

    if mindist == len(a):
        return -1
    else:
        return mindist

a = [int(i) for i in input().strip().split(' ')]
print(mindistlist(a))