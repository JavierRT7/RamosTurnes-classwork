import random
correct=0
for x in range(100):
    number=[]
    for y in range(6):
        number.append(random.randint(1,9))
    check=(number[0]+(number[1]*3)+number[2]+(number[3]*3)+number[4])%10
    if check==number[5]:
        correct=correct+1
print(correct)


