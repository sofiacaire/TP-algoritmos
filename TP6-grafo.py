from graph import Graph


def crear_grafo(vertices, aristas):
    grafo = Graph(is_dir=False)
    for nombre, tipo in vertices:
        grafo.add_vertex(nombre, other_values={"tipo": tipo})
    for origen, destino, peso in aristas:
        grafo.add_edge(peso, origen, destino)
    return grafo


def obtener_vertice(grafo, nombre):
    posicion = grafo.search(nombre, "value")
    if posicion is None:
        raise ValueError(f"No existe el vértice {nombre}.")
    return grafo[posicion]


def camino_mas_corto(grafo, origen, destino):
    obtener_vertice(grafo, origen)
    obtener_vertice(grafo, destino)

    resultados = {}
    pendientes = grafo.dijkstra(origen)
    while pendientes.size() > 0:
        nombre, distancia, anterior = pendientes.pop()
        resultados[nombre] = (distancia, anterior)

    distancia_final, _ = resultados[destino]
    if distancia_final == float("inf"):
        raise ValueError(f"No hay camino entre {origen} y {destino}.")

    camino = [destino]
    while camino[-1] != origen:
        anterior = resultados[camino[-1]][1]
        if anterior is None:
            raise ValueError(f"No hay camino entre {origen} y {destino}.")
        camino.append(anterior)
    camino.reverse()
    return camino, distancia_final


def arbol_expansion_minima(grafo, origen):
    obtener_vertice(grafo, origen)
    aristas_arbol = []

    resultado = grafo.kruskal(origen)
    for arista in resultado.split(";"):
        inicio, destino, peso = arista.rsplit("-", 2)
        aristas_arbol.append((inicio, destino, int(peso)))

    if len(aristas_arbol) != len(grafo) - 1:
        raise ValueError("No se puede generar el árbol: el grafo no es conexo.")
    return aristas_arbol, sum(peso for _, _, peso in aristas_arbol)


def mostrar_camino(etiqueta, resultado, unidad=""):
    camino, distancia = resultado
    sufijo = f" ({distancia:g} {unidad})" if unidad else f" (peso: {distancia:g})"
    print(f"{etiqueta}: {' -> '.join(camino)}{sufijo}")


def mostrar_arbol_expansion(grafo, origen, unidad=""):
    aristas, peso_total = arbol_expansion_minima(grafo, origen)
    print(f"Árbol de expansión mínima desde {origen}:")
    for inicio, destino, peso in aristas:
        print(f"  {inicio} -- {destino}: {peso} {unidad}".rstrip())
    print(f"Peso total: {peso_total:g} {unidad}".rstrip())


# EJERCICIO 5 - DATOS DE LA RED
# Los equipos y las conexiones con sus pesos están definidos en esta función.
def crear_grafo_red():
    vertices = [
        ("Manjaro", "pc"),
        ("Parrot", "pc"),
        ("Ubuntu", "pc"),
        ("Mint", "pc"),
        ("Fedora", "pc"),
        ("Red Hat", "notebook"),
        ("Debian", "notebook"),
        ("Arch", "notebook"),
        ("Guaraní", "servidor"),
        ("MongoDB", "servidor"),
        ("Impresora", "impresora"),
        ("Switch 01", "switch"),
        ("Switch 02", "switch"),
        ("Router 01", "router"),
        ("Router 02", "router"),
        ("Router 03", "router"),
    ]
    aristas = [
        ("Red Hat", "Router 02", 25),
        ("Guaraní", "Router 02", 9),
        ("Router 02", "Router 03", 50),
        ("Router 02", "Router 01", 37),
        ("Router 01", "Router 03", 43),
        ("Debian", "Switch 01", 17),
        ("Ubuntu", "Switch 01", 18),
        ("Switch 01", "Impresora", 22),
        ("Switch 01", "Mint", 80),
        ("Switch 01", "Router 01", 29),
        ("Router 03", "Switch 02", 61),
        ("Manjaro", "Switch 02", 40),
        ("Parrot", "Switch 02", 12),
        ("MongoDB", "Switch 02", 5),
        ("Switch 02", "Arch", 56),
        ("Switch 02", "Fedora", 3),
    ]
    return crear_grafo(vertices, aristas)


# EJERCICIO 14 - DATOS DE LA CASA
# Los ambientes y las distancias (en metros) están definidos en esta función.
def crear_grafo_casa():
    ambientes = [
        "Cocina",
        "Comedor",
        "Cochera",
        "Quincho",
        "Baño 1",
        "Baño 2",
        "Habitación 1",
        "Habitación 2",
        "Sala de estar",
        "Terraza",
        "Patio",
    ]
    vertices = [(ambiente, "ambiente") for ambiente in ambientes]

    # Distancias de ejemplo en metros
    aristas = [
        ("Cocina", "Comedor", 3),
        ("Cocina", "Cochera", 7),
        ("Cocina", "Baño 1", 4),
        ("Cocina", "Sala de estar", 5),
        ("Cocina", "Patio", 8),
        ("Comedor", "Quincho", 6),
        ("Comedor", "Baño 1", 3),
        ("Comedor", "Sala de estar", 2),
        ("Cochera", "Quincho", 5),
        ("Cochera", "Patio", 4),
        ("Quincho", "Terraza", 7),
        ("Baño 1", "Habitación 1", 5),
        ("Baño 2", "Habitación 1", 3),
        ("Baño 2", "Habitación 2", 4),
        ("Baño 2", "Sala de estar", 6),
        ("Habitación 1", "Sala de estar", 2),
        ("Habitación 1", "Terraza", 8),
        ("Habitación 2", "Sala de estar", 3),
        ("Habitación 2", "Patio", 5),
        ("Terraza", "Patio", 6),
    ]
    return crear_grafo(vertices, aristas)


if __name__ == "__main__":
    print("EJERCICIO 5 - RED")
    red = crear_grafo_red()

    for notebook in ("Red Hat", "Debian", "Arch"):
        print(f"\nRecorrido en profundidad desde {notebook}:")
        red.deep_show(notebook)
        print(f"Recorrido en amplitud desde {notebook}:")
        red.amplitude_show(notebook)

    for pc in ("Manjaro", "Red Hat", "Fedora"):
        mostrar_camino(
            f"Camino más corto desde {pc} hasta la impresora",
            camino_mas_corto(red, pc, "Impresora"),
        )

    mostrar_arbol_expansion(red, "Manjaro")

    pcs = [
        vertice.value
        for vertice in red
        if vertice.other_values["tipo"] == "pc"
    ]
    caminos_a_guarani = [
        (camino_mas_corto(red, pc, "Guaraní")[1], pc)
        for pc in pcs
    ]
    distancia_guarani, pc_guarani = min(caminos_a_guarani)
    mostrar_camino(
        f"PC más cercana a Guaraní ({distancia_guarani:g})",
        camino_mas_corto(red, pc_guarani, "Guaraní"),
    )

    equipos_switch_01 = ("Debian", "Ubuntu", "Mint")
    caminos_a_mongodb = [
        (camino_mas_corto(red, equipo, "MongoDB")[1], equipo)
        for equipo in equipos_switch_01
    ]
    distancia_mongodb, equipo_mongodb = min(caminos_a_mongodb)
    mostrar_camino(
        f"Computadora de Switch 01 más cercana a MongoDB ({distancia_mongodb:g})",
        camino_mas_corto(red, equipo_mongodb, "MongoDB"),
    )

    print("\nSe cambia la conexión de la impresora de Switch 01 a Router 02.")
    red.delete_edge("Switch 01", "Impresora")
    red.add_edge(22, "Router 02", "Impresora")
    for notebook in ("Red Hat", "Debian", "Arch"):
        print(f"\nRecorrido en profundidad desde {notebook}:")
        red.deep_show(notebook)
        print(f"Recorrido en amplitud desde {notebook}:")
        red.amplitude_show(notebook)

    print("\nEJERCICIO 14 - CASA")
    casa = crear_grafo_casa()
    mostrar_arbol_expansion(casa, "Cocina", "m")
    mostrar_camino(
        "Camino de red más corto de Habitación 1 a Sala de estar",
        camino_mas_corto(casa, "Habitación 1", "Sala de estar"),
        "m",
    )