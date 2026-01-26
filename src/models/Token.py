from enum import Enum, auto
from dataclasses import dataclass

class TokenType(Enum):
    """
    Estrictamente define los tipos de token existentes
    """

    ## Usar auto asigna automaticamente un numero identificador a cada token construido

    # Palabras reservadas
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FUNCTION = auto()
    
    # Simbolos
    PLUS = auto()      # +
    MINUS = auto()     # -
    ASSIGN = auto()    # =
    LPAREN = auto()    # (
    RPAREN = auto()    # )
    SEMICOLON = auto() # ;
    
    # Literales e identificadores
    ID = auto()        # nombres de variables
    NUMBER = auto()    # numero
    EOF = auto()       # Fin de archivo (para el Parser)


@dataclass # define la calse como solamente datos
class Token:
    type: TokenType
    value: str
    line: int
    column: int

    def __repr__(self):
        """Esto hace que al hacer print(token) se vea mas profesional en la consola"""
        return f"Tkn({self.type}, '{self.value}', l:{self.line}, c:{self.column})"