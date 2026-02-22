#Importacion de future y typing 
    #Future para evitar errores de referencia hacia adelante al usar tipos en anotaciones, posponiendo su evaluación.
from __future__ import annotations
    #typing para usar tipos opcionales y listas en las anotaciones de tipo, mejorando la claridad del código y facilitando el análisis estático.
from typing import Optional, List

#Clases base para el AST (Abstract Syntax Tree)
class Node:
    def __init__(self, line: int = 0, column: int = 0):
        self.line = line
        self.column = column


class Expression(Node):
    """Fragmentos de codigo que 'valen algo'"""
    def __init__(self, line: int = 0, column: int = 0):
        super().__init__(line, column)


class Statement(Node):
    """Instrucciones que 'hacen algo'"""
    def __init__(self, line: int = 0, column: int = 0):
        super().__init__(line, column)


#Programa completo, raiz del AST (donde se guardan todas las sentencias)

class ProgramNode(Node):
    def __init__(self, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.sentences: List[Statement] = []

    def add_node(self, node: Statement):
        self.sentences.append(node)


# Tipos de nodos para expresiones y sentencias
    #Nodos literales para valores constantes (números, cadenas, etc.) 
class LiteralNode(Expression):
    def __init__(self, value, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.value = value

    #nodos numericos y de cadenas
class NumberLiteral(LiteralNode):
    def __init__(self, value, line: int = 0, column: int = 0):
        super().__init__(value, line, column)

    #nodos de cadenas tipo string, con comillas dobles o simples
class StringLiteral(LiteralNode):
    def __init__(self, value: str, line: int = 0, column: int = 0):
        super().__init__(value, line, column)


#clase para identificadores (variables, funciones, etc.) que se usan en expresiones y sentencias# 

class Identifier(Expression):
    def __init__(self, name: str, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.name = name


#Nodos para operadores unarios y binarios para expresiones aritméticas, lógicas, etc.

class UnaryOp(Expression):
    def __init__(self, op, expr: Expression, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.op = op
        self.expr = expr


class BinaryOp(Expression):
    def __init__(self, op, left: Expression, right: Expression, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.op = op
        self.left = left
        self.right = right


# Nodos para sentencias de declaración de variables, asignación, impresión, bloques, condicionales y bucles

class VarDecl(Statement):
    def __init__(self, var_type, name: str, init: Optional[Expression] = None,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.var_type = var_type
        self.name = name
        self.init = init


class Assign(Statement):
    def __init__(self, name: str, expr: Expression,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.name = name
        self.expr = expr


class PrintStmt(Statement):
    def __init__(self, expr: Expression,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.expr = expr


class BlockStmt(Statement):
    def __init__(self, statements: Optional[List[Statement]] = None,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.statements = statements if statements is not None else []


class IfStmt(Statement):
    def __init__(self, condition: Expression,
                 then_branch: Statement,
                 else_branch: Optional[Statement] = None,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class WhileStmt(Statement):
    def __init__(self, condition: Expression,
                 body: Statement,
                 line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.condition = condition
        self.body = body