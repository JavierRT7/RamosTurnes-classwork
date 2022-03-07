import random
import time
def quicksort(arr):
  if len(arr) <= 1:
    return arr

  left  = []
  right = []
  equal = []
  pivot = arr[-1]
  for num in arr:
    if num < pivot:
      left.append(num)
    elif num == pivot:
      equal.append(num)
    else:
      right.append(num)

  return quicksort(left) + equal + quicksort(right)

arr1 = []
for i in range(998):
    arr1.append(i)
arr2 = []
for i in range(998):
    arr2.append(random.randint(1,998))
arr3 = []
for i in range(998):
    arr3.append(998-i)
start1 = time.time()
quicksort(arr1)
end1 = time.time()
start2 = time.time()
quicksort(arr2)
end2 = time.time()
start3 = time.time()
quicksort(arr3)
end3 = time.time()
print(end1-start1)
print(end2-start2)
print(end3-start3)