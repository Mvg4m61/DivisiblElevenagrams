from itertools import combinations
def divisibleby11():
    n = int(input("\nEnter number: "))
    nstr = str(n)
    arr = [int(x) for x in nstr]
    if len(arr) == 1:
        if arr[0] == 0:
            return 1
        else:
            return -1
        
    k = len(arr)//2
    b = arr[:] 
    comblist = combinations(arr,k)
    flag = 0
    for a in comblist:
        a = list(a)
        sum1 = 0
        sum2 = 0
        for i in range(len(a)):
            b.remove(a[i])
            sum1 = sum1 + a[i]
        print(sum1)
        print(b)
        for j in b:
            sum2 = sum2 + j
        print(sum2)
        b = arr[:]
        diff = abs(sum1 - sum2)
        if diff%11 == 0:
            flag = 1
            break
    if flag == 0:
        print("\nNo combination possible.")
    else:
        print("\nCombination possible!")
#main environment
y = divisibleby11()
if y == -1:    
    print("\nNo combination possible.")
if y == 1:
    print("\nCombination possible.")