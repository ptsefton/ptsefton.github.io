---
Title: "Don't invent your own word processing template"
Slug: dont_invent_your_own_word_processing_template
Date: 2006-01-12

---
<div>

Tim Bray [has a
go](http://www.tbray.org/ongoing/When/200x/2006/01/08/No-New-XML-Languages%20)
at convincing people not to go inventing more XML languages. He has a
point or two.

I want to add one point: don't go inventing your own styles or templates
in OpenOffice.org or Word either.

Two of five use cases presented by Tim Bray particularly interest me.
XHTML and ODF (Open Document Format).

> <span id="p-9"></span>**XHTML + Microformats** · If you’re delivering
> information to humans over the Web, even if you don’t think of it as
> “Web Pages”, it’s almost certainly insane not to use XHTML. Yes, XHTML
> is semantically weak and doesn’t really grok hierarchy and has a bunch
> of other problems. That’s OK, because it has a general-purpose `class`
> attribute and ignores markup it doesn’t know about and you can
> bastardize it eight ways from center without anything breaking. The
> Kool Kids call this “Microformats” and in fact I accidentally
> [invented
> one](http://www.tbray.org/ongoing/When/200x/2005/11/12/Resume-Blues)
> on ongoing last November; look at that template and its `class`
> attributes.[¶](http://www.tbray.org/ongoing/When/200x/2006/01/08/No-New-XML-Languages#p-9)
>
> And of course, if you use XHTML you can feed it to the browsers that
> are already there on a few hundred million desktops and humans can
> read it, and if they want to know how to do what it’s doing, they can
> “View Source”—these are powerful arguments.
>
> <span id="p-11"></span>**ODF** · Suppose you’re working with material
> that’s going to have a lot of workflow around it, and be complex,
> visually if not structurally, and maybe some day will be printed out
> and have signatures at the bottom. ODF is what you want. Not the most
> Web-oriented approach, but on the other hand the authoring tools are
> more human-friendly than anything else on this
> list.[¶](http://www.tbray.org/ongoing/When/200x/2006/01/08/No-New-XML-Languages#p-11)

> <http://www.tbray.org/ongoing/When/200x/2006/01/08/No-New-XML-Languages>

So what if you want to work with both? You want to work on complex
material, using human-friendly tools and **ODF** and you want to deliver
it to humans over the web using **XHTML**?

There's a **missing link between ODF and XHTML** which is the point of
the work we've been doing at [USQ](http://www.usq.edu.au/) on the [ICE
project](http://ice.usq.edu.au/) to build general purpose templates. We
hope to be able to better than what Tim Bray calls “Not the most
Web-oriented approach”.

Why not use microformats in ODF as well? And why not standardize on a
set of `class `attributes? (They're called `styles` in the word
processing world)

The next release of ICE, due later this month will ship with (mostly)
interoperable Word and OpenOffice templates, so you can collaborate
across platforms and applications, with a pre-built but extensible set
of styles. It will make both PDF and XTHML for your stuff and link it
all together into stand-alone packages suitable for uploading into a
learning management system. That is, you can distribute on the web in
XHTML with PDFs for individual pages and for an entire book, and still
have the more human-friendly tools with which to author. Not only that,
ICE uses [Subversion](http://subversion.tigris.org/) to look after and
version-control your content. I'll announce the new version here.

Along with generic middle of the road document formatting ICE has
experimental-stage microformats for quizzing, so you can author a quiz
using tables in the word processor and have it come out as a bit of live
interactive HTML, as well as (eventually) the IMS
[QTI](http://www.imsglobal.org/question/) quiz interchange standard.

I will add to Tim Bray's call to not invent your own XML language. I say
**don't invent your own Word / OpenDocument template** either. Start
with one that's XHTML compatible already, and help us work out some
conventions for extending the base template, by joining the
[as-yet-dormant mailing
list](http://ptsefton.com/blog/2005/12/12/ice_mailing_lists_created).
You can avoid all the [pain I described in this
article](http://ptsefton.com/blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)
about the woeful state of XHTML export from OpenOffice.org.

While ODF is a standard format, it's a very very generic one with a very
complex customization layer. To use it well in a complex workflow you
need templates, but **designing good templates is just as hard as
designing an XML language**. If you want to produce a set of consistent
documents efficiently you have to design something that deals with the
underlying document model in a simple sensible way. And while it would
be nice to assume that using ODF makes documents portable I doubt this
is the case in the short term, as new implementations will have subtle
differences in the way they handle various features and you have to
think about Word interop as well.

The lists in ODF for example, at least as implemented in OpenOffice.org
version 2, are a nightmare (and the list model is only partly
implemented by the way), but we have done all the hard work of figuring
out how to work with lists and how to do so in a way that will
interoperate with Microsoft Word.

[ICE](http://ice.usq.edu.au/) does have Windows and Mac OS X 10.4
downloads available. Get the [latest version of the application and
templates here](http://ice.usq.edu.au/browser/ice/downloads/latest/),
but it's only a version 0.2 at the moment. Try it if you're curious and
email [me](mailto:pt@ptsefton.com) if you need assistance. A few people
have downloaded it and contacted me, how are the rest of you going with
ICE?

</div>
