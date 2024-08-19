# PCI-entregas-AD24
Repositorio para la entrega de actividades y proyectos para "Pensamiento Computacional para Ingeniería" AD24


**PROYECTO**

## GENERADOR DE CONTRASEÑAS
Consiste en un programa que permita al usuario generar contraseñas seguras basadas en ciertas características que el mismo usuario va establecer, como puede ser: longitud de la contraseña, uso de letras mayúsculas, uso de letras minúsculas, uso de números o uso de caracteres especiales.

A continuación el algoritmo pensado para la creación del proyecto:

**Entradas:**

 - Longitud de la contraseña: valor entero
 - Letras mayúsculas: (Si / No)
 - Letras minúsculas: (Si / No
 - Números: (Si / No)
 - Caracteres especiales: (Si / No)


 **Salidas:**
 
 - Contraseña generada 


**Algoritmo:**

 1. Inicio. 
 2. Solicitar la longitud de la contraseña.
 
 3. Solicitar el uso de mayúsculas.

 4. Solicitar el uso de minúsculas.
 5. Solicitar el uso de números.
 6. Solicitar el uso caracteres especiales.
 7. Validar opciones.
 8. Si uso de mayúsculas = "Si"
 8.1  Crear una lista de caracteres con mayúsculas de la A a la Z.
 9. Si uso de minúsculas = "Si"
 9.1 Agregar a lista minúsculas de la a a la z.
 10. Si uso de números = "Si"
 10.1 Agregar a lista números del 0 al 9.
 11. Si uso de caracteres especiales = Si
 11.1 Agregar a lista caracteres !@#$%*
 12. Desde i=1 hasta i=longitud de contraseña 
 13. Contraseña generado(i) = lista de caracteres (número aleatorio)
 14. Imprimir contraseña generada.
 15. Fin
