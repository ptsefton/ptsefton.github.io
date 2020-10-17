---
Title: "Bibliographic Software: a biased summary"
Slug: bibliographic_software:_a_biased_summary
Date: 2006-03-13

---
<div>

In February, Cameron Loudon (RUBRIC communications person and fellow
NextEd roadkill) and I dropped in to
[MELCOE](http://www.melcoe.mq.edu.au/) at Macquarie Uni to talk to James
Dalziel and Eric Vullings; we told them a bit about
[RUBRIC](http://www.rubric.edu.au/) and [ICE](http://ice.usq.edu.au/)
and they showed us some work they've been doing on repository access
control using open standards. We look forward to seeing more of their
work in this area in future.

One of the issues that came up was bibliographic software, which I've
been sort-of tracking for the ICE project. I promised to send James a
summary of some of the work going on at the moment so here goes.

If you want to keep up with what's going on in this space, and don't
feel like reading my ramblings, subscribe to the RSS feed at Bruce
D'Arcus' [site](http://netapps.muohio.edu/blogs/darcusb/darcusb/). Bruce
is a bibliographic powerhouse who's working on several fronts to improve
tools.

## <span id="id628167"></span>What am talking about here?

I'm talking about bibliographic software that lets you keep a library of
references, insert citations into a document and then format citations
and add a bibliography automatically. Here at USQ that means EndNote.
Bruce D'Arcus has [plenty to say about
EndNote.](http://netapps.muohio.edu/blogs/darcusb/darcusb/index.php?s=endnote)But
don't let him scare you off, if your institution has a site license you
probably should still use it until a compelling replacement emerges.

(If you're doing academic work at any level including undergraduate and
you're not using bibliographic software then you need to get down to
your library and ask for help!)

There's a well-maintained list of this kind of software at the
[OpenOffice
site](http://wiki.services.openoffice.org/wiki/Bibliographic_Software_and_Standards_Information).
And some advice for OpenOffice Writer users.

> **But what can I do now?** In the meantime, if you are not happy with
> OOo's basic bibliographic support, you may like to use some of the
> third-party bibliographic applications that can work with OpenOffice.
> See the [bibliographic software
> page](http://wiki.services.openoffice.org/wiki/Bibliographic_Software_and_Standards_Information)
> for more details. You may like to look at the package
> [B3](http://wiki.services.openoffice.org/wiki/Bibliographic_Software_and_Standards_Information#B3)
> or
> [Jabref](http://wiki.services.openoffice.org/wiki/Bibliographic_Software_and_Standards_Information#JabRef)(version
> 2 beta +) both of which have a nice user interface and can write
> bibliographic records to a Openoffice Bibliographic text database.
> [Bibus](http://bibliographic.openoffice.org/biblio-sw.html#Bibus) is
> Bibliography application with good integration with OpenOffice.

> <http://bibliographic.openoffice.org/>

For Word users I can't really recommend anything in particular, go with
whatever is supported at your institution or [pick something off the
list](http://wiki.services.openoffice.org/wiki/Bibliographic_Software_and_Standards_Information).

I am starting to hear a bit about [RefWorks](http://www.refworks.com/)
now. It's web-based with an optional local bit to add citations as you
write, and I've signed up for a free trial. I'll see if it's bearable
enough to work with, but I have already established that it **does not
like OpenDocument** formatted docs one little bit.

## <span id="id628361"></span>What are we doing in ICE?

In the active ICE pilots our users will be using Word + EndNote to
format bibliographies. OpenOffice is still used behind the scenes to
make PDF and to generate XHTML. This is a bit of an anticlimax. Nothing
to see here, move on.

## <span id="id628373"></span>My opinion

I think [CSL](http://xbiblio.sourceforge.net/cite/), the Citation Style
Language invented by Bruce D'Arcus is a great idea, and I'd love to see
software that works with it that can process word processing and XML
documents to format citations and bibliographies.

CSL is a way of specifying a particular citation style in XML, and with
supporting software should let you reformat a document with different
referencing styles automatically, just like EndNote's Output Styles but
with significant improvements in flexibility.

I am very pleased that Bruce has managed to get his ideas in front of
the OpenDocument
[committee](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office),
which he has joined, so that CSL will have a good chance of being
implemented and adopted fairly widely.

But I also think that the proposed additions to OpenDocument which
should appear in OpenOffice.org version 3 might be counter productive,
because they might make interoperability with MS Word in particular much
harder. I favour a lighter-weight approach as outlined in a [message I
wrote to the OpenOffice.org bibliographic
list.](http://www.mail-archive.com/dev@bibliographic.openoffice.org/msg00262.html)

Why not embed citations using a simple hyperlink? Links are already
supported everywhere.

The link might be an [OpenURL](http://en.wikipedia.org/wiki/OpenURL), or
it might point to a bibliographic application either on the web or
running locally in the same way that ICE does (it has its own
webserver), or it could be to an Institutional Repository, to a journal,
to Amazon, or to your local library or to a plain-old web page. A
document post-processor can then resolve that link and try to get
bibliographic details for it. If it can't it can ask you to type them in
or you might choose to ignore that link and leave it as a link rather
than a citation.

**My approach is microformat-ish**; I would like to see loose coupling
by-convention because I think it has a chance of working now, without
waiting for a future release of OOo and avoids building a silo that may
trap content in OpenDocument.

I'd like to see the CSL-driven post-processor as a free software
library, so we could build bibliographic support into the ICE
application itself. I'm assuming that these libraries will emerge from
the work that Bruce and others are doing. I should be helping, at least
on the bits of which I approve, but I'm not finding the time at the
moment.

And I think that the idea of a 'personal repository' has legs. Somewhere
to keep my copies of articles and cache web pages used as references in
case they change or go away. And of course, this should act like a music
playing application, able to fetch metadata for an item automatically as
discussed in this paper, *Why can’t I manage academic papers like MP3s*
([PDF](http://freelancepropaganda.com/archives/MP3vPDF.pdf)) .

## <span id="id628546"></span>Resources to watch

-   The OpenOffice.org [bibliographic project
    page](http://bibliographic.openoffice.org/).

-   The OpenOffice.org bibliographic
    [lists](http://bibliographic.openoffice.org/servlets/ProjectMailingListList).

-   Bruce's [blog](http://netapps.muohio.edu/blogs/darcusb/darcusb/).

-   My bibliographic software
    [posts](http://del.icio.us/ptsefton/ptsefton+bibliographicsoftware)
    (via del.icio.us).

> ****

</div>
