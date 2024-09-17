import os

# Color azul en ANSI
blue = "\033[34m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m" 


teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

consulta = teclado2['Modelo']
consulta1 = teclado2['Precio']
print(f'\n El modelo {blue}{consulta}{reset} cuesta ${blue}{consulta1}{reset} \n')

input('Preciona enter para continuar......')
os.system('cls')


# 32 Iterar un diccionario con un bulce for que muestre las columnas y los valores

# Como los directorios estan creados en la parte de arriba no es necesario volverlos a crear para este ejercicio. 

for x in teclado1:
    print(f'{x}: {blue}{teclado1[x]}{reset}')
input('Preciona enter para continuar......')
os.system('cls')

# 33 Iterar un diccionario con un bulce for que muestre las columnas y los valores

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2)
input('Preciona enter para continuar......')
os.system('cls')


# 34 funciones con argumentos.

def Suma(num_1, num_2):
    resultado = num_1 + num_2
    print(f'\n La suma de {num_1} + {num_2} = {resultado} \n')

pnum1=15
pnum2=15
Suma(pnum1,pnum2)
snum1=20
snum2=30
Suma(snum1, snum2)
tnum1=3000
tnum2=54000
Suma(tnum1, tnum2)

input('Preciona enter para continuar......')
os.system('cls')

# 35 funciones con argumentos y args.



def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')


def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('azul', 'rojo')

def suma5(*args):
     resultado = args[0] + args[1] + args[2] + args[3] + args[4]
     print(f'El resultado de la suma es: {resultado}')
     
suma5(10,12,12,3,4)
input('Preciona enter para continuar......')
os.system('cls')

# 36 funciones con argumentos y kwargs con los diccionarios.


def colores (**kwargs):
	print("Este es el color " + kwargs['color2'] + '.')

colores(color1='rojo', color2='azul')
input('Preciona enter para continuar......')
os.system('cls')

