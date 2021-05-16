# ...................Using reversed method..........................
def Reverse_Using_Reversed(arr):
    return list(reversed(arr))


# .....................Using swap ..................................
def Reverse_Using_Swap(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
    return arr


# .....................Using indexing..................
def Reverse_Using_Indexing(arr):
    return arr[::-1]


arr = list(map(int, input().split()))
print("Using Reversed: ", Reverse_Using_Reversed(arr))
print("Using Indexing: ", Reverse_Using_Indexing(arr))
print("Using Swap: ", Reverse_Using_Swap(arr))
