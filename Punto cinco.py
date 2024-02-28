
def mismos_caracteres(a):

    x = []
    for i in range(len(a)):
        conjunto_palabra = set(a[i])
        for j in range(i + 1, len(a)):
            conjunto_comparar = set(a[j])
            if conjunto_palabra == conjunto_comparar and a[j] not in x:
                x.append(a[i])
                x.append(a[j])

    return f"Las palabras con los mismos caracteres son: {set(x)}"


a = [palabra.strip() for palabra in input("Ingrese sus palabras separadas por comas: ").split(',')]
print(mismos_caracteres(a))