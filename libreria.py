from gui import DjangoServidor
from gi.repository import Gtk

class Libreria_App(Gtk.Window):
	
	server_django = DjangoServidor.DjangoServidor()
	
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("gui/main_window.glade")
		self.window =  self.builder.get_object("window")
		self.window.connect("delete-event", self.on_window_close)
		self.window.show_all()
		
	def on_window_close(self, widget, event):
		Gtk.main_quit()
		

if __name__ == "__main__":
	try:
		a=Libreria_App()
		Gtk.main()
	except KeyboardInterrupt:
		pass
