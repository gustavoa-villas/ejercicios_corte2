
# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")
print("Esta función tiene un except desnudo. Arréglalo para capturar excepciones específicas.")
print()

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    ARREGLA: Usa manejo de excepciones específico en lugar de except desnudo.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
        print("Error: la lista está vacía, no se puede dividir entre cero.")
        return None
    except TypeError:
        print("Error: todos los elementos deben ser numéricos.")
        return None

# print(calcular_promedio([1, 2, 3, 4, 5]))
# print(calcular_promedio([]))
# print(calcular_promedio([1, 2, 'a']))

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")
print("Este código falla silenciosamente. Añade mensajes apropiados.")
print()

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo.
    ARREGLA: Añade manejo de excepciones Y feedback al usuario.
    """
    try:
        with open(archivo, 'w') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en '{archivo}'.")
        return True
    except FileNotFoundError:
        print("Error: la ruta especificada no existe.")
        return False
    except PermissionError:
        print("Error: no tienes permiso para escribir en este archivo.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False

# guardar_datos({"usuario": "Ana"}, "datos.txt")
# guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")
print("Implementa un manejo completo de archivos con else y finally.")
print()

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    TODO: Implementa try-except-else-finally:
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    """
    try:
        f = open(nombre_archivo, 'r')
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    else:
        contenido = f.read()
        print(f"Archivo leído correctamente. Contenido:\n{contenido}")
    finally:
        try:
            f.close()
            print("Archivo cerrado correctamente.")
        except NameError:
            print("No se abrió ningún archivo.")

# procesar_archivo("existente.txt")
# procesar_archivo("faltante.txt")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")
print("Implementa validación con excepciones específicas.")
print()

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    """
    if len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años.")
    if '@' not in email:
        raise ValueError("El email debe contener '@'.")
    print(f"Usuario '{nombre_usuario}' creado correctamente.")
    return {"nombre": nombre_usuario, "edad": edad, "email": email}

# crear_usuario("Ana", 25, "ana@example.com")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")
print("Crea excepciones personalizadas para un sistema bancario.")
print()

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

class MontoInvalidoError(Exception):
    pass

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    """
    if monto <= 0:
        raise MontoInvalidoError("El monto debe ser mayor que cero.")
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo}")
    return nuevo_saldo

# retirar(100, 50)

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")
print("Procesa una lista con manejo de errores.")
print()

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    """
    resultados = []
    errores = []
    for elemento in lista_strings:
        try:
            num = int(elemento)
            resultados.append(num * 2)
        except ValueError as e:
            errores.append((elemento, str(e)))
    return resultados, errores

# resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")
print("Registra errores pero permite que el llamador los maneje.")
print()

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    """
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error en operacion_critica: {e}")
        raise  # Re-lanza la excepción

# try:
#     operacion_critica("0")
# except ZeroDivisionError:
#     print("Llamador: Manejó el error")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")
print("Maneja diferentes tipos de errores de manera diferente.")
print()

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    """
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación inválida.")
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero."
    except TypeError:
        return "Error: los operandos deben ser numéricos."
    except ValueError as e:
        return f"Error: {e}"

# print(calculadora_segura("suma", 10, 5))
# print(calculadora_segura("division", 10, 0))
# print(calculadora_segura("invalida", 10, 5))

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")
print("Preserva el contexto al lanzar nuevas excepciones.")
print()

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON.
    """
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Error al parsear configuración JSON") from e

# print(parsear_configuracion('{"nombre": "Ana"}'))

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 10: Proyecto completo
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")
print("Crea un sistema de gestión de inventario con manejo completo de excepciones.")
print()

class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass

class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""
    
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, codigo, nombre, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if codigo in self.productos:
            raise KeyError(f"El producto con código '{codigo}' ya existe.")
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"Producto '{nombre}' agregado con código {codigo}.")
    
    def retirar_stock(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto '{codigo}' no encontrado.")
        if cantidad > self.productos[codigo]["cantidad"]:
            raise StockInsuficiente(f"No hay suficiente stock para '{codigo}'.")
        self.productos[codigo]["cantidad"] -= cantidad
        print(f"Se retiraron {cantidad} unidades de '{codigo}'. Nuevo stock: {self.productos[codigo]['cantidad']}")
    
    def obtener_producto(self, codigo):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto '{codigo}' no encontrado.")
        return self.productos[codigo]

# inventario = Inventario()
# inventario.agregar_producto("001", "Laptop", 10)
# inventario.retirar_stock("001", 5)

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN")
print("=" * 70 + "\n")

print("1. Se usaron principalmente ValueError, TypeError y FileNotFoundError.")
print("2. Se crearon excepciones personalizadas cuando fue necesario expresar reglas de negocio (banco, inventario).")
print("3. El patrón try-except-else-finally fue el más útil para asegurar limpieza de recursos.")
print("4. El manejo de excepciones mejora la experiencia del usuario al informar errores claros sin detener el programa.")
print("5. Se evitaron errores comunes como división por cero, archivos inexistentes y validaciones de tipo.")

print("=" * 70)
print(" ¡EJERCICIOS COMPLETADOS!")
print("=" * 70)