#El proyecto consite en un generador de passwords.
#Para que las passwors sean mas seguras, se crearan numeros apartir de la suma de dos numero aleatorios
import random
import string

def generar_primer_segmento_contrasena():
    # Generar dos números aleatorios
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    resultado = num1 + num2
    caracter = chr((resultado % 94) + 33) #convertimos el numero a un caracter
    return caracter

def generar_segundo_segmento_contrasena():
    #generamos tres numero aleatorios
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3=random.randint(1,9)
    # para que la contrasena sea mas segura, vamos a generar un numero
    # que es el resultante de la division del producto de tres numeros 
    # generados aleatoriamente
    caracter = (num1*num3)//num2
    return caracter

def letra_azar_mayuscula():
    letra = random.choice(string.ascii_lowercase)  # Selecciona una letra al azar de las minúsculas
    return letra.upper()  # Convierte la letra a mayúscula

def letra_azar_minuscula():
    letra = random.choice(string.ascii_uppercase)  # Selecciona una letra al azar de las mayúsculas
    return letra.lower()  # Convierte la letra a minúscula
num = int
signo = ""
mayusculas = ""
minusculas = ""

segmento_num = int (input("Desea que su password contenga números: 1. Si / 2.No "))
segmento_signos = int (input("Desea que su password contenga signos: 1. Si / 2.No "))
segmento_minusculas = int (input("Desea que su password contenga letras minusculas: 1. Si / 2.No "))
segmento_mayusculas = int (input("Desea que su password contenga letras mayusculas: 1. Si / 2.No "))
if segmento_num == 1: 
    num = generar_segundo_segmento_contrasena
    password = f"{num}"
elif segmento_signos == 1:
    signo = generar_primer_segmento_contrasena
    password = f"{signo}"
elif segmento_minusculas == 1:
    minusculas = letra_azar_minuscula 
    password = f"{minusculas}"
elif segmento_mayusculas == 1:
    mayusculas = letra_azar_mayuscula
    password = f"{mayusculas}"
print (f"Password generada: {password}")
