class IteradorLista:
    def __init__(self, nodo_actual, col):
        ''' Constructor de la clase IteradorLista la cual ayuda a realizar el
        Proceso de iteracion de una lista circular simple.

        Parametros:
        * nodo_actual: Es el primer nodo de lalista.
        * col: Es el ultimo nodo de la lista. '''

        self.nodo_actual = nodo_actual
        self.nodo_col = col
        self.ultimo = True

    def __next__(self):
        ''' Metodo oculto que esta realcionado directamente con el metodo
        __iter__, este metodo retorna cada valor de la lista cuando es llamado
        utilizado en un ciclo for.

        Retorno:
        * dato: es el dato del nodo actual en el que la secuencia de itecion
        se encuentra. '''
        if self.nodo_actual is not None:
            if self.ultimo:
                if self.nodo_actual is self.nodo_col:
                    self.ultimo = False
                dato = self.nodo_actual.dato
                self.nodo_actual = self.nodo_actual.sig
                return dato
            else:
                raise StopIteration
        else:
            raise StopIteration


class IteradorCola:
    def __init__(self, frente):
        self.actual = frente

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.sig
        return dato
