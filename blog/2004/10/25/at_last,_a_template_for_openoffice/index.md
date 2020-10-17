---
Title: "At last, a template for OpenOffice.org"
Slug: at_last,_a_template_for_openoffice
Date: 2004-10-25

---
As promised, but very late, here's a [template for
OpenOffice.org](2004/wp-interop-0-1.stw), as part of the [Word Processor
Interoperability project I'm
slowly](blog/2004/08/16/wordprocessorinterop) chiseling out of a block
of mud. This implements the [styles](http://ptsefton.com/style-basics),
give or take a few. The idea is that if you use this template you will
be able to (a) generate good XHTML (once there is an output stylesheet)
for your blog, your intranet, your website or whatever, and (b)
inter-operate with Microsoft Word, using the same names for things. This
is version 0.1, not finished, but usable.

Updated with a couple of corrections 2004-10-28

In this release I have changed the name of list
[styles](http://ptsefton.com/style-basics) from 'l' to 'li', and
ommitted the 'start' versions of styles to force numbering to 1 as they
don't work in OO.o (they may need to go back in for interop with Word)
but otherwise implemented them as promised. Still to come:

-   Metadata styles (there's a title style and nothing else).
-   A menu to apply the styles, with 'Alt' (maybe this is called 'Meta'
    in Unix?) key combinations to apply them.
-   Stylesheets to turn your docs into XHTML, and
-   a way to apply the stylesheets.
-   Outline numbering for h1\# et al. (There appears to be a bug in OO.o
    that doesn't allow you to save changes to the outline numbering with
    a document or template).
-   Definition lists.

What to do to get it?

[Download the template](2004/wp-interop-0-1.stw) and put it in your
templates directory. If you're not sure where that is, look in |Tools /
Options... / Paths / Templates| in OO.o, and pop it in one of the
directories listed there. Then you can make new docs by via |File / New
/ Templates and Documents|.

You will need to customize the look of the thing for your environment,
of course. I'll publish more soon on good ways of hacking OO.o templates
by busting open the |.stw| file and fiddling with or transforming the
XML found therein.
