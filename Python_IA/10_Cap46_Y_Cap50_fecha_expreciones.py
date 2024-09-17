# fecha con la libreria datetime
import os
import datetime
blue = "\033[34m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m" 

fecha = datetime.datetime.now()

print('\n', fecha, '\n')

input('Preciona enter para continuar......')
os.system('cls')


ahora = datetime.datetime.now()

print(ahora.strftime("Día de la semana abreviado: %a "))
print(ahora.strftime("Día de la semana completo: %A "))
print(ahora.strftime("Mes abreviado: %b "))
print(ahora.strftime("Mes abreviado: %B "))
print(ahora.strftime("Fecha completa: %c "))
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))
print(ahora.strftime("Día del mes (01 - 31): %d "))
print(ahora.strftime("Día/hora/año: %D "))
print(ahora.strftime("Día del mes (1 - 31): %e "))
print(ahora.strftime("Año en dos dígitos: %g "))
print(ahora.strftime("Año en cuatro dígitos: %G "))
print(ahora.strftime("Mes abreviado: %h "))
print(ahora.strftime("Hora (00 - 23): %H "))
print(ahora.strftime("Hora (01 - 12): %I "))
print(ahora.strftime("Día del año: %j "))
print(ahora.strftime("Mes del 01 al 12: %m "))
print(ahora.strftime("Minuto: %M "))
print(ahora.strftime("Salto de línea: %n"))
print(ahora.strftime("AM o PM: %p "))
print(ahora.strftime("Hora + AM o PM: %r"))
print(ahora.strftime("Hora y minutos: %R"))
print(ahora.strftime("Segundos: %S"))
print(ahora.strftime("Tabulación: %t"))
print(ahora.strftime("Hora, minutos y segundos: %T"))
print(ahora.strftime("Día de la semana (número): %u"))
print(ahora.strftime("Semana del año (empieza en domingo): %U"))
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))
print(ahora.strftime("Semana del año (empieza en lunes): %W"))
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))
print(ahora.strftime("Hora/minutos/segundos: %X"))
print(ahora.strftime("Año corto: %y"))
print(ahora.strftime("Año largo: %Y"))

input('Preciona enter para continuar......')
os.system('cls')


# funcion para buscar letras o cadenas

#libreria para la busqueda

import re

# Se crea un texto

texto = "3x + 2y -3z = 0"
busqueda = re.search("x", texto)
print('\n',busqueda )
busqueda2 = re.search('c', texto)
print(busqueda2, '\n')
#if busqueda != 'None':
#   print(texto[i])

input('Preciona enter para continuar......')
os.system('cls')
# utilizas findall para encontrar letras o string pero te arroja todas las coincidencias. 

texto = "tres tristes tigres comen trigo en un trigal"
busqueda3 = re.findall("e", texto)
print(busqueda3)

input('Preciona enter para continuar......')
os.system('cls')

# utilizas split() y sub() sirven para buscar y la de sub para modificar

texto = "hola mi nombre es edgar alejandro esparza palencia"
busqueda4 = re.sub(" ",  "-",  texto)
print(busqueda4)

texto = "hola mi nombre es edgar alejandro esparza palencia"
busqueda5 = re.split(" ",  texto)
print(busqueda5)
print(f'\n Se puede utilizar en una {blue} ecuacion{reset} para que quite las letras y solo quede el numero y el simbolo')
texto2='3x+4y-5z=0'
busqueda6 = re.split('x', texto2)
tx1 = busqueda6[1]
busqueda7 = re.split('y', tx1)
tx2 = busqueda7[1]
busqueda8 = re.split('z', tx2)
print('\n',texto2)
print('\n', busqueda6[0], busqueda7[0],busqueda8[0])

input('Preciona enter para continuar......')
os.system('cls')


# Cap 50 y practicmente se explican metacaracteres y secuencias especiales como es /d /D o [1-2], [a-d] que solo buscan el rengo puesto o especificado
# tambien los {2} o .. que es para que en una cadena de caracteres no importe si hay letras que no contemplas como en programacion

texto = "Bienvenidos a Programación fácil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto)
print(buscar)

input('Preciona enter para continuar......')
os.system('cls')

# Try valida si la variable see declaro anteriormente y except es para manejar en dicho caos que no se declarara. 

variable = "Correcto."

try:
	print(variable)
except:
	print("La variable no está declarada.")
	
input('Preciona enter para continuar......')
os.system('cls')
