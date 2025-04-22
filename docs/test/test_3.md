# Preguntas de Programación Básica en Python

1.  ¿Cuál es la fase que generalmente precede a la fase de diseño en el modelo Waterfall?
    1. Implementación
    2. Pruebas
    3. Requisitos
    4. Mantenimiento

2.  En la fase de diseño del modelo Waterfall, ¿qué se define principalmente?
    1. El código fuente final del programa
    2. La estructura general y la arquitectura del sistema
    3. Los errores encontrados durante la ejecución
    4. La documentación del usuario final

3.  ¿Es común volver a una fase anterior (como requisitos) una vez que se ha completado la fase de diseño en el modelo Waterfall clásico?
    1. Sí, es parte del flujo normal
    2. No, el modelo es estrictamente secuencial
    3. Solo si se usa una metodología ágil
    4. Solo durante la fase de mantenimiento

4.  La creación de diagramas de flujo o diagramas UML para representar la estructura del programa es una actividad típica de la fase de:
    1. Implementación
    2. Pruebas
    3. Diseño
    4. Despliegue

5.  ¿Qué documento importante suele ser el resultado principal de la fase de diseño detallado?
    1. Informe de pruebas
    2. Manual de usuario
    3. Especificación de diseño de software (SDS)
    4. Código ejecutable

6.  En el contexto del diseño, ¿qué significa "diseño de bajo nivel" o "diseño detallado"?
    1. Definir la arquitectura general del sistema
    2. Especificar cómo se implementarán los componentes individuales
    3. Identificar los requisitos del usuario
    4. Realizar pruebas de integración

7.  ¿Cuál es uno de los principales objetivos de la fase de diseño en cualquier modelo de desarrollo de software?
    1. Escribir el código más rápido posible
    2. Planificar cómo resolver el problema y construir la solución
    3. Comercializar el producto
    4. Recopilar feedback de los usuarios finales

8.  Si en la fase de diseño se descubre una ambigüedad en los requisitos, ¿qué debería ocurrir idealmente en un proceso Waterfall estricto?
    1. Continuar con el diseño asumiendo una interpretación
    2. Documentar la ambigüedad y resolverla en la fase de implementación
    3. Detener el diseño y volver a la fase de requisitos para clarificar
    4. Pedir al equipo de pruebas que decida la interpretación

9.  La elección de estructuras de datos y algoritmos a un nivel conceptual es una actividad de la fase de:
    1. Mantenimiento
    2. Despliegue
    3. Diseño
    4. Pruebas

10. ¿Qué riesgo se intenta mitigar con una fase de diseño exhaustiva antes de la implementación?
    1. No encontrar errores en las pruebas
    2. Tener que hacer cambios mayores y costosos en etapas posteriores
    3. Que el software sea demasiado rápido
    4. Que el equipo de desarrollo no tenga suficiente trabajo

11. ¿Cuál es el objetivo principal del diseño modular en programación?
    1. Escribir todo el código en un solo archivo
    2. Dividir un sistema complejo en partes más pequeñas e independientes
    3. Usar la mayor cantidad posible de librerías externas
    4. Hacer el código difícil de entender para otros

12. En Python, ¿qué mecanismo se utiliza comúnmente para implementar la modularidad?
    1. Comentarios extensos
    2. Variables globales
    3. Funciones y módulos (archivos .py)
    4. Bucles infinitos

13. Considera el siguiente código:
    ```python
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    resultado_suma = sumar(10, 5)
    resultado_resta = restar(10, 5)
    ```
    Este código es un ejemplo simple de:
    1. Programación orientada a objetos
    2. Diseño modular (uso de funciones)
    3. Programación lineal
    4. Uso de hilos concurrentes

14. ¿Qué ventaja principal ofrece el diseño modular en términos de mantenimiento del software?
    1. Hace que los errores sean más difíciles de encontrar
    2. Permite modificar una parte del sistema sin afectar otras (si está bien diseñado)
    3. Requiere reescribir todo el código para cualquier cambio pequeño
    4. Elimina la necesidad de documentación

15. La idea de "alta cohesión" en diseño modular se refiere a:
    1. Que los módulos dependan fuertemente unos de otros
    2. Que los elementos dentro de un módulo estén fuertemente relacionados y trabajen juntos para una única finalidad
    3. Que el código no esté bien organizado
    4. Que un módulo realice muchas tareas no relacionadas

16. La idea de "bajo acoplamiento" en diseño modular se refiere a:
    1. Que los módulos dependan fuertemente unos de otros
    2. Que los módulos sean tan independientes como sea posible, con mínimas dependencias entre ellos
    3. Que el código sea difícil de reutilizar
    4. Que un módulo no tenga ninguna función

17. ¿Qué hace que un módulo en Python (un archivo .py) sea reutilizable en otros proyectos?
    1. Debe tener un nombre muy largo
    2. Debe estar bien documentado y tener funciones o clases con interfaces claras
    3. Debe usar solo variables globales
    4. Debe tener muchos errores

18. Si tienes una función grande que realiza varias tareas distintas, ¿cómo aplicarías el diseño modular para mejorarla?
    1. La dejaría como está
    2. La dividiría en funciones más pequeñas, cada una encargada de una única tarea específica
    3. Añadiría más código a la función existente
    4. La eliminaría por completo

19. El concepto de ocultación de información (information hiding) está estrechamente relacionado con el diseño modular porque:
    1. Obliga a mostrar todos los detalles internos de un módulo
    2. Permite que los detalles internos de un módulo se mantengan privados, exponiendo solo una interfaz pública
    3. Hace que el código sea menos seguro
    4. No tiene ninguna relación

20. Al importar un módulo en Python (por ejemplo, `import math`), ¿qué se está utilizando?
    1. Un paradigma de programación lineal
    2. Una característica del diseño modular
    3. Un tipo de bucle
    4. Una declaración de variable

21. ¿Cuál es la característica principal del diseño Top-Down?
    1. Comenzar por los detalles más pequeños e ir construyendo hacia la solución general
    2. Dividir un problema grande en subproblemas más pequeños hasta que sean manejables
    3. Escribir el código sin ninguna planificación previa
    4. Probar el código antes de escribirlo

22. En un enfoque Top-Down, ¿por dónde se empieza el diseño?
    1. Por las funciones más pequeñas y detalladas
    2. Por el problema principal o la función de más alto nivel
    3. Por la base de datos
    4. Por la interfaz de usuario

23. Si estás diseñando un programa para procesar datos de ventas usando un enfoque Top-Down, ¿cuál sería probablemente el primer paso?
    1. Escribir la función para calcular impuestos
    2. Definir la función principal que gestiona todo el proceso de ventas
    3. Crear una clase para representar un producto
    4. Diseñar la base de datos de productos

24. Considera la siguiente estructura conceptual de funciones:
    `ProcesarVentas()` llama a `LeerDatos()` y `GenerarInforme()`
    `GenerarInforme()` llama a `CalcularTotales()` y `FormatearSalida()`

    Esto es un ejemplo de:
    1. Diseño Bottom-Up
    2. Diseño lineal
    3. Diseño Top-Down
    4. Programación reactiva

25. En el diseño Top-Down, después de identificar el problema principal, ¿qué se hace con los subproblemas resultantes de la división?
    1. Se ignoran hasta que se complete el problema principal
    2. Se resuelven inmediatamente con código
    3. Se dividen a su vez en subproblemas más pequeños (si es necesario)
    4. Se documentan y se olvidan

26. ¿Qué tipo de estructura de programa suele resultar de un diseño Top-Down?
    1. Una secuencia simple de instrucciones
    2. Una jerarquía de funciones o módulos
    3. Un único bloque de código sin divisiones
    4. Una red compleja de interconexiones aleatorias

27. ¿Qué ventaja ofrece el diseño Top-Down en la comprensión de un sistema complejo?
    1. Obliga a entender todos los detalles pequeños primero
    2. Permite entender la estructura general y el flujo de control antes de profundizar en los detalles
    3. No ofrece ninguna ventaja en la comprensión
    4. Solo es útil para programas muy simples

28. Si tienes un programa que debe `ProcesarPedido(pedido)`, y sabes que esto implica `ValidarPedido(pedido)`, `CalcularTotal(pedido)` y `ActualizarInventario(pedido)`, ¿qué enfoque de diseño estás aplicando al definir `ProcesarPedido` primero?
    1. Diseño Bottom-Up
    2. Diseño aleatorio
    3. Diseño Top-Down
    4. Diseño iterativo

29. En un equipo de desarrollo, ¿cómo puede facilitar la colaboración el diseño Top-Down?
    1. Haciendo que todos trabajen en la misma pequeña parte del código al mismo tiempo
    2. Permitiendo asignar diferentes subproblemas (módulos/funciones de nivel inferior) a diferentes miembros del equipo una vez definida la estructura superior
    3. Evitando cualquier tipo de comunicación entre los miembros
    4. Requiriendo que cada miembro diseñe y codifique el sistema completo de forma independiente

30. ¿Qué se define típicamente *antes* de escribir el código de las funciones individuales en un enfoque Top-Down?
    1. Los resultados de las pruebas unitarias
    2. La estructura jerárquica del programa y las interfaces entre los módulos/funciones
    3. El número exacto de líneas de código
    4. Los errores de sintaxis

---

## Respuestas

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2  | 2  | 3  | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 2  | 3  | 3  | 2  | 2  | 3  | 2  | 2  |
