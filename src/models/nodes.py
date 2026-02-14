from dataclasses import dataclass
from typing import TypeVar, Generic

@dataclass
class ProgramNode:
    """El contenedor raíz (la "caja" que guarda todo el archivo)"""

@dataclass
class Expression: 
    """Fragmentos de codigo que "valen algo" (numeros, sumas, variables)"""
    pass


@dataclass
class statement:
    """Instrucciones que "hacen algo" (declarar, imprimir, repetir)."""
    pass


# Definimos una Tipo generico
T = TypeVar('T') # ignoren esta parte, es solo para type hints del IDE

@dataclass
class LiteralNode(Generic[T]):
    value: T
