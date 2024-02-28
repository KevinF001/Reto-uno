
def operacion(a):

    if a[2] == '+':
        return f"El resultado de la suma es: {int(a[0]) + int(a[1])}"
    elif a[2] == '-':
        return f"El resultado de la resta es: {int(a[0]) - int(a[1])}"
    elif a[2] == '*':
        return f"El resultado de la multipliación es: {int(a[0]) * int(a[1])}"
    elif a[2] == '/' and int(a[1]) != 0:
        return f"El resultado de la división es: {int(a[0]) / int(a[1])}"
    else:
        return "Operación no valida"

a = ([str(entrada) for entrada in input("Ingrese sus dos valores a operar y el simbolo de la operación, separados por comas: ").split(',')])
print(operacion(a))
