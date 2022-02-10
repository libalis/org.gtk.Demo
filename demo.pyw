#!/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
textview = Gtk.TextView()

window.set_title("GTK+ Demo")
window.set_default_size(1280, 720)
window.set_default_icon_name("application-x-executable")

window.add(textview)

window.set_position(Gtk.WindowPosition.CENTER)
window.set_resizable(False)
window.set_focus()

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
