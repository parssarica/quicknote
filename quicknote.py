#!/usr/bin/python3

from peewee import *
import sys
import os

help = """Usage: quicknote [OPTIONS]

Quicknote is a command line application for taking notes. In quicknote, you add tags to notes so you get all notes about searched tag in quicknote.

Options:
    -h | --help:   Shows this help message and exit.
    -n | --new:    Creates a new note.
    -s | --search: Searches notes with a tag.
    -a | --all:    Shows all notes.
    -v | --view:   Shows a specific note.
    -d | --delete: Deletes notes.
    -e | --edit:   Edit notes.
"""

create = False
if not os.path.exists(os.environ["HOME"] + "/.config/quicknote"):
    os.mkdir(os.environ["HOME"] + "/.config/quicknote")
    create = True
db = SqliteDatabase(os.environ["HOME"] + "/.config/quicknote/quicknote.db")


class BaseModel(Model):
    class Meta:
        database = db


class Note(BaseModel):
    note_title = CharField(unique=True)
    note = TextField()
    tags = TextField()


db.connect()
if create:
    db.create_tables([Note])

def new():
    uniquetitles = [""]
    while len(uniquetitles) != 0:
        title = input("Title of note: ")
        uniquetitles = Note.select().where(Note.note_title==title)
        if len(uniquetitles) != 0:
            print("There is a note that has the same title.")
    content = input("Content of note: ")
    tags = []
    tag = " "
    i = 1
    while tag != "":
        tag = input(f"Tag {i}: ")
        if tag == "":
            continue
        tags.append(tag.replace(" ", "_"))
        i += 1
    tags = " ".join(tags)
    Note.create(note_title=title, note=content, tags=tags)


def search():
    tag = input("Write a tag: ").replace(" ", "_")
    total_notes = []
    for note in Note.select():
        if tag not in note.tags.split(" "):
            continue
        total_notes.append(note)
        print(note.note_title)

    if len(total_notes) >= 1:
        print("Press D to see the notes' contents.")
        print("Press any key else to quit.")
        choice = input("").lower()
        if choice == "d":
            for note in total_notes:
                print(note.note_title)
                print()
                print(note.note)
                print(f"ID of note: {note.id}")
                print("All tags belonged to this note:")
                print(note.tags.replace(" ", "\n").replace("_", " "))
                print("-----------")
    else:
        print(f"There isn't any notes that include '{tag}' tag.")


def allnotes():
    notes = Note.select()
    if len(notes) == 0:
        print("You didn't create any notes yet. You can create one by running 'quicknote -n'.")
        return

    for note in notes:
        print(note.note_title)
        print()
        print(note.note)
        print(f"ID of note: {note.id}")
        print("All tags belonged to this note:")
        print(note.tags.replace(" ", "\n").replace("_", " "))
        print("-----------")


def view():
    choice = input("Enter the specific note's title or ID: ")
    try:
        note = Note.select().where(Note.id == int(choice))
    except:
        note = Note.select().where(Note.note_title == choice)

    try:
        note = note[0]
    except:
        print("Note not found.")
        return
    print(note.note_title)
    print()
    print(note.note)
    print(f"ID of note: {note.id}")
    print("All tags belonged to this note:")
    print(note.tags.replace(" ", "\n").replace("_", " "))
    print("-----------")


def delete():
    id = input("Enter the note's ID that you want to delete: ")
    try:
        note = Note.get(Note.id == id)
    except:
        print("Note not found.")
        return
    note.delete_instance()


def edit():
    id = input("Enter the note's ID that you want to edit: ")
    try:
        note = Note.get(Note.id == id)
    except:
        print("Note not found.")
        return
    print(note.note)
    content = input("New content (Press enter to pass): ")
    choice = input("Do you want to add more tags (Press any key else enter to decline)?")
    tags_new = []
    if choice == "":
        tag = " "
        tags = note.tags.split(" ")
        i = len(tags)
        while tag != "":
            tag = input(f"Tag {i}: ")
            if tag == "":
                continue
            tags_new.append(tag.replace(" ", "_"))
            i += 1

        for tag in tags_new:
            tags.append(tag)

    if content == "" and tags_new == []:
        print("You didn't edit anything.")
        return

    if content != "":
        Note.update(note=content).where(Note.id == id).execute()
        if tags_new != []:
            Note.update(tags=" ".join(tags)).where(Note.id == id).execute()
    else:
        Note.update(tags=tags).where(Note.id == id).execute()


if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
    print(help)
    sys.exit()


for argument in sys.argv:
    if argument == "-n" or argument == "--new":
        new()
    elif argument == "-s" or argument == "--search":
        search()
    elif argument == "-a" or argument == "--all":
        allnotes()
    elif argument == "-v" or argument == "--view":
        view()
    elif argument == "-d" or argument == "--delete":
        delete()
    elif argument == "-e" or argument == "--edit":
        edit()
    else:
        continue
