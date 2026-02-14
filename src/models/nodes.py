from dataclasses import dataclass
from typing import TypeVar, Generic

class ProgramNode:
    """El contenedor raíz (la "caja" que guarda todos los stmts)"""
    def __init__(self):
        # Una lista donde guardaremos cada Statement (sentencia) 
        # que el parser encuentre.
        self.sentencias = []

    def add_node(self, node):
        self.sentencias.append(node)

    def __repr__(self):
        return f"ProgramNode(sentencias={self.sentencias})"
    

@dataclass
class Expression: 
    """Fragmentos de codigo que "valen algo" (numeros, sumas, variables)"""
    pass


@dataclass
class Statement:
    """Instrucciones que "hacen algo" (declarar, imprimir, repetir)."""
    pass


# Definimos una Tipo generico
T = TypeVar('T') # ignoren esta parte, es solo para type hints del IDE
@dataclass
class LiteralNode(Generic[T]):
    """Almacena valores literales, como cadenas o numeros"""
    value: T
