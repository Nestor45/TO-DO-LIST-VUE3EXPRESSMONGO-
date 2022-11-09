## 1. crear la serie de [0.1,0.2,0.3,...1.0] ##

list1 = [i/10 for i in range(1,11)]
print(list1)

list2 = [i**0.5 for i in range(1,51)]
print(list2)

list3 = [1/i for i in range(-10,10) if i!=0]
print(list3)

my_tuple= (1,1,'nestor','alvarez')
my_other_tuple = (['hola']*4)
print(my_tuple)
print('alvarez' in my_tuple)