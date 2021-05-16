def Using_Max_Min(arr):
    maxi = max(arr)
    mini = min(arr)
    return "minimum = " + str(mini) + " maximun= " + str(maxi)

def Using_Linear_Traverse(arr):
    mini = 999999
    maxi = -9999999
    for i in arr:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    return "minimum = " + str(mini) + " maximun= " + str(maxi)

arr = list(map(int, input().split()))
print(Using_Max_Min(arr))
print(Using_Linear_Traverse(arr))
