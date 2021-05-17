# .......................Using Sort method.....................
def kth_max_and_min(arr, k):
    arr.sort()
    return "min = " + str(arr[k - 1]), "max = " + str(arr[len(arr) - k])


arr = list(map(int, input("Enter Array: ").split()))
k = int(input("Enter Valur of k: "))
print(kth_max_and_min(arr, k))
