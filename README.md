# APLICACIÓN DE CODIFICACIÓN Y DECODIFICACIÓN HUFFMAN 

Esta es una aplicación desarrollada en Python utilizando el framework Kivy, que permite codificar y decodificar mensajes utilizando el algoritmo de compresión Huffman. Además cuenta con una base de datos en NeonDB. 


## ¿Quién hizo esto?

Mayezly Tatiana Gafaro Boada

## ¿Qué es y para qué es?

Este proyecto es una aplicación de codificación y decodificación utilizando el algoritmo de compresión Huffman. Permite comprimir mensajes de texto utilizando el algoritmo de Huffman para generar una secuencia de bits más corta y eficiente. Además, puede decodificar mensajes codificados previamente utilizando el mismo algoritmo.


## ¿Cómo funciona el algoritmo de compresion Huffman?

El algoritmo de compresión Huffman es un método que asigna códigos de longitud variable a cada carácter en un mensaje, basándose en su frecuencia de aparición. Los caracteres más comunes reciben códigos más cortos, mientras que los menos comunes reciben códigos más largos. Esto resulta en una representación más eficiente del mensaje, ya que se utilizan menos bits para los caracteres más frecuentes.


## Pre-requisitos

- Python 3.x instalado en tu sistema. 
- La biblioteca Kivy, esta se puede instalar ejecutando pip install kivy.

## ¿Cómo está hecho?

Este proyecto está implementado en Python y utiliza el framework Kivy para la interfaz de usuario. La arquitectura del proyecto está organizada de la siguiente manera:

- Carpeta 'sql': Contiene los archivos .sql donde se encuentra la instrucción sql para crear las tablas en NeonDB.
    - crear_historial.sql: Se encuentra la instrucción sql para crear las tabla de historial en NeonDB.
    - crear_usuarios.sql: Se encuentra la instrucción sql para crear las tabla de usuarios en NeonDB.

- Carpeta 'src': Contiene en controller, mmodel y los view tanto por consola como por el gui.
    - Carpeta 'controller': Contiene los controladores de las tablas de la base de datos.
    - Carpeta 'model': Contiene la lógica huffman, ademas de la creación de los objetos historial y usuario.
    - Carpeta 'view-console': Contiene la interfaz por consola conectada a la base de datos.
    - Carpeta 'view-gui': Contiene la interfaz gráfica.

- Carpeta 'tests': Contiene pruebas unitarias para la lógica de la aplicación.
    - test_huffman.py: Pruebas unitarias para las funciones de codificación y decodificación de Huffman.
    - testMVC.py: Pruebas unitarias para las funciones de las tablas en la base de datos.


## Uso

Para poder hacer uso de la base de datos debe conectarse a su NeonDB, incluyendo los datos de conexión en SecretConfig-sample.py y renombrando el archivo como SecretConfig.py.

Se deben ejecutar primero las pruebas unitarias para que se creen las tablas en la base de datos. 

- Uso del código fuente Huffman por consola: Para hacer uso de la aplicación por consola se debe correr el archivo console.py que se encuentra en la carpeta 'consoleHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-console\console.py

    - Recuerde que la base de datos unicamente esta conectada a la interfaz por consola. 

- Uso del Kivy: Para hacer uso de la aplicación con interfaz gráfica se debe correr el archivo interfaz.py que se encuentra en la carpeta 'interfazHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-gui\huffman_gui.py 
  
