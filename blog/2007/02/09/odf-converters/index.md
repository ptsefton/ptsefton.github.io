---
Title: "Document converter week"
Slug: odf-converters
Date: 2007-02-09

---
<div>

[Updated this to fix up some of the more stupid sentences and add a
link, wrote it too late last night]

There are file format converters flying everywhere this week.  Jean
Hollis Weber has [a
roundup](http://www.oreillynet.com/windows/blog/2007/02/plugins_for_converting_between.html).

This is a depressing business, because none of these things ever seem to
work as promised, but here goes with an update on the ICE context.

([ICE](http://ice.ice.usq.edu.au/)is an open source content management
system that allows people to create both web and print content from a
word processor. The current version of ICE is not for the casual user,
as it requires you to install software locally but we are working on a
web-based version for more casual use, where you will be able to upload
a document and get it back as HTML and PDF.

ICE works by[using styles](http://del.icio.us/ptsefton/usestyles)in the
word processor, this means we can make really good HTML and our
documents can be moved between Microsoft Word and OpenOffice.org
writer.)

Here's my opinion on the things I've looked at.

# <span id="id917204"></span>The Open XML Translator

I've [written before](http://ptsefton.com/blog/2006/10/23/odf-plugin)
about the Microsoft-sponsored converter. It's now claiming to be version
one. I took it for a another spin. This is a Windows-only Word plugin
backed by an open source engine that should run elsewhere.

First of all you need to install the Office computability updates so
that your old version of Word can read and write OOXML files. Then you
can [install this
plugin](http://sourceforge.net/projects/odf-converter).

The good

:   -   A superficial look shows that it actually imports ICE documents
        reasonably well into Word.

    -   It uses XSLT to do the conversion so maybe we could hack a
        custom version to work in our environment.

The bad

:   -   It uses XSLT so it is glacially, agonizingly slow, like ICE used
        to be until we rewrote the converter.

    -   Import and export is only superficially good. For example
        complex lists set up in Writer look OK when imported into Word,
        but the list style information (as opposed to the paragraph
        style) is missing. We know how to fix this in iCE, but you'd
        need to run a macro on each import to re-establish styles.

        Same goes the other way round. Word list styles are dumped on
        export, but because we use redundant paragraph and list styles
        the ICE document repair function could fix things automatically.

    -   It's really annoying because it can only import and export.
        There's no opening an ODF document editing and saving, you have
        to save to OOXML first, then export. That alone would stop us
        from using it with ICE, where we'd love to have Word users
        working in ODF.

This thing confirms what I've been saying for the last few years. [Use
styles](http://del.icio.us/ptsefton/usestyles). If you use styles then a
document can be repaired even though ODF and OOXML have incompatible
list structures that do not map to each other.

## <span id="id920383"></span>Verdict

This could be used in a style-driven system like ICE, but we would
probably ditch the Word plugin part and just use the XSLT translation.
That is, users would use Word's OOXML format.  If we add some
refinements and fix-ups based our set of styles then we may even be able
to round-trip documents in and out of OOXML, something we don't try to
do now.

The XSLT is really going to hurt adoption of this thing, though, because
of the slooow speed.

# <span id="id920415"></span>The Open Document Foundation's ACME376 plugin

I wrote about the the Open Document Foundation's [outlandish
claims](http://ptsefton.com/blog/2006/05/11/a_word_plugin_for_opendocument%3F_maybe.)
about a magic way of saving Word documents into ODF last year.

I had someone at the mysterious 'foundation' contact me and offer to let
us participate in a Beta program if we signed an NDA. I wouldn't have
signed, but I heard nothing more. Obviously **anyone who has tried this
thing has done so is still under an NDA** 'cos there's still no usable
information on their file format converter.

A new [download
page](http://opendocument.foundation.googlepages.com/home) promises a
proof of concept. The installer doesn't work for me, and there are no
contact details on the page. I note with amusement that the Open
Document foundation still doesn't seem to have sorted out its web
hosting, this one is a googlepage.

There's something odd about this proof of concept.

> ACME 376 XML files are XML encoded RTF files. The ACME 376
> Compatibility Kit is a demonstration of the power of our da Vinci
> conversion engine, which is currently being re factored to comply with
> ODF v. 1.2.  A [da Vinci
> demonstration](http://fussnotes.typepad.com/fr0mat/2006/07/plugin_transpar_1.html)
> walk through is available at Fr0mat.  A demo that might prove helpful
> with ACME 376 installation and use.

What is this meant to show? That you can hack word to save to RTF then
wrap \<xml\> tags around it? Thanks Open Document Foundation. By the
way, the promised 'walkthrough' is a single screenshot.

There is now a [blog](http://fussnotes.typepad.com/fr0mat/), where there
are a smattering of long, rambling often incoherent posts about this *da
Vinci* technology. They seem to be saying that they map Word's internal
binary structure onto ODF and anything that doesn't fit into this
structure is saved as foreign XML <span class="spCh spChx2013">–</span>
I get the impression that ODF documents created this way don't
interoperate with other word processors, there's a defensive comment
about the target being Word fidelity.

I wonder if the ODF converter form last year was just saving as RTF then
wrapping the RTF in an OpenDocument wrapper?

## <span id="id916733"></span>Verdict

I am increasingly inclined to treat this is an elaborate joke. Wake me
up when there's some real code to try out.

# <span id="id916771"></span>Sun's Word plugin

Sun [announced a Word
plugin](http://blogs.sun.com/webmink/entry/sun_announces_odf_plug_in)
based on OpenOffice.org code. See a discussion between me and the author
in the comments section.

This will allow word users to save to ODF directly. While Simon Phipps
is enthusiastic about using OOo's in-built Word conversion the catch is
that this system is going to inherit all of Writer's current
limitations.  

One big question occurs to me: what will happen to EndNote citations in
Word?

## <span id="id924965"></span>Verdict

Too early to tell, but I'm interested to try this out. It may be that
Word users would get used to the converter, and work around the
limitations.

On the ICE project we currently have to repair ODF documents after they
have been round-tripped in and out of Word, so I guess we could do that
as an adjunct to the converter. I think that adding a macro that runs
automatically when you open an ODF document in Word would end up being a
lot faster than using the Open XML translator; but I can't tell you yet
which one will have better fidelity.

</div>
