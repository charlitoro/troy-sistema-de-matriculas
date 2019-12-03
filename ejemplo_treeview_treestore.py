from gi.repository import Gtk
from gi.repository import Pango
import sys

books = [["Tolstoy, Leo", ["War and Peace", '2', False], ["Anna Karenina", '5', False]],
         ["Shakespeare, William", ["Hamlet", '3', False],
             ["Macbeth", '6',False], ["Othello", '4',False]],
         ["Tolkien, J.R.R.", ["The Lord of the Rings", '1',False]]]


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Library", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

        # the data are stored in the model
        # create a treestore with two columns
        self.store = Gtk.TreeStore(str, str, bool)
        # fill in the model
        for i in range(len(books)):
            # the iter piter is returned when appending the author in the first column
            # and False in the second
            piter = self.store.append(None, [books[i][0], '',  False])
            # append the books and the associated boolean value as children of
            # the author
            j = 1
            while j < len(books[i]):
                self.store.append(piter, books[i][j])
                j += 1

        # the treeview shows the model
        # create a treeview on the model self.store
        view = Gtk.TreeView()
        view.set_model(self.store)

        # the cellrenderer for the first column - text
        renderer_books = Gtk.CellRendererText()
        # the first column is created
        column_books = Gtk.TreeViewColumn("Books", renderer_books, text=0)
        # and it is appended to the treeview
        view.append_column(column_books)

        # the cellrenderer for the second column - text
        renderer_quan = Gtk.CellRendererText()
        # the first column is created
        column_quan = Gtk.TreeViewColumn("Quantity", renderer_quan, text=1)
        # and it is appended to the treeview
        view.append_column(column_quan)

        # the cellrenderer for the second column - boolean rendered as a toggle
        renderer_in_out = Gtk.CellRendererToggle()
        renderer_in_out.set_radio(True)
        # the second column is created
        column_in_out = Gtk.TreeViewColumn("Out?", renderer_in_out, active=2)
        # and it is appended to the treeview
        view.append_column(column_in_out)
        # connect the cellrenderertoggle with a callback function
        renderer_in_out.connect("toggled", self.on_toggled)

        # add the treeview to the window
        self.add(view)

    # callback function for the signal emitted by the cellrenderertoggle
    def on_toggled(self, widget, path):
        if len(path) == 1:
            # get the iter associated with the path
            piter = self.store.get_iter(path)
            # get the iter associated with its first child
            citer = self.store.iter_children(piter)
            # while there are children, change the state of their boolean value
            # to the value of the author
            while citer is not None:
                self.store[citer][2] = False
                citer = self.store.iter_next(citer)
            self.store[piter][2] = True
        # if the length of the path is not 1 (that is, if we are selecting a
        # book)
        elif len(path) != 1:
            # get the first child of the parent of the book (the first book of
            # the author)
            citer = self.store.get_iter(path)
            piter = self.store.iter_parent(citer)
            cs_iter = self.store.iter_children(piter)
            # check if all the children are selected
            while cs_iter is not None:
                self.store[piter][2] = False
                if self.store[cs_iter][2] is True:
                    self.store[cs_iter][2] = False
                cs_iter = self.store.iter_next(cs_iter)
            self.store[citer][2] = True
            # if they do, the author as well is selected; otherwise it is not


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
