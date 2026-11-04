<<<<<<< HEAD
"""Resolución del ejercicio 1: índice de Pokémon."""

from dataclasses import dataclass
import json
from pathlib import Path
from textwrap import fill

from queue_ import Queue
from tree import BinaryTree


@dataclass(frozen=True)
class Pokemon:
    number: int
    name: str
    types: tuple[str, ...]
    weaknesses: tuple[str, ...]
    mega_evolution: bool
    gigamax: bool

    def __str__(self):
        types = ", ".join(self.types)
        weaknesses = ", ".join(self.weaknesses)
        return (
            f"#{self.number} {self.name} | tipos: {types} | "
            f"débil frente a: {weaknesses or 'ningún tipo'} | "
            f"megaevolución: {self.mega_evolution} | gigamax: {self.gigamax}"
        )


def cargar_pokemones():
    data_path = Path(__file__).with_name("pokemones.json")
    with data_path.open(encoding="utf-8") as data_file:
        records = json.load(data_file)

    especies = [
        Pokemon(
            number=record["numero"],
            name=record["nombre"],
            types=tuple(record["tipos"]),
            weaknesses=tuple(record["debilidades"]),
            mega_evolution=record["megaevolucion"],
            gigamax=record["gigamax"],
        )
        for record in records
    ]
    return especies


def _inorden(arbol):
    elementos = []

    def recorrer(nodo):
        if nodo is not None:
            recorrer(nodo.left)
            elementos.append(nodo)
            recorrer(nodo.right)

    recorrer(arbol.root)
    return elementos


class IndicePokemon:
    def __init__(self, pokemones):
        self.por_nombre = BinaryTree()
        self.por_numero = BinaryTree()
        self.por_tipo = BinaryTree()

        pokemones_por_tipo = {}
        for pokemon in pokemones:
            self.por_nombre.insert_node(pokemon.name.casefold(), pokemon)
            self.por_numero.insert_node(pokemon.number, pokemon)
            for pokemon_type in pokemon.types:
                tipo_normalizado = pokemon_type.casefold()
                if tipo_normalizado not in pokemones_por_tipo:
                    pokemones_por_tipo[tipo_normalizado] = [pokemon_type, []]
                pokemones_por_tipo[tipo_normalizado][1].append(pokemon)

        self.nombres_tipo = {}
        for tipo_normalizado, (nombre_tipo, especies) in pokemones_por_tipo.items():
            self.por_tipo.insert_node(tipo_normalizado, especies)
            self.nombres_tipo[tipo_normalizado] = nombre_tipo

    def buscar_numero(self, number):
        nodo = self.por_numero.search(number)
        return nodo.other_values if nodo is not None else None

    def buscar_nombre(self, name):
        nodo = self.por_nombre.search(name.casefold())
        return nodo.other_values if nodo is not None else None

    def buscar_proximidad(self, text):
        fragment = text.casefold()
        return [
            nodo.other_values
            for nodo in _inorden(self.por_nombre)
            if fragment in nodo.value
        ]

    def nombres_por_tipo(self, pokemon_type):
        nodo = self.por_tipo.search(pokemon_type.casefold())
        return sorted(pokemon.name for pokemon in nodo.other_values) if nodo is not None else []

    def listado_por_numero(self):
        return [nodo.other_values for nodo in _inorden(self.por_numero)]

    def listado_por_nombre(self):
        return [nodo.other_values for nodo in _inorden(self.por_nombre)]

    def listado_por_nivel(self):
        resultado = []
        pendientes = Queue()
        if self.por_nombre.root is not None:
            pendientes.arrive(self.por_nombre.root)
        while pendientes.size() > 0:
            nodo = pendientes.attention()
            resultado.append(nodo.other_values)
            if nodo.left is not None:
                pendientes.arrive(nodo.left)
            if nodo.right is not None:
                pendientes.arrive(nodo.right)
        return resultado

    def nombres_debiles_frente_a(self, buscado_name):
        buscado = self.buscar_nombre(buscado_name)
        if buscado is None:
            raise ValueError(f"No existe el Pokémon {buscado_name}.")
        target_types = set(buscado.types)
        return [
            pokemon
            for pokemon in self.listado_por_numero()
            if target_types.intersection(pokemon.weaknesses)
        ]

    def contar_tipos(self):
        resultado = []
        for nodo in _inorden(self.por_tipo):
            cantidad = len(nodo.other_values)
            resultado.append((self.nombres_tipo[nodo.value], cantidad))
        return resultado

    def contar_megaevoluciones(self):
        return sum(pokemon.mega_evolution for pokemon in self.listado_por_numero())

    def contar_gigamax(self):
        return sum(pokemon.gigamax for pokemon in self.listado_por_numero())


def main():
    pokemones = cargar_pokemones()
    indice = IndicePokemon(pokemones)

    print("EJERCICIO 1 - POKÉMON")
    print(f"Pokémon cargados: {len(indice.listado_por_numero())}")

    # b. Búsqueda por número y nombre por proximidad.
    print("\nb. Búsqueda por número 25:")
    print(indice.buscar_numero(25))
    print("\nBúsqueda por proximidad 'bul':")
    for pokemon in indice.buscar_proximidad("bul"):
        print(pokemon)

    # c. Nombres de Pokémon de los tipos solicitados.
    for buscado in ("Fantasma", "Fuego", "Acero", "Eléctrico"):
        print(f"\nc. Nombres de tipo {buscado}:")
        print(", ".join(indice.nombres_por_tipo(buscado)) or "Sin resultados")

    # d. Listados ordenados por número, nombre y nivel del árbol.
    print("\nd. Pokémon ordenados por número:")
    print(fill(", ".join(
        f"{pokemon.number}: {pokemon.name}"
        for pokemon in indice.listado_por_numero()
    ), width=100, subsequent_indent="  "))
    print("\nPokémon ordenados por nombre:")
    print(fill(", ".join(
        pokemon.name for pokemon in indice.listado_por_nombre()
    ), width=100, subsequent_indent="  "))
    print("\nPokémon por nivel del árbol de nombres:")
    print(fill(", ".join(
        pokemon.name for pokemon in indice.listado_por_nivel()
    ), width=100, subsequent_indent="  "))

    # e. Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum.
    for nombre in ("Jolteon", "Lycanroc", "Tyrantrum"):
        try:
            debiles = indice.nombres_debiles_frente_a(nombre)
        except ValueError:
            print(f"\ne. Debilidades frente a {nombre}: no está en la selección cargada")
            continue
        print(f"\ne. Pokémon débiles frente a {nombre}:")
        print(fill(", ".join(pokemon.name for pokemon in debiles), width=100, subsequent_indent="  "))

    # f. Cantidad de Pokémon por tipo y totales de megaevolución y gigamax.
    print("\nf. Cantidad de Pokémon por tipo:")
    for pokemon_type, cantidad in indice.contar_tipos():
        print(f"{pokemon_type}: {cantidad}")
    print(f"\nCon megaevolución: {indice.contar_megaevoluciones()}")
    print(f"Con forma gigamax: {indice.contar_gigamax()}")


if __name__ == "__main__":
    main()
=======
"""Resolución del ejercicio 1: índice de Pokémon."""

from dataclasses import dataclass
import json
from pathlib import Path
from textwrap import fill

from queue_ import Queue
from tree import BinaryTree


@dataclass(frozen=True)
class Pokemon:
    number: int
    name: str
    types: tuple[str, ...]
    weaknesses: tuple[str, ...]
    mega_evolution: bool
    gigamax: bool

    def __str__(self):
        types = ", ".join(self.types)
        weaknesses = ", ".join(self.weaknesses)
        return (
            f"#{self.number} {self.name} | tipos: {types} | "
            f"débil frente a: {weaknesses or 'ningún tipo'} | "
            f"megaevolución: {self.mega_evolution} | gigamax: {self.gigamax}"
        )


def cargar_pokemones():
    data_path = Path(__file__).with_name("pokemones.json")
    with data_path.open(encoding="utf-8") as data_file:
        records = json.load(data_file)

    especies = [
        Pokemon(
            number=record["numero"],
            name=record["nombre"],
            types=tuple(record["tipos"]),
            weaknesses=tuple(record["debilidades"]),
            mega_evolution=record["megaevolucion"],
            gigamax=record["gigamax"],
        )
        for record in records
    ]
    return especies


def _inorden(arbol):
    elementos = []

    def recorrer(nodo):
        if nodo is not None:
            recorrer(nodo.left)
            elementos.append(nodo)
            recorrer(nodo.right)

    recorrer(arbol.root)
    return elementos


class IndicePokemon:
    def __init__(self, pokemones):
        self.por_nombre = BinaryTree()
        self.por_numero = BinaryTree()
        self.por_tipo = BinaryTree()

        pokemones_por_tipo = {}
        for pokemon in pokemones:
            self.por_nombre.insert_node(pokemon.name.casefold(), pokemon)
            self.por_numero.insert_node(pokemon.number, pokemon)
            for pokemon_type in pokemon.types:
                tipo_normalizado = pokemon_type.casefold()
                if tipo_normalizado not in pokemones_por_tipo:
                    pokemones_por_tipo[tipo_normalizado] = [pokemon_type, []]
                pokemones_por_tipo[tipo_normalizado][1].append(pokemon)

        self.nombres_tipo = {}
        for tipo_normalizado, (nombre_tipo, especies) in pokemones_por_tipo.items():
            self.por_tipo.insert_node(tipo_normalizado, especies)
            self.nombres_tipo[tipo_normalizado] = nombre_tipo

    def buscar_numero(self, number):
        nodo = self.por_numero.search(number)
        return nodo.other_values if nodo is not None else None

    def buscar_nombre(self, name):
        nodo = self.por_nombre.search(name.casefold())
        return nodo.other_values if nodo is not None else None

    def buscar_proximidad(self, text):
        fragment = text.casefold()
        return [
            nodo.other_values
            for nodo in _inorden(self.por_nombre)
            if fragment in nodo.value
        ]

    def nombres_por_tipo(self, pokemon_type):
        nodo = self.por_tipo.search(pokemon_type.casefold())
        return sorted(pokemon.name for pokemon in nodo.other_values) if nodo is not None else []

    def listado_por_numero(self):
        return [nodo.other_values for nodo in _inorden(self.por_numero)]

    def listado_por_nombre(self):
        return [nodo.other_values for nodo in _inorden(self.por_nombre)]

    def listado_por_nivel(self):
        resultado = []
        pendientes = Queue()
        if self.por_nombre.root is not None:
            pendientes.arrive(self.por_nombre.root)
        while pendientes.size() > 0:
            nodo = pendientes.attention()
            resultado.append(nodo.other_values)
            if nodo.left is not None:
                pendientes.arrive(nodo.left)
            if nodo.right is not None:
                pendientes.arrive(nodo.right)
        return resultado

    def nombres_debiles_frente_a(self, buscado_name):
        buscado = self.buscar_nombre(buscado_name)
        if buscado is None:
            raise ValueError(f"No existe el Pokémon {buscado_name}.")
        target_types = set(buscado.types)
        return [
            pokemon
            for pokemon in self.listado_por_numero()
            if target_types.intersection(pokemon.weaknesses)
        ]

    def contar_tipos(self):
        resultado = []
        for nodo in _inorden(self.por_tipo):
            cantidad = len(nodo.other_values)
            resultado.append((self.nombres_tipo[nodo.value], cantidad))
        return resultado

    def contar_megaevoluciones(self):
        return sum(pokemon.mega_evolution for pokemon in self.listado_por_numero())

    def contar_gigamax(self):
        return sum(pokemon.gigamax for pokemon in self.listado_por_numero())


def main():
    pokemones = cargar_pokemones()
    indice = IndicePokemon(pokemones)

    print("EJERCICIO 1 - POKÉMON")
    print(f"Pokémon cargados: {len(indice.listado_por_numero())}")

    # b. Búsqueda por número y nombre por proximidad.
    print("\nb. Búsqueda por número 25:")
    print(indice.buscar_numero(25))
    print("\nBúsqueda por proximidad 'bul':")
    for pokemon in indice.buscar_proximidad("bul"):
        print(pokemon)

    # c. Nombres de Pokémon de los tipos solicitados.
    for buscado in ("Fantasma", "Fuego", "Acero", "Eléctrico"):
        print(f"\nc. Nombres de tipo {buscado}:")
        print(", ".join(indice.nombres_por_tipo(buscado)) or "Sin resultados")

    # d. Listados ordenados por número, nombre y nivel del árbol.
    print("\nd. Pokémon ordenados por número:")
    print(fill(", ".join(
        f"{pokemon.number}: {pokemon.name}"
        for pokemon in indice.listado_por_numero()
    ), width=100, subsequent_indent="  "))
    print("\nPokémon ordenados por nombre:")
    print(fill(", ".join(
        pokemon.name for pokemon in indice.listado_por_nombre()
    ), width=100, subsequent_indent="  "))
    print("\nPokémon por nivel del árbol de nombres:")
    print(fill(", ".join(
        pokemon.name for pokemon in indice.listado_por_nivel()
    ), width=100, subsequent_indent="  "))

    # e. Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum.
    for nombre in ("Jolteon", "Lycanroc", "Tyrantrum"):
        try:
            debiles = indice.nombres_debiles_frente_a(nombre)
        except ValueError:
            print(f"\ne. Debilidades frente a {nombre}: no está en la selección cargada")
            continue
        print(f"\ne. Pokémon débiles frente a {nombre}:")
        print(fill(", ".join(pokemon.name for pokemon in debiles), width=100, subsequent_indent="  "))

    # f. Cantidad de Pokémon por tipo y totales de megaevolución y gigamax.
    print("\nf. Cantidad de Pokémon por tipo:")
    for pokemon_type, cantidad in indice.contar_tipos():
        print(f"{pokemon_type}: {cantidad}")
    print(f"\nCon megaevolución: {indice.contar_megaevoluciones()}")
    print(f"Con forma gigamax: {indice.contar_gigamax()}")


if __name__ == "__main__":
    main()
>>>>>>> 71f60bce2f4f0437b75fa869e4553471cde54f1d
