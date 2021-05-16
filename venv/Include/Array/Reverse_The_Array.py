#           Ussing reversed method
def Reverse_Using_Reversed(arr):
    return list(reversed(arr))

def Reverse_Using_Swap(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
    return arr

arr = list(map(int,input().split()))
print("Using Reversed: ", Reverse_Using_Reversed(arr))
print("Using Swap: ", Reverse_Using_Swap(arr))
