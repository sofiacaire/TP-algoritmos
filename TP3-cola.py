from typing import Any
from copy import copy

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]

    def show(self) -> None:
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)


class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None: 
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__elements)):
            value = self.move_to_end()
            print(value)


# EJERCICIO 10

notificaciones = Queue()

notificaciones.arrive (("09:00", "instagram", "Nuevo seguidor"))
notificaciones.arrive (("09:15", "whatsapp", "Llamada perdida"))
notificaciones.arrive (("11:50", "twitter", "Aprendiendo Python"))
notificaciones.arrive (("12:38", "facebook", "Nuevo mensaje"))
notificaciones.arrive (("14:40", "twitter", "Nuevo tuit"))
notificaciones.arrive (("14:53", "whatsapp", "A Juancito le gusta tu estado"))
notificaciones.arrive (("15:00", "facebook", "Otro mensaje"))
notificaciones.arrive (("16:15", "whatsapp", "A Pedrito le gusta tu estado"))

#inciso a)
def eliminar_notif_facebook(notificaciones):
    notif_aux = Queue()
    while notificaciones.size() > 0:
        elemento = notificaciones.attention()  
        if elemento[1].lower() != "facebook":   
            notif_aux.arrive(elemento)          

    while notif_aux.size() > 0:
        notificaciones.arrive(notif_aux.attention())
    return notificaciones



#inciso b)
def mostrar_twitter_python(notificaciones):
    notif_aux = Queue()
    while notificaciones.size() > 0:
        elemento = notificaciones.attention()  
        # Convertimos el mensaje a minúsculas con .lower() para buscar 'python' de manera insensible a mayúsculas
        if elemento[1].lower() == "twitter" and "python" in elemento[2].lower():   
            print(elemento)
        
        notif_aux.arrive(elemento)         

    while notif_aux.size() > 0:
        notificaciones.arrive(notif_aux.attention())


#inciso c)
def notif_11_43_15_57 (notificaciones):
    pila_temp = Stack()
    notif_aux = Queue()
    
    while notificaciones.size() > 0:
        elemento = notificaciones.attention()  
        if "11:43" <= elemento[0] <= "15:57": 
            pila_temp.push(elemento)

        notif_aux.arrive(elemento)         

    while notif_aux.size() > 0:
        notificaciones.arrive(notif_aux.attention())

    cantidad = pila_temp.size()
    print(f"Cantidad de notificaciones encontradas en el rango horario: {cantidad}")
    print("Notificaciones en la pila (de la más reciente a la más antigua):")
    pila_temp.show()
    return cantidad


print("--- Cola original ---")
notificaciones.show()

print("\n--- Ejecutando eliminación ---")
eliminar_notif_facebook(notificaciones)

print("\n--- Cola resultante ---")
notificaciones.show()

print("\n--- Mostrando notificaciones de Twitter relacionadas con Python")
mostrar_twitter_python(notificaciones)

print("\n--- Mostrando notificaciones entre 11:43 y 15:57 ---")
notif_11_43_15_57 (notificaciones)





# EJERCICIO 22

personajes = Queue()

personajes.arrive (("Tony Stark", "Iron Man", "M"))
personajes.arrive (("Bruce Banner", "Hulk", "M"))
personajes.arrive (("Steve Rogers", "Capitán América", "M"))
personajes.arrive (("Natasha Romanoff", "Viuda Negra", "F"))
personajes.arrive (("Thor Odinson", "Thor", "M"))
personajes.arrive (("Scott Lang", "Ant-Man", "M"))
personajes.arrive (("Stephen Strange", "Doctor Strange", "M"))
personajes.arrive (("Carol Danvers", "Capitana Marvel", "F"))
personajes.arrive (("Wade Wilson", "Deadpool", "M"))
personajes.arrive (("Wanda Maximoff", "Bruja Escarlata", "F"))


#inciso a)

def buscar_nombre_personaje(buscado,personajes):
    personaje_aux = Queue()
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if elemento[1].lower() == buscado.lower():
            print(elemento[0])
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    return personajes


#inciso b)

def personajes_fem (personajes):
    personaje_aux = Queue()
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if elemento[2] == "F":
            print(elemento[1])
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    return personajes


#inciso c)
def personajes_masc (personajes):
    personaje_aux = Queue()
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if elemento[2] == "M":
            print(elemento[0])
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    return personajes


#inciso d)
def buscar_nombre_superheroe (buscado,personajes):
    personaje_aux = Queue()
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if buscado.lower() == elemento[0].lower():
            print(elemento[1])
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    return personajes


#inciso e) 
def buscar_inicial_ps (letra,personajes):
    personaje_aux = Queue()
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if elemento[0].lower().startswith(letra.lower()) or elemento[1].lower().startswith(letra.lower()):
            print(elemento)
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    return personajes


#inciso f)
def buscar_superheroe(buscado, personajes):
    personaje_aux = Queue()
    encontrado = False
    nombre_superheroe = ""
    
    while personajes.size() > 0:
        elemento = personajes.attention()  
        if buscado.lower() == elemento[0].lower():
            encontrado = True
            nombre_superheroe = elemento[1]
        
        personaje_aux.arrive(elemento)        

    while personaje_aux.size() > 0:
        personajes.arrive(personaje_aux.attention())
    
    if encontrado:
        print(f"El personaje '{buscado}' se encuentra en la cola. Su nombre de superhéroe es '{nombre_superheroe}'.")
    else:
        print(f"El personaje '{buscado}' no se encuentra en la cola.")
        
    return personajes



#-----main-----

print ('\nLista de personajes de Marvel')
personajes.show ()

print ('\nBuscar nombre del personaje')
buscar_nombre_personaje ('Capitana Marvel',personajes)

print ('\nPersonajes femeninos')
personajes_fem (personajes)

print ('\nPersonajes masculinos')
personajes_masc (personajes)

print ('\nBuscar nombre del superheroe')
buscar_nombre_superheroe ('Scott Lang',personajes)

print ('\nBuscar personaje/superheroe por inicial')
buscar_inicial_ps ('S',personajes)

print ('\nBuscar superheroe por nombre completo')
buscar_superheroe ('Carol Danvers',personajes)

