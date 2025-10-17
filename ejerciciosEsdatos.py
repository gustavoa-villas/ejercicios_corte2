
#ejercicio 1
def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares
print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#ejercicio 2
def invertir_diccionario(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        invertido[valor] = clave
    return invertido
print(invertir_diccionario({"a": 1, "b": 2, "c": 3}))

#ejercicio 3
def elementos_comunes(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    comunes = conjunto1 & conjunto2
    return list(comunes)
print(elementos_comunes([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

#ejercicio 4
def contar_palabras(texto):

    palabras = texto.lower().split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
print(contar_palabras("hola mundo"))

#ejercicio 5
def eliminar_duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista
print(eliminar_duplicados([1, 2, 2, 3, 4, 3, 5]))

#Nivel avanzado
#Ejercicio 1
def agrupar_por(objetos, atributo):
    resultado = {}
    for obj in objetos:
        valor = obj[atributo]
        if valor not in resultado:
            resultado[valor] = []
        resultado[valor].append(obj)
    return resultado

estudiantes = [
    {"nombre": "Ana", "ciudad": "Madrid"},
    {"nombre": "Juan", "ciudad": "Barcelona"},
    {"nombre": "Maria", "ciudad": "Madrid"},
    {"nombre": "Pedro", "ciudad": "Valencia"}
]
print(agrupar_por(estudiantes, "ciudad"))

#ejercicio 2
def fusionar_diccionarios(dict1, dict2):
    resultado = dict1.copy()

    for clave, valor in dict2.items():
        if clave in resultado and isinstance(resultado[clave], dict) and isinstance(valor, dict):
            resultado[clave] = fusionar_diccionarios(resultado[clave], valor)
        else:
            resultado[clave] = valor
    return resultado
dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
dict2 = {"c": 3, "b": {"y": 30, "z": 40}}
print(fusionar_diccionarios(dict1, dict2))

#ejercicio 3
def encontrar_par_suma(numeros, objetivo):
    vistos = set()  
    for num in numeros:
        complemento = objetivo - num
        if complemento in vistos:
            return (complemento, num)
        vistos.add(num)
    return None 
print(encontrar_par_suma([1, 5, 3, 7, 9, 2], 10))

#ejercicio 4
def transponer(matriz):
    return [list(fila) for fila in zip(*matriz)]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transponer(matriz))

#ejercicio 5
def contar_por_categoria(datos):
    categorias = {}
    for categoria, elemento in datos:
        if categoria not in categorias:
            categorias[categoria] = set()  
        categorias[categoria].add(elemento)  
    return {categoria: len(elementos) for categoria, elementos in categorias.items()}

datos = [
    ("fruta", "manzana"),
    ("verdura", "zanahoria"),
    ("fruta", "plátano"),
    ("fruta", "manzana"),
    ("verdura", "lechuga")
]
print(contar_por_categoria(datos))

#Nivel Avanzado
#ejercicio 1
def fibonacci(n):
    memoria = {}

    def fib_memo(n):
        if n in memoria:
            return memoria[n]
        if n <= 1:
            resultado = n
        else:
            resultado = fib_memo(n - 1) + fib_memo(n - 2)
        memoria[n] = resultado
        return resultado

    return fib_memo(n)
print(fibonacci(10))

#ejercicio 2
class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad 
        self.cache = {}             
        self.orden_uso = []         

    def get(self, clave):
        if clave not in self.cache:
            return None

        self.orden_uso.remove(clave)
        self.orden_uso.append(clave)

        return self.cache[clave]

    def put(self, clave, valor):
        if clave in self.cache:
            self.orden_uso.remove(clave)
        elif len(self.cache) >= self.capacidad:
            clave_antigua = self.orden_uso.pop(0)
            del self.cache[clave_antigua]

        self.cache[clave] = valor
        self.orden_uso.append(clave)

cache = LRUCache(2)
cache.put(1, "uno")
cache.put(2, "dos")
print(cache.get(1))   
cache.put(3, "tres")  
print(cache.get(2))   

#ejercicio 3
class MiConjunto:
    def __init__(self):
        self.elementos = []  

    def add(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remove(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            raise KeyError(f"{elemento} no está en el conjunto")

    def discard(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def __contains__(self, elemento):
        return elemento in self.elementos

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"

mi_conjunto = MiConjunto()
mi_conjunto.add(1)
mi_conjunto.add(2)
mi_conjunto.add(1) 
print(len(mi_conjunto))  
print(1 in mi_conjunto)  
print(mi_conjunto)       

#ejercicio 4
def filtrar_jugadores(datos, condicion):
    resultado = {}  

    for equipo, info in datos.items():
        resultado[equipo] = {"jugadores": []}
        for jugador in info["jugadores"]:
            if condicion(jugador):
                resultado[equipo]["jugadores"].append(jugador)

    return resultado

datos = {
    "equipo1": {"jugadores": [{"nombre": "Ana", "puntos": 120}, {"nombre": "Juan", "puntos": 80}]},
    "equipo2": {"jugadores": [{"nombre": "Maria", "puntos": 90}, {"nombre": "Pedro", "puntos": 150}]}
}
print(filtrar_jugadores(datos, lambda j: j["puntos"] > 100))

#ejercicio 5 
def encontrar_ruta(arbol, valor):
    def buscar(nodo, camino_actual):
        if nodo is None:
            return None
        camino_actual.append(nodo["valor"])
        if nodo["valor"] == valor:
            return camino_actual
        camino_izq = buscar(nodo["izquierdo"], camino_actual.copy())
        if camino_izq:
            return camino_izq
        camino_der = buscar(nodo["derecho"], camino_actual.copy())
        if camino_der:
            return camino_der
        return None
    return buscar(arbol, [])
arbol = {
    "valor": "A",
    "izquierdo": {
        "valor": "B",
        "izquierdo": {"valor": "D", "izquierdo": None, "derecho": None},
        "derecho": {"valor": "E", "izquierdo": None, "derecho": None}
    },
    "derecho": {
        "valor": "C",
        "izquierdo": None,
        "derecho": {"valor": "F", "izquierdo": None, "derecho": None}
    }
}
print(encontrar_ruta(arbol, "F"))









