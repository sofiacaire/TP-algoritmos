#ejercicio 20
class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        return self.__elements.pop()

    def size(self):
        return len(self.__elements)
    
    def show(self):
        print(self.__elements)  



def registrar_movimientos():
    pila_movimientos = Stack()
    print("--- Registro de movimientos del Robot ---")
    print("Direcciones válidas: norte, sur, este, oeste, noreste, noroeste, sureste, suroeste")
    print("Ingrese 'fin' en la cantidad de pasos para terminar el registro.\n")
    
    while True:
        entrada_pasos = input("Cantidad de pasos (o 'fin' para terminar): ").strip().lower()
        if entrada_pasos == 'fin':
            break
        
        try:
            pasos = int(entrada_pasos)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
            
        direccion = input("Dirección: ").strip().lower()
        direcciones_validas = ['norte', 'sur', 'este', 'oeste', 'noreste', 'noroeste', 'sureste', 'suroeste']
        
        if direccion not in direcciones_validas:
            print(f"Dirección '{direccion}' no válida. Intente de nuevo.")
            continue
            
        pila_movimientos.push((pasos, direccion))
        print(f"Movimiento registrado: {pasos} pasos hacia el {direccion}.\n")
        
    return pila_movimientos

def retorno_robot(pila_movimientos):
    opuestas = {
        'norte': 'sur',
        'sur': 'norte',
        'este': 'oeste',
        'oeste': 'este',
        'noreste': 'suroeste',
        'suroeste': 'noreste',
        'noroeste': 'sureste',
        'sureste': 'noroeste'
    }
    
    print("\n--- Secuencia de retorno al punto de partida ---")
    if pila_movimientos.size() == 0:
        print("El robot no se movió, ya está en el punto de partida.")
        return

    # Mientras la pila tenga elementos, desapilamos
    while pila_movimientos.size() > 0:
        pasos, direccion = pila_movimientos.pop()
        dir_opuesta = opuestas[direccion] # Buscamos la dirección contraria en el diccionario
        print(f"Mover {pasos} pasos hacia el {dir_opuesta}")
        
    
    print("El robot ha regresado al lugar de partida")



# --- Ejercicio 24: Análisis MCU ---
def analizar_mcu(pila_personajes):
    pila_auxiliar = Stack()
    
    pos_rocket = -1
    pos_groot = -1
    posicion_actual = 1
    
    mas_de_5 = []
    peliculas_viuda_negra = 0
    empiezan_c_d_g = []

    # Desapilar para procesar cada personaje
    while pila_personajes.size() > 0:
        personaje = pila_personajes.pop()
        nombre = personaje[0]
        peliculas = personaje[1]
        
        # a. Posición de Rocket Raccoon y Groot
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual
            
        # b. Personajes con más de 5 películas
        if peliculas > 5:
            mas_de_5.append((nombre, peliculas))
            
        # c. Películas de Viuda Negra
        if nombre in ["Black Widow", "Viuda Negra"]:
            peliculas_viuda_negra = peliculas
            
        # d. Empiezan con C, D, G
        if nombre and nombre[0].upper() in ['C', 'D', 'G']:
            empiezan_c_d_g.append(nombre)
            
        # Guardamos en la pila auxiliar para no perder los datos
        pila_auxiliar.push(personaje)
        posicion_actual += 1

    # Restaurar la pila original (para que vuelva a quedar como estaba)
    while pila_auxiliar.size() > 0:
        pila_personajes.push(pila_auxiliar.pop())

    # Devolver los resultados
    return {
        "pos_rocket": pos_rocket,
        "pos_groot": pos_groot,
        "mas_de_5": mas_de_5,
        "peliculas_viuda_negra": peliculas_viuda_negra,
        "empiezan_c_d_g": empiezan_c_d_g
    }


# Ejercicio 24 - Datos de prueba 
def probar_ejercicio_24():
    pila_mcu = Stack()
    pila_mcu.push(("Iron Man", 10))
    pila_mcu.push(("Capitán América", 9))
    pila_mcu.push(("Groot", 4))
    pila_mcu.push(("Black Widow", 8))
    pila_mcu.push(("Doctor Strange", 6))
    pila_mcu.push(("Rocket Raccoon", 5))
    
    resultados = analizar_mcu(pila_mcu)
    
    # --- Mostrar Resultados ---
    print("\n--- Resultados del Análisis MCU ---")
    
    # a.
    if resultados["pos_rocket"] != -1:
        print(f"a. Rocket Raccoon está en la posición {resultados['pos_rocket']}.")
    else:
        print("a. Rocket Raccoon no está en la pila.")
        
    if resultados["pos_groot"] != -1:
        print(f"a. Groot está en la posición {resultados['pos_groot']}.")
    else:
        print("a. Groot no está en la pila.")

    # b.
    print("b. Personajes con más de 5 películas:")
    if resultados["mas_de_5"]:
        for p in resultados["mas_de_5"]:
            print(f"   - {p[0]} ({p[1]} películas)")
    else:
        print("   - Ninguno")
        
    # c.
    print(f"c. Black Widow participó en {resultados['peliculas_viuda_negra']} películas.")
    
    # d.
    print("d. Personajes que empiezan con C, D o G:")
    if resultados["empiezan_c_d_g"]:
        for p in resultados["empiezan_c_d_g"]:
            print(f"   - {p}")
    else:
        print("   - Ninguno")


# --- Bloque Principal ---
if __name__ == "__main__":
    movimientos = registrar_movimientos()
    print("\n")
    print("Pila de movimientos \n")
    movimientos.show()
    retorno_robot(movimientos)

    probar_ejercicio_24()