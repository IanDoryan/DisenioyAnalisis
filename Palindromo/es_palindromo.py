def es_palindromo(cadena):
    n = len(cadena)
    j = n - 1
    for i in range(n // 2):
        if cadena[i] != cadena[j]:
            return False
        j -= 1
    return True