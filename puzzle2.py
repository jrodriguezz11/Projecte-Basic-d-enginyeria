from pruebalcd import Puzzle1

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Pango

class Finestra(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="LCD_Display")
		self.set_default_size(286, 170)
		
		self.contenedor = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.contenedor)
		
		self.textview= Gtk.TextView()
		self.textview.set_wrap_mode(Gtk.WrapMode.NONE)
		self.textview.set_size_request(200,80)
		
		fuente=Pango.FontDescription.from_string("monospace 18")
		self.textview.modify_font(fuente)
		
		self.buffer= self.textview.get_buffer()
		self.textview.connect("size-allocate", self.TamanyFixe)
		self.contenedor.pack_start(self.textview, True, True, 0)
		
		self.boton=Gtk.Button(label="Display in LCD")
		self.boton.connect("clicked", self.Imprimir_LCD)
		self.contenedor.pack_start(self.boton, False, False, 0)
		
	def TamanyFixe(self, widget, allocation):
		widget.set_size_request(200, 80)
		
	def Imprimir_LCD(self, widget):
		inicio_iter = self.buffer.get_start_iter()
		fin_iter= self.buffer.get_end_iter()
		contenido=self.buffer.get_text(inicio_iter, fin_iter, False)
		contenidolisto=contenido.replace('\n', '')
		ObjetoP1= Puzzle1()
		ObjetoP1.Imprimir(contenidolisto)
		
		
	
finestra= Finestra()
finestra.connect("destroy", Gtk.main_quit)
finestra.show_all()
Gtk.main()
	
