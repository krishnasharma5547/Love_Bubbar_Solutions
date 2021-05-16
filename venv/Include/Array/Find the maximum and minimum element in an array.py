def Using_Max_Min(arr):
    maxi = max(arr)
    mini = min(arr)
    return "minimum = " + str(mini) + " maximun= " + str(maxi)


arr = list(map(int, input().split()))
print(Using_Max_Min(arr))
