import datetime
import sqlite3
from gi.repository import Gtk, Gdk
from ei.listas import LSE


class Usuario:
    '''Clase que modela los métodos y atributos que tendrá un usuario del
    sistema.
    '''
    def __init__(self, identificacion='', nombre='', direccion='',
                 telefono='', email='', contraseña='123', estado=True):
        '''Método de la clase Usuario que se encarga de inicializar un nuevo
        usuario.
        Parámetros:
        *identificacion: Identificación del usuario.
        *nombre: Nombre del usuario, por defecto vacío.
        *direccion: Dirección del usuario, por defecto vacío.
        *telefono: Teléfono del usuario, por defecto vacío.
        *email: E-mail del usuario, por defecto vacío.
        *contraseña: Contraseña del usuario, por defecto 123.
        *estado: Estado del usuario, por defecto True.
        '''
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__contraseña = contraseña
        self.__estado = estado

    def get_identificacion(self):
        '''Método de la clase Usuario que devuelve la identificación del
        usuario.
        Retornos:
        *self.__identificacion: identificación del usuario.
        '''
        return self.__identificacion

    def get_nombre(self):
        '''Método de la clase Usuario que devuelve el nombre del usuario.
        Retornos:
        *self.__nombre: Nombre del usuario.
        '''
        return self.__nombre

    def get_direccion(self):
        '''Método de la clase Usuario que devuelve la dirección del usuario.
        Retornos:
        *self.__direccion: Dirección del usuario.
        '''
        return self.__direccion

    def get_telefono(self):
        '''Método de la clase Usuario que devuelve el teléfono del usuario.
        Retornos:
        *self.__telefono: Teléfono del usuario.
        '''
        return self.__telefono

    def get_email(self):
        '''Método de la clase Usuario que devuelve el e-mail del usuario.
        Retornos:
        *self.__email: E-mail del usuario.
        '''
        return self.__email

    def get_contraseña(self):
        '''Método de la clase Usuario que devuelve la contraseña del usuario.
        Retornos:
        *self.__contraseña: Contraseña del usuario.
        '''
        return self.__contraseña

    def get_estado(self):
        '''Método de la clase Usuario que devuelve el estado del usuario.
        Retornos:
        *self.__estado: Estado del usuario.
        '''
        return self.__estado

    def set_identificacion(self, la_id):
        '''Método de la clase Usuario que asigna la identificación del usuario.
        Parámetros:
        *la_id: Identificación del usuario.
        '''
        self.__identificacion = la_id

    def set_nombre(self, el_nombre):
        '''Método de la clase Usuario que asigna el nombre del usuario.
        Parámetros:
        *el_nombre: Nombre del usuario.
        '''
        self.__nombre = el_nombre

    def set_direccion(self, la_dire):
        '''Método de la clase Usuario que asigna la dirección del usuario.
        Parámetros:
        *la_dire: Dirección del usuario.
        '''
        self.__direccion = la_dire

    def set_telefono(self, el_telefono):
        '''Método de la clase Usuario que asigna el teléfono del usuario.
        Parámetros:
        *el_telefono: Teléfono del usuario.
        '''
        self.__telefono = el_telefono

    def set_email(self, el_email):
        '''Método de la clase Usuario que asigna el e-mail del usuario.
        Parámetros:
        *el_email: E-mail del usuario.
        '''
        self.__email = el_email

    def set_contraseña(self, la_contraseña):
        '''Método de la clase Usuario que asigna la contraseña del usuario.
        Parámetros:
        *la_contraseña: Contraseña del usuario.
        '''
        self.__email = la_contraseña

    def set_estado(self, el_estado):
        '''Método de la clase Usuario que asigna el estado del usuario.
        Parámetros:
        *el_estado: Estado del usuario.
        '''
        self.__estado = el_estado


class Materia:
    '''Clase que modela los métodos y atributos que tendrá un usuario del
    sistema.
    '''
    def __init__(self, el_codigo, el_nombre='', los_creditos=0, el_semestre=0,
                 el_programa=''):
        '''Método de la clase Materia que se encarga de inicializar una nueva
        materia.
        Parámetros:
        *el_codigo: Código de la materia.
        *el_nombre: Nombre de la materia, por defecto vacío.
        *los_creditos: Créditos de la materia, por defecto 0.
        *el_semestre: Semestre de la materia, por defecto 0.
        *el_programa: Programa de la materia, por defecto vacío.
        '''
        self.__codigo_mat = el_codigo
        self.__nombre_mat = el_nombre
        self.__creditos = los_creditos
        self.__semestre = el_semestre
        self.__programa = el_programa

    def get_codigo_mat(self):
        '''Método de la clase Materia que devuelve el código de la materia.
        Retornos:
        *self.__codigo_mat: Código de la materia.
        '''
        return self.__codigo_mat

    def get_nombre_mat(self):
        '''Método de la clase Materia que devuelve el nombre de la materia.
        Retornos:
        *self.__nombre_mat: Nombre de la materia.
        '''
        return self.__nombre_mat

    def get_creditos(self):
        '''Método de la clase Materia que devuelve los créditos de la materia.
        Retornos:
        *self.__creditos: Créditos de la materia.
        '''
        return self.__creditos

    def get_semestre_mat(self):
        '''Método de la clase Materia que devuelve el semestre de la materia.
        Retornos:
        *self.__semestre: Semestre de la materia.
        '''
        return self.__semestre

    def get_programa_mat(self):
        '''Método de la clase Materia que devuelve el programa de la materia.
        Retornos:
        *self.__programa: Programa de la materia.
        '''
        return self.__programa


class Programa:
    '''Clase que modela los métodos y atributos que tendrá un programa en el
    sistema.
    '''
    def __init__(self, el_codigo_pro='', el_nombre_pro='', la_facultad=''):
        '''Método de la clase Programa que se encarga de inicializar un nuevo
        programa.
        Parámetros:
        *el_codigo_pro: Código del programa, por defecto vacío.
        *el_nombre_pro: Nombre del programa, por defecto vacío.
        *la_facultad: Facultad del programa, por defecto vacío.
        '''
        self.__codigo_pro = el_codigo_pro
        self.__nombre_pro = el_nombre_pro
        self.__facultad = la_facultad
        self.__materias = LSE()
        self.__docentes = LSE()
        self.__estudiantes = LSE()

    # Métodos get
    def get_codigo_pro(self):
        '''Método de la clase Programa que devuelve el código del programa.
        Retornos:
        *self.__codigo_pro: Código del programa.
        '''
        return self.__codigo_pro

    def get_nombre_pro(self):
        '''Método de la clase Programa que devuelve el nombre del programa.
        Retornos:
        *self.__nombre_pro: Nombre del programa.
        '''
        return self.__nombre_pro

    def get_facultad(self):
        '''Método de la clase Programa que devuelve la facultad del programa.
        Retornos:
        *self.__facultad: Facultad del programa.
        '''
        return self.__facultad

    # Métodos set
    def set_codigo_pro(self, el_codigo_pro):
        '''Método de la clase Programa que asigna el código del programa.
        Parámetros:
        *el_codigo_pro: Código del programa.
        '''
        self.__codigo_pro = el_codigo_pro

    def set_nombre_pro(self, el_nombre_pro):
        '''Método de la clase Programa que asigna el nombre del programa.
        Parámetros:
        *el_nombre_pro: Nombre del programa.
        '''
        self.__nombre_pro = el_nombre_pro

    def set_facultad(self, la_facultad):
        '''Método de la clase Programa que asigna la facultad del programa.
        Parámetros:
        *la_facultad: Facultad del programa.
        '''
        self.__facultad = la_facultad


class Facultad:
    '''Clase que modela los métodos y atributos que tendrá una facultad en el
    sistema.
    '''
    def __init__(self, el_codigo_fac='', el_nombre_fac='',
                 el_administrador=None):
        '''Método de la clase Facultad que se encarga de inicializar una nueva
        facultad.
        Parámetros:
        *codigo_fac: Código de la facultad, por defecto vacío.
        *nombre_fac: Nombre de la facultad, por defecto vacío.
        *el_administrador: Administrador de la facultad, por defecto None.
        '''
        self.__codigo_fac = el_codigo_fac
        self.__nombre_fac = el_nombre_fac
        self.__administrador = el_administrador
        self.__programas = LSE()

    # Métodos get
    def get__codigo_fac(self):
        '''Método de la clase Facultad que devuelve el código de la facultad.
        Retornos:
        *self.__codigo_fac: Código de la facultad.
        '''
        return self.__codigo_fac

    def get_nombre_fac(self):
        '''Método de la clase Facultad que devuelve el nombre de la facultad.
        Retornos:
        *self.__nombre_fac: Nombre de la facultad.
        '''
        return self.__nombre_fac

    def get_administrador(self):
        '''Método de la clase Facultad que devuelve el administrador de la
        facultad.
        Retornos:
        *self.__administrador: Administrador de la facultad.
        '''
        return self.__administrador

    # Metods set
    def set_codigo_fac(self, el_codigo_fac):
        '''Método de la clase Facultad que asigna el código de la facultad.
        Parámetros:
        *el_codigo_fac: Código de la facultad.
        '''
        self.__codigo_fac = el_codigo_fac

    def set_nombre_fac(self, el_nombre_fac):
        '''Método de la clase Facultad que asigna el nombre de la facultad.
        Parámetros:
        *el_nombre_fac: Nombre de la facultad.
        '''
        self.__nombre_fac = el_nombre_fac

    def set_administrador(self, el_administrador):
        '''Método de la clase Facultad que asigna al administrador de la
        facultad.
        Parámetros:
        *el_administrador: Administrador de la facultad.
        '''
        self.__administrador = el_administrador


class Estudiante(Usuario):
    '''Clase que modela los métodos y atributos que tendrá un estudiante en el
    sistema.
    '''
    def __init__(self, el_codigo='', la_identificacion='', el_nombre='',
                 la_direccion='', el_telefono='', el_email='', el_semestre=0,
                 la_contraseña='123', el_programa=None, el_estado=True, el_num_cance=4):
        '''Método de la clase Estudiante que se encarga de inicializar un nuevo
        estudiante.
        Parámetros:
        *el_codigo: Código del estudiante, por defecto vacío.
        *la_identificacion: Identificación del estudiante, por defecto vacío.
        *el_nombre: Nombre del estudiante, por defecto vacío.
        *la_direccion: Dirección del estudiante, por defecto vacío.
        *el_telefono: Teléfono del estudiante, por defecto vacío.
        *el_email: E-mail del estudiante, por defecto vacío.
        *el_semestre: Semestre del estudiante, por defecto 0.
        *la_contraseña: Contraseña del estudiante, por defecto 123.
        *el_programa: Programa del estudiante, por defecto None.
        *el_estado: Estado del estudiante, por defecto True.
        *el_num_cance: Número de cancelaciones disponibles del estudiante, por
         defecto 4.
        '''
        Usuario.__init__(self, la_identificacion, el_nombre, la_direccion,
                         el_telefono, el_email, la_contraseña, el_estado)
        self.__codigo = el_codigo
        self.__semestre = el_semestre
        self.__programa = el_programa
        self.__num_cance = el_num_cance

    def get_codigo(self):
        '''Método de la clase Estudiante que devuelve el código del estudiante.
        Retornos:
        *self.__codigo: Código del estudiante.
        '''
        return self.__codigo

    def get_semestre(self):
        '''Método de la clase Estudiante que devuelve el semestre del
        estudiante.
        Retornos:
        *self.__semestre: Semestre del estudiante.
        '''
        return self.__semestre

    def get_programa(self):
        '''Método de la clase Estudiante que devuelve el programa del
        estudiante.
        Retornos:
        *self.__programa: Programa del estudiante.
        '''
        return self.__programa

    def get_num_cancelaciones(self):
        '''Método de la clase Estudiante que devuelve el número de
        cancelaciones disponibles del estudiante.
        Retornos:
        *self.__num_cance: Número de cancelaciones disponibles del estudiante.
        '''
        return self.__num_cance

    def set_codigo(self, el_codigo):
        '''Método de la clase Estudiante que asigna el código del estudiante.
        Parámetros:
        *el_codigo: Código del estudiante.
        '''
        self.__codigo = el_codigo

    def set_semestre(self, el_semestre):
        '''Método de la clase Estudiante que asigna el semestre del estudiante.
        Parámetros:
        *el_semestre: Semestre del estudiante.
        '''
        self.__semestre = el_semestre

    def set_programa(self, el_programa):
        '''Método de la clase Estudiante que asigna el programa del estudiante.
        Parámetros:
        *el_programa: Programa del estudiante.
        '''
        self.__programa = el_programa

    def set_num_cancelaciones(self, el_num_cance):
        '''Método de la clase Estudiante que asigna el número de cancelaciones
        disponibles del estudiante.
        Parámetros:
        *el_num_cance: Número de cancelaciones disponibles del estudiante.
        '''
        self.__num_cance = el_num_cance


class Docente(Usuario):
    '''Clase que modela los métodos y atributos que tendrá un docente en el
    sistema.
    '''
    def __init__(self, el_codigo='', la_identificacion='', el_nombre='',
                 la_direccion='', el_telefono='', el_email='',
                 la_contraseña='123', el_programa=None, el_estado=True):
        '''Método de la clase Docente que se encarga de inicializar un nuevo
        docente.
        Parámetros:
        *el_codigo: Código del docente, por defecto vacío.
        *la_identificacion: Identificación del docente, por defecto vacío.
        *el_nombre: Nombre del docente, por defecto vacío.
        *la_direccion: Dirección del docente, por defecto vacío.
        *el_telefono: Teléfono del docente, por defecto vacío.
        *el_email: E-mail del docente, por defecto vacío.
        *la_contraseña: Contraseña del docente, por defecto 123.
        *el_programa: Programa del docente, por defecto None.
        *el_estado: Estado del docente, por defecto True.
        '''
        Usuario.__init__(self, la_identificacion, el_nombre, la_direccion,
                         el_telefono, el_email, la_contraseña, el_estado)
        self.__codigo = el_codigo
        self.__programa = el_programa

    def get_codigo(self):
        '''Método de la clase Docente que devuelve el código del docente.
        Retornos:
        *self.__codigo: Código del docente.
        '''
        return self.__codigo

    def get_programa(self):
        '''Método de la clase Docente que devuelve el programa del docente.
        Retornos:
        *self.__programa: Programa del docente.
        '''
        return self.__programa

    def set_codigo(self, el_codigo):
        '''Método de la clase Docente que asigna el código del docente.
        Parámetros:
        *el_codigo: Código del docente.
        '''
        self.__codigo = el_codigo

    def set_programa(self, el_programa):
        '''Método de la clase Docente que asigna el programa del docente.
        Parámetros:
        *el_programa: Programa del docente.
        '''
        self.__programa = el_programa


class Administrador(Usuario):
    '''Clase que modela los métodos y atributos que tendrá un administrador en
    el sistema.
    '''
    def __init__(self, el_codigo='', la_identificacion='', el_nombre='',
                 la_direccion='', el_telefono='', el_email='',
                 la_contraseña='123', la_facultad=None, el_estado=True):
        '''Método de la clase Administrador que se encarga de inicializar un
        nuevo administrador.
        Parámetros:
        *el_codigo: Código del administrador, por defecto vacío.
        *la_identificacion: Identificación del administrador, por defecto
         vacío.
        *el_nombre: Nombre del administrador, por defecto vacío.
        *la_direccion: Dirección del administrador, por defecto vacío.
        *el_telefono: Teléfono del administrador, por defecto vacío.
        *el_email: E-mail del administrador, por defecto vacío.
        *la_contraseña: Contraseña del administrador, por defecto 123.
        *la_facultad: Facultad del administrador, por defecto None.
        *el_estado: Estado del administrador, por defecto True.
        '''
        Usuario.__init__(self, la_identificacion, el_nombre, la_direccion,
                         el_telefono, el_email, la_contraseña, el_estado)
        self.__codigo = el_codigo
        self.__facultad = la_facultad

    def get_codigo(self):
        '''Método de la clase Administrador que devuelve el código del
        administrador.
        Retornos:
        *self.__codigo: Código del administrador.
        '''
        return self.__codigo

    def get_facultad(self):
        '''Método de la clase Administrador que devuelve la facultad del
        administrador.
        Retornos:
        *self.__facultad: Facultad del administrador.
        '''
        return self.__facultad

    def set_codigo(self, el_codigo):
        '''Método de la clase Administrador que asigna el programa del
        administrador.
        Parámetros:
        *el_codigo: Código del administrador.
        '''
        self.__codigo = el_codigo

    def set_facultad(self, la_facultad):
        '''Método de la clase Administrador que asigna el programa del
        administrador.
        Parámetros:
        *la_facultad: Facultad del administrador.
        '''
        self.__facultad = la_facultad


class Grupo:
    '''Clase que modela los métodos y atributos que tendrá un grupo en el
    sistema.
    '''
    def __init__(self, el_codigo='', el_nombre='', el_cupo=0,
                 la_materia=None, el_docente=None):
        '''Método de la clase Grupo que se encarga de inicializar un nuevo
        grupo.
        Parámetros:
        *el_codigo: Código del grupo, por defecto vacío.
        *el_nombre: Nombre del grupo, por defecto vacío.
        *el_cupo: Número de cupos que tiene el grupo, por defecto 0.
        *la_materia: Materia a la que está asociada el grupo, por defecto None.
        *el_docente: Docente asignado al grupo, por defecto None.
        '''
        self.__codigo_grupo = el_codigo
        self.__nombre_grupo = el_nombre
        self.__cupo = el_cupo
        self.__materia = la_materia
        self.__docente = el_docente
        self.__estudiantes = LSE()

    # Métodos get
    def get_codigo_grupo(self):
        '''Método de la clase Grupo que devuelve el código del grupo.
        Retornos:
        *self.__codigo_grupo: Código del grupo.
        '''
        return self.__codigo_grupo

    def get_nombre_grupo(self):
        '''Método de la clase Grupo que devuelve el nombre del grupo.
        Retornos:
        *self.__nombre_grupo: Nombre del grupo.
        '''
        return self.__nombre_grupo

    def get_cupo(self):
        '''Método de la clase Grupo que devuelve el número de cupos disponibles
        del grupo.
        Retornos:
        *self.__cupo: Cupos disponibles del grupo.
        '''
        return self.__cupo

    def get_materia(self):
        '''Método de la clase Grupo que devuelve la materia asociada al grupo.
        Retornos:
        *self.__materia: Materia asociada al grupo.
        '''
        return self.__materia

    def get_docente(self):
        '''Método de la clase Grupo que devuelve el docente asignado al grupo.
        Retornos:
        *self.__docente: Docente asignado al grupo.
        '''
        return self.__docente

    # Métodos set
    def set_codigo_grupo(self, el_codigo_grupo):
        '''Método de la clase Grupo que asigna el código al grupo.
        Parámetros:
        *el_codigo_grupo: Código del grupo.
        '''
        self.__codigo_grupo = el_codigo_grupo

    def set_nombre_grupo(self, el_nombre_grupo):
        '''Método de la clase Grupo que asigna el nombre al grupo.
        Parámetros:
        *el_nombre_grupo: Nombre del grupo.
        '''
        self.__nombre_grupo = el_nombre_grupo

    def set_cupo(self, el_cupo):
        '''Método de la clase Grupo que asigna un número de cupos disponibles
        al grupo.
        Parámetros:
        *el_cupo: Número de cupos disponibles del grupo.
        '''
        self.__cupo = el_cupo

    def set_materia(self, la_materia):
        '''Método de la clase Grupo que asigna la materia asociada al grupo.
        Parámetros:
        *la_materia: Materia asociada al grupo.
        '''
        self.__materia = la_materia

    def set_docente(self, el_docente):
        '''Método de la clase Grupo que asigna al docente encargado del grupo.
        Parámetros:
        *el_docente: Docente encargado del grupo.
        '''
        self.__docente = el_docente

    # Numero de estudiantes en el Grupo
    def get_numero_estudiantes(self):
        '''Método de la clase Grupo que devuelve el número de estudiantes
        matriculados en el grupo.
        Retornos:
        *len(self.__estudiantes): Número de estudiantes matriculados en el
         grupo.
        '''
        return len(self.__estudiantes)


class Administracion:
    '''
    Clase que se encarga de la administración de la base de datos del sistema.
    '''
    def __init__(self):
        '''
        Constructor de la clase donde se hace la conexión con la base
        de datos y se inicializa el controlador que interactua con ella.
        '''
        self.conx_bd = sqlite3.connect("db/db_troy.db")
        self.cursor = self.conx_bd.cursor()

    def get_estudiante(self, codigo, contraseña):
        '''
        Método que busca en base de datos un estudiante segun su código y
        contraseña como usuario del sistema.

        Parametros:
        * codigo: codigo estudiante a buscar.
        * contraseña: contraseña estudiante a verificar.
        Retornos:
        * estudiante: en el caso de que el estudiante buscado es encontrado,
        de lo contrario retornara None.
        '''
        contraseña = self.encriptar(codigo, contraseña)
        dat_usuario = [codigo, contraseña]
        self.cursor.execute('''SELECT *
                               FROM Estudiantes
                               WHERE codigo_est = ? AND contraseña = ?;''', dat_usuario)
        # print(self.cursor.fetchone())
        for est in self.cursor:
            (el_codigo, la_identificacion, el_nombre, la_direccion, el_telefono,
             el_email, el_semestre, la_contraseña, el_programa, estado, num_cance) = est
            la_contraseña = self.desencriptar(el_codigo, la_contraseña)
            estudiante = Estudiante(el_codigo, la_identificacion, el_nombre,
                                    la_direccion, el_telefono, el_email,
                                    el_semestre, la_contraseña, el_programa, estado, num_cance)
            return estudiante
        return None

    def get_docente(self, codigo, contraseña):
        '''
        Método que busca en base de datos un docente segun su codigo y
        contraseña como usuario del sistema.

        Parametros:
        * codigo: codigo docente a buscar.
        * contraseña: contraseña docente a verificar.
        Retornos:
        * docente: en el caso de que el docente buscado es encontrado,
        de lo contrario retornara None.
        '''
        contraseña = self.encriptar(codigo, contraseña)
        dat_usuario = [codigo, contraseña]
        self.cursor.execute(''' SELECT *
                                FROM docentes
                                WHERE codigo_doc = ? AND contraseña = ?;''' , dat_usuario)
        for doc in self.cursor:
            (el_codigo, la_identificacion, el_nombre, la_direccion, el_telefono,
             el_email, la_contraseña, el_programa, el_estado) = doc
            la_contraseña = self.desencriptar(el_codigo, la_contraseña)
            docente = Docente(el_codigo, la_identificacion, el_nombre,
                              la_direccion, el_telefono, el_email,
                              la_contraseña, el_programa, el_estado)
            return docente
        return None

    def get_docente_repo(self, cod_gru):
        '''
        Método que busca en base de datos un docente asignado a una materia
        dictada. El docente es buscado segun el grupo asignado que tiene.

        Parametros:
        * cod_gru: codigo del grupo al cual esta asignado el docente buscado.
        Retornos:
        * docente: el docente buscado segun codigo de grupo.
        '''
        self.cursor.execute(''' SELECT docente
                            FROM grupos
                            WHERE codigo_gru='%s';''' %cod_gru)
        cod_doc, = self.cursor.fetchone()
        self.cursor.execute(''' SELECT *
                                FROM Docentes
                                WHERE codigo_doc='%s';''' %cod_doc)
        (el_codigo, la_identificacion, el_nombre, la_direccion, el_telefono,
         el_email, la_contraseña, el_programa, el_estado) = self.cursor.fetchone()
        la_contraseña = self.desencriptar(el_codigo, la_contraseña)
        docente = Docente(el_codigo, la_identificacion, el_nombre,
                          la_direccion, el_telefono, el_email,
                          la_contraseña, el_programa, el_estado)
        return docente

    def get_administrador(self, codigo, contraseña):
        '''
        Método que busca en base de datos un administrador segun su codigo y
        contraseña como usuario del sistema.

        Parametros:
        * codigo: codigo administrador a buscar.
        * contraseña: contraseña administrador a verificar.
        Retornos:
        * administrador: en el caso de que el administrador buscado es encontrado,
        de lo contrario retornara None.
        '''
        contraseña = self.encriptar(codigo, contraseña)
        dat_usuario = [codigo, contraseña]
        self.cursor.execute(''' SELECT *
                                FROM administradores
                                WHERE codigo_adm = ? AND contraseña = ?;''' , dat_usuario)
        for adm in self.cursor:
            (el_codigo, la_identificacion, el_nombre, la_direccion, el_telefono,
             el_email, la_contraseña, la_facultad, el_estado) = adm
            la_contraseña = self.desencriptar(el_codigo, la_contraseña)
            administrador = Administrador(el_codigo, la_identificacion,
                                          el_nombre, la_direccion, el_telefono,
                                          el_email, la_contraseña, la_facultad, el_estado)
            return administrador
        return None

    def get_programa(self, codigo_pro):
        '''
        Método que busca en base de datos un programa segun su codigo de
        programa.

        Parametros:
        * codigo_pro: Codigo del programa a buscar.
        Retornos:
        * programa: en el caso de que el programa buscado es encontrado,
        de lo contrario retornara None.
        '''
        self.cursor.execute(''' SELECT *
                                FROM Programas
                                WHERE codigo_pro = '%s';''' %codigo_pro)
        for pro in self.cursor:
            codigo, nombre, facultad = pro
            programa = Programa(codigo, nombre, facultad)
            return programa
        return None

    def get_facultad(self, codigo_fac):
        '''
        Método que busca en base de datos una facultad segun su codigo de
        facultad.

        Parametros:
        * codigo_fac: Codigo de la facultad a buscar.
        Retornos:
        * facultad: en el caso de que la facultad buscado es encontrado,
        de lo contrario retornara None.
        '''
        self.cursor.execute(''' SELECT *
                                FROM Facultades
                                WHERE codigo_fac = '%s';''' %codigo_fac)
        for fac in self.cursor:
            cod_fac, nom_fac = fac
            facultad = Facultad(cod_fac, nom_fac)
            return facultad
        return None

    def get_conse_cod_matri(self):
        '''
        Método que se encarga de obtener de la base de datos el codigo
        consecutivo para realizar una nueva insercion de un registro de
        matricula.

        Retorno:
        * numero consecutivo de matricula.
        '''
        self.cursor.execute(''' SELECT MAX(codigo_matri) FROM matriculas''')
        for max in self.cursor:
            if max[0] is None:
                return 1
            return 1 + max[0]

    def get_info_matriculas(self, nom_gru, nom_mat, cod_pro):
        '''
        Método que se encarga de obtener de la base de datos el codigo del
        grupo y la materia selecionada a matricular.

        Parametros:
        * nom_gru: nombre del grupo matriculado.
        * nom_mat: nombre de la materia matriculada.
        * cod_pro: codigo del programa del estudiante que realizo la matricula.
        Retorno:
        * cod_gru: codigo del grupo matriculado.
        * cod_mat: codigo de la materia matriculada.
        '''
        datos = [nom_gru, nom_mat, cod_pro]
        self.cursor.execute(''' SELECT codigo_gru, codigo_mat
                                FROM grupos join materias on materia = codigo_mat
                                WHERE nombre_gru = ? and nombre_mat = ? and programa = ?;''', datos)
        cod_gru, cod_mat = self.cursor.fetchone()
        return(cod_gru, cod_mat)

    def get_mat_matriculadas(self, cod_est):
        '''
        Método que busca en base de datos todas las materias matriculadas por
        un estudiante.

        Parametros:
        * cod_est: codigo del estudiante a buscar sus materias matriculadas.
        Retornos:
        * arr: lista de nombres de las materias buscadas.
        '''
        arr = []
        self.cursor.execute(''' SELECT nombre_mat
                                FROM estudiantes join matriculas as matri on codigo_est = matri.estudiante
                                    join materias on codigo_mat=matri.materia
                                WHERE codigo_est = '%s' and matri.estado = 'MATRICULADA';''' %cod_est)
        for mat in self.cursor:
            arr.append(mat[0])
        return arr

    def set_matricula(self, cod_matri, cod_est, cod_gru, cod_mat):
        '''
        Método que se encarga de registra en base de datos una nueva matricula
        de materias de un estudiante.

        Parametros:
        *cod_matri: Codigo unico consecutivo para el registro.
        *cod_est: Codigo del estudiante que realiza la matricula.
        *cod_gru: Codigo del grupo al que se matriculo el estudiante.
        *cod_mat: Codigo de materia a la que se matriculo el estudiante.
        '''
        datos = [cod_matri, cod_est, cod_gru, cod_mat, 'MATRICULADA']
        self.cursor.execute(''' INSERT INTO Matriculas VALUES (?, ?, ?, ?, ?);''', datos)
        self.cursor.execute(''' UPDATE grupos
                                SET cupo = cupo-1
                                WHERE codigo_gru = '%s'; ''' %cod_gru)
        self.conx_bd.commit()

    def set_cancelacion(self, cod_matri, nom_mat, nom_gru, cod_est):
        '''
        Método que se encarga de registra en base de datos una nueva cancelacion
        de materias de un estudiante.

        Parametros:
        * cod_matri: Codigo unico consecutivo para el registro.
        * nom_mat: Nombre de la materia cancelada.
        * nom_gru: Nombre del grupo de la materia cancelado.
        * cod_est: Codigo del estudiante que realizo la cancelacion.
        '''
        datos = [cod_est, nom_mat]
        self.cursor.execute(''' SELECT codigo_mat, grupo
                                FROM matriculas join materias on materia=codigo_mat
                                WHERE estudiante=? and nombre_mat=?;''', datos)
        cod_mat, cod_gru = self.cursor.fetchone()
        datos = [cod_matri, cod_est, cod_gru, cod_mat, 'CANCELADA']
        self.cursor.execute(''' INSERT INTO Matriculas VALUES (?, ?, ?, ?, ?);''', datos)
        self.cursor.execute(''' DELETE FROM matriculas
                            WHERE estudiante=? and materia=? and estado='MATRICULADA';''', [cod_est, cod_mat])
        self.cursor.execute(''' UPDATE grupos
                                SET cupo = cupo+1
                                WHERE codigo_gru = '%s';''' %cod_gru)
        self.cursor.execute('''UPDATE estudiantes
                               SET num_cance = num_cance-1
                               WHERE codigo_est='%s';''' %cod_est)
        self.conx_bd.commit()

    def validar_cod_usuario(self, cod_usu):
        '''
        Método que busca en base de datos un usuario por su codigo.

        Parametros:
        * cod_usu: Codigo del usuario buscado.
        Retorno:
        * codigo_usu: si el usuario buscado es encontrado, de lo contrario
        retorna None.
        '''
        self.cursor.execute(''' SELECT codigo_est
                                From estudiantes
                                WHERE codigo_est='%s' ''' %cod_usu)
        for usu in self.cursor:
            codigo_usu, = usu
            return codigo_usu
        self.cursor.execute(''' SELECT codigo_doc
                                FROM docentes
                                WHERE codigo_doc='%s' ''' %cod_usu)
        for usu in self.cursor:
            codigo_usu, = usu
            return codigo_usu
        self.cursor.execute(''' SELECT codigo_adm
                                FROM administradores
                                WHERE codigo_adm='%s' ''' %cod_usu)
        for usu in self.cursor:
            codigo_usu, = usu
            return codigo_usu
        return None

    def get_num_cancelaciones(self, cod_usu):
        '''
        Método que busca en base de datos el numero de cancelaciones que tiene
        permitido un estudiante.

        Parametros:
        * cod_usu: codigo del usuario buscado.
        Retorno:
        * num_cance: el numero de cancelaciones permitido por el estudiante.
        '''
        self.cursor.execute(''' SELECT num_cance
                                FROM Estudiantes
                                WHERE codigo_est='%s';''' %cod_usu)
        num_cance, = self.cursor.fetchone()
        return num_cance

    def get_reporte_matri(self, cod_est):
        '''
        Método que busca en base de datos todos los registro de matricula y
        cancelacion de un estudiante.

        Parametros:
        * cod_est: Codigo del estudiante a buscar sus registros.
        Retorno:
        * mat_matri: informacion de codigo y nombre de la materia, nombre de
        grupo, semestrem y estado por cada una de las materias matriculadas
        y canceladas.
        '''
        self.cursor.execute(''' SELECT mat.codigo_mat, mat.nombre_mat, gru.nombre_gru, est.semestre, matri.estado
                                FROM matriculas matri join materias mat on matri.materia=mat.codigo_mat
                                	join grupos gru on matri.grupo=gru.codigo_gru
                                	join estudiantes est on matri.estudiante=est.codigo_est
                                WHERE codigo_est='%s';''' %cod_est)
        mat_matri = []
        for matri in self.cursor:
            cod_mat, nom_mat, nom_gru, sem, estado = matri
            mat_matri.append([cod_mat, nom_mat, nom_gru, sem, estado])
        return mat_matri

    def get_est_matri(self, cod_gru):
        '''
        Método que busca en base de datos los etudiantes matriculados en un
        grupo de un una materia determinada.

        Parametros:
        * cod_gru: codigo del grupo en el cual se encuentran matriculados los
        estudiantes.
        Retornos:
        * estu_matri: listado de los estudiantes que estan en ese grupo.
        '''
        self.cursor.execute(''' SELECT codigo_est, nombre_est
                            FROM matriculas join estudiantes on estudiante=codigo_est
                                join grupos on grupo=codigo_gru
                            WHERE codigo_gru='%s';''' %cod_gru)
        estu_matri = []
        for est in self.cursor:
            cod_est, nom_est = est
            estu_matri.append([cod_est, nom_est])
        return estu_matri

    def invalidar_usuario(self, cod_usu, tipo_usu):
        '''
        Método que se encarga de cambiar en base de datos el estado de un
        usuario, true si ya es habilitado o false si queda inhabilitado Para
        ingresar al sistema.

        Parametros:
        * cod_usu: Codigo del usuario al cual se le cambiara el estado.
        * tipo_usu: Tipo de usuario para poder realizar la busqueda.
        '''
        if tipo_usu == 'EST':
            self.cursor.execute(''' UPDATE estudiantes
                                    SET estado=0
                                    WHERE codigo_est='%s';''' %cod_usu)
        elif tipo_usu == 'DOC':
            self.cursor.execute(''' UPDATE docentes
                                    SET estado=0
                                    WHERE codigo_doc='%s';''' %cod_usu)
        else:
            self.cursor.execute(''' UPDATE administradores
                                    SET estado=0
                                    WHERE codigo_adm='%s';''' %cod_usu)
        self.conx_bd.commit()

    def get_estado(self, cod_usu, tipo_usu):
        '''
        Método que se encarga de buscar en base de datos el estado de hactividad
        o inhactiviade de un usuario.
        Parametros:
        * cod_usu: Codigo del usuario del cual se quiere saber su estado.
        * tipo_usu: Tipo de ususario para poder realizar la busqueda.
        '''
        if tipo_usu == 'EST':
            self.cursor.execute(''' SELECT estado FROM estudiantes WHERE codigo_est='%s';''' %cod_usu)
            estado = self.cursor.fetchone()
        elif tipo_usu == 'DOC':
            self.cursor.execute(''' SELECT estado FROM docentes WHERE codigo_doc='%s';''' %cod_usu)
            estado = self.cursor.fetchone()
        else:
            self.cursor.execute(''' SELECT estado FROM administradores WHERE codigo_adm='%s';''' %cod_usu)
            estado = self.cursor.fetchone()
        return estado[0]

    def init_treeS_matricula(self, treeS_matricula, codigo_est):
        '''
        Método que carga en el TreeStore de la seccion de matriculas las
        materias con sus respectivos grupos que el estudiante puede matricular.

        Parametros:
        * treeS_matricula: es el TreeStore modelo del TreeView de matricula.
        * codigo_est: Codigo del estudiante del cual se obtendra la información.
        '''
        treeS_matricula.clear()
        mat_matri = self.get_mat_matriculadas(codigo_est)
        print('-'*50)
        print(mat_matri)
        self.cursor.execute(""" SELECT nombre_mat, nombre_gru, cupo
                                FROM (estudiantes as est join programas as pro on pro.codigo_pro = est.programa
	                                  join materias as mat on pro.codigo_pro = mat.programa)
	                                  join grupos as gru on mat.codigo_mat = gru.materia
                                WHERE est.semestre = mat.semestre and cupo > 0 and est.codigo_est = '%s';""" %codigo_est)
        grupos = []
        aux = None
        con = 0
        for gru in self.cursor:
            nom_mat, nom_gru, cupo = gru
            cupo = str(cupo)
            if nom_mat not in mat_matri:
                if aux is not None:
                    if nom_mat == aux:
                        grupos[con].append([nom_gru, cupo, False])
                    else:
                        grupos.append([nom_mat, [nom_gru, cupo, False]])
                        aux = nom_mat
                        con += 1
                else:
                    grupos.append([nom_mat, [nom_gru, cupo, False]])
                    aux = nom_mat
        for i in range(len(grupos)):
            piter = treeS_matricula.append(None, [grupos[i][0], '', True])
            j = 1
            while j < len(grupos[i]):
                treeS_matricula.append(piter, grupos[i][j])
                j += 1

    def init_list_cancelacion(self, list_cancelacion, codigo_est):
        '''
        Método que carga en el LisStore de la seccion de cancelacion las
        materias con sus respectivos grupos que el estudiante puede cancelar.

        Parametros:
        * list_cancelacion: es el ListStore modelo del TreeView de cancelacion.
        * codigo_est: Codigo del estudiante del cual se obtendra la información.
        '''
        list_cancelacion.clear()
        self.cursor.execute(''' SELECT m2.nombre_mat, nombre_gru
                                FROM matriculas m1 join materias m2 on m1.materia = m2.codigo_mat
                                     join grupos on m1.grupo = codigo_gru
                                WHERE estudiante = '%s' and estado='MATRICULADA';''' %codigo_est)
        for mat in self.cursor:
            nom_mat, nom_gru = mat
            list_cancelacion.append([nom_mat, nom_gru, False])

    def init_list_mate_doc(self, codigo, list_inst):
        '''
        Método que se encarga de cargar en el ListStore las materias que tiene
        a cargo un docente.

        Parametros:
        * codigo: codigo del docente del cual se quiere obtener sus materias.
        * list_inst: LisStore modelo del combo box de las materias del docente.
        '''
        list_inst.clear()
        self.cursor.execute(''' SELECT DISTINCT codigo_mat, nombre_mat
                                FROM Grupos join Docentes on docente = codigo_doc
                                        join Materias as mat on codigo_mat = materia
                                WHERE docente = '%s';''' %codigo)
        for mat in self.cursor:
            cod_mat, nom_mat = mat
            list_inst.append([nom_mat, cod_mat])

    def init_list_grup_doc(self, codigo_mat, list_inst):
        '''
        Método que se encarga de cargar en el ListStore los grupos que tiene
        una materia a cargo de un docente.

        Parametros:
        * codigo_mat: codigo de la materia del cual se quiere obtener sus grupos.
        * list_inst: LisStore modelo del combo box de los grupos.
        '''
        list_inst.clear()
        self.cursor.execute(''' SELECT codigo_gru, nombre_gru
                                FROM Grupos
                                WHERE materia = '%s';''' %codigo_mat)
        for gru in self.cursor:
            cod_gru, nom_gru = gru
            list_inst.append([nom_gru, cod_gru])

    def init_list_prog_adm(self, codigo_adm, list_inst):
        '''
        Método que se encarga de cargar en el ListStore los programas que tiene
        a cargo un administrador de facultad.

        Parametros:
        * codigo_adm: codigo del administrador del cual se quiere obtener sus
        programas.
        * list_inst: LisStore modelo del combo box de los programas.
        '''
        list_inst.clear()
        self.cursor.execute(''' SELECT codigo_pro, nombre_pro
                                FROM (Administradores join facultades on facultad = codigo_fac) as t1
                                join programas as pro on t1.codigo_fac = pro.facultad
                                WHERE t1.codigo_adm = '%s';''' %codigo_adm)
        for pro in self.cursor:
            cod_pro, nom_pro = pro
            list_inst.append([nom_pro, cod_pro])

    def init_list_mate_adm(self, codigo_pro, list_inst):
        '''
        Método que se encarga de cargar en el ListStore las materias que tiene
        a cargo un administrador.

        Parametros:
        * codigo_pro: codigo del programa del cual se quiere obtener sus materias.
        * list_inst: LisStore modelo del combo box de las materias del
        administrador.
        '''
        list_inst.clear()
        self.cursor.execute(''' SELECT codigo_mat, nombre_mat
                                FROM Programas join materias on codigo_pro = programa
                                WHERE codigo_pro = '%s';''' %codigo_pro)
        for mat in self.cursor:
            cod_mat, nom_mat = mat
            list_inst.append([nom_mat, cod_mat])

    def init_list_grup_adm(self, codigo_mat, list_grup):
        '''
        Método que se encarga de cargar en el ListStore los grupos que tiene
        una materia a cargo de un administrador.

        Parametros:
        * codigo_mat: codigo de la materia del cual se quiere obtener sus grupos.
        * list_grup: LisStore modelo del combo box de los grupos.
        '''
        list_grup.clear()
        self.cursor.execute(''' SELECT codigo_gru, nombre_gru
                                FROM Grupos join Materias on materia = codigo_mat
                                WHERE codigo_mat = '%s';''' %codigo_mat)
        for gru in self.cursor:
            cod_gru, nom_gru = gru
            list_grup.append([nom_gru, cod_gru])

    def desencriptar(self, cod_usu, contra):
        try:
            digito = int(cod_usu[-1])
            desencri = ''
            for c in contra:
                ce = chr(ord(c)-digito)
                desencri += ce
            return desencri
        except ValueError:
            return ''

    def encriptar(self, cod_usu, contra):
        try:
            digito = int(cod_usu[-1])
            desencri = ''
            for c in contra:
                ce = chr(ord(c)+digito)
                desencri += ce
            return desencri
        except ValueError:
            return ''


    # def encriptar(self):
    #     self.cursor.execute(''' SELECT codigo_est, contraseña FROM estudiantes;''')
    #     arr_encri = []
    #     for est in self.cursor:
    #         cod_est, contra = est
    #         digito = int(cod_est[-1])
    #         arr_encri.append([digito, contra, cod_est])
    #     for est in arr_encri:
    #         encriptada = ''
    #         for c in est[1]:
    #             ce = chr(ord(c) + est[0])
    #             encriptada += ce
    #         self.cursor.execute(''' UPDATE estudiantes SET contraseña=? WHERE codigo_est=? ;''', [encriptada, est[2]])
    #     #
    #     self.cursor.execute(''' SELECT codigo_doc, contraseña FROM docentes;''')
    #     arr_encri = []
    #     for doc in self.cursor:
    #         cod_doc, contra = doc
    #         digito = int(cod_doc[-1])
    #         arr_encri.append([digito, contra, cod_doc])
    #     for doc in arr_encri:
    #         encriptada = ''
    #         for c in doc[1]:
    #             ce = chr(ord(c) + doc[0])
    #             encriptada += ce
    #         self.cursor.execute(''' UPDATE docentes SET contraseña=? WHERE codigo_doc=? ;''', [encriptada, doc[2]])
    #     #
    #     self.cursor.execute(''' SELECT codigo_adm, contraseña FROM administradores;''')
    #     arr_encri = []
    #     for adm in self.cursor:
    #         cod_adm, contra = adm
    #         digito = int(cod_adm[-1])
    #         arr_encri.append([digito, contra, cod_adm])
    #     for adm in arr_encri:
    #         encriptada = ''
    #         for c in adm[1]:
    #             ce = chr(ord(c) + adm[0])
    #             encriptada += ce
    #         self.cursor.execute(''' UPDATE administradores SET contraseña=? WHERE codigo_adm=? ;''', [encriptada, adm[2]])
    #     self.conx_bd.commit()
    #     print('-'*50)
    #     print('Todo encriptado ')
