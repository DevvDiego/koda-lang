### TODO 
Utiliza [x] para marcar una tarea completada y [] para una tarea NO completada.

- [x] Generar un splitting personalizado, para ir agrupando caracter por caracter de forma automatica y poder revisar si es un keyword o no.

- [x] Averiguar como hacer que los otros tipos de identifiacacion de token funcionen correctamente

- [x] Generar la tokenizacion final despues de los pasos del splitter.

- [x] Revisar alguna forma mas optima de identificar letras y caracteres especiales como * / - +, quiza usando regex?

- [x] Averiguar como hacer que el lexer identifique strings y no los clasifique como IDs

- [x] Averiguar como hacer que el lexer identifique cadenas como <"cadena con espacios"> porque las toma como diferentes

- [x] Potencial peligro de lentitud de compilacion, el programa tarda alrededor de 3 segundos en ejecutar el lexer, quiza es hora de optimizar?

- [x] Generar un archivo orquestrador que maneje logica de obtencion de archivos (y la interfaz probablemente) 



- [] Verificar con el equipo si entienden POO a algun nivel, para poder simplificar la logica dentro de una clase (Usando solo el concepo de encapsulamiento)

- [] Agregar todas las Palabras Reservadas dentro de la clase TokenType

- [] Verificar si el if deberia ser una cadena de if-elif para manejar tokens no reconocidos, o incluso usar un match.

- [] Averiguar porque al usar ; al final de un string """ """ no lo reconoce el lexer, ¿quiza hace un trim python naturalmente de los dos lados del string extendido? De todas formas no es un error, solo algo a tomar en cuenta en los ejemplos

- [] En la clase TokenType, quizas añadir una optimizacion seria lo justo? un map en vez del bucle para keyword_exists

- [] Dado caso que no encuentre el token doublequot de cierre que hariamos?

- [] Empezar con la parte de la interfaz usando Flask? o Tkinter? Hay que verlo por el lado en el que todos logren entender y aportar en cierta medida.

