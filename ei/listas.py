from ei.nodos import NodoLSE
from ei.validación import validar_dato, validar_pos
from ei.iterador import IteradorLista

# Universidad de Nariño
# Ingenieria de Sistemas
# Estructuras de Información
#
# Juan Sebastian Rubio
# Carlos Andres Toro


# Clase para el manejo de listas circulares simples
class LCSE:
    # Inicializacion
    def __init__(self):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de inicializar la lista
        de nodos.

        Parámetros:
        Sin Parámetros

        Retornos:
        Sin retornos
        '''
        self.cab = None
        self.col = None

    # Validación
    def es_vacia(self):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de verificar si la lista
        contiene nodos o está vacía.

        Parámetros:
        Sin Parámetros

        Retornos:
        * True: Si la lista no contiene nodos.
        * False: Si la lista contiene nodos.
        '''
        if self.cab is not None:
            return True
        return False

    # Insertar
    def agregar(self, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de agregar un nuevo nodo
        dentro de la lista haciendo uso de un dato u objeto que entre como
        parámetro.

        Parámetros:
        * nuevo_dato: Es el dato que contendrá el nodo que se está creando.

        Retornos:
        * True: El método retornará True si el nodo pudo ser creado.
        * False: El método retornará False si el nodo no pudo ser creado.
        '''
        if validar_dato(self.cab, nuevo_dato):
            nuevo_nodo = NodoLSE(nuevo_dato)
            if self.es_vacia():
                self.col.sig = nuevo_nodo
                self.col = nuevo_nodo
                self.col.sig = self.cab
            else:
                self.cab = nuevo_nodo
                self.col = nuevo_nodo
                self.col.sig = self.cab
            return True
        return False

    def posicionar(self, pos_rel, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de agregar un nodo con
        el dato que llegue como parámetro en una posición relativa específica
        dentro de la lista. Esta posición se determinará recorriendo la lista
        en círculos hasta encontrar la posición.

        Parámetros:
        * pos_rel: Se lo toma como la posición relativa donde se desea agregar
        el nuevo nodo.
        * nuevo_dato: Es el dato que contendrá el nuevo nodo.

        Retornos:
        * True: El método retornará True si el nodo pudo ser agregado.
        * False: El método retornará False si el nodo no pudo ser agregado.
        '''
        if validar_dato(self.cab, nuevo_dato):
            if validar_pos(pos_rel):
                nuevo_nodo = NodoLSE(nuevo_dato)
                nodo_actual = self.cab
                nodo_anterior = None
                con = 0
                if self.es_vacia():
                    while con != pos_rel:
                        nodo_anterior = nodo_actual
                        nodo_actual = nodo_actual.sig
                        con += 1
                    # vlidar cuando es la posicion 0
                    if pos_rel != 0:
                        if nodo_actual is self.cab:
                            self.col.sig = nuevo_nodo
                            nuevo_nodo.sig = self.cab
                            self.col = nuevo_nodo
                            nuevo_nodo.sig = nodo_actual
                            nodo_anterior.sig = nuevo_nodo
                    else:
                        nuevo_nodo.sig = nodo_actual
                        self.cab = nuevo_nodo
                        self.col.sig = self.cab
                elif pos_rel == 0:
                    self.cab = nuevo_nodo
                    self.col = nuevo_nodo
                    self.col.sig = self.cab
                else:
                    return False
                return True
        return False

    # Eliminar
    def remover(self, item, por_pos=False, all=False):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de remover un nodo dentro
        de la lista sea uno o varios a la vez.

        Parámetros:
        * item: Este parámetro actúa de dos maneras bien sea actuando como dato
        para eliminar uno o todos los nodos que lo contengan, también eliminar
        un nodo siendo este su posición.
        * por_pos: Se lo inicializa por defecto en False. Si este se vuelve
        True, "item" sea comporta como posición.
        * all: Este parámetro actúa cuando por_pos es False. Se lo inicializa
        por defecto en False. Si este es false, item es un dato y borra un solo
        nodo que lo contenga. Si este es True, se eliminarán todos los nodos
        que tengan el dato item.

        Retornos:
        * True: El método retornará True si el nodo, o nodos, pudo ser removido
        * False: El método retornará False si el nodo, o nodos, no pudo ser
        removido.
        '''
        if self.es_vacia():  # validación cuando la lista esta vacia
            nodo_actual = self.cab
            nodo_anterior = None
            ban = False
            if por_pos:
                if validar_pos(item):
                    con = 0
                    while con != item:
                        nodo_anterior = nodo_actual
                        nodo_actual = nodo_actual.sig
                        con += 1
                    if nodo_actual is self.col:
                        nodo_anterior.sig = self.cab
                        self.col = nodo_anterior
                    elif nodo_actual is self.cab:
                        nodo_actual = nodo_actual.sig
                        self.cab = nodo_actual
                        self.col.sig = nodo_actual
                    else:
                        nodo_actual = nodo_actual.sig
                        nodo_anterior.sig = nodo_actual
                    return True
            elif all:
                while nodo_actual is not self.col:
                    if nodo_actual.dato == item:
                        if nodo_actual is self.cab:
                            nodo_actual = nodo_actual.sig
                            self.cab = nodo_actual
                            self.col.sig = nodo_actual
                        else:
                            nodo_actual = nodo_actual.sig
                            nodo_anterior.sig = nodo_actual
                        ban = True
                    else:
                        nodo_anterior = nodo_actual
                        nodo_actual = nodo_actual.sig
                if nodo_actual.dato == item:
                    nodo_anterior.sig = self.cab
                    self.col = nodo_anterior
                    ban = True
                return ban
            else:
                while nodo_actual is not self.col:
                    if nodo_actual.dato == item:
                        if nodo_actual is self.cab:
                            nodo_actual = nodo_actual.sig
                            self.cab = nodo_actual
                            self.col.sig = nodo_actual
                            return True
                        nodo_actual = nodo_actual.sig
                        nodo_anterior.sig = nodo_actual
                        return True
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.sig
                if nodo_actual.dato == item:
                    nodo_anterior.sig = self.cab
                    self.col = nodo_anterior
                    return True
                return False
        return False

    # buscar
    def encontrar(self, dato):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de encontrar un nodo
        dentro de la lista.

        Parámetros:
        * dato: Este parámetro es el dato que se utilizará para encontrar el
        nodo que lo contiene.

        Retornos:
        * nodo_actual: El método retornará el nodo que corresponda al dato
        buscado.
        * None: El método retornará None si el nodo no pudo ser encontrado o
        no existe.
        '''
        if self.es_vacia():
            nodo_actual = self.cab
            while nodo_actual != self.col:
                if nodo_actual.dato == dato:
                    return nodo_actual
                nodo_actual = nodo_actual.sig
            if nodo_actual.dato == dato:
                return nodo_actual
            else:
                return None
            return None
        else:
            return None

    def ruleta(self, pos_rel):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de encontrar un dato
        contenido en un nodo dentro de la lista.

        Parámetros:
        * pos_rel: Este parámetro es la posición relativa del nodo que contenga
        el dato.

        Retornos:
        * nodo_actual.dato: El método retornará el dato que corresponda al nodo
        buscado.
        * None: El método retornará None si el nodo no pudo ser encontrado o
        no existe.
        '''
        if self.es_vacia():
            if validar_pos(pos_rel):
                nodo_actual = self.cab
                con = 0
                while con != pos_rel:
                    nodo_actual = nodo_actual.sig
                    con += 1
                return nodo_actual.dato
        return None

    # Recorrer
    def recorrer(self, sep=""):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de recorrer e imprimir
        los datos que se encuentren en los nodos dentro la lista.

        Parámetros:
        * sep: Este parámetro es el separador para los datos, se inicializa por
        defecto como una cadena vacía("").

        Retornos:
        * cad: El método retornará la cadena con los datos en ella.
        * None: El método retornará None si la lista está vacía.
        '''
        if self.es_vacia():
            nodo_actual = self.cab
            cad = ''
            while nodo_actual is not self.col:
                cad += str(nodo_actual.dato) + sep
                nodo_actual = nodo_actual.sig
            cad += str(nodo_actual.dato) + sep
            return cad
        return None

    # Tamaño
    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de retornar la cantidad
        de nodos que se encuentren actualmente en la lista.

        Parámetros:
        Sin parámetros.

        Retornos:
        * con: El método retornará cont con la cantidad de nodos en la lista
        si la lista no está vacía.
        * 0: El método retornará 0 si la lista está vacía.
        '''
        if self.es_vacia():
            nodo_actual = self.cab
            con = 0
            while nodo_actual is not self.col:
                nodo_actual = nodo_actual.sig
                con += 1
            con += 1
            return con
        else:
            return 0

    def __iter__(self):
        ''' Documentación:
        Este método dentro de la clase LCSE se encarga de convertir a la lista
        en una lista iterable por un ciclo for.

        Parámetros:
        Sin parámetros.

        Retornos:
        * IteradorLista: Devuelve el iterador de la lista.
        '''
        return IteradorLista(self.cab, self.col)


# Clase para el manejo de las listas simplemente enlazadas
class LSE:
    def __init__(self, separador='\n'):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de inicializar la lista
        de nodos.

        Parámetros:
        * separador: Se lo toma como un separador en la impresión de los datos
        de los nodos de la lista en el método __str__ que por defecto se
        encuentra inicializado.

        Retornos:
        Sin retornos
        '''

        self.separador = separador
        self.cab = None

    def agregar(self, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de agregar un nuevo nodo
        dentro de la lista haciendo uso de un dato u objeto que entre como
        parámetro.

        Parámetros:
        * nuevo_dato: Es el dato que contendrá el nodo que se está creando.

        Retornos:
        * True: El método retornará True si el nodo pudo ser creado.
        * False: El método retornará False si el nodo no pudo ser creado.
        '''

        if validar_dato(self.cab, nuevo_dato):
            nuevo_nodo = NodoLSE(nuevo_dato)
            if self.cab is None:
                self.cab = nuevo_nodo
            else:
                aux = self.cab
                while aux.sig is not None:
                    aux = aux.sig
                aux.sig = nuevo_nodo
            return True
        return False

    def remover(self, item, por_pos=True):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de remover un nodo dentro
        de la lista sea uno o varios a la vez.

        Parámetros:
        * item: Este parámetro actúa de dos maneras bien sea actuando como dato
        para eliminar todos los nodos que lo contengan a eliminar un nodo
        siendo este su posición.
        * por_pos: Se lo inicializa por defecto en True haciendo que "item" sea
        una posición. Si se lo cambia a falso, "item" es el dato que se
        contiene en los nodos a eliminar.

        Retornos:
        * True: El método retornará True si el nodo, o nodos, pudo ser removido
        * False: El método retornará False si el nodo, o nodos, no pudo ser
        removido.
        '''

        if por_pos:
            nodo_anterior = None
            nodo_actual = self.cab
            cont = 0
            while cont != item:
                if nodo_actual is None:
                    break
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
                cont += 1
            if nodo_actual is not None:
                if item == 0:
                    self.cab = nodo_actual.sig
                else:
                    nodo_anterior.sig = nodo_actual.sig
            if item > cont:
                return False
        else:
            if validar_dato(self.cab, item):
                ban = False
                nodo_anterior = None
                nodo_actual = self.cab
                while nodo_actual is not None:
                    if nodo_actual.dato == item:
                        if nodo_anterior is None:
                            nodo_actual = nodo_actual.sig
                            self.cab = nodo_actual
                        else:
                            nodo_actual = nodo_actual.sig
                            nodo_anterior.sig = nodo_actual
                        ban = True
                    else:
                        nodo_anterior = nodo_actual
                        nodo_actual = nodo_actual.sig
                return ban
            else:
                return False

    def posicionar(self, pos, nuevo_dato):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de agregar un nodo con el
        dato que llegue como parámetro en una posición específica de la lista.

        Parámetros:
        * pos: Se lo toma como la posición donde se desea agregar el nuevo nodo
        * nuevo_dato: Es el dato que contendrá el nuevo nodo.

        Retornos:
        * True: El método retornará True si el nodo pudo ser agregado.
        * False: El método retornará False si el nodo no pudo ser agregado.
        '''

        if validar_dato(self.cab, nuevo_dato):
            nodo_anterior = None
            nodo_actual = self.cab
            nuevo_nodo = NodoLSE(nuevo_dato)
            cont = 0
            if pos != 0:
                while cont != pos:   # and nodo_actual is not None:
                    if nodo_actual is None:
                        break
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.sig
                    cont += 1
                if cont == pos:
                    nuevo_nodo.sig = nodo_actual
                    nodo_anterior.sig = nuevo_nodo
                    return True
                return False
            elif self.cab is None:
                self.cab = nuevo_nodo
            else:
                nuevo_nodo.sig = self.cab
                self.cab = nuevo_nodo
            return True
        else:
            return False

    def encontrar(self, dato_buscado):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de encontrar un nodo
        dentro de la lista.

        Parámetros:
        * dato_buscado: Este parámetro es el dato que se utilizará para
        encontrar el nodo que lo contiene.

        Retornos:
        * nodo_actual: El método retornará el nodo que corresponda al dato
        buscado.
        * None: El método retornará Nodo si el nodo no pudo ser encontrado o
        no existe.
        '''

        if validar_dato(self.cab, dato_buscado):
            nodo_actual = self.cab
            while nodo_actual is not None:
                if dato_buscado == nodo_actual.dato:
                    return nodo_actual
                nodo_actual = nodo_actual.sig
            return None
        else:
            return None

    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de retornar la cantidad
        de nodos que se encuentren actualmente en la lista.

        Parámetros:
        Sin parámetros.

        Retornos:
        * cont: El método retornará cont con la cantidad de nodos en la lista
        si la lista no está vacía.
        * 0: El método retornará 0 si la lista está vacía.
        '''

        if self.cab is not None:
            nodo_actual = self.cab
            cont = 0
            while nodo_actual is not None:
                nodo_actual = nodo_actual.sig
                cont += 1
            return cont
        else:
            return 0

    def __str__(self):
        ''' Documentación:
        Este método dentro de la clase LSE se encarga de retornar una cadena
        con todos los datos contenidos en los nodos uno detrás de otro o con
        un separador si en el constructor se envió uno.

        Parámetros:
        Sin parámetros

        Retornos:
        * cad: El método retornará la cadena "cad" con los datos dentro de los
        nodos de la lista.
        * : El método retornará un mensaje informando que no se encuentran
        datos en la lista si esta lista está vacía.
        '''

        nodo_actual = self.cab
        cad = ''
        if nodo_actual is not None:
            while nodo_actual is not None:
                cad += str(nodo_actual.dato) + self.separador
                nodo_actual = nodo_actual.sig
            return cad
        else:
            return None
