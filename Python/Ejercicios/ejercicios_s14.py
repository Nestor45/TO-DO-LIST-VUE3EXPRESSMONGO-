## CONJUNTOS ##
my_digits = {8,3,6,6,"hola"}
print(my_digits)

my_digits.remove("hola")
print(my_digits)

print(8 in my_digits) #Is True

print(my_digits)

letters = {'a', 'b','c','d','e','f','g','a'}
vowels = {'a','e','i','o','u'}

letters.add('h')
print(letters)
print(vowels)

print(letters.union(vowels))
print(vowels.union(letters))

print(vowels | letters | {'a', 'b', 'h', 'y'})

# Diccionarios #

my_dict = {
    'jugador': 'Messi',
}