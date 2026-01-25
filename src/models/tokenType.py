from enum import Enum, auto

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
    
    # Literales e Identificadores
    ID = auto()        # nombres de variables
    NUMBER = auto()    # numero
    EOF = auto()       # Fin de archivo (para el Parser)