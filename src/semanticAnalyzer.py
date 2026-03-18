from src.models.nodes import (
    BlockStmt, BoolLiteral, IfStmt, ProgramNode, VarDecl, Assign, PrintStmt,
    Identifier, NumberLiteral, StringLiteral,
    UnaryOp, BinaryOp, WhileStmt
)
from src.symbolTable import SymbolTable
from src.models.token import TokenType

class Visitor:
    """Clase base para que todos los analizadores sigan la misma estructura."""
    def generic_visit(self, node):
        raise Exception(f"No se definio visit_{type(node).__name__}")


class SemanticAnalyzer(Visitor):
    def __init__(self):
        self.table = SymbolTable()

    def visit_ProgramNode(self, node: ProgramNode):
        for sentence in node.sentences:
            sentence.accept(self)
        print("--- Analisis semantico finalizado con exito ---")

    def visit_VarDecl(self, node: VarDecl):
        # 1. Verificar si la variable ya fue declarada
        if self.table.exists(node.name):
            raise Exception(f"Error Semantico: La variable '{node.name}' ya existe.")

        # 2. Si tiene un valor inicial, verificar que el tipo coincida
        if node.init:
            # RECURSION: Obtenemos el tipo del valor que se le quiere asignar
            actual_type = node.init.accept(self) 
            
            if actual_type != node.var_type:
                raise Exception(f"Error de Tipo: No puedes asignar {actual_type} a {node.var_type} ('{node.name}')")

        # 3. Guardar en la tabla de símbolos
        self.table.define(node.name, node.var_type)
    
    def visit_PrintStmt(self, node: PrintStmt):
        # Solo necesitamos ejecutar el análisis de la expresión
        # Si la expresión es 'x + 5', el accept(self) se encargará de:
        #   - Buscar 'x' en la tabla de símbolos (visit_Identifier)
        #   - Verificar que 'x' y '5' sean compatibles (visit_BinaryOp)
        #   - Devolver el tipo final.
        
        if node.expr:
            tipo_resultante = node.expr.accept(self)
            
            # Opcional: lenguaje prohíbe imprimir algo? 
            # Por ejemplo, si no permite funciones:
            # if tipo_resultante == TokenType.FUNCTION:
            #     raise Exception("No se pueden imprimir objetos de tipo funcion")
            
            return tipo_resultante

    def visit_IfStmt(self, node: IfStmt):
        # 1. Analizar la condición
        # No importa si es 'x > 5' o 'true', accept(self) nos dará el tipo resultante
        condition_type = node.condition.accept(self)

        # 2. Validar que la condición sea booleana
        # (Si tu lenguaje no tiene TokenType.BOOL, podrías usar INT y validar que sea 0 o 1)
        if condition_type != TokenType.BOOL:
            raise Exception(
                f"Línea {node.line}: La condición del 'if' debe ser BOOL, "
                f"pero se encontro {condition_type.name}"
            )

        # 3. Analizar el bloque 'then' (siempre existe)
        # Si tu bloque es un BlockStmt, este ya debería llamar a push_scope() y pop_scope()
        # node.then_branch.accept(self) 
        ### Dejar esta parte? revisar las Palabras reservadas

        # 4. Analizar el bloque 'else' (es opcional)
        if node.else_branch:
            node.else_branch.accept(self)        

    def visit_Assign(self, node: Assign):
        # 1. Verificar si la variable existe
        var_type = self.table.lookup(node.name)
        if not var_type:
            raise Exception(f"Error: La variable '{node.name}' no ha sido declarada.")

        # 2. Verificar que el nuevo valor sea del tipo correcto
        new_value_type = node.expr.accept(self)
        if new_value_type != var_type:
            raise Exception(f"Error: No puedes asignar {new_value_type} a la variable '{node.name}' que es {var_type}")

    def visit_NumberLiteral(self, node: NumberLiteral):
        # Aquí es donde vinculamos el valor real con el Enum
        if isinstance(node.value, float):
            return TokenType.FLOAT
        return TokenType.INT

    def visit_StringLiteral(self, node: StringLiteral):
        return TokenType.STRING
        
    def visit_BoolLiteral(self, node: BoolLiteral):
        return TokenType.BOOL

    def visit_Identifier(self, node: Identifier):
        # Si usamos una variable en una expresión, devolvemos su tipo guardado
        tipo = self.table.lookup(node.name)
        if not tipo:
            raise Exception(f"Error: Uso de variable no definida '{node.name}'")
        return tipo