
def primos(a):

    x = []
    for i in a:
        if i < 2:
            continue
        primo = True
        for j in range(2, int(i**0.5) + 1):
            if (i % j) == 0:
                primo = False
        if primo:
            x.append(i)
    return f"Los números primos son: {x}"

a = [int(n) for n in input("Ingrese sus números separados por coma: ").split(',')]
print(primos(a))