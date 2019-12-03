
def validar_dato(cab, dato):
    ''' Metodo que se encarga de hacer la validacion de homogeneidad de typo
    de dato. Recibe el primer nodo y el dato a comparar, donde el tipo del
    dato debe ser igual al del primer ingresao en la lista

    Parametros:
    * cab: direccion del primer nodo ingresado en la lista.
    * dato: el dato a validar con respecto al typo del primero ingesado.

    Retorno:
    * True: si el tipo de dato del primer dato (cab) es igual al del dato ó
    si la cabecera apunta a None.
    * False: Cuando El tipo de dato es diferente al del primero de la lista
    (cab) '''

    if cab is not None:
        if type(cab.dato) == type(dato):
            return True
        return False
    return True


def validar_pos(pos):
    ''' Metodo que permite validar si la posición relativa es un numero entero
    y ademas sea mayor o igual que 0.

    Parametros:
    * Pos: Es la posicion que se decea validar.

    Retorno:
    * True: Si la posicion es tipo entero y ademas sea positiva.
    * False: Cuando el tipo de dato de la posicion no sea entero o negativa.'''

    if type(pos) == int:
        if pos >= 0:
            return True
    return False
