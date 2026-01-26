from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    """
    Estrictamente define los tipos de token existentes
    """

    # Palabras reservadas
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    FUNCTION = "function"
    
    # Simbolos
    PLUS = "+"
    MINUS = "-"
    ASSIGN = "="
    LPAREN = "("
    RPAREN = ")"
    SEMICOLON = ";" 
    
    # Literales e identificadores
    ID = "ID"         # nombres de variables
    NUMBER = "NUMBER" # numero
    EOF = "EOF"       # Fin de archivo (usado en el Parser)



@dataclass # define la calse como solamente datos
class Token:
    type: TokenType
    value: str
    line: int
    column: int

    def __repr__(self):
        """Esto hace que al hacer print(token) se vea mas profesional en la consola"""
        return f"Tkn({self.type}, '{self.value}', l:{self.line}, c:{self.column})"