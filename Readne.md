Descripción general

Este programa permite calcular las corrientes en cada malla de un circuito eléctrico utilizando el método de mallas de Kirchhoff. Además, guarda los resultados en un archivo y dibuja un diagrama visual simplificado del circuito mostrando resistencias, voltajes y corrientes.

Paso a paso de lo que hace el programa

Pide al usuario el número de mallas

Una malla es un lazo cerrado en un circuito eléctrico.

El usuario escribe un número entero (por ejemplo, 3 para un circuito con 3 mallas).

Solicita las resistencias de cada malla

El programa pregunta: “Resistencia total de la malla 1 (Ω):”, y así sucesivamente para cada malla.

La resistencia se ingresa en ohmios (Ω).

Ejemplo de entrada:

Malla 1: 6
Malla 2: 8
Malla 3: 10


Solicita las resistencias compartidas entre mallas (acoplamientos)

Si dos mallas tienen una resistencia en común, se debe ingresar su valor.

Si no tienen ninguna resistencia compartida, se ingresa 0.

Ejemplo de entrada para 3 mallas:

Resistencia entre malla 1 y 2: 2
Resistencia entre malla 1 y 3: 1
Resistencia entre malla 2 y 3: 3


Solicita las fuentes de voltaje de cada malla

El programa pregunta la suma de todas las fuentes de voltaje dentro de cada malla.

Ejemplo de entrada:

Malla 1: 12
Malla 2: 5
Malla 3: 8


Construye la matriz del sistema de ecuaciones

Internamente, el programa arma una tabla de números llamada matriz de coeficientes, basada en la Ley de Mallas de Kirchhoff.

Esta matriz relaciona las resistencias de las mallas y las resistencias compartidas para poder calcular las corrientes.

Resuelve las corrientes de cada malla

El programa calcula automáticamente la corriente en cada malla usando matemáticas (resolviendo un sistema de ecuaciones).

Luego muestra los resultados en la pantalla.

Para los datos de ejemplo anteriores, los resultados aproximados serían:

Corriente I1 = 1.614 A
Corriente I2 = 0.833 A
Corriente I3 = 0.865 A


Guarda los resultados en un archivo CSV

El archivo se llama resultados_mallas.csv.

Contiene una tabla con:

Número de malla

Resistencia (Ω)

Fuente de voltaje (V)

Corriente calculada (A)

Esto permite abrir los resultados en Excel o cualquier editor de texto.

Dibuja un esquema simplificado del circuito

Cada malla aparece como un nodo.

Las resistencias compartidas se muestran como líneas entre nodos.

Cada nodo muestra:

La resistencia de la malla

El voltaje de la fuente

La corriente calculada

Esto ayuda a visualizar cómo circula la corriente en el circuito.

Datos de prueba para usar con el programa

Número de mallas: 3

Resistencias de cada malla (Ω):

Malla 1: 6

Malla 2: 8

Malla 3: 10

Resistencias compartidas entre mallas (Ω):

Malla 1 y 2: 2

Malla 1 y 3: 1

Malla 2 y 3: 3

Fuentes de voltaje en cada malla (V):

Malla 1: 12

Malla 2: 5

Malla 3: 8

Resultados esperados:

Corriente I1 ≈ 1.614 A
Corriente I2 ≈ 0.833 A
Corriente I3 ≈ 0.865 A

Resumen

Este programa hace todo el trabajo matemático y visual de forma automática:

Calcula corrientes en cada malla.

Muestra los resultados en pantalla.

Guarda un archivo CSV con los resultados.

Dibuja un esquema visual del circuito con nodos y aristas, mostrando resistencias, voltajes y corrientes