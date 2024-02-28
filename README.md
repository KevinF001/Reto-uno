# Reto-uno

# Punto 1
# Problema: Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3)
Pasos:
Definición de la función operacion(a):

La función operacion toma una lista a como argumento.
Esta función evalúa el tercer elemento de la lista a para determinar el tipo de operación a realizar.
Determinación de la operación:

Se utiliza un condicional if-elif-else para identificar el tipo de operación basado en el tercer elemento de la lista a.
Realización de la operación:

Si el tercer elemento de a es +, se realiza una suma utilizando los primeros dos elementos de la lista a.
Si el tercer elemento de a es -, se realiza una resta utilizando los primeros dos elementos de la lista a.
Si el tercer elemento de a es *, se realiza una multiplicación utilizando los primeros dos elementos de la lista a.
Si el tercer elemento de a es / y el segundo elemento de a no es cero, se realiza una división utilizando los primeros dos elementos de la lista a.
Manejo de casos especiales:

Se verifica si el segundo elemento de a es cero en el caso de una división para evitar una división por cero.
Impresión del resultado:

El resultado de la operación se imprime utilizando f-strings para formatear el mensaje.
Entrada de usuario:

Se solicita al usuario que ingrese dos valores y el símbolo de la operación, separados por comas.
Los valores ingresados se convierten a cadenas de texto y se almacenan en una lista a.
Llamada a la función operacion(a):

Se llama a la función operacion con la lista a como argumento.
El resultado de la operación se imprime en la consola.
