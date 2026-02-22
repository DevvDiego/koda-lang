class Splitter():
    """
    Splitter personalizado que nos permite mover posiciones y hacer peek al siguiente valor
    caracter por caracter

    """

    src: list[str]
    src_length: int
    current_position: int
    current_column: int
    current_row: int
    current_char: str

    def __init__(self, src:str) -> None:
        """
        Inicializa las variables para el splitter
        """
        self.src = [char for char in src] #split every character
        self.src_length = len(self.src)
        self.current_position = 0
        self.current_column = 1
        self.current_row = 1
        self.current_char = src[0]

    
    def next_char(self):
        """
        Mueve el puntero al siguiente caracter de src
        """
        if( self.isOutOfBounds( self.current_position + 1 ) ):
            print("Imposible avanzar, out of bounds")
            return
        
        if(self.current_char == "\n"): #new line
            self.increaseRow()
            self.current_column = 0 # reset column

        self.increaseColumn()

        self.current_position = self.current_position + 1
        self.current_char = self.src[self.current_position]

    def peek_next(self):
        """
        Revisa el valor del siguiente caracter en src sin mover el puntero
        """
        if( self.isOutOfBounds(self.current_position+1) ):
            print("Imposible avanzar, out of bounds")
            return ""
        
        return self.src[self.current_position + 1]
    
    def return_current_char(self):
        return self.current_char
    
    def isOutOfBounds(self, idx:int):
        if idx < 0:
            return True

        if idx >= self.src_length:
            return True

        return False

    def increaseColumn(self):
        self.current_column = self.current_column + 1
    
    def increaseRow(self):
        self.current_row = self.current_row + 1