
from queue_ import Queue
from super_heroes_data import superheroes
from tree import BinaryTree


# EJERCICIO 5

def cargar_arbol_marvel():
    arbol_marvel = BinaryTree()

    for personaje in superheroes:
        datos_personaje = personaje.copy()
        datos_personaje["is_hero"] = not personaje["is_villain"]
        arbol_marvel.insert_node(personaje["name"], other_value=datos_personaje)

    return arbol_marvel


def contar_nodos(arbol):
    def __contar(nodo):
        if nodo is None:
            return 0
        return 1 + __contar(nodo.left) + __contar(nodo.right)

    return __contar(arbol.root)


def listar_inorden(arbol):
    elementos = []

    def __inorden(nodo):
        if nodo is not None:
            __inorden(nodo.left)
            elementos.append(nodo)
            __inorden(nodo.right)

    __inorden(arbol.root)
    return elementos


def listar_villanos(arbol):
    print("Villanos ordenados alfabéticamente:")
    arbol.inorden_villain()


def listar_heroes_con_c(arbol):
    print("Superhéroes que empiezan con C:")
    arbol.inorden_hero_star_with("C")


def corregir_doctor_strange(arbol):
    print("Búsqueda por proximidad para encontrar a Doctor Strange:")
    nombre_correcto = "Doctor Strange"
    nodo = None

    for candidato in listar_inorden(arbol):
        if candidato.value.lower().startswith("dr st"):
            if nodo is not None:
                print("Hay más de un nombre parecido a Doctor Strange.")
                return False
            nodo = candidato

    if nodo is None:
        print(f"No se encontró un nombre parecido a {nombre_correcto}.")
        return False

    nombre_mal_cargado = nodo.value
    datos_personaje = nodo.other_values.copy()
    datos_personaje["name"] = nombre_correcto
    arbol.delete_node(nombre_mal_cargado)
    arbol.insert_node(nombre_correcto, other_value=datos_personaje)
    print(f"Se corrigió {nombre_mal_cargado} por {nombre_correcto}")
    return True


def listar_heroes_descendente(arbol):
    print("Superhéroes ordenados de manera descendente:")

    def __postorden_heroes(nodo):
        if nodo is not None:
            __postorden_heroes(nodo.right)
            if not nodo.other_values["is_villain"]:
                print(nodo.value)
            __postorden_heroes(nodo.left)

    __postorden_heroes(arbol.root)


def generar_bosque(arbol):
    arbol_heroes = BinaryTree()
    arbol_villanos = BinaryTree()

    for nodo in listar_inorden(arbol):
        if nodo.other_values["is_villain"]:
            arbol_villanos.insert_node(nodo.value, nodo.other_values)
        else:
            arbol_heroes.insert_node(nodo.value, nodo.other_values)

    return arbol_heroes, arbol_villanos


# EJERCICIO 23

def cargar_arbol_criaturas():
    datos_criaturas = [
        ("Ceto", []),
        ("Tifón", ["Zeus"]),
        ("Equidna", ["Argos Panoptes"]),
        ("Dino", []),
        ("Pefredo", []),
        ("Enio", []),
        ("Escila", []),
        ("Caribdis", []),
        ("Euríale", []),
        ("Esteno", []),
        ("Medusa", ["Perseo"]),
        ("Ladón", ["Heracles"]),
        ("Águila del Cáucaso", []),
        ("Quimera", ["Belerofonte"]),
        ("Hidra de Lerna", ["Heracles"]),
        ("León de Nemea", ["Heracles"]),
        ("Esfinge", ["Edipo"]),
        ("Dragón de la Cólquida", []),
        ("Cerbero", []),
        ("Cerda de Cromión", ["Teseo"]),
        ("Ortro", ["Heracles"]),
        ("Toro de Creta", ["Teseo"]),
        ("Jabalí de Calidón", ["Atalanta"]),
        ("Carcinos", []),
        ("Gerión", ["Heracles"]),
        ("Cloto", []),
        ("Láquesis", []),
        ("Átropos", []),
        ("Minotauro de Creta", ["Teseo"]),
        ("Harpías", []),
        ("Argos Panoptes", ["Hermes"]),
        ("Aves del Estínfalo", []),
        ("Talos", ["Medea"]),
        ("Sirenas", []),
        ("Pitón", ["Apolo"]),
        ("Cierva de Cerinea", []),
        ("Basilisco", []),
        ("Jabalí de Erimanto", []),
    ]

    arbol_criaturas = BinaryTree()
    for nombre, derrotado_por in datos_criaturas:
        otros_datos = {
            "defeated_by": derrotado_por,
            "description": "",
            "capturada": "",
        }
        arbol_criaturas.insert_node(nombre, other_value=otros_datos)
    return arbol_criaturas


def cargar_descripcion(arbol, nombre, descripcion):
    nodo = arbol.search(nombre)
    if nodo is None:
        print(f"No se encontró a {nombre}.")
        return False
    nodo.other_values["description"] = descripcion
    return True


def listar_criaturas_y_derrotadores(arbol):
    print("a. Criaturas y quiénes las derrotaron (inorden):")
    for nodo in listar_inorden(arbol):
        derrotadores = ", ".join(nodo.other_values["defeated_by"]) or "Nadie"
        print(f"{nodo.value}: {derrotadores}")


def mostrar_informacion_criatura(arbol, nombre):
    nodo = arbol.search(nombre)
    if nodo is None:
        print(f"No se encontró a {nombre}.")
        return
    print(f"c. Información de {nombre}:")
    print(f"Derrotado por: {', '.join(nodo.other_values['defeated_by']) or 'Nadie'}")
    print(f"Descripción: {nodo.other_values['description'] or 'Sin descripción cargada'}")
    print(f"Capturada por: {nodo.other_values['capturada'] or 'Nadie'}")


def contar_derrotas(arbol):
    cantidades = {}
    for nodo in listar_inorden(arbol):
        for heroe in nodo.other_values["defeated_by"]:
            cantidades[heroe] = cantidades.get(heroe, 0) + 1
    return cantidades


def mostrar_tres_mayores_derrotadores(arbol):
    cantidades = contar_derrotas(arbol)
    mayores = sorted(cantidades.items(), key=lambda elemento: elemento[1], reverse=True)[:3]
    print("d. Tres héroes o dioses que derrotaron más criaturas:")
    for heroe, cantidad in mayores:
        print(f"{heroe}: {cantidad}")


def listar_derrotadas_por(arbol, heroe):
    print(f"e. Criaturas derrotadas por {heroe}:")
    for nodo in listar_inorden(arbol):
        if heroe in nodo.other_values["defeated_by"]:
            print(nodo.value)


def listar_no_derrotadas(arbol):
    print("f. Criaturas que no fueron derrotadas:")
    for nodo in listar_inorden(arbol):
        if not nodo.other_values["defeated_by"]:
            print(nodo.value)


def marcar_captura(arbol, nombre_criatura, heroe):
    nodo = arbol.search(nombre_criatura)
    if nodo is None:
        print(f"No se encontró a {nombre_criatura}.")
        return False
    nodo.other_values["capturada"] = heroe
    return True


def buscar_por_coincidencia(arbol, texto):
    coincidencias = []
    texto = texto.casefold()

    def __buscar(nodo):
        if nodo is not None:
            __buscar(nodo.left)
            if texto in nodo.value.casefold():
                coincidencias.append(nodo)
            __buscar(nodo.right)

    __buscar(arbol.root)
    return coincidencias


def eliminar_criatura(arbol, nombre):
    eliminado, _ = arbol.delete_node(nombre)
    return eliminado is not None


def agregar_derrotador(arbol, nombre_criatura, heroe):
    nodo = arbol.search(nombre_criatura)
    if nodo is None:
        print(f"No se encontró a {nombre_criatura}.")
        return False
    if heroe not in nodo.other_values["defeated_by"]:
        nodo.other_values["defeated_by"].append(heroe)
    return True


def renombrar_criatura(arbol, nombre_actual, nombre_nuevo):
    nombre_eliminado, otros_datos = arbol.delete_node(nombre_actual)
    if nombre_eliminado is None:
        print(f"No se encontró a {nombre_actual}.")
        return False
    arbol.insert_node(nombre_nuevo, other_value=otros_datos)
    return True


def listar_por_nivel(arbol):
    print("m. Criaturas por nivel:")
    pendientes = Queue()
    if arbol.root is not None:
        pendientes.arrive(arbol.root)
    while pendientes.size() > 0:
        nodo = pendientes.attention()
        derrotadores = ", ".join(nodo.other_values["defeated_by"]) or "Nadie"
        print(f"{nodo.value}: {derrotadores}")
        if nodo.left is not None:
            pendientes.arrive(nodo.left)
        if nodo.right is not None:
            pendientes.arrive(nodo.right)


def listar_capturadas_por(arbol, heroe):
    print(f"n. Criaturas capturadas por {heroe}:")
    for nodo in listar_inorden(arbol):
        if nodo.other_values["capturada"] == heroe:
            print(nodo.value)


if __name__ == "__main__":
    arbol_marvel = cargar_arbol_marvel()

    print("EJERCICIO 5")
    listar_villanos(arbol_marvel)
    print()
    listar_heroes_con_c(arbol_marvel)
    print(f"\nCantidad de superhéroes: {arbol_marvel.count_heroes()}")
    print()
    corregir_doctor_strange(arbol_marvel)
    print()
    listar_heroes_descendente(arbol_marvel)

    arbol_heroes, arbol_villanos = generar_bosque(arbol_marvel)
    print("\nBosque de superhéroes:")
    print(f"Cantidad de nodos: {contar_nodos(arbol_heroes)}")
    arbol_heroes.inorden()
    print("\nBosque de villanos:")
    print(f"Cantidad de nodos: {contar_nodos(arbol_villanos)}")
    arbol_villanos.inorden()

    arbol_criaturas = cargar_arbol_criaturas()

    print("\nEJERCICIO 23")
    listar_criaturas_y_derrotadores(arbol_criaturas)

    cargar_descripcion(
        arbol_criaturas,
        "Talos",
        "Gigante de bronce que protegía la isla de Creta.",
    )
    print("\nb. Descripción cargada para Talos.")
    mostrar_informacion_criatura(arbol_criaturas, "Talos")
    print()

    mostrar_tres_mayores_derrotadores(arbol_criaturas)
    listar_derrotadas_por(arbol_criaturas, "Heracles")
    listar_no_derrotadas(arbol_criaturas)

    for nombre in (
        "Cerbero",
        "Toro de Creta",
        "Cierva de Cerinea",
        "Jabalí de Erimanto",
    ):
        marcar_captura(arbol_criaturas, nombre, "Heracles")
    print("g-h. Se registró que Heracles capturó Cerbero, Toro de Creta,")
    print("     Cierva de Cerinea y Jabalí de Erimanto.")

    print("i. Búsqueda por coincidencia ('dragón'):")
    for nodo in buscar_por_coincidencia(arbol_criaturas, "dragón"):
        print(nodo.value)

    eliminadas = []
    for nombre in ("Basilisco", "Sirenas"):
        if eliminar_criatura(arbol_criaturas, nombre):
            eliminadas.append(nombre)
    print("j. Criaturas eliminadas:", ", ".join(eliminadas))

    agregar_derrotador(arbol_criaturas, "Aves del Estínfalo", "Heracles")
    cargar_descripcion(
        arbol_criaturas,
        "Aves del Estínfalo",
        "Heracles derrotó a varias de estas aves.",
    )
    print("k. Aves del Estínfalo: se agregó a Heracles entre sus derrotadores.")

    if renombrar_criatura(arbol_criaturas, "Ladón", "Dragón Ladón"):
        print("l. Se cambió Ladón por Dragón Ladón.")
    listar_por_nivel(arbol_criaturas)
    listar_capturadas_por(arbol_criaturas, "Heracles")
