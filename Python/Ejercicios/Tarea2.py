# Ejercicio 2. ¿Llegarás o no a tiempo a tu destino?
# Ejecución 1
# ¿Cuál es tu velocidad promedio en km/hr [1-200]? 110
# Cuántos kilómetros te hacen falta [> 0]? 110
# En cuántos minutos tienes que llegar [> 0]? 59
# Lo siento, no llegarás a tiempo. Llegarás 1 minuto(s) tarde.

# Ejecución 2
# ¿Cuál es tu velocidad promedio en km/ hr [1-200]? 110
# ¿Cuántos kilómetros te hacen falta [> 0]? 110
# ¿En cuántos minutos tienes que llegar [> 0]? 61
# Felicidades. Llegarás 1 minuto(s) más temprano.
# V = 110 km/h. D = 110 km. Tobj = 59 min. T = ?
# V = D/T. VT = TD/T.  VT = D. VT/V = D/V. T = D/V

velocity = float(input("¿Cuál es tu velocidad promedio en km/hr [1-200]?"))
if velocity < 0 or velocity > 200:
    print("Velocidad no válida, te asignaré el más cercano: 200.")
    velocity = 200.0

km = float(input("¿Cuántos kilómetros te hacen falta [> 0]?"))
if km <= 0:
    print("Kilómetros no válidos, te asignaré 1.")
    km = 1.0

t = km / velocity
t = t * 60
print(f"minutos: {t}")

min = float(input("¿En cuántos minutos tienes que llegar [> 0]?"))

if min < 0:
    print("Minutos no válidos, te asignaré 1.")
    min = 1.0


if (min-t) > 0 and (min-t) < 1:
    print(f"Felicidades. Llegarás {min-t} minuto(s) más temprano.")
elif min-t == 0:
    print(f"Felicidades. Llegarás justo a tiempo")
elif (min-t) > 0:  
    print(f"Felicidades. Llegarás {int(min-t)} minuto(s) más temprano.")
else:
    print(f"Lo siento, no llegarás a tiempo. Llegarás {int(abs(min-t))} minuto(s) tarde.")