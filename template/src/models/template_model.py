class template_model:
    def __init__(self) -> None:
        pass

    def to_dict(self):
        '''Metodo que se encarga de convertir una clase a diccionario'''
        return self.__dict__