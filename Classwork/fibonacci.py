def i(x,y,z): 
    for i in range(100):
        print(z)
        x=y
        y=z
        z=x+y
i(0,0,1)
def r(y,z,i):
    i+=1
    print(z)
    if i<100:
        r(z,y+z,i)
r(0,1,0)