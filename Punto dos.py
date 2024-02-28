
def palindromo(a):
    
    x = -1
    for i in a:
        if i != a[x]:
            return "No es palíndromo"
        x -= 1
    return f"{a} sí es un palíndromo"

a = str(input("Ingrese su palabra a analizar: "))
print(palindromo(a))