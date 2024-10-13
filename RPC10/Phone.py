def contar_digitos_distintos(telefono):
    telefono = telefono.replace("-", "")
    digitos_distintos = set(telefono)
    return len(digitos_distintos)

telefono = input("")
cantidad_digitos_distintos = contar_digitos_distintos(telefono)
print(cantidad_digitos_distintos)
