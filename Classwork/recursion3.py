import time
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    #End If
#End Function
def fibonacci2(n):
    fibNumbers = [0, 1] #list of first two Fibonacci numbers
    #now append the sum of the two previous numbers to the list
    for i in range(2, n + 1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #Next
    return fibNumbers[n]
#End Function
startTime1 = time.perf_counter()
print(fib(10))
endTime1 = time.perf_counter()
startTime2 = time.perf_counter()
print(fibonacci2(10))
endTime2 = time.perf_counter()
print("Time 1: {} seconds".format(endTime1 - startTime1))
print("Time 2: {} seconds".format(endTime2 - startTime2))
