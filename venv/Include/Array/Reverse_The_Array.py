#           Ussing reversed method
def Reverse_Using_Reversed(arr):
    return list(reversed(arr))


arr = list(map(int,input().split()))
print("Using Reversed: ",Reverse_Using_Reversed(arr))


