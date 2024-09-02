#El proyecto consite en un generador de passwords.
#Para que las passwors sean mas seguras, se crearan numeros apartir de la suma de dos numero aleatorios
import random

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



# Este sería solo el primer segmento de la contraseña
primer_segmento = generar_primer_segmento_contrasena()
print(f"Segmento de la contraseña: {primer_segmento}")

# Este seria solo el segundo segmento de la contrasena
segundo_segmento = generar_segundo_segmento_contrasena()
print(f"Segmento de la contrasena: {segundo_segmento}")

#Esta seria la contrasena generado por el momento
contrasena_generada = f"{primer_segmento}{segundo_segmento}"
print(f"Tu contrasena es: {contrasena_generada}")