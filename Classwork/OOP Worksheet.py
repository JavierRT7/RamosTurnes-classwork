class Dog:
    #public
    #name
    #colour
    def __init__(self, my_name, bark):
        self.name = my_name
        self.colour = ''
        self.bark = bark
    def set_colour(self, my_colour):
        if my_colour in ('Brown', 'Black', 'Champagne'):
            self.colour = my_colour
        #End If
    #End procedure
    def get_colour(self):
        return self.colour
    #End Function
class Puppy(Dog):
    def __init__(self, my_name, bark):
        super().__init__(my_name, bark)
        self.shoesChewed = shoesChewed
        self.bark = bark
    #end procedure
    def chewShoe(self, shoesChewed):
        self.shoesChewed = self.shoesChewed + 1
    #end procedure
    def getShoesChewed(self):
        return self.shoesChewed
    #end function
#end class
#end class
shoesChewed = 0
my_dog1 = Dog('Juno', 'Awhoooooo')
my_dog2 = Dog('Domino', 'Woof!')
puppy = Puppy('Juno Jr', 'Yap!')
puppy2 = Puppy('Domino Jr', 'Ruff!')
dog_list = [my_dog1, my_dog2, puppy, puppy2]
#my_dog1.name = 'Fido'
#my_dog2.name = 'Rex'
my_dog1.set_colour('Champagne')
my_dog2.set_colour('Black')
puppy.set_colour('Brown')
puppy2.set_colour('Black')
for counter in range(1, 3):
    puppy.chewShoe(puppy.shoesChewed)
#Next
for counter in range(1, 48):
    puppy2.chewShoe(puppy.shoesChewed)
#Next
print(puppy.name)
print(puppy.get_colour())
print(puppy.name, 'has chewed', puppy.getShoesChewed(), 'shoes')
print(puppy2.name)
print(puppy2.get_colour())
print(puppy2.name, 'has chewed', puppy2.getShoesChewed(), 'shoes')
print(my_dog1.name)
print(my_dog1.get_colour())
print(my_dog2.name)
print(my_dog2.get_colour())
