---
Title: "XHTML as a word processing format"
Slug: futureoffice
Date: 2004-08-09

---
I have been thinking about Tim Bray's [plaintive plea for an XHTML-based
word
processor](http://www.tbray.org/ongoing/When/200x/2004/07/20/AuthoringPain).
I started writing down the requirements, looking at features that would
need to be in and out of such a product, but I reached the conclusion,
eventually, that any attempt to write yet another word processor will
end up (a) as a niche product for some corner of the web, or (b) turn
into another office suite, and therefore not happen. These ruminations
led me to my post on the [benefits of blogging
software](http://localhost:8000/blog/2004/08/02/the_best_thing_about_blogs),
about how blogs implement the separation between content and
presentation/navigation. That is, blogging and some Content Management
System, (CMS) software lets you author pages without all the wrapping
that makes the content into a web site.

I have decided the way forward is to adapt the existing leading word
processors using their programmable interfaces (APIs), their template
and style systems, and their macro languages that make them
programmable.

Tim Bray has updated his post to include some feedback that
OpenOffice.org is the product to do this:

> [Geof Glass](http://www.geof.net/blog/index.html) says: “I think you
> answered your own question about a good HTML content authoring tool
> some time ago - it’s a standard XSLT export filter for Open Office.
> The OO.o tags are close to XHTML so transformation is easy (though I
> haven't done tables). It separates content and style - which is
> essential. And for non-web distribution you aren't bound by the
> limitations of the web (e.g. problems with paged media in existing CSS
> implementations).” [Mark
> Hughes](http://kuoi.asui.uidaho.edu/%7Ekamikaze/read.php?topic=News&id=14)
> would agree.

I agree, provided the export filter for OpenOffice.org can export
images. But I don't think it's just OO.o that's a contender. MS Word (is
that MS.W?) can be made to export to XHTML, probably with less work than
OO.o. Next step would be to set up common style names between the two of
them with base styles that map to HTML elements, and some domain
specific sets of styles and conventions (the conventions are for when we
reach the limits of styles). I have a fair bit of experience in this
matter, so as of tonight, I am beginning a series of small articles that
work through the design of such a system.

I think a well thought-out set of styles and some macro/API work in both
packages will result in a really useful constellation of opportunities,
including the ability to edit documents in your geek-tool-of-choice,
such as Emacs and use OpenOffice to render nice print, and to generate
Word documents that lesser mortals, such as lawyers, can edit and give
back to you. The key to all of this is to interface to some kind of
Content Management System that knows how to accept content into a
scalable website without the author doing DreamWeaver or FrontPage style
site management. The obvious protocol for this will be Atom - if it ends
up with the required scope.

At this stage I think that there are really only two contenders for
existing word processors. MS.W and OO.o. (and yes I have chased down
lots of the links that sprouted from Tim Bray's post, and visited lots
of interesting places), although it occurred to me today that
WordPerfect ought to be in there too; it's also mature and even has an
inbuilt XML editor. I have downloaded the trial, to have a play. At this
stage the XML support looks just like the SGML support I remember from
five-ish years ago — that is frustratingly close to useful. We'll see.

Maybe a new XHTML based word processor application *will* emerge from
the recent discussions, but I'm not holding my breath. I'll keep an eye
on [this site, dedicated to the idea of a XHTML + CSS for word
processing](http://muux.com/wp/pages/Discussions%20elsewhere), which
links back here.

Finally, I include here my draft notes on the feature set that needed to
be in a new Word processor, even though I am now going to forget about
this and work on adapting the *old* ones.

This new word processor needs to:

-   Be usable for print as well as web, not necessarily optimised, but
    ''usable' - certainly needs to be able to make PDF.

<!-- -->

-   Have a default drawing (and maybe paint) package included. And this
    will lead to spreadsheets and presentation (PowerBloodyPoint) as
    well, you mark my words.

<!-- -->

-   Have the usual spelling checker and styles (which would map directly
    to CSS, of course).

<!-- -->

-   Be able to import the common word processing formats with (at least)
    the text and tables intact. It would be nice to map existing styles
    to CSS and to HTML elements.

<!-- -->

-   Be able to tidy existing HTML resources.

<!-- -->

-   NOT be able to export in common word processing formats. Think about
    it.

<!-- -->

-   Use an Atom (or other) repository in preference to the file system.

<!-- -->

-   Have file / FTP / WebDAV export.

<!-- -->

-   Most emphatically NOT have DreamWeaver or FrontPage-like ability to
    mange entire webs - this will be the task of the Atom (or other)
    repository.

<!-- -->

-   Ship with an inbuilt set of classes for semantic markup.

