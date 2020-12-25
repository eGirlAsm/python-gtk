import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



window = Gtk.Window(title="Hello world")
window.set_default_size(860,640)
window.set_position(Gtk.WindowPosition.CENTER)
window.show()
window.connect("destroy",Gtk.main_quit)
Gtk.main()




