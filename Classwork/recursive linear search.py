import random

def search(list, count, value):
    if list[count] == value:
        return count
    else:
        return search(list, count + 1, value)

count = 0
list = []
for x in range(1000):
    list.append(random.randint(1,1000))
value = int(input("What number do you want to find?"))
if value in list:
    print("That value is at index " + str(search(list, count, value)))
else:
    print("That value is not in the list")