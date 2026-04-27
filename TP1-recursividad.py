# ejercicio 5: convertir numero romano a decimal

#primero corroborar que sea un numero válido
def romano_valido (rom:str)-> bool:
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # 1. letras válidas
    for n in rom:
        if n not in valores:
            return False

    # 2. no más de 3 iguales seguidos
    cont = 1
    for i in range(1, len(rom)):
        if rom[i] == rom[i-1]:
            cont += 1
            if cont > 3:
                return False
        else:
            cont = 1

    # 3. reglas de resta
    for i in range(len(rom)-1):
        actual = valores[rom[i]]
        siguiente = valores[rom[i+1]]

        if actual < siguiente:
             if i > 0 and rom[i] == rom[i-1]:
                return False
    
                if not (
                (rom[i] == "I" and rom[i+1] in ["V", "X"]) or
                (rom[i] == "X" and rom[i+1] in ["L", "C"]) or
                (rom[i] == "C" and rom[i+1] in ["D", "M"])
                ):
                    return False

    return True

#pasar de romano a decimal
def romano_decimal (rom:str)-> int:
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if len(rom)== 1:
        return valores [rom]

    if valores [rom[0]] < valores [rom[1]]:
        return - valores[rom[0]] + romano_decimal(rom[1:])
    else:
        return valores[rom[0]] + romano_decimal(rom[1:])


num= input('Ingrese un número romano válido: ').upper()

if romano_valido(num):
    print(romano_decimal(num))
else:
    print("El número romano ingresado no es válido")


#ejercicio 22

def usar_la_fuerza(mochila, indice=0):   #para saber si no esta vacia
    if indice == len(mochila):
        return False, indice

    if mochila[indice] == "sable de luz":
        return True, indice + 1

    return usar_la_fuerza(mochila, indice + 1)


# Programa principal
mochila = ['comida', 'capa', 'mapa', 'sable de luz','botiquin']

encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
    print("La mochila contiene un sable de luz.")
    print("Cantidad de objetos sacados:", cantidad)
else:
    print("La mochila no contiene un sable de luz.")
    print("Cantidad de objetos sacados:", cantidad)