# tarea2rrnn
# Tarea 2 Algoritmo Genetico

Cristóbal Fuentes

# Analisis

## Resultados

Para todos los siguientes resultados (a menos que se indice contrariamente) se usó una población de **100 individuos**, y una **tasa de mutación de 0.1**.

La selección de padres se hizo por torneo (5 individuos). Se mantuvo el ganador de cada generación intacto para la siguiente (elitismo de 1 individuo). El crossover era del tipo partición de cromosoma y unión de las mitades de forma cruzada, generando un único hijo.

### 1. Secuencia de bits

Consideré un Cromosoma de largo = largo del string buscado. Cada gen del cromosoma es 0 o 1, y describen la palabra de forma literal (cromosoma: 011011 = string "011011").

La función de fitness usada simplemente cuenta las diferencias punto a punto entre la palabra buscada y la representada por el cromosoma y le resta esto a un puntaje considerado el óptimo (el largo de la palabra).

Para el resultado seguidamente mostrado se buscaba encontrar el string "**001010101101010110101110**"

```javascript
Generation 1 Winner: [0 0 1 0 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 0 1 1]
Max Score: 17 ; Average Score: 12.0 ; Min Score: 6
Generation 2 Winner: [0 0 0 0 1 0 1 1 1 0 0 1 0 1 0 1 1 0 1 0 1 1 1 1]
Max Score: 20 ; Average Score: 15.0 ; Min Score: 9
Generation 3 Winner: [0 0 0 0 1 0 1 1 1 0 0 1 0 1 0 1 1 0 1 0 1 1 1 1]
Max Score: 20 ; Average Score: 16.0 ; Min Score: 12
...
Max Score: 23 ; Average Score: 21.0 ; Min Score: 17
Generation 11 Winner: [0 0 1 0 1 0 1 0 1 1 0 1 1 1 0 1 1 0 1 0 1 1 1 0]
Max Score: 23 ; Average Score: 21.0 ; Min Score: 18
Generation 12 Winner: [0 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 1 0 1 0 1 1 1 0]
Max Score: 24 ; Average Score: 21.0 ; Min Score: 18
```

![Figure 1](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_1.5.png)


### 2.Encontrar una palabra/frase:

Cromosoma de largo igual al largo de la palabra buscada. Cada gen equivale a la representación decimal ASCII de un carácter entre los ordinales 32 (" ") y 90 ("Z"). El crómosoma representa literalmente la palabra carácter por carácter.

La función de fitness usada simplemente cuenta las diferencias punto a punto entre la palabra buscada y la representada por el cromosoma y le resta esto a un puntaje considerado el óptimo (el largo de la palabra).

Para el siguiente resultado se buscaba el string "**Hello World!**" (sin commilas)

```javascript
Generation 1 Winner: [ 64 101  75 108  65  79  91  70 111  82  94  85]
Max Score: 2 ; Average Score: 0.0 ; Min Score: 0
Generation 2 Winner: [ 64 101  75 108  65  79  91  70 111  82  94  99]
Max Score: 2 ; Average Score: 0.0 ; Min Score: 0
Generation 3 Winner: [ 56 105  52 108  40  54 106  82  46  56 100  86]
Max Score: 2 ; Average Score: 1.0 ; Min Score: 0
Generation 4 Winner: [ 64 101  75 108  65  78  87  43  66  96  62  75]
Max Score: 3 ; Average Score: 1.0 ; Min Score: 0
Generation 5 Winner: [ 44  42 102 108  40  54  75  64 114  50 100  86]
Max Score: 3 ; Average Score: 2.0 ; Min Score: 0
Generation 6 Winner: [ 59 101  75 108  65  64  69  70  72 108  77  70]
Max Score: 3 ; Average Score: 2.0 ; Min Score: 0
Generation 7 Winner: [ 59 101  75 108  72  64  76  70  95 108  94  98]
Max Score: 3 ; Average Score: 2.0 ; Min Score: 0
Generation 8 Winner: [ 59 101  75 108  33  74  69 111 111  58 100  43]
Max Score: 4 ; Average Score: 2.0 ; Min Score: 0
....
Generation 208 Winner: [ 72 101 108 108 111  32  44 111 114 108 100  33]
Max Score: 11 ; Average Score: 8.0 ; Min Score: 3
Generation 209 Winner: [ 72 101 108 108 111  32  44 111 114 108 100  33]
Max Score: 11 ; Average Score: 7.0 ; Min Score: 2
Generation 210 Winner: [ 72 101 108 108 111  32  50 111 114 108 100  33]
Max Score: 11 ; Average Score: 7.0 ; Min Score: 3
Generation 211 Winner: [ 72 101 108 108 111  32  87 111 114 108 100  33]
Max Score: 12 ; Average Score: 7.0 ; Min Score: 3
```

![Figure 2](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_2.png)

El puntaje alcanza el máximo deseado (12) en la generación 211, deteniendo el algoritmo. 


El siguiente buscaba el string "**lkqjwekjasdm AKHV-!@#$345132**" (sin comillas)


```javascript
Generation 1 Winner: [ 63  56  42 111  95 112  85  36 114 117  79 106  65  48  66 122 100  45
  49  51 111  65  51  67  38  49  71  54]
Max Score: 3 ; Average Score: 0.0 ; Min Score: 0
Generation 2 Winner: [ 81 107  57 114  67 104 107  35  48 100  38 109 104  75  70 117  53 117
  85  45  45  54  97 118  54  84  69  48]
Max Score: 3 ; Average Score: 1.0 ; Min Score: 0
Generation 3 Winner: [ 81 107  57 114  67 104 107  78 101 100  38 109 104  46  70 117  53  56
  85  45  45  52  40  86  50  75  51  89]
...
Generation 2481 Winner: [108 107 113 106 119 101 107 106  97 115 100 109  32  65  75  72  86  45
  33  64  35  36  51  39  53  49  51  50]
Max Score: 27 ; Average Score: 22.0 ; Min Score: 17
Generation 2482 Winner: [108 107 113 106 119 101 107 106  97 115 100 109  32  65  75  72  86  45
  33  64  35  36  51  52  53  49  51  50]
Max Score: 28 ; Average Score: 22.0 ; Min Score: 16
```

![Figure 2.5](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_2.5.png)

Se alcanzó en la generación 2482.

### 3.Unbound-Knapsack

Cada cromosoma tiene largo igual a la cantidad cajas. El gen iésimo de un cromosoma indica la cantidad de cajas de tipo iésimo en la mochila (un número entero mayor o igual que cero)

La función de fitness calcula la suma total de valores, si y solo si la suma de pesos es menor al límite. En caso contrario la función de fitness retorna 0 (mínimo).

```javascript
Generation 1 Winner: [0 1 1 4 2]
Max Score: 28 ; Average Score: 0.0 ; Min Score: 0
Generation 2 Winner: [0 1 1 4 2]
Max Score: 28 ; Average Score: 0.0 ; Min Score: 0
Generation 3 Winner: [0 1 1 4 2]
...
Generation 42 Winner: [0 1 1 0 3]
Max Score: 34 ; Average Score: 0.0 ; Min Score: 0
Generation 43 Winner: [0 0 3 0 3]
Max Score: 36 ; Average Score: 0.0 ; Min Score: 0
...
Generation 198 Winner: [0 0 3 0 3]
Max Score: 36 ; Average Score: 0.0 ; Min Score: 0
Generation 199 Winner: [0 0 3 0 3]
Max Score: 36 ; Average Score: 0.0 ; Min Score: 0
Generation 200 Winner: [0 0 3 0 3]
Max Score: 36 ; Average Score: 0.0 ; Min Score: 0
```

![Figure 3](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_3.png)

La función logra el óptimo en la generación 43, y mantiene este puntaje hasta la cantidad máxima de iteraciones permitidas (200). 


### 4. 0-1-Knapsack

Igual que la anterior, pero los genes solo pueden 0 o 1.

```javascript
Generation 1 Winner: [0 1 1 1 1]
Max Score: 15 ; Average Score: 4.0 ; Min Score: 0
Generation 2 Winner: [0 1 1 1 1]
Max Score: 15 ; Average Score: 8.0 ; Min Score: 0
...
Generation 200 Winner: [0 1 1 1 1]
Max Score: 15 ; Average Score: 14.0 ; Min Score: 0
```

![Figure 4](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_4.png)




### Heatmap

String a obtener: "0010101011010111"

Límite generaciones: 200

Poblaciones a probar: 1, 10, 20, ..., 100

Tasas de mutación: 0.0, 0.1, 0.2, ..., 1.0

```javascript
[[200. 200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]
 [200.  12.  13.  17.  54. 154. 200. 200. 200. 200. 200.]
 [200.   4.   9.  15.  12.  28.  44. 200. 200.  56. 200.]
 [200.   6.  10.  16.  16.  34.  36. 200. 200. 200. 167.]
 [200.   9.   7.   5.   9.   7.  21. 109. 200. 200. 200.]
 [ 10.   8.   9.  12.   5.   9.  24. 200. 200.  83. 166.]
 [200.   4.   6.   8.   7.  39. 200. 200. 200. 200. 200.]
 [  7.   6.   7.  12.  23.  25.  18. 200. 200. 200. 200.]
 [200.   6.   7.  16.  21.  27.  31.  65.  35. 191. 200.]
 [  7.   7.   7.  18.   4.   6.  16.  27. 200.  18. 200.]
 [  6.   7.   7.  11.  17.  14.  67. 117. 200.   3. 200.]]
 ```

![Figure 5](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_5.png)

X axis: tasa de mutación (0.0 a 1.0 de izquierda a derecha)

Y axis: poblacion (1 a 100 de arriba a abajo)

Como se ve, cuando la tasa de mutación es 1, el problema de encontrar el string no se logra en la cantidad de generaciones impuestas, pues no hay herencia, todos los genes son aleatorios cada generación.

Mayor población tiene una relación directa con menor cantidad de generaciones requeridas, ya que es más probable encontrar la combinación correcta de genes. Sin embargo, la tasa de mutación demasiado alta disminuye la efectividad de aumentar la población.

La tasa de mutación alcanza sus mejores resultados cuando es 0.1 para este caso. Esto podría deberse a la función de fitness usada, pues le da igual importancia a todos los genes. Para un cromosoma de 16 genes (como el del ejemplo), una tasa de mutación de 0.1 corresponde, en promedio, entre 1 y 2 genes aleatorios por individuo, lo cual evita que se pierda el valor de los padres, pero permite suficiente variabilidad para potencialmente mejorar.

Otra conclusión que obtuve es que eventualmente el crecimiento del fitness de la población disminuye drásticamente y el mejoramiento depende casi por completo de la tasa de mutación. Esto hace preguntarme si sería inteligente incrementar la tasa de mutación después de cierto punto (como que no haya crecimiento de fitness en n generaciones)

