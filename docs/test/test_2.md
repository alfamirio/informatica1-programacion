# Preguntas de Programación Muy Básica con Python

1.  ¿Qué palabra clave se utiliza en Python para definir una función?
    1.  `function`
    2.  `def`
    3.  `func`
    4.  `define`

2.  ¿Cómo se llama el acto de ejecutar el código dentro de una función?
    1.  Definir la función
    2.  Declarar la función
    3.  Llamar a la función
    4.  Importar la función

3.  ¿Cuál es la salida del siguiente código?
    ```python
    def saludar():
        print("Hola")

    saludar()
    ```
    1.  Hola
    2.  saludar()
    3.  Nada (solo se define)
    4.  Error

4.  ¿Qué son los "parámetros" en una función?
    1.  El nombre de la función.
    2.  Los valores que la función devuelve.
    3.  Variables listadas entre paréntesis en la definición de la función, que reciben valores al llamarla.
    4.  El bloque de código dentro de la función.

5.  ¿Cuál es la salida del siguiente código?
    ```python
    def mostrar_doble(numero):
        print(numero * 2)

    mostrar_doble(5)
    ```
    1.  5
    2.  10
    3.  numero * 2
    4.  Error

6.  ¿Qué palabra clave se utiliza en Python para especificar el valor que una función debe devolver?
    1.  `print`
    2.  `yield`
    3.  `return`
    4.  `output`

7.  ¿Cuál es la salida del siguiente código?
    ```python
    def sumar(a, b):
        return a + b

    resultado = sumar(3, 4)
    print(resultado)
    ```
    1.  sumar(3, 4)
    2.  3 + 4
    3.  7
    4.  Error

8.  ¿Qué operador de comparación se utiliza para comprobar si dos valores son iguales?
    1.  `=`
    2.  `==`
    3.  `!=`
    4.  `>`

9.  ¿Qué operador de comparación se utiliza para comprobar si un valor es *mayor que* otro?
    1.  `<`
    2.  `>`
    3.  `<=`
    4.  `>=`

10. ¿Cuál es la salida del siguiente código?
    ```python
    edad = 18
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
    ```
    1.  Mayor de edad
    2.  Menor de edad
    3.  Error
    4.  Nada

11. ¿Cuál es la salida del siguiente código?
    ```python
    temperatura = 25
    if temperatura > 30:
        print("Calor")
    elif temperatura < 10:
        print("Frío")
    else:
        print("Templado")
    ```
    1.  Calor
    2.  Frío
    3.  Templado
    4.  Error

12. ¿Qué operador lógico devuelve `True` si *al menos una* de las condiciones que conecta es verdadera?
    1.  `and`
    2.  `or`
    3.  `not`
    4.  `is`

13. ¿Cuál es la salida del siguiente código?
    ```python
    tiene_carnet = True
    tiene_coche = False
    if tiene_carnet and tiene_coche:
        print("Puede conducir")
    else:
        print("No puede conducir")
    ```
    1.  Puede conducir
    2.  No puede conducir
    3.  Error
    4.  True

14. ¿Cuál es el rango de números generado por `range(3)`?
    1.  1, 2, 3
    2.  0, 1, 2
    3.  1, 2
    4.  0, 1, 2, 3

15. ¿Cuál es la salida del siguiente código?
    ```python
    for i in range(2):
        print("Python")
    ```
    1.  Python
    2.  Python
        Python
    3.  Python Python
    4.  Nada

16. ¿Cuántas veces se imprimirá "Hola" en el siguiente código?
    ```python
    for _ in range(4):
        print("Hola")
    ```
    1.  0
    2.  3
    3.  4
    4.  5

17. ¿Cuál es la salida del siguiente código?
    ```python
    fruta = "manzana"
    for letra in fruta:
        print(letra)
    ```
    1.  manzana
    2.  m a n z a n a
    3.  m
        a
        n
        z
        a
        n
        a
    4.  Error

18. ¿Qué hace la sentencia `break` en un bucle `for` cuando se ejecuta?
    1.  Pasa a la siguiente iteración del bucle.
    2.  Termina completamente el bucle.
    3.  Reinicia el bucle desde el principio.
    4.  Omite el resto del código en la iteración actual.

19. ¿Qué hace la sentencia `continue` en un bucle `for` cuando se ejecuta?
    1.  Pasa a la siguiente iteración del bucle.
    2.  Termina completamente el bucle.
    3.  Reinicia el bucle desde el principio.
    4.  Genera un error.

20. ¿Cuál es la salida del siguiente código?
    ```python
    numeros = [10, 20, 30]
    suma = 0
    for num in numeros:
        suma += num
    print(suma)
    ```
    1.  102030
    2.  60
    3.  3
    4.  Error

21. ¿Cuál es la salida del siguiente código?
    ```python
    contador = 0
    for i in range(5):
        if i == 3:
            break
        contador += 1
    print(contador)
    ```
    1.  0
    2.  1
    3.  2
    4.  3

22. ¿Cuál es la salida del siguiente código?
    ```python
    resultado = ""
    for letra in "abc":
        if letra == "b":
            continue
        resultado += letra
    print(resultado)
    ```
    1.  abc
    2.  ac
    3.  bc
    4.  ab

23. ¿Qué valor debe tener la variable `x` para que la siguiente condición sea verdadera?
    ```python
    if x > 5 and x < 10:
        print("OK")
    ```
    1.  5
    2.  10
    3.  7
    4.  3

24. Si una condición `es_lluvioso` es `False`, ¿qué operador lógico la haría `True`?
    1.  `and`
    2.  `or`
    3.  `not`
    4.  `is`

25. ¿Cómo se termina la ejecución de un bucle `while` si la condición sigue siendo verdadera pero quieres salir antes?
    1.  Con la sentencia `continue`.
    2.  Con la sentencia `pass`.
    3.  Con la sentencia `break`.
    4.  Con la sentencia `return`.

26. ¿Qué tipo de dato en Python se define usando corchetes `[]` y puede contener elementos de diferentes tipos?
    1.  Tupla
    2.  Diccionario
    3.  Conjunto (Set)
    4.  Lista

27. ¿Cuál es el índice del segundo elemento en una lista de Python?
    1.  0
    2.  1
    3.  2
    4.  -1

28. Dada la lista `colores = ['rojo', 'verde', 'azul']`, ¿cómo accedes al elemento 'verde'?
    1.  `colores[1]`
    2.  `colores[2]`
    3.  `colores[0]`
    4.  `colores.get(1)`

29. ¿Cuál es la salida del siguiente código?
    ```python
    numeros = [1, 2, 3, 4]
    print(len(numeros))
    ```
    1.  1
    2.  4
    3.  3
    4.  1234

30. ¿Qué método se utiliza para añadir un elemento al final de una lista?
    1.  `insert()`
    2.  `add()`
    3.  `append()`
    4.  `push()`

31. ¿Cuál es la salida del siguiente código?
    ```python
    frutas = ['manzana', 'banana']
    frutas.append('cereza')
    print(frutas[2])
    ```
    1.  manzana
    2.  banana
    3.  cereza
    4.  Error

32. ¿Cómo se elimina el último elemento de una lista llamada `mis_cosas`?
    1.  `mis_cosas.remove()`
    2.  `del mis_cosas[-1]`
    3.  `mis_cosas.pop()`
    4.  Tanto 2 como 3 son opciones válidas

33. ¿Cuál es la salida del siguiente código?
    ```python
    letras = ['a', 'b', 'c', 'd']
    letras.remove('b')
    print(letras)
    ```
    1.  ['a', 'c', 'd']
    2.  ['b']
    3.  ['a', 'b', 'c', 'd']
    4.  Error

34. ¿Qué tipo de dato en Python almacena elementos en pares clave-valor?
    1.  Lista
    2.  Tupla
    3.  Conjunto (Set)
    4.  Diccionario

35. ¿Qué se utiliza para separar la clave del valor en un par clave-valor de un diccionario?
    1.  `=`
    2.  `:`
    3.  `,`
    4.  `;`

36. ¿Cómo se accede al valor asociado a una clave en un diccionario?
    1.  Usando corchetes `[]` con la clave.
    2.  Usando el método `.get()` con la clave.
    3.  Ambas 1 y 2 son formas comunes de acceder.
    4.  Usando paréntesis `()` con la clave.

37. Dada el diccionario `persona = {'nombre': 'Ana', 'edad': 25}`, ¿cómo accedes al valor de la clave 'nombre'?
    1.  `persona['nombre']`
    2.  `persona('nombre')`
    3.  `persona.key('nombre')`
    4.  `persona.value('nombre')`

38. ¿Cómo se añade un nuevo par clave-valor (`'ciudad': 'París'`) al diccionario `persona = {'nombre': 'Ana', 'edad': 25}`?
    1.  `persona.add('ciudad', 'París')`
    2.  `persona['ciudad'] = 'París'`
    3.  `persona.append('ciudad': 'París')`
    4.  `persona.update({'ciudad': 'París'})`
    *(Nota: Ambas 2 y 4 son válidas, pero 2 es la forma más básica)*

39. ¿Cuál es la salida del siguiente código?
    ```python
    capitales = {'España': 'Madrid', 'Francia': 'París'}
    print(capitales['España'])
    ```
    1.  España
    2.  Madrid
    3.  París
    4.  Error

40. ¿Cuál es la salida del siguiente código?
    ```python
    animales = {'gato': 1, 'perro': 2, 'pez': 5}
    print(len(animales))
    ```
    1.  1
    2.  2
    3.  3
    4.  8

41. ¿Cómo se elimina la clave 'edad' y su valor del diccionario `persona = {'nombre': 'Ana', 'edad': 25}`?
    1.  `persona.remove('edad')`
    2.  `del persona['edad']`
    3.  `persona.popitem('edad')`
    4.  `persona.discard('edad')`

42. ¿Qué método de diccionario devuelve una lista (o vista) de todas las claves?
    1.  `values()`
    2.  `keys()`
    3.  `items()`
    4.  `get()`

43. ¿Qué método de diccionario devuelve una lista (o vista) de todos los valores?
    1.  `values()`
    2.  `keys()`
    3.  `items()`
    4.  `get()`

44. ¿Qué sucede si intentas acceder a una clave que no existe en un diccionario usando el método `.get()`?
    1.  Se produce un error `KeyError`.
    2.  Se devuelve el valor `None` por defecto.
    3.  Se devuelve una cadena vacía `""`.
    4.  Se añade la clave al diccionario.

45. ¿Cuál es la salida del siguiente código?
    ```python
    mi_lista = [10, 20]
    mi_lista[0] = 15
    print(mi_lista)
    ```
    1.  [10, 20]
    2.  [15, 20]
    3.  [15]
    4.  Error

46. ¿Cuál es la salida del siguiente código?
    ```python
    mi_diccionario = {'a': 1, 'b': 2}
    mi_diccionario['b'] = 20
    print(mi_diccionario['b'])
    ```
    1.  2
    2.  20
    3.  b
    4.  Error

47. ¿Qué operador se utiliza para comprobar si un elemento existe en una lista o si una clave existe en un diccionario?
    1.  `==`
    2.  `in`
    3.  `is`
    4.  `has`

48. ¿Cuál es la salida del siguiente código?
    ```python
    lista = [1, 2, 3]
    print(2 in lista)
    ```
    1.  True
    2.  False
    3.  Error
    4.  2

49. ¿Cuál es la salida del siguiente código?
    ```python
    dicc = {'x': 1, 'y': 2}
    print('z' in dicc)
    ```
    1.  True
    2.  False
    3.  Error
    4.  z

50. ¿Es posible tener dos claves iguales en un mismo diccionario de Python?
    1.  Sí, y ambas claves apuntarán al mismo valor.
    2.  Sí, y la última clave definida sobrescribirá a la anterior.
    3.  No, las claves deben ser únicas.
    4.  Solo si los valores asociados son diferentes.

---

## Tabla de Respuestas

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
| :------- | :-------- | :------- | :-------- | :------- | :-------- | :------- | :-------- | :------- | :-------- |
| 1        | 2         | 11       | 3         | 21       | 4         | 31       | 3         | 41       | 2         |
| 2        | 3         | 12       | 2         | 22       | 2         | 32       | 4         | 42       | 2         |
| 3        | 1         | 13       | 2         | 23       | 3         | 33       | 1         | 43       | 1         |
| 4        | 3         | 14       | 2         | 24       | 3         | 34       | 4         | 44       | 2         |
| 5        | 2         | 15       | 2         | 25       | 3         | 35       | 2         | 45       | 2         |
| 6        | 3         | 16       | 3         | 26       | 4         | 36       | 3         | 46       | 2         |
| 7        | 3         | 17       | 3         | 27       | 2         | 37       | 1         | 47       | 2         |
| 8        | 2         | 18       | 2         | 28       | 1         | 38       | 2         | 48       | 1         |
| 9        | 2         | 19       | 1         | 29       | 2         | 39       | 2         | 49       | 2         |
| 10       | 1         | 20       | 2         | 30       | 3         | 40       | 3         | 50       | 3         |
