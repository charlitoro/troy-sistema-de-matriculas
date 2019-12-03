class NodoLSE:
    def __init__(self, dato):
        ''' Documentación:
        Este método dentro de la clase NodoLSE se encarga de crear un nuevo nodo
        con un dato que se le proporcione.

        Parámetros:
        * dato: Es el dato u objeto que contendrá el nodo.

        Retornos:
        Sin retorno
        '''
        self.dato = dato
        self.sig = None
