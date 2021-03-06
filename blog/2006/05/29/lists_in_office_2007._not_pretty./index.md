---
Title: "Lists in Office 2007. Not pretty."
Slug: lists_in_office_2007._not_pretty.
Date: 2006-05-29

---
<div>

I [wrote recently](http://ptsefton.com/blog/2006/05/11) that Word does
not have list styles, while OpenDocument does. Actually, I know better
than that. Word does have list styles, or at least named list formats,
it's just that you **can't apply them in any sensible way**, even in the
recently released beta version of Word 2007.

[UPDATE: I have not been paying attention to a feature introduced in
Word 2003 (or XP?). This is because the ICE template bypasses all the
mess described below. In what follows I have confused List styles (a
Word 2003 feature I never noticed) with named outline lists. List styles
are linked to named outline lists in some way, and while both have names
they can be different). If you define a list syle (as opposed to a named
list outline then you can get back to it via the styles menu, although
Word 2007 Beta 2 seems to have a few bugs and does not show the list
styles everywhere.]

This is a great time to talk about lists, as Brian Jones has just
[thrown](http://blogs.msdn.com/brian_jones/archive/2006/05/26/607630.aspx)
a couple of rocks in the direction of the OpenDocument specification and
its lack of internationalization (well aimed, I
[gather](http://www.oreillynet.com/xml/blog/2006/05/open_xml_at_iso_sideshow.html)).

(Me, I think that Microsoft's approach to managing lists at the file
format level is probably better that OpenDocument's. Word doesn't
introduce any extra structure for lists. Paragraphs just carry some
pointer information back to a list definition, while OpenDocument has an
ill-conceived nested-list structure that coexists very uneasily with the
paragraph-based interface. Word can also associate a paragraph style
with a particular level in an named list and that works pretty reliably.
The same cannot be said for OpenOffice.org working with OpenDocument.)

But format-wars aside the **user interface to access lists** in Word has
been woeful since Word '97. That's ten years of virtually unusable
functionality that looks set to continue.

Here's my so stupid it's funny list story. It's timelessly funny too,
because you can play the same trick in Word 2007. Timeless as measured
in Internet years, anyway.

Circa 1997 I was working with Standards Australia, using Microsoft Word
97 to build a template-driven publishing system. That package had a new
way of creating multi-level lists called Outline lists.

**Outline lists were very unstable** in Word 97. Sometimes a small,
innocuous seeming change to the document would make numbering go crazy
and sometimes you'd to go back and repair the lists you had carefully
set up and named. Only you can't, because from 1997 to 2003 the
interface for selecting the things was a 'gallery' with seven choices.
If you happened to want to get back to a previously-defined list then
you had no way to do it unless you were lucky enough to find a paragraph
that used the list style. Word also gives you helpful messages like 'An
outline with that name already exists' when you have made no changes to
anything.

I'll say this again. While you can name an outline, there is no way in
the interface to get back to it to change it, or reapply it. Even in the
very latest versions of Word (including version 2007 – I just checked,
more below) the outline dialog gives you a **choice of seven outlines**,
and if the one you want is not showing, then you can neither use it nor
edit it. Not that you can see the name of a list in the gallery without
opening it up, anyway.

This is one the **worst bits of interface design in the history of
computing**.

In the end at Standards we decided to write macros to set and repair
outline lists. These macros live on in the [ICE
templates](http://ice.usq.edu.au/svn/ice/downloads/latest/templates/).
Using Word's macro language you can create an outline, set it up to look
the way you want and link it to a set of paragraph styles. When things
go awry then you just re-run the macro.

Great stuff, and it made for a fairly stable working environment that
has served several organizations well. Once we had the macro I stopped
worrying about the lists and got on with using Word.

Here's the funny part. As part of the work on the list fixup macro, I
thought I'd see if there was a limit to the number of lists you could
create. So I wrote a macro to create a thousand or so named outlines,
then delete them. My recollection is that the delete method silently,
happily, did nothing. Nothing as in; didn't fail and didn't delete. My
recollection could be wrong, but in the result was a document with lots
of named outlines List1 ... List1000.

Next, I must have accidentally saved all those lists into a template.
And a I gave the template to other people to test having no idea of what
lay within.

Oops, new documents created from the infected template ran to about a
megabyte of RTF, even empty. In those days that was a biiiiig document,
and if you tried to load it, it would crash Word. We relied on RTF to
drive an SGML converter.

This was my Denial of Service attack, *Death by Outlines* for Word. I
never unleashed it on the world, though.

The only fix once you had saved an infected document out as RTF was to a
use a Perl script to remove the offending list definitions. Eventually
we got rid of the infection. And eventually I went through the
extraordinary pain of reporting the issue to Microsoft.

So what's happened in Word 2007?

The interface has changed a bit, but it is still a gallery with no way
to select a particular list you may have defined.

There is one interesting button that should be changed. It's labeled
'Define New Multilevel List'. This had me confused until I worked out
that it actually functions to change the list you're already clicked in.
Of course.

Still no way to get back to a list you created that does not happen to
be showing in the gallery, though. You'd think that something that lets
you define named lists would at least **GIVE YOU A LIST OF THEM.**

There's another tempting new button in Word 2007 called
`Define New List Style`. Same issues apply. [UPDATE: I made a mistake,
list styles are different from the names on outline numbered lists]

I did a bit more investigation of Word 2007. Wrote a macro like this
one, to make lots of lists called `FindThis 1`... `FindThis 100`:

    Sub makeLotsOfLists()
     For i = 1 To 100
     Set NewList = ActiveDocument.ListTemplates.Add(OutlineNumbered:=True, Name:="”FindThis" + Str(i))
    Next

The 'good' news is that now Word has a zipped XML file format just like
OpenDocument, so I could unpack the .`docx` file and find my 100 list
definitions in nice neat XML in the `numbering.xml` file.

The bad news is that there is still no `Remove` or `Delete` method on
`ListTemplates`, that I can see, to go with the `Add`. So if you wanted
to be mean, then you could run a macro like this to silently use up
space in a user's document and they'd have no clue from the **cruel joke
of an interface** what was up. Given the efficiency of the zipped format
you might need to set the number a bit larger than 100.

Lol.

Looks to me like all the work on the new version of word has gone into
the bottom (file formats) and the top (interface). Given that the former
will be available for (licensed) old versions I'm not sure that there's
much of interest for the projects I work on, but I'll have a think about
that.

</div>
