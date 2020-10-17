---
title: How to save a PowerPoint or Impress presentation as a PDF with slide notes from the command line using the descendants of StarOffice; OpenOffice, LibreOffice, soffice
date: 2017-10-30
slug: pres_to_pdf_with_notes
category: Word Processing
author: ptsefton
---
tl;dr: The magic incantation you need is:

```
soffice --headless --convert-to pdf:"impress_pdf_Export:ExportNotesPages=True"  'My presentation.pptx'
```
Where 'My presentation.pptx' is the path to, you know, your presentation. It can
be in Powerpoint or OpenDocument presentation format (.odp).

It's possible to turn presentations into PDF and many other formats using the
command line, but most of the flags you need to change the behaviour of the
various converters are completely undocumented at *both* OpenOffice and the
forked project LibreOffice. I had a very hard time figuring out how to save
a presentation as PDF *with slide notes*, hence this post to help others.

*NOTE ALSO*: the result of saving a presentation as PDF with slide notes in
StarOffice derivatives is a bit odd - you get twice as many pages of PDF as you
have slides. For presentations with *p* pages the first *p* slides are the
slides without notes and the second *p* have both the slide and the notes
(unless the notes are too long in which case they are cut off). This doesn't
bother me, I don't actually want the PDF as such, I am working on a script to
turn the PDF into a series of images, extract the slide and notes text and wrap
them in a markdown document so I can publish presentations here. I'll put that
up on github soon.  If anyone knows other flags with better behaviour, then
please let me know. A complete list of conversion flags would be great, like for
example how to trigger all the HTML export options. Ta.

The key, hard to find part of this is the flag:
"impress_pdf_Export:ExportNotesPages=True".

NOTE: on some platforms the binary might be ```libreoffice``` or some other
variant rather than ```soffice```.

# To get set up OS X so you can just type ```soffice```
*  Install LibreOffice
*  Type this in a terminal:
   ```sudo ln -s  /Applications/LibreOffice.app/Contents/MacOS/soffice /usr/local/bin/soffice```
   

There's a handy tool that wraps the soffice binary called [unoconv] (installable
with brew install unoconv) that provides an abstracted interface with a few
extra features over typing ```soffice``` but [at the moment it doesn't work on
OS X](https://github.com/dagwieers/unoconv/issues/391#issuecomment-336716901)
with recent versions of LibreOffice.

[unoconv]: https://github.com/dagwieers/unoconv/
