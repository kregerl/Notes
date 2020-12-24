#!/usr/bin/python3
import notes
import textwrap
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def openWindow(win):
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


class AddNoteWindow(Gtk.Window):
    def __init__(self, db, args):
        Gtk.Window.__init__(self, title="Add Note")
        self.set_size_request(400, 100)
        self.db = db
        self.args = args

        container= Gtk.Fixed()
        self.add(container)

        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.submit)
        self.entry.set_placeholder_text("Add Note")
        self.entry.set_width_chars(45)
        container.put(self.entry, 10, 10)

        self.button = Gtk.Button(label="Add Note")
        self.button.connect("clicked", self.button_submit)
        container.put(self.button, 305, 40)

    def submit(self, entry):
        note = notes.Note(self.args.path, entry.get_text())
        notes.set_note(self.db, note)
        self.destroy()

    def button_submit(self, button):
        self.submit(self.entry)

class ViewNoteWindow(Gtk.Window):
    def __init__(self, note):
        Gtk.Window.__init__(self, title="View Note")
        self.set_size_request(200, 100)

        container = Gtk.Fixed()
        self.add(container)

        self.label = Gtk.Label(textwrap.fill(note, width = 75))
        self.label.set_margin_right(10)
        container.put(self.label, 10, 10)

