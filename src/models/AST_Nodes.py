class LiteralNode:
    def __init__(self, value):
        self.value = value #nodo que literalmente almacena "string" o numeros

class BinaryOpNode:
    def __init__(self, left, operand, right):
        self.left = left
        self.operand = operand
        self.right = right

class VarDeclarationNode:
    def __init__(self, type, name, expression):
        self.tipo = type
        self.nombre = name
        self.expression = expression # aqui deberian de ir una lista de nodos por ej.