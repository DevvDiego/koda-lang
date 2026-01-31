from models.token import TokenType, Token
from tools.splitter import Splitter


def buildToken(line:int, col:int, value:list[str], type:TokenType = TokenType.ID) -> Token :
    """
    Builds a standarized token
    """

    # une todos los caracteres splitteados en una sola cadena
    joined_token_chars = "".join(value)    

    isKeyword = TokenType.keyword_exists(joined_token_chars)

    if(isKeyword):
        keyword = isKeyword
        type = keyword


    return Token(type, joined_token_chars, line, col);

# tomando de ejemplo la cadena "let x = 10 * 2 + 1"
    
#src =  "let x = 10*2+1;"\
#"print(\"something\");"\
#"print(x);"
#"if((2*2)=4){" \

#TODO averiguar porque al usar ; al final de un string "" no lo reconoce el lexer
src = "print(x);" #esta cadena no identifica el ; al final


src = """
let x = 10*2+1;
print(\"something\");
print(x);
"""


splitter = Splitter(src)

tokens = []


flag_stopLexer = False;
while flag_stopLexer == False:
    #deberia quiza agregar verificacion aqui o en el splitter para que el src no sea algo vacio???

    token = []

    #si es una letra
    if(splitter.current_char.isalpha()):
        #averiguar si el siguiente caracter es caracter y si si, seguir agregando como token
        while True:
            if( (splitter.peek_next().isalpha()) == False ):
                # añadir el caracter actual antes de salir
                token.append(splitter.current_char)

                #no tokentype pasado porque se espera que pueda ser algun keyword, sino sera ID
                tokens.append( buildToken(0,0,token) )

                break #terminar el while si el siguiente caracter no es letra
            
            token.append(splitter.current_char)
            splitter.next_char();




    #si es una operador (TODO Revisar alguna manera mejor de analizar esto)
    """ is_operator = splitter.current_char in ';"+-*/=(){}' #devuelve el caracter encontrado """
    possible_operator = TokenType.keyword_exists(splitter.current_char)

    if( possible_operator ):
        #resulto que si habia operador, lo asigno para mas legibilidad
        operator = possible_operator;

        #aqui no agrego while porque aun son operadores de un solo digito
        token.append(splitter.current_char)
        tokens.append( buildToken(0,0, token, operator) )




    #si es un numero
    if(splitter.current_char.isdigit()):
        #averiguar si el siguiente caracter es digito y si si, seguir agregando como token
        while True:
            if( (splitter.peek_next().isdigit()) == False ):
                # añadir el caracter actual antes de salir
                token.append(splitter.current_char)
                tokens.append( buildToken(0,0, token, TokenType.NUMBER) )
                break #terminar el while si el siguiente caracter no es letra
            
            token.append(splitter.current_char)
            splitter.next_char();




    #si es un espacio
    if(splitter.current_char.isspace()):
        pass
        # tomar en cuenta los espacios? yo creo no ya que tenemos el semicolon (;)
        # token.append(splitter.current_char)
        # igual aqui los espacios son solo un caracter
        #print(splitter.current_char, splitter.current_position)
    
    
    
    #TODO revisar si deberia hacer if y elif en lugar de simples ifs para poder manejar
    #el caso donde un caracer sea no reconocido
    
    #si es un caracter no reconocido
    #if(flag_isLetter or flag_isNum or flag_isOperator or flag_isSpace):
        #hacemos saber que tenemos un caracter no reconocido
    #    print(f"""
    #          [LEXER] Caracter no reconocido: 
    #          value:{splitter.current_char}, pos:{splitter.current_position}"""
    #        )
        


    # TODO identificar posible mejor forma de manejar los EOF
    if( (splitter.isInBounds( splitter.current_position + 1 )) ):
        flag_stopLexer = True
        continue


    splitter.next_char()


for token in tokens:
    print()
    print(token)