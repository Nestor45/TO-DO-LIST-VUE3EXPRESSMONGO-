#Serie de ULAM
#n = int(input("Ingrese el numero: "))
# while n > 0:
#     print(n)
#     if n == 1:
#         break
#     elif n % 2 == 0:        
#         n = n // 2
#     else:
#         n = 1+(n*3)

# while n > 1:
#     print("HOLA",n)
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 1+(n*3)

n = int(input("ingrese los primeros n pares de numeros"))
c = 0
p = 0
while c <= n:
    print(p, end=" ")
    p += 2
    c += 1