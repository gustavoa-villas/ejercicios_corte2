
"""
ESTRUCTURAS DE CONTROL CONFUSAS 
"""

import os
import time

def limpiar_pantalla():
    """Limpiar la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")

def mostrar_titulo(texto):
    """Muestra un título formateado"""
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")

def mostrar_seccion(texto):
    """Muestra un encabezado de sección"""
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)


# Inicio del programa interactivo
limpiar_pantalla()
mostrar_titulo("ESTRUCTURAS DE CONTROL EN PYTHON - Versión Resuelta")

print("¡Bienvenidos a la exploración interactiva de estructuras de control (versión resuelta)!")
print("Aquí podrás ver las respuestas correctas y explicaciones de cada confusión común.")
esperar_enter()


# ===========================================================================
# Ejercicio 1: Modificación de una lista mientras se itera
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 1: MODIFICACIÓN DURANTE ITERACIÓN")

mostrar_seccion("Código:")
print("""
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(f"Lista después del bucle: {numeros}")
""")

mostrar_seccion("Resultado real:")
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")
for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)
print(f"Lista después del bucle: {numeros}")

mostrar_seccion("Explicación:")
print("""
No se eliminaron todos los números pares. El resultado fue [1, 3, 5].
Esto ocurre porque cuando eliminamos un elemento, los índices de la lista cambian
y el bucle 'for' salta elementos. Python no vuelve atrás para revisar los que
se movieron de posición.

Solución: crear una nueva lista en lugar de modificar la original.
""")

mostrar_seccion("Versión corregida:")
numeros = [1, 2, 3, 4, 5]
numeros_filtrados = [num for num in numeros if num % 2 != 0]
print(f"Resultado correcto: {numeros_filtrados}")
esperar_enter()


# ===========================================================================
# Ejercicio 2: Confusión con range()
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 2: CONFUSIÓN CON RANGE()")

mostrar_seccion("Código:")
print("""
print("Usando range(10):")
for i in range(10):
    print(i, end=" ")

print("\\n\\nUsando range(1, 10):")
for i in range(1, 10):
    print(i, end=" ")
""")

mostrar_seccion("✅ Resultado real:")
print("Usando range(10):")
for i in range(10):
    print(i, end=" ")

print("\n\nUsando range(1, 10):")
for i in range(1, 10):
    print(i, end=" ")

mostrar_seccion("🧠 Explicación:")
print("""
range(10) genera los números del 0 al 9.
range(1, 10) genera del 1 al 9 (el último número nunca se incluye).
✅ Para obtener del 1 al 10, se usa range(1, 11).
""")

print("\nNúmeros del 1 al 10 correctamente:")
for i in range(1, 11):
    print(i, end=" ")
esperar_enter()


# ===========================================================================
# Ejercicio 3: Bucle while infinito
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 3: BUCLE WHILE INFINITO")

mostrar_seccion("📝 Código erróneo:")
print("""
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    # Falta contador += 1
""")

mostrar_seccion("⚠️ Resultado:")
print("""
Este código nunca termina, porque la variable 'contador' nunca cambia.
Por lo tanto, la condición siempre se cumple y el bucle se repite indefinidamente.
""")

mostrar_seccion("✅ Versión corregida:")
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

mostrar_seccion("🧠 Explicación:")
print("""
El incremento contador += 1 es necesario para avanzar la condición.
🟢 'for' se usa cuando conocemos el número exacto de iteraciones.
🟡 'while' se usa cuando solo tenemos una condición de salida.
""")
esperar_enter()


# ===========================================================================
# Ejercicio 4: Confusión con break vs. continue
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 4: BREAK VS. CONTINUE")

mostrar_seccion("📝 Código:")
print("""
print("Código 1 (usando break):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saliendo del bucle.")
        break
    print(f"Procesando número {i}")

print("\\nCódigo 2 (usando continue):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saltando a la siguiente iteración.")
        continue
    print(f"Procesando número {i}")
""")

mostrar_seccion("✅ Resultado:")
print("Código 1 (usando break):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saliendo del bucle.")
        break
    print(f"Procesando número {i}")

print("\nCódigo 2 (usando continue):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saltando a la siguiente iteración.")
        continue
    print(f"Procesando número {i}")

mostrar_seccion("🧠 Explicación:")
print("""
🔹 break → detiene completamente el bucle.
🔹 continue → salta la iteración actual y continúa con la siguiente.
En el primer código, el bucle se detiene al llegar a 5.
En el segundo, simplemente se omite el 5 y el bucle sigue.
""")
esperar_enter()


# ===========================================================================
# Ejercicio 5: Bucles anidados y confusión con break
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 5: BUCLES ANIDADOS Y BREAK")

mostrar_seccion("📝 Código:")
print("""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
objetivo = 6
encontrado = False

for fila in matriz:
    for elemento in fila:
        print(f"Verificando: {elemento}")
        if elemento == objetivo:
            print(f"¡Encontrado {objetivo}!")
            encontrado = True
            break
    print("Fin de la fila")

print(f"Búsqueda terminada. Encontrado: {encontrado}")
""")

mostrar_seccion("✅ Resultado real:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
objetivo = 6
encontrado = False

for fila in matriz:
    for elemento in fila:
        print(f"Verificando: {elemento}")
        if elemento == objetivo:
            print(f"¡Encontrado {objetivo}!")
            encontrado = True
            break
    print("Fin de la fila")

print(f"Búsqueda terminada. Encontrado: {encontrado}")

mostrar_seccion("🧠 Explicación:")
print("""
El 'break' solo detiene el bucle interno.
Por eso, después de encontrar el 6, aún se ejecuta "Fin de la fila",
y el bucle externo continúa.

✅ Para salir de ambos bucles:
""")

print("""
encontrado = False
for fila in matriz:
    for elemento in fila:
        if elemento == objetivo:
            encontrado = True
            break
    if encontrado:
        break
""")
esperar_enter()


# ===========================================================================
# Ejercicio 6: Comprensiones de lista vs bucles tradicionales
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 6: COMPRENSIONES VS. BUCLES TRADICIONALES")

mostrar_seccion("📝 Código:")
print("""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Método 1: Bucle tradicional")
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num ** 2)
print(f"Cuadrados de números pares: {pares}")

print("\\nMétodo 2: Comprensión de lista")
pares = [num ** 2 for num in numeros if num % 2 == 0]
print(f"Cuadrados de números pares: {pares}")
""")

mostrar_seccion("✅ Resultado:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Método 1: Bucle tradicional")
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num ** 2)
print(f"Cuadrados de números pares: {pares}")

print("\nMétodo 2: Comprensión de lista")
pares = [num ** 2 for num in numeros if num % 2 == 0]
print(f"Cuadrados de números pares: {pares}")

mostrar_seccion("🧠 Explicación:")
print("""
Ambos producen el mismo resultado: [4, 16, 36, 64, 100]

✅ Comprensiones → más compactas y elegantes.
⚙️ Bucles tradicionales → más flexibles cuando se necesita lógica compleja.
""")
esperar_enter()
