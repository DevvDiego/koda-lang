from src import Lexer

# Este archivo es el orquestrador, 
# el punto de entrada para el compilador en general

print("Koda compiler: Loading file \"main.kd\" \n\n")

src = ""


try:
    with open("main.kd") as f:
        src = f.read()

except:
    #cualquier error
    print("Ocurrio un error al tratar de leer el archivo fuente")
    print("se usara el src: 'int x = 10;'\n\n")
    src = "int x = 10;"

#a partir de aqui en teoria ya deberiamos tener el archivo en la variable src

tokens = Lexer(src=src)

for token in tokens:
    print(f"tipo: {token.type}, valor: {token.value} ")