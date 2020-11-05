class Dog:
    #public
    #name
    #colour
    def __init__(self, my_name):
        self.name = my_name
        self.colour = ''

my_dog1 = Dog('Fido')
my_dog2 = Dog('Rex')

#my_dog1.name = 'Fido'
#my_dog2.name = 'Rex'
my_dog1.colour = 'Brown'
my_dog2.colour = 'Black'

print(my_dog1.name)
print(my_dog1.colour)
print(my_dog2.name)
print(my_dog2.colour)
