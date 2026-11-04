<<<<<<< HEAD
"""Resolución del ejercicio 2: grafo de personajes de Star Wars."""

from graph import Graph
from heap import HeapMin


STAR_WARS_APPEARANCES = {
    "Luke Skywalker": (4, 5, 6, 7, 8, 9),
    "Darth Vader": (3, 4, 5, 6),
    "Yoda": (1, 2, 3, 5, 6, 8),
    "Boba Fett": (2, 5, 6),
    "C-3PO": (1, 2, 3, 4, 5, 6, 7, 8, 9),
    "Leia": (4, 5, 6, 7, 8, 9),
    "Rey": (7, 8, 9),
    "Kylo Ren": (7, 8, 9),
    "Chewbacca": (3, 4, 5, 6, 7, 8, 9),
    "Han Solo": (4, 5, 6, 7, 9),
    "R2-D2": (1, 2, 3, 4, 5, 6, 7, 8, 9),
    "BB-8": (7, 8, 9),
}


def cargar_grafo_star_wars(apariciones=None):
    personajes = STAR_WARS_APPEARANCES if apariciones is None else apariciones
    grafo = Graph(is_dir=False)
    for nombre in personajes:
        grafo.add_vertex(nombre, other_values=tuple(personajes[nombre]))

    nombres = list(personajes)
    for index, origen in enumerate(nombres):
        episodios_origen = set(personajes[origen])
        for destino in nombres[index + 1:]:
            compartidos = len(episodios_origen.intersection(personajes[destino]))
            if compartidos:
                grafo.add_edge(compartidos, origen, destino)
    return grafo


def arbol_expansion_minimo(grafo, origen):
    if grafo.search(origen, "value") is None:
        raise ValueError(f"No existe el personaje {origen}.")

    visitados = {origen}
    aristas_pendientes = HeapMin()
    aristas_arbol = []

    def cargar_aristas(nombre):
        posicion = grafo.search(nombre, "value")
        for arista in grafo[posicion].edges:
            if arista.destination not in visitados:
                aristas_pendientes.arrive(
                    (nombre, arista.destination),
                    arista.weight,
                )

    cargar_aristas(origen)
    while aristas_pendientes.size() > 0 and len(visitados) < len(grafo):
        peso, (inicio, destino) = aristas_pendientes.attention()
        if destino in visitados:
            continue
        visitados.add(destino)
        aristas_arbol.append((inicio, destino, peso))
        cargar_aristas(destino)

    if len(visitados) != len(grafo):
        raise ValueError("El grafo no es conexo.")
    return aristas_arbol, sum(arista[2] for arista in aristas_arbol)


def camino_mas_corto(grafo, origen, destino):
    if grafo.search(origen, "value") is None:
        raise ValueError(f"No existe el personaje {origen}.")
    if grafo.search(destino, "value") is None:
        raise ValueError(f"No existe el personaje {destino}.")

    pendientes = HeapMin()
    for vertice in grafo:
        distancia = 0 if vertice.value == origen else float("inf")
        pendientes.arrive([vertice.value], distancia)

    anteriores = {}
    distancia_final = None
    while pendientes.size() > 0:
        distancia, (actual,) = pendientes.attention()
        if distancia == float("inf"):
            break
        if actual == destino:
            distancia_final = distancia
            break

        posicion = grafo.search(actual, "value")
        for arista in grafo[posicion].edges:
            siguiente = pendientes.search(arista.destination)
            if siguiente is None:
                continue
            nueva_distancia = distancia + arista.weight
            if nueva_distancia < pendientes.elements[siguiente][0]:
                anteriores[arista.destination] = actual
                pendientes.change_priority(siguiente, nueva_distancia)

    if destino != origen and destino not in anteriores:
        raise ValueError(f"No hay camino entre {origen} y {destino}.")

    camino = [destino]
    while camino[-1] != origen:
        camino.append(anteriores[camino[-1]])
    camino.reverse()
    return camino, distancia_final


def main():
    grafo = cargar_grafo_star_wars()
    print("EJERCICIO 2 - STAR WARS")

    # a. Árboles de expansión mínima desde los tres vértices solicitados.
    for nombre in ("C-3PO", "Yoda", "Leia"):
        aristas, peso_total = arbol_expansion_minimo(grafo, nombre)
        print()
        print(f"Árbol de expansión mínimo desde {nombre} (peso total: {peso_total}):")
        for inicio, destino, peso in aristas:
            cantidad_episodios = "episodio compartido" if peso == 1 else "episodios compartidos"
            print(f"  {inicio} -- {destino}: {peso} {cantidad_episodios}")

    # b. Máximo de episodios compartidos y todos los pares que lo alcanzan.
    maximo = max(
        edge.weight
        for vertex in grafo
        for edge in vertex.edges
    )
    pares_maximos = []
    for vertex in grafo:
        for edge in vertex.edges:
            if vertex.value < edge.destination and edge.weight == maximo:
                pares_maximos.append((vertex.value, edge.destination))
    print(f"\nMáximo de episodios compartidos: {maximo}")
    for origen, destino in pares_maximos:
        print(f"  {origen} y {destino}")

    # c. Caminos más cortos solicitados.
    for origen, destino in (("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")):
        camino, distancia = camino_mas_corto(grafo, origen, destino)
        print(
            f"\nCamino más corto de {origen} a {destino}: "
            f"{' -> '.join(camino)} (peso: {distancia})"
        )

    # d. Personajes que aparecieron en los nueve episodios.
    todos_los_episodios = [
        vertex.value
        for vertex in grafo
        if len(vertex.other_values) == 9
    ]
    print("\nPersonajes presentes en los nueve episodios:")
    print(", ".join(sorted(todos_los_episodios)))


if __name__ == "__main__":
    main()
=======
"""Resolución del ejercicio 2: grafo de personajes de Star Wars."""

from graph import Graph
from heap import HeapMin


STAR_WARS_APPEARANCES = {
    "Luke Skywalker": (4, 5, 6, 7, 8, 9),
    "Darth Vader": (3, 4, 5, 6),
    "Yoda": (1, 2, 3, 5, 6, 8),
    "Boba Fett": (2, 5, 6),
    "C-3PO": (1, 2, 3, 4, 5, 6, 7, 8, 9),
    "Leia": (4, 5, 6, 7, 8, 9),
    "Rey": (7, 8, 9),
    "Kylo Ren": (7, 8, 9),
    "Chewbacca": (3, 4, 5, 6, 7, 8, 9),
    "Han Solo": (4, 5, 6, 7, 9),
    "R2-D2": (1, 2, 3, 4, 5, 6, 7, 8, 9),
    "BB-8": (7, 8, 9),
}


def cargar_grafo_star_wars(apariciones=None):
    personajes = STAR_WARS_APPEARANCES if apariciones is None else apariciones
    grafo = Graph(is_dir=False)
    for nombre in personajes:
        grafo.add_vertex(nombre, other_values=tuple(personajes[nombre]))

    nombres = list(personajes)
    for index, origen in enumerate(nombres):
        episodios_origen = set(personajes[origen])
        for destino in nombres[index + 1:]:
            compartidos = len(episodios_origen.intersection(personajes[destino]))
            if compartidos:
                grafo.add_edge(compartidos, origen, destino)
    return grafo


def arbol_expansion_minimo(grafo, origen):
    if grafo.search(origen, "value") is None:
        raise ValueError(f"No existe el personaje {origen}.")

    visitados = {origen}
    aristas_pendientes = HeapMin()
    aristas_arbol = []

    def cargar_aristas(nombre):
        posicion = grafo.search(nombre, "value")
        for arista in grafo[posicion].edges:
            if arista.destination not in visitados:
                aristas_pendientes.arrive(
                    (nombre, arista.destination),
                    arista.weight,
                )

    cargar_aristas(origen)
    while aristas_pendientes.size() > 0 and len(visitados) < len(grafo):
        peso, (inicio, destino) = aristas_pendientes.attention()
        if destino in visitados:
            continue
        visitados.add(destino)
        aristas_arbol.append((inicio, destino, peso))
        cargar_aristas(destino)

    if len(visitados) != len(grafo):
        raise ValueError("El grafo no es conexo.")
    return aristas_arbol, sum(arista[2] for arista in aristas_arbol)


def camino_mas_corto(grafo, origen, destino):
    if grafo.search(origen, "value") is None:
        raise ValueError(f"No existe el personaje {origen}.")
    if grafo.search(destino, "value") is None:
        raise ValueError(f"No existe el personaje {destino}.")

    pendientes = HeapMin()
    for vertice in grafo:
        distancia = 0 if vertice.value == origen else float("inf")
        pendientes.arrive([vertice.value], distancia)

    anteriores = {}
    distancia_final = None
    while pendientes.size() > 0:
        distancia, (actual,) = pendientes.attention()
        if distancia == float("inf"):
            break
        if actual == destino:
            distancia_final = distancia
            break

        posicion = grafo.search(actual, "value")
        for arista in grafo[posicion].edges:
            siguiente = pendientes.search(arista.destination)
            if siguiente is None:
                continue
            nueva_distancia = distancia + arista.weight
            if nueva_distancia < pendientes.elements[siguiente][0]:
                anteriores[arista.destination] = actual
                pendientes.change_priority(siguiente, nueva_distancia)

    if destino != origen and destino not in anteriores:
        raise ValueError(f"No hay camino entre {origen} y {destino}.")

    camino = [destino]
    while camino[-1] != origen:
        camino.append(anteriores[camino[-1]])
    camino.reverse()
    return camino, distancia_final


def main():
    grafo = cargar_grafo_star_wars()
    print("EJERCICIO 2 - STAR WARS")

    # a. Árboles de expansión mínima desde los tres vértices solicitados.
    for nombre in ("C-3PO", "Yoda", "Leia"):
        aristas, peso_total = arbol_expansion_minimo(grafo, nombre)
        print()
        print(f"Árbol de expansión mínimo desde {nombre} (peso total: {peso_total}):")
        for inicio, destino, peso in aristas:
            cantidad_episodios = "episodio compartido" if peso == 1 else "episodios compartidos"
            print(f"  {inicio} -- {destino}: {peso} {cantidad_episodios}")

    # b. Máximo de episodios compartidos y todos los pares que lo alcanzan.
    maximo = max(
        edge.weight
        for vertex in grafo
        for edge in vertex.edges
    )
    pares_maximos = []
    for vertex in grafo:
        for edge in vertex.edges:
            if vertex.value < edge.destination and edge.weight == maximo:
                pares_maximos.append((vertex.value, edge.destination))
    print(f"\nMáximo de episodios compartidos: {maximo}")
    for origen, destino in pares_maximos:
        print(f"  {origen} y {destino}")

    # c. Caminos más cortos solicitados.
    for origen, destino in (("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")):
        camino, distancia = camino_mas_corto(grafo, origen, destino)
        print(
            f"\nCamino más corto de {origen} a {destino}: "
            f"{' -> '.join(camino)} (peso: {distancia})"
        )

    # d. Personajes que aparecieron en los nueve episodios.
    todos_los_episodios = [
        vertex.value
        for vertex in grafo
        if len(vertex.other_values) == 9
    ]
    print("\nPersonajes presentes en los nueve episodios:")
    print(", ".join(sorted(todos_los_episodios)))


if __name__ == "__main__":
    main()
>>>>>>> 71f60bce2f4f0437b75fa869e4553471cde54f1d
