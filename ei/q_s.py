from ei.nodos import NodoLSE
from ei.validación import validar_dato
from ei.iterador import IteradorCola


class Stack:
    def __init__(self, sep=''):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de inicializar la pila.

        Parámetros:
        *sep: Separador que se utilizará para la presentación de los elementos
        contenidos en la pila una vez desapilados inicializado por defecto como
        una cadena vacía.

        Retornos:
        Sin Retornos
        '''
        self.la_cima = None
        self.sep = sep

    def es_vacio(self):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de verificar si la pila
        se encuentra vacía.

        Parámetros:
        Sin Parámetros

        Retornos:
        *True: Retorna este valor booleano si la pila se encuentra vacía.
        *False: Retorna este valor booleano si la pila no se encuentra vacía.
        '''
        if self.la_cima is not None:
            return True
        return False

    def apilar(self, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de apilar un nuevo
        elemento.

        Parámetros:
        *nuevo_dato: Dato que será apilado.

        Retornos:
        *True: Retorna este valor booleano si el dato pudo ser apilado.
        *False: Retorna este valor booleano si el dato no pudo ser apilado.
        '''
        if validar_dato(self.la_cima, nuevo_dato):
            nuevo_nodo = NodoLSE(nuevo_dato)
            if self.es_vacio():
                nuevo_nodo.sig = self.la_cima
                self.la_cima = nuevo_nodo
            else:
                self.la_cima = nuevo_nodo
            return True
        return False

    def desapilar(self):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de desapilar el dato
        que se encuentre en la cima de la pila.

        Parámetros:
        Sin Parámetros

        Retornos:
        *nodo_aux.dato: Retorna el dato que se encontraba en la cima de la pila
        y fue desapilado.
        *None: Retorna este valor si la pila se encontraba vacía.
        '''
        if self.es_vacio():
            nodo_aux = self.la_cima
            self.la_cima = self.la_cima.sig
            return nodo_aux.dato
        return None

    def cima(self):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de obtener el dato que
        contiene la cima de la pila.

        Parámetros:
        Sin Parámetros

        Retornos:
        *self.la_cima.dato: Retorna el dato que se encuentra en la cima de la
        pila.
        *None: Retorna este valor si la pila se encontraba vacía.
        '''
        if self.es_vacio():
            return self.la_cima.dato
        return None

    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase Stack se encarga de contar el número de
        elementos que contiene la pila.

        Parámetros:
        Sin Parámetros

        Retornos:
        *con: Retorna la cantidad de elementos encontrados en la pila.
        *0: Retorna este valor si la pila se encontraba vacía.
        '''
        if self.es_vacio():
            nodo_actual = self.la_cima
            con = 0
            while nodo_actual is not None:
                nodo_actual = nodo_actual.sig
                con += 1
            return con
        return 0

    def __str__(self):
        ''' Documentación:
        Este método dentro de la clase Stack se retornar una cadena
        con todos los datos contenidos en la pila uno detrás de otro o con
        un separador si en el constructor se envió uno.

        Parámetros:
        Sin Parámetros

        Retornos:
        *cad: Retorna la cadena con los datos de la pila y el separador si se
        tiene.
        *'': Retorna una cadena vacía si la pila se encontraba vacía.
        '''
        if self.es_vacio():
            nodo_actual = self.la_cima
            cad = ''
            while nodo_actual is not None:
                cad += str(nodo_actual.dato) + self.sep
                nodo_actual = nodo_actual.sig
            return cad[:len(cad)-len(self.sep)]
        return ''


class Queue:
    def __init__(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de inicializar la cola.

        Parámetros:
        Sin Parámetros

        Retornos:
        Sin Retornos
        '''
        self.el_frente = None
        self.cola = None

    def es_vacio(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de verificar si la cola
        se encuentra vacía.

        Parámetros:
        Sin Parámetros

        Retornos:
        *True: Retorna este valor booleano si la cola se encuentra vacía.
        *False: Retorna este valor booleano si la cola no se encuentra vacía.
        '''
        if self.el_frente is not None:
            return True
        return False

    def encolar(self, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de agregar un nuevo
        elemento a la cola.

        Parámetros:
        *nuevo_dato: Dato que va a ser agregado a la cola.

        Retornos:
        *True: Retorna este valor booleano si el dato pudo ser agregado.
        *False: Retorna este valor booleano si el dato no pudo ser agregado.
        '''
        if validar_dato(self.el_frente, nuevo_dato):
            nuevo_nodo = NodoLSE(nuevo_dato)
            if self.es_vacio():
                self.col.sig = nuevo_nodo
                self.col = nuevo_nodo
            else:
                self.el_frente = nuevo_nodo
                self.col = nuevo_nodo
            return True
        return False

    def desencolar(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de remover un elemento
        de la cola.

        Parámetros:
        Sin Parámetros

        Retornos:
        *nodo_aux.dato: Retorna el dato del elemento removido.
        *None: Retorna este valor si la cola se encontraba vacía.
        '''
        if self.es_vacio():
            nodo_aux = self.el_frente
            self.el_frente = self.el_frente.sig
            return nodo_aux.dato
        return None

    def frente(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de obtener el dato del
        elemento que se encuentre al frente de la cola.

        Parámetros:
        Sin Parámetros

        Retornos:
        *self.el_frente.dato: Retorna el dato del elemento al frente de la cola.
        *None: Retorna este valor si la cola se encontraba vacía.
        '''
        if self.es_vacio():
            return self.el_frente.dato
        return None

    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de obtener número de
        elementos que se encuentran en la cola.

        Parámetros:
        Sin Parámetros

        Retornos:
        *con: Retorna el número de elementos de la cola.
        *0: Retorna este valor si la cola se encontraba vacía.
        '''
        if self.es_vacio():
            nodo_actual = self.el_frente
            con = 0
            while nodo_actual is not None:
                nodo_actual = nodo_actual.sig
                con += 1
            return con
        return 0

    def __iter__(self):
        ''' Documentación:
        Este método dentro de la clase Queue se encarga de hacer que la cola
        sea iterable a través de un ciclo for.

        Parámetros:
        Sin Parámetros

        Retornos:
        *IteradorCola: Retorna el iterador de la cola.
        '''
        return IteradorCola(self.el_frente)
