import random
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