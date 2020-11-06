class Dog:
    #public
    #name
    #colour
    def __init__(self, my_name):
        self.name = my_name
        self.colour = ''
    def set_colour(self, my_colour):
        if my_colour in ('Brown', 'Black'):
            self.colour = my_colour
        #End If
    #End procedure
    def get_colour(self):
        return self.colour
    #End Function
    class Puppy:
        def __init__(self, shoesChewed):
            shoesChewed = 0
        #end procedure
        def chewShoe():
            shoesChewed = shoesChewed + 1
        #end procedure
        def getShoesChewed():
            return shoesChewed
        #end function
    #end class
#end class
my_dog1 = Dog('Fido')
my_dog2 = Dog('Rex')

#my_dog1.name = 'Fido'
#my_dog2.name = 'Rex'
my_dog1.set_colour('Brown')
my_dog1.set_colour('XYZ')
my_dog2.set_colour('Black')
puppy = Puppy('Dog')
for counter in range(1, 3):
    chewShoe()
#Next

print(my_dog1.name)
print(my_dog1.get_colour())
print(my_dog2.name)
print(my_dog2.get_colour())
