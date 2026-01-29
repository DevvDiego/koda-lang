

class Splitter():
    """
    Splitter personalizado que nos permite mover posiciones y hacer peek al siguiente valor
    caracter por caracter

    """

    src: list[str]
    src_length: int
    current_position: int
    current_char: str

    def __init__(self, src:str) -> None:
        """
        Inicializa las variables para el splitter
        """
        self.src = [char for char in src] #split every character
        self.src_length = len(self.src)
        self.current_position = 0
        self.current_char = src[0]

    
    def next_char(self):
        """
        Mueve el puntero al siguiente caracter de src
        """
        if( self.current_position + 1 > self.src_length  ):
            print("Imposible avanzar al siguiente caracter, out of bounds")

        self.current_position = self.current_position + 1
        self.current_char = self.src[self.current_position]

    def peek_next(self):
        """
        Revisa el valor del siguiente caracter en src sin mover el puntero
        """
        if( self.current_position + 1 > self.src_length  ):
            print("Imposible avanzar al siguiente caracter, out of bounds")
        
        return self.src[self.current_position + 1]
    
    def return_current_char(self):
        return self.current_char


