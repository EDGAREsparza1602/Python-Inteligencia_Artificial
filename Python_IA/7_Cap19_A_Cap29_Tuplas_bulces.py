import os

# Color azul en ANSI
blue = "\033[34m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m" 

# Capitulo 19 manejo de tuplas con numero y demas cosas.

print('\nEjercicios ' + f"{blue}capitulo 19{reset}" + ' Manejo de tuplas con numero y demas cosas\n')

colores10 = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
numeros = (10, 1, 5, 11)
print(colores10,'\n',colores10[2],'\n', numeros[0] + numeros[2] + numeros[3] - numeros[1])

input('Presiona enter para continuar....')
os.system('clear')
# Capitulo 20 convertir listas a tuplas.

print('\nEjercicios ' + f"{blue}capitulo 19{reset}" + ' Covertir listas a tuplas\n')
colore10 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colore10)
tupla = tuple(colore10)
print(type(tupla))
print(tupla)
input('Presiona enter para continuar....')
os.system('clear')
# Capitulo 21 Condicion if mas operadores

num1 = 15
num2 = 20

if num1 != num2:
	print('\nSe cambia el opreador "==" por "!=" diferente')
	print('Se ejecuta el if.')
num1 = 1450
num2 = 60

if num1 > num2:
	print('\nSe cambia el opreador "<" por ">" mayor que')
	print('Se ejecuta el if.')
num1 = 1450
num2 = 1450

if num1 != num2:
	print('Se ejecuta el if.')
	
print('\nSe igualaron los valores, no se ejecuto el if')

input('Presiona enter para continuar....')
os.system('clear')
# Capitulo 22 Condicion if mas operadores

color=input('\ningrese el color rojo: ')
if color == 'rojo':
    print('\nEl color es rojo.')
else:
    print("\nEl color no es rojo.")
input('Presiona enter para continuar....')
os.system('clear')
# Capitulo 23 Condicion if, elif

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de 18 pero menor de 45')
elif edad >= 100 and edad <= 120:
	print('Estas muerto padrino')
else:
	print('Edad no válida.')
input('Presiona enter para continuar....')
os.system('clear')
    # Capitulo 24 ejercicio de comparacion de datos.
	

naveg=input('Ingrese un navegador: ')
navegadores = ['chrome', 'firefox', 'opera', 'safari']

if naveg in navegadores and naveg == navegadores[0]:
	print('El navegador seleccionado es chrome')
elif naveg in navegadores and naveg == navegadores[1]:
    print('El navegador seleccionado es firefox')
elif naveg in navegadores and naveg == navegadores[2]:
    print('El navegador seleccionado es opera')
elif naveg in navegadores and naveg == navegadores[3]:
	print('El navegador seleccionado es safari')
else:
	print('El navegador ingreado no esta en la lista')
input('Presiona enter para continuar....')
os.system('clear')
    # Capitulo 25 y 26 ejercicio varias condiciones if y tips para condiciones


num3=int(input('ingrese el primer valor: \n'))
num4=int(input('ingrese el segundo valor: \n'))
if num3 > num4: print('El primer numero es mayor') 
if num3 < num4: print('El segundo valor es mayor') 
if num3 == num4: print('Los numeros son iguales') 

input('Presiona enter para continuar....')
os.system('clear')

   # Capitulo 27 crear bucles con while 

x=0
print('\nResultado\n')
while x < 16:
	print(x)
	x += 5

y = 0
print('\nResultado\n')
while y > -101:
	print(y)
	y -= 20

print('\nResultado\n')
z = 10
while  0 < z:
	print(z)
	z -= 1
input('Presiona enter para continuar....')
os.system('clear')
   # Capitulo 28 crear bucles con while con condicion if

print('\n\n')
print('Ejercicio con bucle y condicion if')
x = 0
while x <= 30:
	x += 1
	if x == 4 or x == 6 or x == 10: 
		print(f'Se saltó el valor  {red}{x}{reset}') 
		continue
	if x == 15: 
		print(f'Se rompió la ejecución del bucle cuando x valía {red}{x}{reset}') 
		break
	if x != 4 or x != 6 or x != 10: 
		print(f'{blue}{x}{reset}')

input('Presiona enter para continuar....')
os.system('clear')
   # Capitulo 29 crear bucles for


colores = ('rojo','azul','verde','amarillo')

for x in colores: 

	if x == 'rojo': print(f'El color es: {red}{x}{reset}')
	if x == 'azul': print(f'El color es: {blue}{x}{reset}')
	if x == 'verde': print(f'El color es: {green}{x}{reset}')
	if x == 'amarillo': print(f'El color es: {yellow}{x}{reset}')
input('Presiona enter para continuar....')
os.system('clear')

    # Capitulo 30 Utilizar el bucle for con la funcion range()

print('Se utilizara la funcion rangue con el bucle range')

for x in range(7, 700, 100):
	print(x)

input('Presiona enter para continuar....')
os.system('clear')