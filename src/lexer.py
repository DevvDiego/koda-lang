from src.models.token import TokenType, Token
from src.tools.splitter import Splitter


def buildToken(row:int, col:int, value:list[str], type:TokenType = TokenType.ID) -> Token :
    """
    Builds a standarized token
    """

    # une todos los caracteres splitteados en una sola cadena
    joined_token_chars = "".join(value)    

    isKeyword = TokenType.keyword_exists(joined_token_chars)

    if(isKeyword):
        keyword = isKeyword
        type = keyword


    return Token(type, joined_token_chars, row, col);

# EJEMPLOS USANDO NUESTRO ALFABETO

#src = """
#int x = 10*2+1;
#print(\"something\");
#print(x);
#if((2*2)=4){
#    print("ejemplo largoooote")
#}
#"""

#ejemplo super simple
#src = "int x =10+2" #notese como llegan a faltar espacios


#ejemplo mas simple 
# (NOTA: use \ para "escapar" el caracter de comilla y que 
# el interpete de python no lo use, sino nosotros)
#src = """
#int x = 10*2+1;
#print(\"something asd\");
#print(x);
#"""





tokens = []



def Lexer(src: str):
    splitter = Splitter(src)

    while not splitter.isOutOfBounds(splitter.current_position + 1):
        #deberia quiza agregar verificacion aqui o en el splitter para que el src no sea algo vacio???

        token = []
        current_char = splitter.current_char

        match current_char:

            #si es una letra
            case char if char.isalpha():
                #averiguar si el siguiente caracter es caracter y si si, seguir agregando como token
                while True:
                    if( (splitter.peek_next().isalpha()) == False ):
                        # añadir el caracter actual antes de salir
                        token.append(splitter.current_char)

                        #no tokentype pasado porque se espera que pueda ser algun keyword, sino sera ID
                        tokens.append(buildToken(
                            col=splitter.current_column,
                            row=splitter.current_row,
                            value=token 
                        ))

                        break #terminar el while si el siguiente caracter no es letra
                    
                    token.append(splitter.current_char)
                    splitter.next_char();
            
            #si es un numero
            case char if char.isdigit():
                #averiguar si el siguiente caracter es digito y si si, seguir agregando como token
                while True:
                    if not splitter.peek_next().isdigit():
                        # añadir el caracter actual antes de salir
                        token.append(current_char)
                        tokens.append(buildToken(
                            row=splitter.current_row,
                            col=splitter.current_column,  
                            value=token,
                            type=TokenType.NUMBER
                        ))
                        break #terminar el while si el siguiente caracter no es letra
                    
                    token.append(splitter.current_char)
                    splitter.next_char();
                    current_char = splitter.current_char

            case char if char.isspace():
                #si es un espacio
                pass

            case '"': # Comilla doble
                splitter.next_char(); #salta el caracter DQ
                while True:
                    
                    #Aqui pudiera haber otro raise Error si no queremos que haya algun otro " en medio
                    #si el caracter actual no es otro DQ
                    #if( (splitter.current_char == "\"") == False ):
                        #pass

                    #Se encuentra el DQ de cierre 
                    if( splitter.current_char == "\"" ):
                        #saltamos el DQ de cierre y no lo almacenamos
                        #token.append(splitter.current_char)

                        #se añade el token a los tokens como un STRING
                        tokens.append(buildToken(
                            row=splitter.current_row,
                            col=splitter.current_column,  
                            value=token,
                            type=TokenType.STRING_LITERAL
                        ))

                        break #termina el while
                        #TODO dado caso que no encuentre el token de cierre que hariamos?
                    

                    token.append(splitter.current_char)
                    splitter.next_char();

            case _: # Operadores o cualquier otro caracter
                #si es una operador
                possible_operator = TokenType.keyword_exists(current_char)

                if( possible_operator ):
                    #resulto que si era operador
                    token.append(splitter.current_char)
                    tokens.append(buildToken(
                        row=splitter.current_row,
                        col=splitter.current_column,  
                        value=token,
                        type=possible_operator
                    ))
                else: # Caracteres no reconocidos
                    #TODO Asegurarse que el parsing se detenga en estos casos
                    # quiza usar directamente un raise sea lo correcto?
                    print(
                        "[LEXER] Caracter no reconocido: " \
                        f"value: {current_char}, " \
                        f"row: {splitter.current_row} col: {splitter.current_column}\n"
                    )
                

        splitter.next_char()




    #agregar token EOF (end of file)
    tokens.append(buildToken(
        row=splitter.current_row + 1,
        col=splitter.current_column,  
        value=["EOF"],
        type=TokenType.EOF
    ))

    return tokens