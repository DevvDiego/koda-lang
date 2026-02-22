from __future__ import annotations
from dataclasses import dataclass, field    
from typing import Optional, TypeVar, Generic, List

# base para los nodos del AST (Abstract Syntax Tree)
@dataclass
class Node:
    line: int = 0
    column: int = 0

@dataclass
class Expression(Node): 
    """Fragmentos de codigo que "valen algo" (numeros, sumas, variables)"""
    pass


@dataclass
class Statement(Node):
    """Instrucciones que "hacen algo" (declarar, imprimir, repetir)."""
    pass

# Este archivo define los nodos del AST (Abstract Syntax Tree) que el parser va a construir.
@dataclass
class ProgramNode(Node):
    sentences: list[Statement] = field(default_factory=list)

    def add_node(self, node: Statement):
        self.sentences.append(node)
    
# Definimos una Tipo generico
T = TypeVar('T') # ignoren esta parte, es solo para type hints del IDE

@dataclass
class LiteralNode(Expression,Generic[T]):
    """Almacena valores literales, como cadenas o numeros"""
    value: T

@dataclass    
class Numberliteral(LiteralNode[int,float]):
    pass  

@dataclass
class StringLiteral(LiteralNode[str]):
    pass

@dataclass
class identifier(Expression):
    name: str = ""

@dataclass
class UnaryOp(Expression):
    op: object = None          # TokenType (PLUS/MULT/...)
    left: Expression = None
    right: Expression = None

@dataclass
class VarDecl(Statement):
    var_type: object = None    # TokenType.INT/FLOAT/...
    name: str = ""
    init: Optional[Expression] = None

@dataclass
class Assign(Statement):
    name: str = ""
    expr: Expression = None

@dataclass
class PrintStmt(Statement):
    expr: Expression = None

@dataclass
class BlockStmt(Statement):
    statements: List[Statement] = field(default_factory=list)

@dataclass
class IfStmt(Statement):
    condition: Expression = None
    then_branch: Statement = None
    else_branch: Optional[Statement] = None

@dataclass
class WhileStmt(Statement):
    condition: Expression = None
    body: Statement = None