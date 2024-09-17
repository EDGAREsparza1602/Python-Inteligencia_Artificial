# Color azul en ANSI
blue = "\033[34m"
reset = "\033[0m"
red = "\033[31m"

Colores1 = ["rojo", "azul", "verde", "amarillo", "marron", "lila", "negro", "rosa",]

# El color rojo se encuentra en la posision 0
print('----------------------------------------------\n')
print('\nEjercicios ' + f"{blue}capitulo 10{reset}" + '\nSe imprimira el color de la ultima posision')
print(f'{red}{Colores1[7]}{reset}')
print("\n")

# El color rosa se encuentra en la posision 7  
# Ejercicio de listas

Lista1 = ["tres", "dos", "cinco", "cuatro", "uno"]

#-------------------------------------------------------

# Capitulo 11 ejercicios y ejemplos
print('----------------------------------------------\n')
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 11{reset}" + '\nSe imprime los colores propuestos')
print(f'{red}{colores[-1]}{reset}')
print(f'{red}{colores[-10]}{reset}')
print(f'{red}{colores[-7]}{reset}')
print(f'{red}{colores[-7+2]}{reset}')
print(f'{red}{colores[-2]}{reset}')
input('Presiona enter para continuar....')

# Capitulo 12 Eliminar elementos de una lista con del

print('----------------------------------------------\n')
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 12{reset}" + ' Se eliminan los colores propuestos y se imprime la lsita')
del colores[1]
del colores[3]
del colores[-4]
del colores[-3]
print('\nLista despues de eliminar los colores propuestos\n')
print(f'{red}{colores}{reset}')
input('Presiona enter para continuar....')


# Capitulo 13 Eliminar elementos de una lista con remove

print('----------------------------------------------\n')
colores2 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 13{reset}" + ' Se eliminan los colores propuestos y se imprime la lista')
colores2.remove('amarillo' and'rojo')
print (f'\n{red}{colores2}{reset}')
input('Presiona enter para continuar....')


# Capitulo 14 Eliminar elementos de una lista con pop

print('----------------------------------------------\n')
colores4 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 14{reset}" + ' Se eliminan los colores propuestos y se imprime la lista')
primer_color_eliminado = colores4.pop(1)
segundo_color_eliminado = colores4.pop(-2)
print (f'\n{red}{colores4}{reset}')
print ('\n Los colores eliminados son: ', primer_color_eliminado + ', ' + segundo_color_eliminado)
input('Presiona enter para continuar....')

# Capitulo 15 insertar valores con append

print('----------------------------------------------\n')
colores5 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 15{reset}" + ' Se insertara un color que tu elijas en la ultima posicion')
print(f'\n{red}{colores5}{reset}\n')

# Se preguntan los colores a ingresar

col = input('\nIngrese un color para insertar:\n' )
col2 = input('\nIngrese un color para insertar:\n' )

# Se ingresa ambos colores a la lista colores5

colores5.append(col)
colores5.append(col2)

# Se muestra en azul la tabla con los colores añadidos.

print(f'\n{blue}{colores5}{reset}\n')
input('Presiona enter para continuar....')
      
# Capitulo 16 insertar valores con insert (puedes decir la posision)

print('----------------------------------------------\n')
colores5 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 16{reset}" + ' Se insertara un color que tu elijas en la posicion elejida')
print(f'\n{red}{colores5}{reset}\n')

# Se ingresan los colores

color = input('\nIngrese un color para insertar:\n' )
color1= input('\nIngrese un color para insertar:\n' )

# Se ingresa la posision en negativo
posicion = int(input(f'Ingrese la posicion en negativo de {color}: \n'))
posicion1 = int(input(f'Ingrese la posicion en negativo de {color1}: \n'))
 
# Se insertan los datos en la lista

colores5.insert(posicion, color)
colores5.insert(posicion1, color1)
print(f'\n{blue}{colores5}{reset}\n')
input('Presiona enter para continuar....')


# Capitulo 17 ordenar la lista de colores por orden alfabetico az y za

print('----------------------------------------------\n')
colores6 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Ejercicios ' + f"{blue}capitulo 17{reset}" + ' Se ordenara la lista de A-Z ')
print(f'\n{red}{colores5}{reset}\n')

colores6 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores6.sort(reverse=False)
print(f'{colores6}\n')
print('Ahora se ordenara de orden Z-A')
colores6.sort(reverse=True)
print(f'\n{colores6}')


# Capitulo 18 se utiliza len para que cuente los elemetos. 

print('\nEjercicios ' + f"{blue}capitulo 18{reset}" + 'Se aplica len para contar los elementos de la lsita')
print('\n Se realizara el conteo de la lista de arriba \n')
print(len(colores6))

