# koda-lang


### Instalacion
El proyecto necesita python 3.7+
Actualmente no se tiene ninguna libreria de dependencia.

### Pruebas simples
Para ejecutar el proyecto yo recomiendo trabajar parte por parte. Es decir, ejecutar solo el lexer, parser y similares dentro del archivo main.py.

Ejemplo para ejecutar solo el Lexer
```python
#El resto de codigo de main.py...
src = "let x=10;"
tokens = Lexer(src=src)

for token in tokens:
    print(f"tipo: {token.type}, valor: {token.value} ")
```

Para ejecutar el proyecto
```bash
#Y dentro de src ejecuto directamente el lexer
python3 ./main.py

```