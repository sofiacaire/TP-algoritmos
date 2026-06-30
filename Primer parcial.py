from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes


# PUNTO 1
lista_15 = List([
    "Iron Man", "Hulk", "Thor", "Black Widow", "Hawkeye",
    "Captain America", "Spiderman", "Wolverine", "Storm", "Daredevil",
    "Deadpool", "Black Panther", "Doctor Strange", "Ant Man", "Batman"
])


def buscar_capitan_america(lista, indice=0):
    if indice == len(lista):
        return False

    if lista[indice] == "Captain America":
        return True

    return buscar_capitan_america(lista, indice + 1)


def listar_superheroes_recursivo(lista, indice=0):
    if indice == len(lista):
        return

    print(lista[indice])
    listar_superheroes_recursivo(lista, indice + 1)



def by_name(item):
    return item["name"]


def by_real_name(item):
    if item["real_name"] is None:
        return ""
    return item["real_name"]


def by_first_appearance(item):
    return item["first_appearance"]



# PUNTO 2

def listar_ordenado_por_nombre(lista):
    lista.add_criterion("name", by_name)
    lista.sort_by_criterion("name")

    for personaje in lista:
        print(personaje["name"])


def buscar_posicion(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["name"] == nombre:
            return i
    return -1


def listar_villanos(lista):
    for personaje in lista:
        if personaje["is_villain"]:
            print(personaje["name"])


def cargar_villanos_en_cola(lista):
    cola = Queue()

    for personaje in lista:
        if personaje["is_villain"]:
            cola.arrive(personaje)

    return cola


def listar_villanos_antes_1980(cola):
    while cola.size() > 0:
        villano = cola.attention()

        if villano["first_appearance"] < 1980:
            print(villano["name"], "-", villano["first_appearance"])


def listar_superheroes_por_iniciales(lista):
    for personaje in lista:
        nombre = personaje["name"]

        if (nombre[:2] == "Bl" or
            nombre[:1] == "G" or
            nombre[:2] == "My" or
            nombre[:1] == "W"):
            print(nombre)


def listar_ordenado_por_nombre_real(lista):
    lista.add_criterion("real_name", by_real_name)
    lista.sort_by_criterion("real_name")

    for personaje in lista:
        print(personaje["real_name"], "-", personaje["name"])


def listar_por_fecha(lista):
    lista.add_criterion("first_appearance", by_first_appearance)
    lista.sort_by_criterion("first_appearance")

    for personaje in lista:
        print(personaje["first_appearance"], "-", personaje["name"])


def modificar_ant_man(lista):
    for personaje in lista:
        if personaje["name"] == "Ant Man":
            personaje["real_name"] = "Scott Lang"
            print(personaje)
            return


def buscar_por_biografia(lista):
    for personaje in lista:
        bio = personaje["short_bio"].lower()

        if "time-traveling" in bio or "suit" in bio:
            print(personaje["name"])


def eliminar_personajes(lista):
    for nombre in ["Electro", "Baron Zemo"]:

        encontrado = None

        for personaje in lista:
            if personaje["name"] == nombre:
                encontrado = personaje
                break

        if encontrado is not None:
            lista.remove(encontrado)
            print("Eliminado:")
            print(encontrado)
        else:
            print(nombre, "no estaba en la lista")


# =========================
# PROGRAMA PRINCIPAL
# =========================

lista_superheroes = List(superheroes)

print("LISTA DE 15 SUPERHÉROES")
listar_superheroes_recursivo(lista_15)

print("\n¿Está Captain America en la lista?")
if buscar_capitan_america(lista_15):
    print("Está en la lista")
else:
    print("No está en la lista")


print("\nLISTADO ORDENADO POR NOMBRE")
listar_ordenado_por_nombre(lista_superheroes)


print("\nPOSICIONES")
print("The Thing:", buscar_posicion(superheroes, "The Thing"))
print("Rocket Raccoon:", buscar_posicion(superheroes, "Rocket Raccoon"))


print("\nVILLANOS")
listar_villanos(lista_superheroes)


print("\nVILLANOS ANTES DE 1980")
cola_villanos = cargar_villanos_en_cola(lista_superheroes)
listar_villanos_antes_1980(cola_villanos)


print("\nPERSONAJES QUE COMIENZAN CON Bl, G, My y W")
listar_superheroes_por_iniciales(lista_superheroes)


print("\nLISTADO ORDENADO POR NOMBRE REAL")
listar_ordenado_por_nombre_real(lista_superheroes)


print("\nSUPERHEROES ORDENADOS POR FECHA DE APARICIÓN")
listar_por_fecha(lista_superheroes)


print("\nMODIFICAR NOMBRE REAL DE ANT MAN")
modificar_ant_man(lista_superheroes)


print("\nPERSONAJES CON 'time-traveling' O 'suit' EN LA BIOGRAFÍA")
buscar_por_biografia(lista_superheroes)


print("\nELIMINAR ELECTRO Y BARON ZEMO")
eliminar_personajes(lista_superheroes)