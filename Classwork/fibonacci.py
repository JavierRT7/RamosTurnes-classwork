fibonacci = []
old_value = 1
value = 1
print(old_value)
print(value)
for counter in range(1000):
    temp = value + old_value
    print(temp)
    fibonacci.append(temp)
    old_value = value
    value = temp