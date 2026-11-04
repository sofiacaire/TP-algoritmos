from list_ import List

#ejercicio 6
class Superheroe:
    def __init__(self, name: str, year: int, house: str, bio: str):
        self.name = name
        self.year = year
        self.house = house
        self.bio = bio

    def __str__(self):
        return f"Nombre: {self.name} | Año: {self.year} | Casa: {self.house} | Bio: {self.bio}"

    def __repr__(self):
        return self.__str__()


# Criterios de ordenamiento y búsqueda
def by_name(hero: Superheroe):
    return hero.name

def by_house(hero: Superheroe):
    return hero.house

def by_year(hero: Superheroe):
    return hero.year


# Carga inicial de superhéroes
def cargar_superheroes() -> List:
    heroes = List([
        Superheroe("Linterna Verde", 1940, "DC", "Miembro de los Green Lantern Corps que posee un anillo de poder y usa un traje verde."),
        Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras retráctiles de adamantium y factor de curación acelerado."),
        Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo que protege la Tierra de amenazas místicas utilizando su armadura espiritual y capa."), # Inicialmente en DC para cambiarlo en punto c
        Superheroe("Capitana Marvel", 1967, "Marvel", "Carol Danvers, heroína Kree de Marvel con fuerza sobrehumana y vuelo."),
        Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con súper fuerza y armadura de combate divina."),
        Superheroe("Flash", 1940, "DC", "El hombre más rápido del mundo que viste un traje rojo y protector."),
        Superheroe("Star-Lord", 1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia que porta un traje espacial con propulsores."),
        Superheroe("Batman", 1939, "DC", "El Caballero de la Noche de Gotham que usa una armadura táctica y traje de murciélago."),
        Superheroe("Superman", 1938, "DC", "El Hombre de Acero nativo de Krypton con poderes sobrehumanos."),
        Superheroe("Iron Man", 1963, "Marvel", "Tony Stark, multimillonario inventor que lucha con una armadura de alta tecnología."),
        Superheroe("Spider-Man", 1962, "Marvel", "Peter Parker, héroe neoyorquino con agilidad arácnida que viste un traje de mallas."),
        Superheroe("Black Widow", 1964, "Marvel", "Natasha Romanoff, espía e investigadora de elite."),
        Superheroe("Magneto", 1963, "Marvel", "Mutante controlador del magnetismo con casco y traje protector."),
    ])

    heroes.add_criterion("name", by_name)
    heroes.add_criterion("house", by_house)
    heroes.add_criterion("year", by_year)

    return heroes


# a. eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(lista: List, value, criterion="name"):
    index = lista.search(value, criterion)
    eliminado = lista.pop(index) if index is not None else None

    if eliminado:
        print(f"Se eliminó correctamente a: {eliminado.name}")
    else:
        print("El superheroe no se encuentra en la lista.")


# b. mostrar el año de aparición de Wolverine
def mostrar_anio_aparicion(lista: List, value, criterion=None):
    index = lista.search(value, criterion)
    if index is not None:
        print(f"{value} apareció por primera vez en el año: {lista[index].year}")
    else:
        print("El superheroe no fue encontrado en la lista.")


# c. cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista: List, value, new_value, criterion=None):
    index = lista.search(value, criterion)
    if index is not None:
        casa_anterior = lista[index].house
        lista[index].house = new_value
        print(f"La casa de {value} se cambió de '{casa_anterior}' a '{lista[index].house}'.")
    else:
        print("El superheroe no fue encontrado en la lista.")


# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
def mostrar_heroes_con_palabras(lista: List, search_value1, search_value2, criterion=None):
    print("Superhéroes con 'traje' o 'armadura' en su biografía:")
    encontrados = False
    for hero in lista:
        bio_lower = hero.bio.lower()
        if search_value1 in bio_lower or search_value2 in bio_lower:
            print(f"- {hero.name}")
            encontrados = True
    if not encontrados:
        print("Ningún superhéroe coincide con el criterio.")


# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def mostrar_heroes_anteriores_anio(lista: List, value):
    print("Superhéroes con aparición anterior a 1963:")
    for hero in lista:
        if hero.year < value:
            print(f"- {hero.name} | Casa: {hero.house} | Año: {hero.year}")


# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def mostrar_casa(lista: List, value1, value2, criterion=None):
    for nombre in [value1, value2]:
        index = lista.search(nombre, criterion)
        if index is not None:
            print(f"- {lista[index].name} pertenece a: {lista[index].house}")
        else:
            print(f"- {nombre} no fue encontrado.")


# g. mostrar toda la información de Flash y Star-Lord
def mostrar_info(lista: List, value1, value2, criterion=None):
    print("Información completa de Flash y Star-Lord:")
    for nombre in [value1, value2]:
        index = lista.search(nombre, criterion)
        if index is not None:
            print(f"  {lista[index]}")
        else:
            print(f"  {nombre} no fue encontrado.")


# h. listar los superhéroes que comienzan con la letra B, M y S
def listar_heroes_por_iniciales(lista: List, value1, value2, value3):
    print("Superhéroes cuyos nombres comienzan con B, M o S:")
    iniciales = (value1, value2, value3)
    for hero in lista:
        if hero.name.startswith(iniciales):
            print(f"- {hero.name}")


# i. determinar cuántos superhéroes hay de cada casa de comic (Marvel y DC)
def contar_superheroes_por_casa(lista: List, house1: str = "Marvel", house2: str = "DC"):
    count1 = 0
    count2 = 0

    for hero in lista:
        if hero.house.lower() == house1.lower():
            count1 += 1
        elif hero.house.lower() == house2.lower():
            count2 += 1

    print(f"Cantidad de superhéroes de {house1}: {count1}")
    print(f"Cantidad de superhéroes de {house2}: {count2}")



# =========================
# PROGRAMA PRINCIPAL - EJ 6
# =========================
if __name__ == "__main__":
    lista_superheroes = cargar_superheroes()

    print("==================================================")
    print("EJERCICIO 6: LISTA DE SUPERHÉROES")
    print("==================================================")
    print("\nLista inicial de superhéroes:")
    lista_superheroes.show()

    print("\n--- a. Eliminar a Linterna Verde ---")
    eliminar_superheroe(lista_superheroes, "Linterna Verde", "name")

    print("\n--- b. Mostrar año de aparición de Wolverine ---")
    mostrar_anio_aparicion(lista_superheroes, "Wolverine", "name")

    print("\n--- c. Cambiar la casa de Dr. Strange a Marvel ---")
    cambiar_casa(lista_superheroes, "Dr. Strange", "Marvel", "name")

    print("\n--- d. Superhéroes con 'traje' o 'armadura' en biografía ---")
    mostrar_heroes_con_palabras(lista_superheroes, "traje", "armadura")

    print("\n--- e. Superhéroes con aparición anterior a 1963 ---")
    mostrar_heroes_anteriores_anio(lista_superheroes, 1963)

    print("\n--- f. Casa de Capitana Marvel y Mujer Maravilla ---")
    mostrar_casa(lista_superheroes, "Capitana Marvel", "Mujer Maravilla", "name")

    print("\n--- g. Información completa de Flash y Star-Lord ---")
    mostrar_info(lista_superheroes, "Flash", "Star-Lord", "name")

    print("\n--- h. Superhéroes que comienzan con B, M y S ---")
    listar_heroes_por_iniciales(lista_superheroes, "B", "M", "S")

    print("\n--- i. Cantidad de superhéroes por casa de comic ---")
    contar_superheroes_por_casa(lista_superheroes, "Marvel", "DC")


# ==============================================================================
# EJERCICIO 15: ENTRENADORES POKÉMON (LISTA DE LISTAS)
# ==============================================================================

class Pokemon:
    def __init__(self, name: str, level: int, type_: str, subtype: str):
        self.name = name
        self.level = level
        self.type = type_
        self.subtype = subtype

    def __str__(self):
        return f"Pokémon: {self.name} | Nivel: {self.level} | Tipo: {self.type} | Subtipo: {self.subtype}"

    def __repr__(self):
        return self.__str__()


class Entrenador:
    def __init__(self, name: str, tournaments_won: int, battles_lost: int, battles_won: int, pokemons: List = None):
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_lost = battles_lost
        self.battles_won = battles_won
        self.pokemons = pokemons if pokemons is not None else List()

    def __str__(self):
        return (f"Entrenador: {self.name} | Torneos Ganados: {self.tournaments_won} | "
                f"Batallas Ganadas: {self.battles_won} | Batallas Perdidas: {self.battles_lost} | "
                f"Cantidad Pokémons: {len(self.pokemons)}")

    def __repr__(self):
        return self.__str__()


def by_trainer_name(trainer: Entrenador):
    return trainer.name


def by_pokemon_name(pokemon: Pokemon):
    return pokemon.name


def cargar_entrenadores() -> List:
    entrenadores = List([
        Entrenador("Ash Ketchum", 4, 20, 80, List([
            Pokemon("Pikachu", 85, "Eléctrico", "Ninguno"),
            Pokemon("Charizard", 90, "Fuego", "Volador"),
            Pokemon("Bulbasaur", 50, "Planta", "Veneno"),
            Pokemon("Wingull", 25, "Agua", "Volador"),
            Pokemon("Pikachu", 10, "Eléctrico", "Ninguno"),  # Repetido para consigna i
        ])),
        Entrenador("Misty", 2, 10, 50, List([
            Pokemon("Starmie", 60, "Agua", "Psíquico"),
            Pokemon("Psyduck", 35, "Agua", "Ninguno"),
            Pokemon("Gyarados", 70, "Agua", "Volador"),
        ])),
        Entrenador("Brock", 1, 40, 30, List([
            Pokemon("Onix", 55, "Roca", "Tierra"),
            Pokemon("Geodude", 40, "Roca", "Tierra"),
            Pokemon("Ludicolo", 48, "Agua", "Planta"),
        ])),
        Entrenador("Cynthia", 8, 10, 150, List([
            Pokemon("Garchomp", 95, "Dragón", "Tierra"),
            Pokemon("Lucario", 88, "Lucha", "Acero"),
            Pokemon("Milotic", 85, "Agua", "Ninguno"),
            Pokemon("Togekiss", 82, "Hada", "Volador"),
            Pokemon("Scovillain", 75, "Fuego", "Planta"),
        ])),
        Entrenador("Leon", 6, 5, 100, List([
            Pokemon("Charizard", 92, "Fuego", "Volador"),
            Pokemon("Dragapult", 87, "Dragón", "Fantasma"),
            Pokemon("Aegislash", 85, "Acero", "Fantasma"),
            Pokemon("Tyrantrum", 86, "Roca", "Dragón"),
        ])),
        Entrenador("Steven", 5, 10, 90, List([
            Pokemon("Metagross", 91, "Acero", "Psíquico"),
            Pokemon("Aggron", 86, "Acero", "Roca"),
            Pokemon("Terrakion", 89, "Roca", "Lucha"),
        ])),
    ])

    entrenadores.add_criterion("name", by_trainer_name)
    for ent in entrenadores:
        ent.pokemons.add_criterion("name", by_pokemon_name)

    return entrenadores


# a. obtener la cantidad de Pokémons de un determinado entrenador;
def a_obtener_cantidad_pokemons(lista: List, nombre_entrenador: str) -> int:
    index = lista.search(nombre_entrenador, "name")
    if index is not None:
        entrenador = lista[index]
        cant = len(entrenador.pokemons)
        print(f"El entrenador '{entrenador.name}' tiene {cant} Pokémon(s).")
        return cant
    else:
        print(f"El entrenador '{nombre_entrenador}' no fue encontrado.")
        return 0


# b. listar los entrenadores que hayan ganado más de determinada cantidad de torneos;
def b_listar_entrenadores_mas_de_torneos(lista: List, cantidad: int = 3):
    print(f"Entrenadores que han ganado más de {cantidad} torneos:")
    encontrados = False
    for entrenador in lista:
        if entrenador.tournaments_won > cantidad:
            print(f"- {entrenador.name}: {entrenador.tournaments_won} torneos ganados")
            encontrados = True
    if not encontrados:
        print(f"Ningún entrenador supera los {cantidad} torneos ganados.")


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def c_pokemon_mayor_nivel_del_mejor_entrenador(lista: List):
    if not lista:
        print("La lista de entrenadores está vacía.")
        return

    mejor_entrenador = lista[0]
    for entrenador in lista:
        if entrenador.tournaments_won > mejor_entrenador.tournaments_won:
            mejor_entrenador = entrenador

    print(f"Entrenador con más torneos ganados: {mejor_entrenador.name} ({mejor_entrenador.tournaments_won} torneos)")

    if mejor_entrenador.pokemons:
        pokemon_top = mejor_entrenador.pokemons[0]
        for pokemon in mejor_entrenador.pokemons:
            if pokemon.level > pokemon_top.level:
                pokemon_top = pokemon
        print(f"Su Pokémon de mayor nivel es: {pokemon_top.name} (Nivel {pokemon_top.level}, Tipo: {pokemon_top.type}/{pokemon_top.subtype})")
    else:
        print("El entrenador no tiene Pokémons en su lista.")


# d. mostrar todos los datos de un entrenador y sus Pokémons;
def d_mostrar_datos_entrenador_y_pokemons(lista: List, nombre_entrenador: str):
    index = lista.search(nombre_entrenador, "name")
    if index is not None:
        entrenador = lista[index]
        total_batallas = entrenador.battles_won + entrenador.battles_lost
        porcentaje = (entrenador.battles_won / total_batallas * 100) if total_batallas > 0 else 0.0

        print(f"\n==================================================")
        print(f"DATOS DEL ENTRENADOR: {entrenador.name}")
        print(f"==================================================")
        print(f"Torneos ganados: {entrenador.tournaments_won}")
        print(f"Batallas ganadas: {entrenador.battles_won}")
        print(f"Batallas perdidas: {entrenador.battles_lost}")
        print(f"Porcentaje de victorias: {porcentaje:.2f}%")
        print(f"Pokémons ({len(entrenador.pokemons)} total):")
        if entrenador.pokemons:
            for i, pok in enumerate(entrenador.pokemons, 1):
                print(f"  {i}. {pok}")
        else:
            print("  (No posee Pokémons)")
    else:
        print(f"El entrenador '{nombre_entrenador}' no fue encontrado.")


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def e_entrenadores_porcentaje_mayor_79(lista: List):
    print("Entrenadores con porcentaje de victorias mayor al 79%:")
    encontrados = False
    for entrenador in lista:
        total = entrenador.battles_won + entrenador.battles_lost
        if total > 0:
            porcentaje = (entrenador.battles_won / total) * 100
            if porcentaje > 79.0:
                print(f"- {entrenador.name}: {porcentaje:.2f}% de victorias ({entrenador.battles_won}G / {entrenador.battles_lost}P)")
                encontrados = True
    if not encontrados:
        print("Ningún entrenador supera el 79% de victorias.")


# f. los entrenadores que tengan Pokémons de determinados tipos y subtipos;
def f_entrenadores_por_tipo_subtipo(lista: List, combinaciones: list = None):
    if combinaciones is None:
        combinaciones = [("Fuego", "Planta"), ("Agua", "Volador")]

    comb_normalizadas = [(t.lower(), st.lower()) for t, st in combinaciones]
    nombres_comb = [f"{t.capitalize()}/{st.capitalize()}" for t, st in combinaciones]
    print(f"Entrenadores que tienen Pokémons con tipo/subtipo ({', '.join(nombres_comb)}):")
    
    encontrados = False
    for entrenador in lista:
        pokemons_coincidentes = []
        for pok in entrenador.pokemons:
            t = pok.type.lower()
            st = pok.subtype.lower()

            for t_buscado, st_buscado in comb_normalizadas:
                if (t == t_buscado and st == st_buscado) or (t == st_buscado and st == t_buscado):
                    pokemons_coincidentes.append(pok)
                    break

        if pokemons_coincidentes:
            print(f"- {entrenador.name}:")
            for p in pokemons_coincidentes:
                print(f"    * {p.name} (Tipo: {p.type} / Subtipo: {p.subtype})")
            encontrados = True

    if not encontrados:
        print("Ningún entrenador posee Pokémons con esas combinaciones de tipo/subtipo.")


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def g_promedio_nivel_pokemons_entrenador(lista: List, nombre_entrenador: str) -> float:
    index = lista.search(nombre_entrenador, "name")
    if index is not None:
        entrenador = lista[index]
        if entrenador.pokemons:
            suma_niveles = sum(p.level for p in entrenador.pokemons)
            promedio = suma_niveles / len(entrenador.pokemons)
            print(f"El promedio de nivel de los Pokémons de '{entrenador.name}' es: {promedio:.2f}")
            return promedio
        else:
            print(f"El entrenador '{entrenador.name}' no tiene Pokémons.")
            return 0.0
    else:
        print(f"El entrenador '{nombre_entrenador}' no fue encontrado.")
        return 0.0


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def h_cuantos_entrenadores_tienen_pokemon(lista: List, nombre_pokemon: str) -> int:
    nombre_p_lower = nombre_pokemon.lower()
    cantidad = 0
    entrenadores_que_lo_tienen = []

    for entrenador in lista:
        if any(p.name.lower() == nombre_p_lower for p in entrenador.pokemons):
            cantidad += 1
            entrenadores_que_lo_tienen.append(entrenador.name)

    print(f"Cantidad de entrenadores que tienen a '{nombre_pokemon}': {cantidad}")
    if entrenadores_que_lo_tienen:
        print(f"  Entrenadores: {', '.join(entrenadores_que_lo_tienen)}")
    return cantidad


# i. mostrar los entrenadores que tienen Pokémons repetidos;
def i_entrenadores_con_pokemons_repetidos(lista: List):
    print("Entrenadores que tienen Pokémons repetidos:")
    encontrados = False
    for entrenador in lista:
        conteo = {}
        for p in entrenador.pokemons:
            nombre = p.name
            conteo[nombre] = conteo.get(nombre, 0) + 1

        repetidos = [nombre for nombre, count in conteo.items() if count > 1]
        if repetidos:
            print(f"- {entrenador.name} tiene Pokémons repetidos: {', '.join(repetidos)}")
            encontrados = True

    if not encontrados:
        print("Ningún entrenador tiene Pokémons repetidos en su lista.")


# j. determinar los entrenadores que tengan al menos uno de una lista de Pokémons (por defecto: Tyrantrum, Terrakion o Wingull);
def j_entrenadores_con_pokemons_especificos(lista: List, lista_nombres: list = None):
    if lista_nombres is None:
        lista_nombres = ["Tyrantrum", "Terrakion", "Wingull"]

    buscados_lower = [nombre.lower() for nombre in lista_nombres]
    print(f"Entrenadores que tienen a uno de los siguientes Pokémons ({', '.join(lista_nombres)}):")
    encontrados = False

    for entrenador in lista:
        coincidencias = []
        for p in entrenador.pokemons:
            if p.name.lower() in buscados_lower:
                if p.name not in coincidencias:
                    coincidencias.append(p.name)

        if coincidencias:
            print(f"- {entrenador.name} posee: {', '.join(coincidencias)}")
            encontrados = True

    if not encontrados:
        print("Ningún entrenador tiene a los Pokémons buscados.")


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#    como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#    deberán mostrar los datos de ambos;
def k_buscar_entrenador_y_pokemon(lista: List, nombre_entrenador: str, nombre_pokemon: str) -> bool:
    print(f"\n--- Búsqueda: Entrenador '{nombre_entrenador}' y Pokémon '{nombre_pokemon}' ---")
    index = lista.search(nombre_entrenador, "name")

    if index is None:
        print(f"El entrenador '{nombre_entrenador}' NO se encuentra en la lista.")
        return False

    entrenador = lista[index]
    pokemon_encontrado = None
    for p in entrenador.pokemons:
        if p.name.lower() == nombre_pokemon.lower():
            pokemon_encontrado = p
            break

    if pokemon_encontrado:
        print("¡ENTRENADOR Y POKÉMON ENCONTRADOS!")
        print("\n[ DATOS DEL ENTRENADOR ]")
        print(entrenador)
        print("\n[ DATOS DEL POKÉMON ]")
        print(pokemon_encontrado)
        return True
    else:
        print(f"El entrenador '{entrenador.name}' existe, pero NO tiene al Pokémon '{nombre_pokemon}'.")
        return False


# =========================
# DEMOSTRACIÓN EJERCICIO 15
# =========================
def ejecutar_ejercicio_15():
    lista_entrenadores = cargar_entrenadores()

    print("\n" + "=" * 60)
    print("EJERCICIO 15: ENTRENADORES POKÉMON (LISTA DE LISTAS)")
    print("=" * 60)

    print("\n--- a. Cantidad de Pokémons de Ash Ketchum ---")
    a_obtener_cantidad_pokemons(lista_entrenadores, "Ash Ketchum")

    print("\n--- b. Entrenadores con más de 3 torneos ganados (o cantidad especificada) ---")
    b_listar_entrenadores_mas_de_torneos(lista_entrenadores, 3)

    print("\n--- c. Pokémon de mayor nivel del entrenador con más torneos ganados ---")
    c_pokemon_mayor_nivel_del_mejor_entrenador(lista_entrenadores)

    print("\n--- d. Mostrar todos los datos de un entrenador y sus Pokémons (ej. Cynthia) ---")
    d_mostrar_datos_entrenador_y_pokemons(lista_entrenadores, "Cynthia")

    print("\n--- e. Entrenadores con porcentaje de victorias > 79% ---")
    e_entrenadores_porcentaje_mayor_79(lista_entrenadores)

    print("\n--- f. Entrenadores con Pokémons Fuego/Planta o Agua/Volador (o combinaciones personalizadas) ---")
    f_entrenadores_por_tipo_subtipo(lista_entrenadores)

    print("\n--- g. Promedio de nivel de Pokémons de Ash Ketchum ---")
    g_promedio_nivel_pokemons_entrenador(lista_entrenadores, "Ash Ketchum")

    print("\n--- h. Cuántos entrenadores tienen a 'Charizard' ---")
    h_cuantos_entrenadores_tienen_pokemon(lista_entrenadores, "Charizard")

    print("\n--- i. Entrenadores con Pokémons repetidos ---")
    i_entrenadores_con_pokemons_repetidos(lista_entrenadores)

    print("\n--- j. Entrenadores con Tyrantrum, Terrakion o Wingull ---")
    j_entrenadores_con_pokemons_especificos(lista_entrenadores)

    print("\n--- k. Buscar si entrenador X tiene al Pokémon Y ---")
    # Caso 1: Encontrado
    k_buscar_entrenador_y_pokemon(lista_entrenadores, "Ash Ketchum", "Pikachu")
    # Caso 2: Pokémon no perteneciente a ese entrenador
    k_buscar_entrenador_y_pokemon(lista_entrenadores, "Misty", "Charizard")


if __name__ == "__main__":
    ejecutar_ejercicio_15()