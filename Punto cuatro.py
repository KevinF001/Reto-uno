
def suma_mayor(a):

    a = sorted(a)
    x = -1
    for i in range(len(a) - 1):
        if a[x] - a[x-1] == 1:
            return f"Los dos elementos de mayor valor consecutivo son: {a[x]} y {a[x-1]} y su suma es: {a[x] + a[x-1]}"
        elif a[x] - a[x-1] == -1:
            return f"Los dos elementos de mayor valor consecutivo son: {a[x]} y {a[x-1]} y su suma es: {a[x] + a[x-1]}"
        x -= 1
    return "No existen dichos elementos"


a = [int(n) for n in input("Ingrese sus números separados por coma: ").split(',')]
print(suma_mayor(a))