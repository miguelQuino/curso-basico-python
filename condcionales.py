
# primero cdeclaras una  variable
calificacion= input("Introduce tu calificacion del AZ-900: ")
calificacion = int(calificacion)
#Preguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("ves, por no estudiar") # si esmenor a 700, muestra esto
elif calificacion > 100:
    print("calificacion invalida")
else: # si no se cumple el if anterior , pasa esta linea 
    print("Felicidades pasa por tu certificado")#se ejecuta si ninguno de los if se cumple
 
#verificador de edad    
edad= input("introduce tu edad: ")
edad=int(edad)
if edad >= 18 and edad <= 100 :
    print("Bienvenido a la adultez")
elif edad > 100:
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajero del timepo")
else:
    print("Eres menor de edad")

# En python no hay switch case
