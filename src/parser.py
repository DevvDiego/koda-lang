from src.models.token import TokenType, Token

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    # --- NAVEGACION ---
    def peek(self, offset=0):
        # Mirar hacia adelante sin avanzar
        if self.pos + offset >= len(self.tokens):
            return self.tokens[-1] # Devolver el ultimo caracter (EOF)
        
        return self.tokens[self.pos + offset]

    def advance(self):
        # Consumir y devolver
        token = self.peek()
        self.pos += 1
        return token

    def eat(self, expected_type):
        # Validar y avanzar
        next_token = self.peek().type
        if next_token == expected_type:
            return self.advance()

        ## TODO: agregar linea aqui {self.peek().line}
        raise SyntaxError(f"Error en linea ###: Se esperaba {expected_type}")
    # --- ------- ---
    
    # --- SECCION: CONSTRUCCION DEL AST ---
    def parse_statement(self):
        # que colocamos aqui??
        pass
        