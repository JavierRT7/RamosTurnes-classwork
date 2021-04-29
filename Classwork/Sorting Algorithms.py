import random
import time

def bubbleSort(numbers):
    temp = 0
    for count in range(len(numbers) - 2):
        for counter in range(len(numbers) - count - 2):
            if numbers[counter] > numbers[counter + 1]:
                temp = numbers[counter]
                numbers[counter] = numbers[counter + 1]
                numbers[counter + 1] = temp
            #End If
        #Next
    #Next
#End Procedure

def insertionSort(numbers):
    for count in range(len(numbers)):
        nextNum = numbers[count]
        counter = count - 1
        while counter >= 0 and numbers[counter] > nextNum:
            numbers[counter + 1] = numbers[counter]
            counter = counter - 1
        #End While
        numbers[counter + 1] = nextNum
    #Next
#End Procedure

def inbuiltSort(numbers):
    numbers.sort()
#End Procedure

numbers = []
for counter in range(30000):
    numbers.append(random.randint(1, 1000))
#Next
startbubble = time.time()
bubbleSort(numbers)
endbubble = time.time()
print("bubble sort done")

numbers = []
for counter in range(30000):
    numbers.append(random.randint(1, 1000))
#Next

startpython = time.time()
inbuiltSort(numbers)
endpython = time.time()
print("in-built sort done")

numbers = []
for counter in range(30000):
    numbers.append(random.randint(1, 1000))
#Next

startinsert = time.time()
insertionSort(numbers)
endinsert = time.time()
print("insertion sort done")

print("The bubble sort took", endbubble - startbubble, "seconds")
print("The in-built sort function took", endpython - startpython, "seconds")
print("The insertion sort took", endinsert - startinsert, "seconds")
