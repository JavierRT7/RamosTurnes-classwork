cases_T = int(input())
for counter in range(cases_T):
    houses_N, dollars_B = [int(x) for x in input().split()]
    prices_A = []
    for count in range(houses_N):
        x = input()
        if x.isdigit():
            prices_A.insert(count, int(x))
        #End If
    #Next
    prices_A.sort()
    x = 0
    answer = 0
    while dollars_B > -1:
        dollars_B = dollars_B - prices_A[x]
        x = x + 1
    #End While
    answer = x - 1
    print("Case #", counter + 1, ":", answer) 
#Next




 
