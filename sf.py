# Integer Array of non-repeatable items -
# Find sets of all integers whose sum is equal to the length of the array.

def lensum(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i+1, l):
            if arr[i] + arr[j] == l:
                print(arr[i], arr[j])

A = [1, 3, 0, 4]
lensum(A)



