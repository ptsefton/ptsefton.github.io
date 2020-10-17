---
Author: ptsefton
Comments: true
Date: 2008-05-13 06:42:39+00:00
Slug: more-on-odf-and-ooxml

Title: More on ODF and OOXML
Wordpress_id: 116
---

<div>

<div class="page-toc">

-   [Updated converter table](#id1)
-   [Revised view: how well does the ODF add-in work?](#id2)

</div>

<div>

I posted yesterday about [document formats and
applications](http://ptsefton.com/2008/05/12/some-comments-on-ooxml-odf-and-microsoft-word.htm).

Today a couple of additions and a correction.

I left the Sun ODF plugin for Microsoft Word off the list. So here's an
update of my summary table. I have not been able to test it yet.

# <span id="id1"></span><!--id1--></a>Updated converter table

All the converters here apart from the last two are using the same
technology: [ODF Add-in for Microsoft Word, Excel, and
PowerPoint](http://odf-converter.sourceforge.net/)

<div class="Table48"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------+--------------------------+--------------------------+
| Platform                 | Application              | What does it do?         |
+--------------------------+--------------------------+--------------------------+
| Windows                  | ODF in Microsoft Word    | The ODF add-in will read |
|                          | 2003+                    | .odt files and turn them |
|                          |                          | into .docx. It's slow.   |
|                          |                          |                          |
|                          |                          | (I couldn't make it run  |
|                          |                          | on my version of Word    |
|                          |                          | 2007 because of what I   |
|                          |                          | think are conflicting    |
|                          |                          | versions of .NET)        |
+--------------------------+--------------------------+--------------------------+
| Windows / Linux          | OOXML in OpenOffice.org  | [OpenOffice.org          |
|                          | or another ODF aware     | Ninja](http://katana.ooo |
|                          | application (but see     | ninja.com/w/odf-converte |
|                          | below <span              | r-integrator);           |
|                          | class="spCh spChx2013">– | a little program that    |
|                          | </span>                  | intervenes when you      |
|                          | are there any?)          | click on a .docx file    |
|                          |                          | and converts it it .odt, |
|                          |                          | slowly.                  |
+--------------------------+--------------------------+--------------------------+
| Windows / Linux          | OOXML in [Novell's       | Uses the ODF Addin and   |
|                          | version of               | allows you to edit a     |
|                          | OpenOffice.org           | .docx file. Open and     |
|                          | writer](http://www.novel | save are, you guessed    |
|                          | l.com/products/desktop/f | it, slow.                |
|                          | eatures/ooo.html)        |                          |
+--------------------------+--------------------------+--------------------------+
| Mac OS X                 | Microsoft Word           | Currently no options for |
|                          |                          | reading ODF AFAIK        |
+--------------------------+--------------------------+--------------------------+
| Mac OS X                 | NeoOffice                | Contains a the Novell    |
|                          |                          | plugin, so you can open  |
|                          |                          | and save .docx files     |
|                          |                          | (slowly, of course).     |
+--------------------------+--------------------------+--------------------------+
| Windows, OS X, Linux     | OpenOffice.org Writer    | Contains a new different |
|                          | version 3 (currently in  | converter which is much  |
|                          | beta)                    | faster than the ODF      |
|                          |                          | add-in. But Sun are not  |
|                          |                          | aiming to provide        |
|                          |                          | round-trip editing of    |
|                          |                          | .docx files. This is     |
|                          |                          | intended to be an import |
|                          |                          | filter only. (Not based  |
|                          |                          | on the ODF add-in        |
+--------------------------+--------------------------+--------------------------+

</div>

<div class="Table49"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------+--------------------------+--------------------------+
| Windows                  | ODF in Microsoft Word    | Sun's [ODF plugin for    |
|                          |                          | Word](http://www.sun.com |
|                          |                          | /software/star/odf_plugi |
|                          |                          | n/get.jsp).              |
|                          |                          | (Uses StarOffice code)   |
+--------------------------+--------------------------+--------------------------+

</div>

# <span id="id2"></span><!--id2--></a>Revised view: how well does the ODF add-in work?

Yesterday [I
wrote](http://ptsefton.com/2008/05/12/some-comments-on-ooxml-odf-and-microsoft-word.htm):

> You know, I'm pleasantly surprised to to be reporting that using
> NeoOffice on the Mac a complex ICE test document seemed to round trip
> from Neo to Word 2008, where I made a few changes and then back to Neo
> with no visible problems. This ODF add-in thing has improved a lot
> since [the first time I tried
> it](http://ptsefton.com/blog/2006/10/23/odf-plugin/).

I was a bit hasty there. I tried again with an ICE sample document
saving it as .docx and reloading it. Most of the formatting is fine,
with a few oddities in the numbering but styles support is very very
lacking.

The biggest issue is that list styles get lost and the associated
paragraph style is kept in the OOXML but none of its formatting is
specified. The result is a document which looks like it is using styles
but actually isn't really doing so 100%.

This is not that big a problem if you are using a known stylesheet like
we do with [ICE](http://ice.usq.edu.au/). We have the style name so we
can write macros or file-fixers to go through the document and repair it
up so that it does styles again. We already have a list-repair macro for
Word and there's code for Writer to create new styles so this should be
doable. Who knows, we may even be able to help fix the ODF addin
converter.

This is the point of the work we've been doing <span
class="spCh spChx2013">–</span> to make sure that our users can have
interoperable portable documents. I recommend checking these converters
with documents from your own environment before trusting them.

We can report this issue and maybe look into helping with the converter.
Daniel? You listening?

</div>

</div>
