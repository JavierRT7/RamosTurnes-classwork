import random
import time

def bubbleSort(numbers):
    temp = 0
    for count in range(len(numbers) * len(numbers)):
        for counter in range(len(numbers) - 1):
            if numbers[counter] > numbers[counter + 1]:
                temp = numbers[counter]
                numbers[counter] = numbers[counter + 1]
                numbers[counter + 1] = temp

def insertionSort(numbers):
    for count in range(len(numbers)):
        nextNum = numbers[count]
        counter = count - 1
        while counter >= 0 and numbers[counter] > nextNum:
            numbers[counter + 1] = numbers[counter]
            counter = counter - 1
        numbers[counter + 1] = nextNum

numbers = []
for counter in range(10):
    numbers.append(random.randint(1, 1000))
#Next
startbubble = time.time()
bubbleSort(numbers)
endbubble = time.time()
print("done")
numbers = []
for counter in range(1000000):
    numbers.append(random.randint(1, 1000))
#Next
startpython = time.time()
numbers.sort()
endpython = time.time()
print("done")
numbers = []
for counter in range(10000):
    numbers.append(random.randint(1, 1000))
#Next
startinsert = time.time()
insertionSort(numbers)
endinsert = time.time()
print("done")
print("The bubble sort took", endbubble - startbubble, "seconds")
print("The in-built sort function took", endpython - startpython, "seconds")
print("The insertion sort took", endinsert - startinsert, "seconds")
