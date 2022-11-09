print("Hola mundo")

number = 10
def func(number = 0):
    number += 90
    return number

number = 20
print(number, func(), func(10))