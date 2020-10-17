---
Author: ptsefton
Comments: true
Date: 2011-03-12 08:34:10+00:00
Slug: beyond-the-pdf-some-ideas-for-document-formats-and-authoring-tools

Title: 'Beyond the PDF: Some ideas for document formats and authoring tools'
Wordpress_id: 692
---

<div class="tf-content-block">

<div>

<div class="rendition-links">

<span class="pdf-rendition-link">[PDF
version](/wp-content/uploads/2011/03/Beyond-authoring-tool-map.pdf.pdf "View the printable version of this page")</span>

</div>

<div class="body">

<div>

This post has been sitting my work folder since Beyond the PDF in
January. I'm going to post what there is of it now, as background to the
[Scholarly HTML
hackfest](http://blogs.ch.cam.ac.uk/pmr/2011/03/10/scholarly-html-%E2%80%93-what-we-are-hoping-for/)
that's on in Cambridge this weekend.

In the lead up to Beyond The PDF there were lots of ideas flying around
about authoring tools, and associated document formats. People have
mentioned Word and OpenOffice.org, [ICE](http://wordpress.org/),
[Drupal](http://drupal.org/), Plone, wikis,
[Lemon8-XML](http://pkp.sfu.ca/lemon8),
[TeX](http://en.wikipedia.org/wiki/TeX)/LaTeX, XML schemas like [NLM
XML](http://dtd.nlm.nih.gov/articleauthoring/) and
[dexy.it](http://dexy.it/). The list goes on. These things are a bit
hard to compare. It's not apples and oranges so much as tropical fruit
salad. In that last sentence, there were editors, combined
editor-content-management systems and document formats, at least one of
which (TeX) is even Turing complete, meaning you can write computer
programs in it (but not, alas, always produce web pages from it).

I thought it might be worth making a start on mapping some of this
space. In this post I want to look at authoring tools, and document
formats <span class="spCh spChx2013">–</span> independently of the other
functions such as publishing and peer review. We need to look at both
formats and tools.

I have made the case in the past for using HTML as a **format** for
scholarly documents, proposing [Scholarly
HTML](http://ptsefton.com/2009/03/31/scholarly-html.htm). Martin Fenner
has also porposed that we <span class="spCh spChx201c">“</span>Use
HTML<span class="spCh spChx201d">”</span> - I agree that we should,:

> All this would be much easier if we just used HTML. With HTML,
> authors, publishers and readers can all use the same document format.
> And they will have an endless number of tools at their hands,
> including of course WordPress for writing and the web browser of
> choice for reading. HTML in 2010 is very different from HTML in 1990.
> HTML5 supports new semantic elements such as \<article\>, microdata,
> embedding of video without plugins, geolocation, and offline web
> applications.
>
> <http://blogs.plos.org/mfenner/2011/01/05/html5-or-messages-from-beyond-the-pdf/>

But, the problem is that tools that create scholarly-quality HTML5,
complete with article tags and so on don't exist at present. And if we
were to set out to create them from scratch, I see a very long road
ahead. Look at all the things that are built into a word processor like
MS Word, which were added over many years of development. There's
outlining and an outline view for document architecture, auto-text for
inserting frequently used text, a very complicated table editor, built
in vector graphic drawing, data-integration with spreadsheet functions
and graphs (that's data-aware publishing right there), document
navigation by headings, objects, tables etc, captions and numbering
systems for embedded objects, cross referencing by document structure,
by bookmark, user definable semantics via styles, revision control,
footnotes and endnotes. This is all stuff that was added in response to
real user feedback, at least in the first couple of decades of word
processor development, after which time many of us think things got
worse, not better.

I really think we need to ask a few questions:

1.  Who can afford to build all that again? Not small teams like mine.
    As Philip Lord put it on the mailing list:

    > It's a busy application space. My worry would be that anything
    > added into wordpress would just be the poor relation of these
    > tools [he mentioned Google Docs, Live Writer, Subversion]

2.  Given that we have authoring tools like Word processors which many
    author know and like, can't we find ways to create HTML (or whatever
    other formats are endorsed by the Beyond The PDF workshop) from word
    processors?

3.  If we are going to invest in tools like a WordPress web-based editor
    it would make sense to try and make work as portable as possible so
    it could be used with other CMS platforms.

4.  Don't forget wiki formats <span class="spCh spChx2013">–</span> it
    would be useful if we had one wiki format to support research, maybe
    along the lines of the apparently stalled [Wiki
    Creole](http://www.wikicreole.org/) <span
    class="spCh spChx2013">–</span> or built on one of the major wiki
    formats like MediaWiki or
    [MarkDown](http://daringfireball.net/projects/markdown/).

I think it's pretty clear that no one approach to authoring is going to
'win' out of this week's workshop, so what we should be looking for is a
way to get the best possible interop between authoring tools and
document formats.

But before we look at potential projects like Scholarly HTML editors
it's worth thinking about what it is that we're authoring. That is,
what's the abstract Model? This work, mentioned by Anita de Waard, who
has a very cool job title, *Disruptive Technologies Director, Elsevier
Labs* was new to me:

> So, in the W3C Health Care and Life Sciences group we are trying to
> come up with an 'ontology of rhetorical blocks' that does not only
> work for biology - and incorporates EPub, PRISM, BiBo, FRBR, and other
> bibliographic
> standards:<http://esw.w3.org/HCLSIG/SWANSIOC/Actions/RhetoricalStructure>
>
> Currently a first pass of an 'Ontology of Rhetorical Blocks' is
> out- http://esw.w3.org/HCLSIG/SWANSIOC/Actions/RhetoricalStructure/models/blocksontology is
> out, and we are working on a 'medium-grained' model -
> <http://esw.w3.org/HCLSIG/SWANSIOC/Actions/RhetoricalStructure/alignment/mediumgrain>
>
> Paolo Ciccarese, Tim Clark, Jodi Schneider and I are all working on
> this, and very much invite comments, contributions, and discussions at
> or before the San Diego meeting.

This is important background because it opens the way to layer a formal
semantics-of-rhetoric on top of any format and the work that has gone
into this is key input to the design of any new format.

# <span id="id2"></span><!--id2--></a>Potential mesh of services

I have some opinions and assumptions about authoring tools, their
strengths and weaknesses, based on long experience working on single
source web publishing systems in the academy. I'll put down some of the
assumptions here; happy to have my opinion changed if anyone wants to
take that on. My comment form awaits your input.

Assumptions:

-   Full schema-validating authoring tools (eg enforcing ordering
    constraints such as 'intro before method') are suitable only for
    trained editorial staff. With this class of tool, simple operations
    like splitting your intro into two sections can be quite complex. I
    have never heard of this class of tool being used successfully with
    a large number of loose affiliates like researchers (I've said that
    quite often here and I can't recall anyone turning up with an
    example, but as I said, the lines are open).

-   A new class of cut-down editor <span class="spCh spChx2013">–</span>
    probably running in the browser <span
    class="spCh spChx2013">–</span> which only allowed you to produce
    sensible documents, is probably doable.

-   Regarding word processors:

    -   There is no magic system that can turn sows ears (any old word
        document) into silk purses (like, say NLM compliant XML).

    -   In many disciplines, lots of authors will use their word
        processor to type stuff and try to paste into your system no
        matter what system you ask them to use.

    -   Giving authors a word processing template with some set of
        styles and-or macros and expecting them to use it to produce
        structured documents doesn't work.

<span
style="display: block"><a name="Object1"><!-- --></a>![Object1](/wp-content/uploads/2011/03/Beyond-authoring-tool-map_filesm5b7ee7cb.gif.gif)</span>Figure
1: A map of authoring tools; 'mass market' tools below the
'specialisation boundary' line, 'pro' tools above.

\
\
Copyright Peter Sefton, 2011. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en;"><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><!-- --></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/03/Beyond-authoring-tool-map_filesm40ca94ba.png.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>

</div>

</div>
