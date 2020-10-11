cases_T = int(input())
prices_A = [0, houses_N]
for counter in range(cases_T):
    houses_N, dollars_B = [int(x) for x in input().split()]
    for count in range(houses_N):
        prices_A[count] = int(input())
    #Next
    print(prices_A)
    prices_A.sort()
    print(prices_A)



 
