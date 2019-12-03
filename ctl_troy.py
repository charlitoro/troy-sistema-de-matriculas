import gi
import pdfkit
gi.require_version('Gtk', '3.0')
from jinja2 import Environment, FileSystemLoader
from gi.repository import Gtk, Gdk
from mod_troy import *
from os.path import abspath, dirname, join, exists


class Troy_ctl:
    ''' Clase encargada de llevar el control del sistema. En esta se realizar
    el enlace con el modelo de interfaz grafica y con el modelo de gestion de
    informacion que tiene como funcion la coneccion con la base de datos.
    En este modulo encontramos todos los eventos de los elementos de la interfaz,
    eventos que el usuario activas cuando esta en interaccion con el sistema.'''

    def __init__(self):
        ''' Constructor de la clase Troy_ctl que realiza el enlace con la
        interfaz gráfica, inicializando todas las variables
        de los objetos.'''
        self.usuario = None
        self.intentos = ['', 0]
        gui = Gtk.Builder()
        gui.add_from_file("gui_troy.glade")
        #
        # Lista de eventos de todas las acciones de las interfaces
        eventos = {"on_w_login_delete_event": Gtk.main_quit,
                   "on_w_estudiante_delete_event": Gtk.main_quit,
                   "on_w_administracion_delete_event": Gtk.main_quit,
                   "on_dlg_about_delete_event": self.__on_dlg_about_delete_event,
                   "on_cbx_tipo_usuario_changed": self.__on_cbx_tipo_usuario_changed,
                   "on_btn_ingresar_clicked": self.__on_btn_ingresar_clicked,
                   "on_cbx_programa_adm_changed": self.__on_cbx_programa_adm_changed,
                   "on_cbx_materias_changed": self.__on_cbx_materias_changed,
                   "on_btn_gen_listado_clicked": self.__on_btn_gen_listado_clicked,
                   "on_btn_salir_adm_clicked": self.__on_btn_salir_adm_clicked,
                   "on_img_about_adm_activate": self.__on_img_about_activate,
                   "on_btn_matricular_clicked": self.__on_btn_matricular_clicked,
                   "on_btn_registrar_clicked": self.__on_btn_registrar_clicked,
                   "on_btn_salir_est_clicked": self.__on_btn_salir_est_clicked,
                   "on_btn_rep_matri_clicked": self.__on_btn_rep_matri_clicked,
                   "on_img_about_est_activate": self.__on_img_about_activate
                }
        # Conexión de los eventos al enlace de la interfaz.
        gui.connect_signals(eventos)
        self.mi_admin = Administracion()
        # self.mi_admin.encriptar()
        #
        ''' INSTANCIACION DE LAS VENTANAS '''
        self.ventana_login = gui.get_object('w_login')
        self.ventana_estudiante = gui.get_object('w_estudiante')
        self.ventana_administracion = gui.get_object('w_administracion')
        self.dlg_about = gui.get_object("dlg_about")
        #
        ''' SECCION VENTANA DE LOGIN '''
        self.cbx_tipo_usuario = gui.get_object('cbx_tipo_usuario')
        self.img_usuario = gui.get_object('img_usuario')
        self.ent_codigo = gui.get_object('ent_codigo')
        self.lbl_tip_usu = gui.get_object('lbl_tip_usu')
        self.ent_contraseña = gui.get_object('ent_contraseña')
        self.btn_ingresar = gui.get_object('btn_ingresar')
        #
        ''' SECCION VENTANA DE ADMINISTRACION '''
        self.lbl_datos = gui.get_object('lbl_datos')
        self.lbl_nom_adm = gui.get_object('lbl_nom_adm')
        self.lbl_id_adm = gui.get_object('lbl_id_adm')
        self.lbl_tel_adm = gui.get_object('lbl_tel_adm')
        self.lbl_email_adm = gui.get_object('lbl_email_adm')
        self.lbl_depen_adm = gui.get_object('lbl_depen_adm')
        self.btn_salir_adm = gui.get_object('btn_salir_adm')
        self.lbl_programa_adm = gui.get_object('lbl_programa_adm')
        self.cbx_programa_adm = gui.get_object('cbx_programa_adm')
        self.cbx_materias = gui.get_object('cbx_materias')
        self.cbx_grupos = gui.get_object('cbx_grupos')
        self.cbx_grupos = gui.get_object('cbx_grupos')
        self.img_about_adm = gui.get_object('img_about_adm')
        #
        ''' SECCION VENTANA DE ESTUDIANTE '''
        self.lbl_nom_est = gui.get_object('lbl_nom_est')
        self.lbl_id_est = gui.get_object('lbl_id_est')
        self.lbl_tel_est = gui.get_object('lbl_tel_est')
        self.lbl_email_est = gui.get_object('lbl_email_est')
        self.lbl_pro_est = gui.get_object('lbl_pro_est')
        self.lbl_sem_est = gui.get_object('lbl_sem_est')
        self.btn_salir_est = gui.get_object('btn_salir_est')
        self.btn_rep_matri = gui.get_object('btn_rep_matri')
        self.btn_matricular = gui.get_object('btn_matricular')
        self.btn_registrar = gui.get_object('btn_registrar')
        self.img_about_est = gui.get_object('img_about_est')
        self.trv_matricula = gui.get_object('trv_matricula')
        self.trv_cancelacion = gui.get_object('trv_cancelacion')
        #
        '''DEFINIR LISTSTORE '''
        self.list_tipo_usuario = Gtk.ListStore(str)
        self.cbx_tipo_usuario.set_model(self.list_tipo_usuario)
        self.list_programa_adm = Gtk.ListStore(str, str)
        self.cbx_programa_adm.set_model(self.list_programa_adm)
        self.list_materias = Gtk.ListStore(str, str)
        self.cbx_materias.set_model(self.list_materias)
        self.list_grupos = Gtk.ListStore(str, str)
        self.cbx_grupos.set_model(self.list_grupos)
        self.list_cancelacion = Gtk.ListStore(str, str, bool)

        ''' DEFINIR TREESTORE'''
        # TreeStore para al TreeView de la seccion de matricula
        self.treeS_matricula = Gtk.TreeStore(str, str, bool)
        self.__definir_treeviews()

        self.list_tipo_usuario.append(['Estudiante'])
        self.list_tipo_usuario.append(['Docente'])
        self.list_tipo_usuario.append(['Administrador'])
        # Función para la primera presentación del login.
        self.ventana_login.show()

    def __on_cbx_tipo_usuario_changed(self, widget):
        '''Evento del objeto cbx_tipo_usuario(Combo box) que se ejecuta cuando
        el usuario cambia su estado. En este método se especifica el tipo de
        usuario seleccionado para realizar el login.
        Parámetros:
        *widget: Propiedades de selección del combo box.
        '''
        item = self.cbx_tipo_usuario.get_active()
        if item == 0:
            self.lbl_tip_usu.set_text('EST')
        elif item == 1:
            self.lbl_tip_usu.set_text('DOC')
        elif item == 2:
            self.lbl_tip_usu.set_text('ADM')

    def __on_btn_ingresar_clicked(self, widget):
        ''' Evento del objeto btn_ingresar(Botón) que se ejecuta cuando es
        clickeado. Este permite verificar los datos diligenciados en los campos
        para ver si concuerdan y así iniciar la sesión del usuario en cuestión.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        if self.cbx_tipo_usuario.get_active() == -1:
            self.__mensaje(None, 'Por favor seleccione un tipo de usuario.')
        else:
            codigo = self.lbl_tip_usu.get_text() + self.ent_codigo.get_text()
            contraseña = self.ent_contraseña.get_text()
            if codigo[3:] == '' or contraseña == '':
                self.__mensaje(None, 'Para ingresar necesita diligenciar todos los campos solicitados.')
            else:
                if codigo[:3] == 'EST':
                    self.usuario = self.mi_admin.get_estudiante(codigo, contraseña)
                    if self.usuario is not None:
                        if self.usuario.get_estado():
                            self.intentos = ['', 0]
                            self.lbl_nom_est.set_text(self.usuario.get_nombre())
                            self.lbl_id_est.set_text(self.usuario.get_identificacion())
                            self.lbl_tel_est.set_text(self.usuario.get_telefono())
                            self.lbl_email_est.set_text(self.usuario.get_email())
                            programa = self.mi_admin.get_programa(self.usuario.get_programa())
                            self.lbl_pro_est.set_text(programa.get_nombre_pro())
                            self.lbl_sem_est.set_text(str(self.usuario.get_semestre()))

                            self.mi_admin.init_treeS_matricula(self.treeS_matricula, self.usuario.get_codigo())
                            self.mi_admin.init_list_cancelacion(self.list_cancelacion, self.usuario.get_codigo())
                            self.ventana_login.hide()
                            self.ventana_estudiante.show()
                        else:
                            self.__mensaje(None, 'Estimado estudiante, el número de intentos de ' +
                                                 'ingreso ha sido superado, actualmente ' +
                                                 'se encuentra inhabilitado para iniciar sesión.\n' +
                                                 'Comuniquese con el administrador de su facultad ' +
                                                 'para realizar el proceso de habilitación.')
                    else:
                        cod_usu = self.mi_admin.validar_cod_usuario(codigo)
                        if cod_usu is not None:
                            if self.mi_admin.get_estado(cod_usu, 'EST'):
                                if self.intentos[0] == cod_usu:
                                    self.intentos[1] += 1
                                    if self.intentos[1] == 4:
                                        self.mi_admin.invalidar_usuario(cod_usu, 'EST')
                                else:
                                    self.intentos = [cod_usu, 0]
                            else:
                                self.__mensaje(None, 'Estimado estudiante, el número de intentos de ' +
                                                     'ingreso ha sido superado, actualmente ' +
                                                     'se encuentra inhabilitado para iniciar sesión.\n' +
                                                     'Comuniquese con el administrador de su facultad ' +
                                                     'para realizar el proceso de habilitación.')
                        else:
                            self.intentos = ['', 0]
                        print(self.intentos)
                        self.__mensaje(None, 'Oops!. Código o contraseña incorrecta.')
                elif codigo[:3] == 'DOC':
                    self.usuario = self.mi_admin.get_docente(codigo, contraseña)
                    if self.usuario is not None:
                        if self.usuario.get_estado():
                            self.intentos = ['', 0]
                            programa = self.mi_admin.get_programa(self.usuario.get_programa())
                            self.list_programa_adm.clear()
                            self.list_programa_adm.append([programa.get_nombre_pro(), programa.get_codigo_pro()])
                            self.lbl_programa_adm.set_text('')
                            self.cbx_programa_adm.set_property('visible', False)
                            self.cbx_programa_adm.set_active(0)
                            self.lbl_datos.set_text('Datos Docente')
                            self.lbl_nom_adm.set_text(self.usuario.get_nombre())
                            self.lbl_id_adm.set_text(self.usuario.get_identificacion())
                            self.lbl_tel_adm.set_text(self.usuario.get_telefono())
                            self.lbl_email_adm.set_text(self.usuario.get_email())
                            programa = self.mi_admin.get_programa(self.usuario.get_programa())
                            self.lbl_depen_adm.set_text(programa.get_nombre_pro())

                            self.mi_admin.init_list_mate_doc(self.usuario.get_codigo(), self.list_materias)
                            self.ventana_login.hide()
                            self.ventana_administracion.show()
                        else:
                            self.__mensaje(None, 'Estimado docente, el número de intentos de ' +
                                                 'ingreso ha sido superado, actualmente ' +
                                                 'se encuentra inhabilitado para iniciar sesión.\n' +
                                                 'Comuniquese con el administrador de su facultad ' +
                                                 'para realizar el proceso de habilitación.')
                    else:
                        cod_usu = self.mi_admin.validar_cod_usuario(codigo)
                        if cod_usu is not None:
                            if self.mi_admin.get_estado(cod_usu, 'DOC'):
                                if self.intentos[0] == cod_usu:
                                    self.intentos[1] += 1
                                    if self.intentos[1] == 4:
                                        self.mi_admin.invalidar_usuario(cod_usu, 'DOC')
                                else:
                                    self.intentos = [cod_usu, 0]
                            else:
                                self.__mensaje(None, 'Estimado docente, el número de intentos de ' +
                                                     'ingreso ha sido superado, actualmente ' +
                                                     'se encuentra inhabilitado para iniciar sesión.\n' +
                                                     'Comuniquese con el administrador de su facultad ' +
                                                     'para realizar el proceso de habilitación.')
                        else:
                            self.intentos = ['', 0]
                        self.__mensaje(None, 'Oops!. Código o contraseña incorrecta.')
                else:
                    self.usuario = self.mi_admin.get_administrador(codigo, contraseña)
                    if self.usuario is not None:
                        self.intentos = ['', 0]
                        self.lbl_programa_adm.set_text('Programa')
                        self.cbx_programa_adm.set_property('visible', True)
                        self.lbl_datos.set_text('Datos Administrador')
                        self.lbl_nom_adm.set_text(self.usuario.get_nombre())
                        self.lbl_id_adm.set_text(self.usuario.get_identificacion())
                        self.lbl_tel_adm.set_text(self.usuario.get_telefono())
                        self.lbl_email_adm.set_text(self.usuario.get_email())
                        facultad = self.mi_admin.get_facultad(self.usuario.get_facultad())
                        self.lbl_depen_adm.set_text(facultad.get_nombre_fac())

                        self.mi_admin.init_list_prog_adm(self.usuario.get_codigo(), self.list_programa_adm)
                        self.ventana_login.hide()
                        self.ventana_administracion.show()
                    else:
                        self.__mensaje(None, 'Oops!. Código o contraseña incorrecta.')

    def __on_cbx_programa_adm_changed(self, widget):
        '''Evento del objeto cbx_programa_adm(Combo box) que se activa cuando
        se cambia su estado. En este objeto estarán cargados todos los
        programas que un administrador tiene a su cargo. Una vez seleccionado
        uno de esos programas se activarán y se cargarán los demás combo box
        con la información pertinente.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        item = self.cbx_programa_adm.get_active()
        if item != -1:
            cod_pro = self.list_programa_adm[item][1]
            self.mi_admin.init_list_mate_adm(cod_pro, self.list_materias)

    def __on_cbx_materias_changed(self, widget):
        '''Evento del objeto cbx_materias(Combo box) que se activa cuando
        se cambia su estado. En este objeto estarán cargados todas las materias
        que un administrador o docente tienen a su cargo. Una vez seleccionado
        uno de estas materias se activarán y se cargarán los demás combo box
        con la información pertinente.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        item = self.cbx_materias.get_active()
        if item != -1:
            cod_mat = self.list_materias[item][1]
            self.mi_admin.init_list_grup_adm(cod_mat, self.list_grupos)

    def __on_btn_gen_listado_clicked(self, widget):
        '''Evento del objeto btn_gen_listado(Botón) que se ejecuta cuando
        es clickeado. Este objeto generará un listado para administrador o
        docente de acuerdo a la materia y grupo seleccionados previamente.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        pro = self.cbx_programa_adm.get_active()
        mat = self.cbx_materias.get_active()
        gru = self.cbx_grupos.get_active()
        if pro != -1 and mat != -1 and gru != -1:
            path = self.cbx_programa_adm.get_active()
            nom_pro, cod_pro = self.list_programa_adm[path]
            path = self.cbx_materias.get_active()
            nom_mat, cod_mat = self.list_materias[path]
            path = self.cbx_grupos.get_active()
            nom_gru, cod_gru = self.list_grupos[path]
            fcd_nuevo = Gtk.FileChooserDialog("Guardar Como", self.ventana_estudiante, Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE,
                                            Gtk.ResponseType.OK))
            fcd_nuevo.add_filter(self.__add_filtro_doc())
            fcd_nuevo.set_current_folder("listados/")
            respuesta = fcd_nuevo.run()
            if respuesta == Gtk.ResponseType.OK:
                # aqui trabajar el reporte en pdf
                env = Environment(loader=FileSystemLoader("Template"))
                template = env.get_template("teacher_admin.html")
                docente = self.mi_admin.get_docente_repo(cod_gru)
                usuario = {'subject': nom_mat,
                           'code': docente.get_codigo(),
                           'name': docente.get_nombre(),
                           'program': nom_pro,
                           'grupo': nom_gru
                }
                i = 1
                estu_matri = self.mi_admin.get_est_matri(cod_gru)
                for est in estu_matri:
                    cod_est, nom_est = est
                    usuario.update({f'code{i}': cod_est,
                                    f'name{i}': nom_est})
                    i += 1
                options = {
                    'page-size': 'A4',
                    'margin-top': '0.1in',
                    'margin-right': '0.1in',
                    'margin-bottom': '0.4in',
                    'margin-left': '0.1in'
                    }
                html = template.render(usuario)
                pdfkit.from_string(html, fcd_nuevo.get_filename(), options=options)
            fcd_nuevo.destroy()
        else:
            self.__mensaje(None, 'Debe seleccionar cada uno de los items solicitados.')

    def __on_btn_salir_adm_clicked(self, widget):
        '''Evento del objeto btn_salir_adm(Botón) que se ejecuta cuando es
        clickeado. Este objeto cerrará la sesión del administrador.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        if self.__mensaje_confirmacion(None, 'Está a punto de cerrar sesión, ¿Desea continuar?'):
            self.ventana_administracion.hide()
            self.__limpiar_datos()
            self.ventana_login.show()
            self.usuario = None

    def __on_img_about_activate(self, widget):
        '''Evento del objeto img_about(Botón Imagen) que se ejecuta cuando es
        clickeado. Este objeto mostrará una ventana con información relacionada
        al sistema(Créditos, logo, etc).
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        self.dlg_about.show()

    def __on_btn_matricular_clicked(self, widget):
        '''Evento del objeto btn_matricular(Botón) que se ejecuta cuando es
        clickeado. Este objeto realizará la matricula de una o varias materias
        de un estudiante dependiendo de la materia y el grupo que el mismo haya
        seleccionado.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        if self.__mensaje_confirmacion(None, 'Está a punto de realizar la matricula de materias.\n¿Desea continuar con la operación?'):
            for i in range(len(self.treeS_matricula)):
                piter = self.treeS_matricula.get_iter(i)
                citer = self.treeS_matricula.iter_children(piter)
                while citer is not None:
                    if self.treeS_matricula[citer][2]:
                        conse_matri = self.mi_admin.get_conse_cod_matri()
                        nom_gru = self.treeS_matricula[citer][0]
                        nom_mat = self.treeS_matricula[piter][0]
                        cod_pro = self.usuario.get_programa()
                        cod_gru, cod_mat = self.mi_admin.get_info_matriculas(nom_gru, nom_mat, cod_pro)
                        cod_est = self.usuario.get_codigo()
                        self.mi_admin.set_matricula(conse_matri, cod_est, cod_gru, cod_mat)
                    citer = self.treeS_matricula.iter_next(citer)
            self.mi_admin.init_treeS_matricula(self.treeS_matricula, self.usuario.get_codigo())
            self.mi_admin.init_list_cancelacion(self.list_cancelacion, self.usuario.get_codigo())

    def __on_btn_registrar_clicked(self, widget):
        '''Evento del objeto btn_registrar(Botón) que se ejecuta cuando es
        clickeado. Este objeto realizará la cancelación de una o varias
        materias de un estudiante dependiendo de la materia y el grupo
        que el mismo haya seleccionado.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        cont = 0
        for i in range(len(self.list_cancelacion)):
            if self.list_cancelacion[i][2]:
                cont += 1
        num_cance = self.mi_admin.get_num_cancelaciones(self.usuario.get_codigo())
        if num_cance >= cont:
            if self.__mensaje_confirmacion(None, 'Está a punto de realizar la cancelación de materias.\n¿Desea continuar con la cancelación?'):
                for i in range(len(self.list_cancelacion)):
                    nom_mat, nom_gru, estado = self.list_cancelacion[i]
                    if estado:
                        cod_matri = self.mi_admin.get_conse_cod_matri()
                        self.mi_admin.set_cancelacion(cod_matri, nom_mat, nom_gru, self.usuario.get_codigo())
                self.mi_admin.init_treeS_matricula(self.treeS_matricula, self.usuario.get_codigo())
                self.mi_admin.init_list_cancelacion(self.list_cancelacion, self.usuario.get_codigo())
        else:
            self.__mensaje(None, f'Solo puede cancelar {self.usuario.get_num_cancelaciones()} materias.')

    def __on_btn_salir_est_clicked(self, widget):
        '''Evento del objeto btn_salir_est(Botón) que se ejecuta cuando es
        clickeado. Este objeto cerrará la sesión del estudiante.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        if self.__mensaje_confirmacion(None, 'Está a punto de cerrar sesión, ¿Desea continuar?'):
            self.ventana_estudiante.hide()
            self.__limpiar_datos()
            self.ventana_login.show()
            self.usuario = None

    def __on_btn_rep_matri_clicked(self, widget):
        '''Evento del objeto btn_rep_matri(Botón) que se ejecuta cuando
        es clickeado. Este objeto generará un listado para un estudiante
        de acuerdo a las materia que tenga matriculadas y también aquellas que
        haya cancelado.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        '''
        if self.__mensaje_confirmacion(None, 'Esta a punto de generar su reporte de matricula.\n'+
                                       '¿Acepta los términos de obtención de información personal?.'):
            fcd_nuevo = Gtk.FileChooserDialog("Guardar Como", self.ventana_estudiante, Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE,
                                            Gtk.ResponseType.OK))
            fcd_nuevo.add_filter(self.__add_filtro_doc())
            fcd_nuevo.set_current_folder("reportes/")
            respuesta = fcd_nuevo.run()
            if respuesta == Gtk.ResponseType.OK:
                # aqui trabajar el reporte en pdf
                env = Environment(loader=FileSystemLoader("Template"))
                template = env.get_template("student.html")
                programa = self.mi_admin.get_programa(self.usuario.get_programa())
                usuario = {
                    # Código, nombre, programa y semestre del estudiante
                    'code': self.usuario.get_codigo(),
                    'name': self.usuario.get_nombre(),
                    'program': programa.get_nombre_pro(),
                    'semester': self.usuario.get_semestre()
                    }
                mat_matri = self.mi_admin.get_reporte_matri(self.usuario.get_codigo())
                i = 1
                for mat in mat_matri:
                    cod_mat, nom_mat, nom_gru, sem, estado = mat
                    if estado == 'MATRICULADA':
                        usuario.update({f'code{i}':cod_mat,
                                       f'subject{i}':nom_mat,
                                       f'group{i}':nom_gru,
                                       f'semester{i}':sem,
                                       f'state{i}':estado})
                        i += 1
                i = 1
                for mat in mat_matri:
                    cod_mat, nom_mat, nom_gru, sem, estado = mat
                    if estado == 'CANCELADA':
                        usuario.update({f'code_cancel{i}':cod_mat,
                                       f'subject_cancel{i}':nom_mat,
                                       f'group_cancel{i}':nom_gru,
                                       f'semester_cancel{i}':sem,
                                       f'state_cancel{i}':estado})
                        i += 1
                options = {
                    'page-size': 'A4',
                    'margin-top': '0.1in',
                    'margin-right': '0.1in',
                    'margin-bottom': '0.4in',
                    'margin-left': '0.1in'
                    }
                html = template.render(usuario)
                pdfkit.from_string(html, fcd_nuevo.get_filename(), options=options)
            fcd_nuevo.destroy()

    def __on_treeS_toggled_active(self, widget, path):
        '''Evento de los check box que se encuentran en la sección de
        matriculas que se activa cuando un recuadro de estos es seleccionado.
        Se seleccionará con un visto indicando que se encuentra seleccionado.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        *path: Hace referencia al registro seleccionado.
        '''
        if len(path) == 1:
            piter = self.treeS_matricula.get_iter(path)
            citer = self.treeS_matricula.iter_children(piter)
            while citer is not None:
                self.treeS_matricula[citer][2] = False
                citer = self.treeS_matricula.iter_next(citer)
            self.treeS_matricula[piter][2] = True
        elif len(path) != 1:
            citer = self.treeS_matricula.get_iter(path)
            piter = self.treeS_matricula.iter_parent(citer)
            cs_iter = self.treeS_matricula.iter_children(piter)
            while cs_iter is not None:
                self.treeS_matricula[piter][2] = False
                if self.treeS_matricula[cs_iter][2] is True:
                    self.treeS_matricula[cs_iter][2] = False
                cs_iter = self.treeS_matricula.iter_next(cs_iter)
            self.treeS_matricula[citer][2] = True

    def __on_list_can_toggled_active(self, widget, path):
        '''Evento de los check box que se encuentran en la sección de
        cancelación que se activa cuando un recuadroe estos es seleccionado. Se
        seleccionará con un visto indicando que se encuentra seleccionado.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        *path: Hace referencia al registro seleccionado.
        '''
        self.list_cancelacion[path][2] = not self.list_cancelacion[path][2]

    def __definir_treeviews(self):
        '''Función de la clase que se encarga de definir los TreeView de
        matriculas y el de cancelaciones. Se carga con información cada una de
        las columnas de los TreeView.
        '''
        ''' TreeView Matricula'''
        self.trv_matricula.set_model(self.treeS_matricula)
        renderer_mat = Gtk.CellRendererText()
        # primera columna del TreeView
        column_mat = Gtk.TreeViewColumn('Materia', renderer_mat, text=0)
        self.trv_matricula.append_column(column_mat)
        # segunda columna del TreeViewColumn
        renderer_cup = Gtk.CellRendererText()
        column_cup = Gtk.TreeViewColumn('Cupos', renderer_cup, text=1)
        self.trv_matricula.append_column(column_cup)
        # Tercera columna del TreeViewColumn
        renderer_in_out = Gtk.CellRendererToggle()
        renderer_in_out.set_radio(True)
        column_in_out = Gtk.TreeViewColumn('Grupo', renderer_in_out, active=2)
        self.trv_matricula.append_column(column_in_out)
        renderer_in_out.connect('toggled', self.__on_treeS_toggled_active)

        ''' TreeView Cancelacion '''
        self.trv_cancelacion.set_model(self.list_cancelacion)
        # Primera columna del TreeView Cancelacion
        renderer_mat_can = Gtk.CellRendererText()
        column_mat_can = Gtk.TreeViewColumn('Materia', renderer_mat_can, text=0)
        self.trv_cancelacion.append_column(column_mat_can)
        # Segunda columna del TreeView Cancelacion
        renderer_gru_can = Gtk.CellRendererText()
        column_gru_can = Gtk.TreeViewColumn('Grupo', renderer_gru_can, text=1)
        self.trv_cancelacion.append_column(column_gru_can)
        # Tercer columna del TreeView Cancelacion
        renderer_sel = Gtk.CellRendererToggle()
        column_sel = Gtk.TreeViewColumn('Seleccion', renderer_sel, active=2)
        self.trv_cancelacion.append_column(column_sel)
        renderer_sel.connect('toggled', self.__on_list_can_toggled_active)

    def __on_dlg_about_delete_event(self, widget, otro):
        '''Evento del objeto dlg_about(Ventana About) que se ejecuta cuando
        se presiona el botón de cierre de la ventana. Este objeto activa el
        cierre de la ventana.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        *otro: Información adicional enviada.
        '''
        self.dlg_about.hide()

    def __mensaje(self, widget, mensaje):
        '''Método de la clase que permite la presentación de mensajes de
        alerta.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        *mensaje: Texto que se mostrará.
        '''
        flags = Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL
        dialogo = Gtk.MessageDialog(widget, flags, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK, mensaje)
        dialogo.run()
        dialogo.destroy()

    def __mensaje_confirmacion(self, widget, mensaje):
        '''Método de la clase que permite tomar una decisión de continuar o de
        finalizar.
        Parámetros:
        *widget: Propiedades del objeto que llamó al evento.
        *mensaje: Texto que se mostrará.
        '''
        flags = Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL
        dialogo = Gtk.MessageDialog(widget, flags, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, mensaje)
        respuesta = dialogo.run()
        res = False
        if respuesta == Gtk.ResponseType.OK:
            res = True
        dialogo.destroy()
        return res

    def __limpiar_datos(self):
        '''Método de la clase que permite reiniciar algunos objetos del
        sistema.
        '''
        ''' SECCIÓN VENTANA DE LOGIN '''
        self.cbx_tipo_usuario.set_active(-1)
        self.ent_codigo.set_text('')
        self.lbl_tip_usu.set_text('   ')
        self.ent_contraseña.set_text('')
        self.list_programa_adm.clear()
        self.list_materias.clear()
        self.list_grupos.clear()

    def __add_filtro_doc(self):
        '''Método de la clase que permite filtrar los tipos de archivos para la
        ventana de guardado de archivos.
        '''
        fft_doc = Gtk.FileFilter()
        fft_doc.set_name("Documentos")
        fft_doc.add_mime_type("text/plain")
        fft_doc.add_pattern("*.pdf")
        return fft_doc


if __name__ == '__main__':
    '''Función principal del sistema'''
    main = Troy_ctl()
    Gtk.main()
