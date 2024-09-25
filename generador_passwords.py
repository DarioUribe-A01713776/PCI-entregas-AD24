#El proyecto consite en un generador de passwords.
import random
import string
import secrets

def segmento_num():
    #Generamos un numero aleatorio seguro entre 0 y 99
    num = secrets.randbelow(100)
    #Pasamos el numero a un caracter
    return str(num)

def segmento_simbolos():
    #Defenimos el conjunto de simbolos
    simbolos = string.punctuation
    #Se toma un caracter aleatorio
    return secrets.choice(simbolos)

def segmento_letra_mn():
    #Se toma un letra minuscula aleatoriamente
    letra_minuscula = random.choice(string.ascii_lowercase)
    return letra_minuscula

def segmento_letra_my():
    #Se toma un letra mayuscula aleatoriamente
    letra_mayuscula = random.choice(string.ascii_uppercase)
    return letra_mayuscula

#Creamos un ciclo while para que el usuario pueda generar otra password
otro = "S"
while otro == "S":
    num_pswd = input("Deseas que tu password contenga números: S / N ").upper()
    simbolos_pswd = input("Deseas que tu password contenga simbolos: S / N ").upper()
    letra_pswd = input("Deseas que tu password contenga letra: S / N ").upper()

    password_generada = ""

    if num_pswd == "S":
        password_generada += segmento_num()
    if simbolos_pswd == "S": 
        password_generada += segmento_simbolos()
    if letra_pswd == "S":
        password_generada += segmento_letra_mn() + segmento_letra_my()

    if password_generada:
        print("Password generada: ",password_generada)
    else:
        print("No se genero ninguna password")
    
    otro = input ("Deseas generar otra password: S / N ").upper()
