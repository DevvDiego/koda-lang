from models.token import TokenType, Token
from tools.splitter import Splitter


def buildToken(type:TokenType, value:str, line:int, col:int) -> Token :
    """
    Builds a standarized token
    """

    return Token(type, value, line, col);

# tomando de ejemplo la cadena "let x = 10 * 2 + 1"
    
#src =  "let x = 10*2+1;"\
#"print(\"something\");"\
#"print(x);"
#"if((2*2)=4){" \

src = """
let x = 10*2+1;
print(\"something\");
print(x);
"""


splitter = Splitter(src)

tokens = []


#flags del caracter actual
flag_isLetter = False;
flag_isOperator = False;
flag_isNum = False;
flag_isSpace = False;

#flag del caracter proximo (obtenido usando peek)
flag_isNextLetter = False;
flag_isNextOperator = False;
flag_isNextNum = False;
flag_isNextSpace = False

flag_stopLexer = False;

#funciones utilitarias para modificar los flags de forma consistente
#quiza cambiar el nombre a flagLetter y similares para mejor entendimiento?
def foundLetter():
    """Sets the letter flag and unsets every other flag"""
    flag_isLetter = True;
    flag_isOperator = False
    flag_isNum = False;
    flag_isSpace = False

def foundOperator():
    """Sets the operator flag and unsets every other flag"""
    flag_isLetter = False;
    flag_isOperator = True
    flag_isNum = False;
    flag_isSpace = False

def foundNum():
    """Sets the num flag and unsets every other flag"""
    flag_isLetter = False;
    flag_isOperator = False
    flag_isNum = True;
    flag_isSpace = False

def foundSpace():
    """Sets the space flag and unsets every other flag"""
    flag_isLetter = False;
    flag_isOperator = False
    flag_isNum = False;
    flag_isSpace = True


while flag_stopLexer == False:
    #deberia quiza agregar verificacion aqui o en el splitter para que el src no sea algo vacio???

    token = []

    #si es una letra
    if(splitter.current_char.isalpha()):
        foundLetter()
        #averiguar si el siguiente caracter es caracter y si si, seguir agregando como token
        while True:
            if( (splitter.peek_next().isalpha()) == False ):
                # añadir el caracter actual antes de salir
                token.append(splitter.current_char) 
                break #terminar el while si el siguiente caracter no es letra
            
            token.append(splitter.current_char)
            splitter.next_char();



    #si es una operador (TODO Revisar alguna manera mejor de analizar esto)
    if( splitter.current_char in [';', '"','+', '-', '*', '/', '=', '(', ')' '{', '}'] ):
        foundOperator()
        #aqui no agrego while porque aun son operadores de un solo digito
        token.append(splitter.current_char)




    #si es un numero
    if(splitter.current_char.isdigit()):
        foundNum()
        #averiguar si el siguiente caracter es digito y si si, seguir agregando como token
        while True:
            if( (splitter.peek_next().isdigit()) == False ):
                # añadir el caracter actual antes de salir
                token.append(splitter.current_char) 
                break #terminar el while si el siguiente caracter no es letra
            
            token.append(splitter.current_char)
            splitter.next_char();




    #si es un espacio
    if(splitter.current_char.isspace()):
        foundSpace()
        # tomar en cuenta los espacios? yo creo no
        #token.append(splitter.current_char)
        # igual aqui los espacios son solo un caracter
        #print(splitter.current_char, splitter.current_position)




    # TODO identificar posible mejor forma de manejar los EOF
    if( (splitter.isInBounds( splitter.current_position + 1 )) ):
        flag_stopLexer = True
        continue

    
    tokens.append(token)
    splitter.next_char()


"""     isKeyword = TokenType.keyword_exists(splitter.current_char)

    if isKeyword:
        keyword = isKeyword
        tokens.append(
            buildToken(keyword, currentChar, 0, 0)
        )
        continue
    
    # Si no es reservado, aplicamos logica basica para dinamicos
    if currentChar.isdigit():
        tokens.append(
            buildToken(TokenType.NUMBER, currentChar, 0, 0)
        )

        continue

    # Si nada de lo anterior pasa, por defecto, asumimos que es un identificador (ID)
    tokens.append(
        buildToken(TokenType.ID, currentChar, 0, 0)
    ) """
    
    


for token in tokens:
    print(token);