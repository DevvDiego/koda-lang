from models.Token import TokenType, Token


def buildToken(type:TokenType, value:str, line:int, col:int) -> Token :
    """
    Builds a standarized token
    """

    return Token(type, value, line, col);

# tomando de ejemplo la cadena "let x = 10 * 2 + 1"
src = "let x = 10 * 2 + 1 \n" \
"if 2 * 2 = 4"

splitted_chars = src.split() # src.split() # returns ['let', 'x', '=', '10', '*', '2', '+', '1']

tokens = []



while len(splitted_chars) > 0:
    isCurrentNum = False
    currentChar = splitted_chars.pop(0)

    isKeyword = TokenType.keyword_exists(currentChar)

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
    )
    
    


for token in tokens:
    print(token);