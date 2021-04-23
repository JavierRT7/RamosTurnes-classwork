import random
import time

numbers = []
for counter in range(200):
    numbers.append(random.randint(1, 1000))
#Next

def bubbleSort(numbers):
    print(numbers)
    temp = 0
    for count in range(len(numbers) * len(numbers)):
        for counter in range(len(numbers) - 1):
            if numbers[counter] > numbers[counter + 1]:
                temp = numbers[counter]
                numbers[counter] = numbers[counter + 1]
                numbers[counter + 1] = temp

    print(numbers)
def insertionSort(numbers):
    print(numbers)
    for count in range(len(numbers) - 1):
        nextNum = numbers[count]
		counter = count – 1
		while counter >= 0 and numbers[counter] > nextNum
			numbers[counter + 1] = numbers[counter]
       		counter = counter - 1    
    	numbers[counter + 1] = nextNum
    print(numbers)
startbubble = time.time()
bubbleSort(numbers)
endbubble = time.time()
print("The bubble sort took", endbubble - startbubble, "seconds")
numbers = []
for counter in range(200):
    numbers.append(random.randint(1, 1000))
#Next
startpython = time.time()
print(numbers)
numbers.sort()
print(numbers)
endpython = time.time()
print("The in-built sort function took", endpython - startpython, "seconds")
numbers = []
for counter in range(200):
    numbers.append(random.randint(1, 1000))
#Next
startinsert = time.time()
insertionSort(numbers)
endinsert = time.time()
print("The insertion sort took", endinsert - startinsert, "seconds")
