#El proyecto consite en un generador de passwords.
#Para que las passwors sean mas seguras, se crearan numeros apartir de la suma de dos numero aleatorios
# .
import random

def generar_segmento_contrasena():
    # Generar dos números aleatorios
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    
   
    resultado = num1 + num2
    
    
    caracter = chr((resultado % 94) + 33)
    
    return caracter

# Este sería solo un segmento de la contraseña
segmento = generar_segmento_contrasena()
print("Segmento de la contraseña:", segmento)
