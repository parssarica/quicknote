# Quicknote
Note: This program only works in UNIX based systems (Linux, MacOS and BSDs).<br><br>
Quicknote is a note program. You tag notes, search with tags. It's a terminal program, you run this program from terminal. Here is how you can use it:

## Getting help in offline

Quicknote comes with a help. You can see it in 3 ways:

`quicknote`<br>
`quicknote -h`<br>
`quicknote --help`<br>

## Creating notes

You can create notes by running:

`quicknote -n` or `quicknote --new`
It will ask you some questions:

`Title of note: Example`<br>
`Content of note: example.com is an example site.`<br>
`Tag 1: example`<br>
`Tag 2: example.com`<br>
`Tag 3:`<br>
If you press enter without writing, it will end asking tags.

## Searching notes

You can search notes by running:

`quicknote -s` or `quicknote --search`
It will ask you a tag name:

`Write a tag: example`<br>
It will show you all notes that has the tag 'example'.

## Viewing all notes

This may be the easiest feature. You can run it by:

`quicknote -a` or `quicknote --all`<br>
It won't ask you questions.
>Example
>
>example.com is an example site.<br>
>ID of note: 1<br>
>All tags belonged to this note:<br>
>example<br>
>example.com<br>
>\-----------

## Viewing a specific note

To view a specific note, you should run this:

`quicknote -v` or `quicknote --view`

It will ask you the ID or the title of note you want to view:

`Enter the specific note's title or ID: 1`

This will show:

>Example
>
>example.com is an example site.<br>
>ID of note: 1<br>
>All tags belonged to this note:<br>
>example<br>
>example.com<br>
>\-----------

It will also show the same result if you enter that note's title.
But it will say 'Note not found' there isn't a note that has the ID you entered or the title you entered.

## Deleting notes

You have to be careful with this ability. You can't get back the notes you deleted unless you have a backup. You can delete notes by:
`Enter the note's ID that you want to delete: 1`
You won't be able to see this note. For example:
> quicknote -v<br>
> Enter the specific note's title or ID: 1<br>
> Note not found.

Same in all command.

## Editing notes

If you forgot something to write while you were creating a note, you can edit by this feature. You can use it by:

`quicknote -e` or `quicknote --edit`

It will ask you:

>Enter the note's ID that you want to edit: 1<br>
>example.com is an example site.<br>
>New content (Press enter to pass): example.com is an example site and a cat is a cat.<br>
>Do you want to add more tags (Press any key else enter to decline):<br>
>Tag 3: cat<br>
>Tag 4:<br>

When you view the note from view or all commands, you would see the new content. You will also see this if you search the tag cat.

### The command 'quicknote' not working

Quicknote wouldn't run if you didn't create a symbolic link. You can create it easily by:
>chmod +x quicknote.py;sudo ln -s \`pwd\`/quicknote.py /usr/local/bin/quicknote<br>
>\[sudo] password for quicknote:<br>

After you enter your password, run this command:

>pip install -r requirements.txt<br>

Pars SARICA
