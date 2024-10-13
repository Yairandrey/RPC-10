
linea1 = input().split()
numero1 = [int(num) for num in linea1]


linea2 = input().split()
numeros2 = [int(num) for num in linea2]


if numeros2[0] / numeros2[1] >= numero1[0]:print("1")
else: print("0")
