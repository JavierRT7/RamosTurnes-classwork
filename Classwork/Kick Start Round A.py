cases_T = int(input())
for counter in range(cases_T):
    houses_N, dollars_B = [int(x) for x in input().split()]
    prices_A = []
    for count in range(houses_N):
        x = input()
        if x.isdigit():
            prices_A[count] = int(x)
        #End If
    #Next
    print(prices_A)
    prices_A.sort()
    print(prices_A)



 
