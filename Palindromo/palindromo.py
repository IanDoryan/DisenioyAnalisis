def es_palindromo(cadena):
    n = len(cadena)
    inv = []
    j = n - 1
    for i in range(n):
        inv.append(cadena[j])
        j -= 1
    inv = "".join(inv)

    if inv == cadena:
        return True
    else:
        return False