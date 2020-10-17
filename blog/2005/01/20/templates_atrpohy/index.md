---
Title: "Templates atrophy in Microsoft Word"
Slug: templates_atrpohy
Date: 2005-01-20

---
To use a word processor sensibly you *need* templates (OK, unless
everything you write is a one-off). I'm not sure if this is planned or
not, but in Microsoft Word, using, installing and maintaining templates
has been getting steadily more difficult, as they have been buried under
the operating system and changes in the Word application. My comments
here apply to Windows versions. Dunno about the Mac, yet.

Two things have happened to make templates recede from view:

-   Changes to the operating system mean that the folder in which
    templates are stored by default is not visible by default, so it's
    pretty hard to send someone a template and tell them where to put
    it.

<!-- -->

-   Word 2003 has moved templates 'down the menu', to the point that you
    really have to look hard to find them.

Result?

Fewer people are going to stumble on templates like I did twenty years
ago, and casual users are likely to give up using them.

More discussion about the details follows. Oh, and OpenOffice.org isn't
too great in this department either. So lets think about how a
well-executed template system would work, and write it up.

The first blow to templates came when Windows started hiding system
folders, including the "Documents and Settings" folder for user
profiles, where templates are stored.

When distributing templates we used to write documentation that
instructed users to look in Tools / Templates and Add-Ins... to find the
path Word uses to store templates, then copy the template to that
directory. Since at least Windows 2000, they can't even *see* the
default directory from the Windows Explorer, so these instructions
became too hard to follow. At NextEd, where our publishing system
depended on templates, the final, alarming, solution, was to write an
installer macro that attempts to write the template into the correct
directory when you open it, if you choose to trust the process and allow
macros to run, which you really shouldn't. Why is this *so* hard?

Writing this, I got to wondering what current Microsoft documentation
has to say about installing templates.

> To check your template file location settings, click Options on the
> Tools menu, and then click the File Locations tab.

Ok, but that doesn't actully show you the path, it gives you a file
dialogue, where you can work out the path if you know how. And:

> Save your custom templates in the Templates folder. Template files
> that you save in the Templates folder appear in the Templates dialog
> box, which you display by clicking New on the File menu, and then
> clicking On my computer in the New Document task pane. Any document
> (.doc) file that you save in the Templates folder also acts as a
> template.

But if the folders are hidden how 'do' you Save your custom templates in
the Templates folder?

There's more, but it's too depressing to go into the details.

The second blow, which may just kill off templates as we know them,
comes in Word 2003, which has replaced some of its dialogs with a "Task
Pain", er "Task Pane". This is what happened to me yesterday:

Me: File / New.

XP: \<apperently nothing\>

Me: File / New.

Me: Oh, there is something. There's a new toolbar thing (called a "Task
Pain", er "Task Pane") on the right of the screen.

This varies between versions but the task pane has this structure,
starting with a generous offer not to open a new document, but open one
of the ones I just closed.

#### Open a document

    Doc 1
    Doc 2
    Doc 3
    Doc 4
    Doc 5
    Doc 6
    Doc 7
    Doc 8
    Doc 9
    More documents...

#### New

#### New from existing document

    Choose document

#### New from Template

    My template
    My other template

So, when I ask for new document, I am offered old ones first, followed
by 'blank' ones, followed by cloning an existing document, followed,
finally, if I have read that far and the window is big enough, creating
a document from a template.

I assume that Microsoft engineers have done this based on the frequency
with which templates get used, according to their research, although I
can't believe that usability labs show that this Task Pane idea is
better than a dialog box. And because I am now an infrequent user of
Word, thanks to OpenOffice.org, I am intially left staring at the place
the dialog should be when I try to open a new document in Word, until I
remember to look to the right.

I suppose that this is *not* a plot to kill off templates but it *is*
one more reflection of the way software companies do business. They sell
on features and demos to the people who do the buying. The Task pane is
apparently a 'feature', even though it interacts strangely with the help
system, and clutters up the screen.

And there is no way they are going to do something like make templates
more prominent rather than less, even though for many enterprises,
including one-person ones, that would be a better way to work.

Imagine the paper clip popping up with "It looks like you're using this
computer like a glorified typewriter, would you like to systematize your
work? Become more efficient? Improve the consistency of the image you
project? Make your documents more usable?".

\$LastChangedDate\$
