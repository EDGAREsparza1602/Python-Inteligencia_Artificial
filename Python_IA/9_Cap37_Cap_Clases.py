import os

# Color azul en ANSI
blue = "\033[34m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m" 


# 37 y 38 Clses con su respectivo objeto.

class telefono:
	# Practicamente la funcion __int__
	def __init__(self, Tipo, Precio):
		self.Tipo = Tipo
		self.Precio = Precio
      
	def imprimir_tipo(self): 
		print('\nEl celular ingresado es:', self.Tipo, '\n Su precio es:', self.Precio)

# Se declara el objeto con el que se podra acceder a las variables tipo y precio
C=input('Ingrese el nombre del celular: \n')
P=input('Ingrese el precio del telefono: \n')

telefono_obj = telefono(C,P)

# Se guarda en sus variables el contenido ingresado por el usuario.

#C=input('Ingrese el nombre del celular: \n')
#P=input('Ingrese el precio del telefono: \n')
#telefono_obj.Tipo=C
#telefono_obj.Precio=P

#Se mandan los valores a la funcion para imprimir. \

telefono_obj.imprimir_tipo()



input('Preciona enter para continuar......')
os.system('cls')



#39 a 51 Clses con su respectivo objeto.
def var_globales():
	global hola, nom, nom1, nom2
	hola = f'\nBienvenido al programa numero 9 de la clase de {blue}inteligencia artificial{reset}\n'
class persona:
    def __init__(self, padre, edad):
        # Aquí defines las variables de la clase
        self.padre = padre
        self.edad = edad
    def imprimir(self):
		    print(f'\nEl nombre ingresado es: {self.padre} \nLa edad ingresada es:  {self.edad}')

class hijo(persona):
    def __init__(self, nombre, edad, madre, padre):
        # Llamamos al constructor de la clase base (persona)
        super().__init__(padre, edad)
        # Asignamos los atributos madre y padre
        self.madre = madre
        self.nombre = nombre
    def imprimir_hijo(self):
		    print(f'\nEl nombre de tu hijo es: {self.nombre} \nsu edad ingresada es:  {self.edad}\n La madre y el padre son: {self.madre} y {self.padre}')
var_globales()
print(hola)
N = input('Ingrese su nombre: ')
E = input('Ingrese su edad: ')

Persona1 = persona(N, E)

Persona1.imprimir()
op = input('Los datso ingresados son correctos: ')
if op == 'si':
	hi=input('Tienes hijos: ')
	if hi == 'si':
		nom=input('Cual es su nombre: ')
		nom1=input('Cual es su edad: ')
		nom2=input('Cual es el nombre de su mama: ')
		hijo1 = hijo(nom,nom1,nom2,N)
		hijo1.imprimir_hijo()
		input('Preciona enter para continuar......')
		os.system('cls')
elif op == 'no':
    modi = input('Ingrese lo que desea cambiar: ')
    if modi == 'nombre':
        N = input('Ingrese el nombre: ')
        Persona1.padre = N
        Persona1.imprimir()
        hi=input('Tienes hijos: ')
        if hi == 'si':
            nom=input('Cual es su nombre: ')
            nom1=input('Cual es su edad: ')
            nom2=input('Cual es el nombre de su mama: ')
            hijo1 = hijo(nom,nom1,nom2,N)
            hijo1.imprimir_hijo()
            input('Preciona enter para continuar......')
            os.system('cls')
    if modi == 'edad':
        ed = input('Ingrese la edad: ')
        Persona1.edad = ed
        Persona1.imprimir()
else:
	print('El valor ingresado no coincide con las respuestas.')
	input('Preciona enter para continuar......')
	os.system('cls')


## Programa matematicos 

import math

class Operaciones:
    def __init__(self, numero1, numero2, resultado=0):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = resultado

    def suma(self):
        self.resultado = self.numero1 + self.numero2
        print('La suma es: ', self.resultado)

    def resta(self):
        self.resultado = self.numero1 - self.numero2
        print('La resta es: ', self.resultado)

# Pedir los números como enteros
N1 = float(input('Ingresa el primer número: '))
N2 = float(input('Ingrese el segundo número: '))
res = 0

# Crear el objeto de operaciones
op = Operaciones(N1, N2, res)

# Ejecutar las operaciones
op.suma()
op.resta()

# Funciones lambda para la división y multiplicación
divi = lambda: (N1 / N2)
print('División: ', divi())

mult = lambda: (N1 * N2)
print('Multiplicación: ', mult())

input('Preciona enter para continuar......')
os.system('cls')
