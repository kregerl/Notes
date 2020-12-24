#!/usr/bin/python3
import notes_db
import argparse
import os
from gui import gtk
from datetime import date


class Note():
    def __init__(self, path, note):
        self.path = path
        today = date.today()
        self.unformatted_note = note
        self.note = '[{date}] {note}'.format(date=today, note=note)

def set_note(db, note):
    if isinstance(note, Note):
        db.set(note.path, note.note)
        os.system('gio set -t stringv "{path}" metadata::emblems emblem-note'.format(path=note.path))
        os.system('xdotool search --desktop 0 --class "nemo" windowfocus && xdotool key F5 ')
        print('Added note "{note}" to file at "{file}"'.format(note=note.unformatted_note, file=note.path))


def validate_args(parser, arg):
    path = os.path.abspath(arg)
    if not os.path.exists(path):
        parser.error('The file {file} does not exist. '.format(file = arg))
    else:
        return path

def handle_args(db, args):
    if args.create is None and not args.add:
        note = db.get(args.path)
        gtk.openWindow(gtk.ViewNoteWindow(note))
    elif args.add:
        gtk.openWindow(gtk.AddNoteWindow(db, args))
    elif args.create is not None:
        note = Note(args.path, args.create)
        set_note(db, note)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=lambda i: validate_args(parser, i), help='Enter a path to a file')
    parser.add_argument('-create', '-c', dest='create', help= 'Enter the note for the specified file, leaving this argument blank will get the note of the specified file.')
    parser.add_argument('-a', '--a', dest='add', help='Add a new note using the gui', action='store_true')
    args = parser.parse_args()
    db = notes_db.JsonDatabase('/home/loucas/Programs/Notes/db.json', 'NoteDatabase')
    handle_args(db, args)
