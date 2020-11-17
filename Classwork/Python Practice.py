import random
def insert_sort():
    import time

    # starting time
    start = time.time()

    # program body starts
    aList = []
    for n in range(10):
        number = random.randint(0, 100)
        aList.append(number)
    print(aList)
    for j in range(1, len(aList) - 1):
        nextNum = aList[j]
        i = j-1
        while i >= 0 and aList[i] > nextNum:
            aList[i + 1] = aList[i]
            i = i - 1
        #endwhile
        aList[i + 1] = nextNum
    #Next
    print(aList)

    # sleeping for 1 sec to get 10 sec runtime
    time.sleep(1)

    # program body ends

    # end time
    end = time.time()

    # total time taken
    print(f"Runtime of the program is {end - start}")
    #End Procedure
def bubble_sort():
    import time
    start = time.time()
    aList = []
    for n in range(10):
        number = random.randint(0, 100)
        aList.append(number)
    print(aList)
    for i in range(0, len(aList) - 2):
        for j in range(0, len(aList) - i - 2):
            if aList[j] > aList[j + 1]:
                temp = aList[j]
                aList[j] = aList[j + 1]
                aList[j + 1] = temp
            #End If
    time.sleep(1)
    end = time.time()
    print(f"Runtime of the program is {end - start}")
insert_sort()
bubble_sort()