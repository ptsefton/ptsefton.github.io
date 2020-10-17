---
Author: ptsefton
Comments: true
Date: 2011-03-09 12:59:39+00:00
Slug: hacking-towards-scholarly-html

Title: Hacking towards Scholarly HTML
Wordpress_id: 688
---

<div class="tf-content-block">

<div>

<div class="rendition-links">

<span class="pdf-rendition-link">[PDF
version](/wp-content/uploads/2011/03/scholarly-html.pdf.pdf "View the printable version of this page")</span>

</div>

<div class="body">

<div>

Following from [my
attendance](http://ptsefton.com/2011/02/08/beyond-the-pdf-workshop-trip-report.htm)
at the [Beyond the PDF](https://sites.google.com/site/beyondthepdf/)
workshop in January, I've been invited to Cambridge by Peter
Murray-Rust. That's where I am now. (We have two just under weeks to
revolutionise scholarly communications :) Peter has organized a hackfest
for the weekend of March 12^th^ and 13^th^ and the theme is <span
class="spCh spChx201c">“</span>[Scholarly
HTML](http://ptsefton.com/2009/03/31/scholarly-html.htm)<span
class="spCh spChx201d">”</span> - something I have been writing about,
but doing much about for a while now.

What's Scholarly HTML?

I think it's a way of representing 'research objects' along with
associated data and metadata, **for the web**, so they can be
efficiently created, then reviewed, discussed, machine processed, copied
and do on. Scholarly HTML is a way to encapsulate research objects in a
portable, preservable and sustainable way using simple technologies so
that research can be not just *on* the web but *of* the web.

What I hope to do at the hackfest is map out some guidelines for what
Scholarly HTML might look like and then start working out how to author
it, and how to present it. And how to do scholarship on top of it. Open
review, machine processing, nanopublications <span
class="spCh spChx2013">–</span> these things all need a platform. Yes
you can do these things in PDF, if you write new PDF viewers and so on,
but it is so much easier to use the web. That's what the web was
originally for, after all. Yes, I will be talking about word processors,
and our work on desktop repositories. And yes Martin Fenner will be
looking at WordPress and PMR's team are looking at machine generated
journals <span class="spCh spChx2013">–</span> but I think it's really
important to think about what we want in an underlying *format*.
Something that can be preserved and exchanged and made to work in
different systems.

(I think that sometimes the format itself is hard to see when you are
looking at tools like WordPress which are both authoring tool and
publishing environment but it is doubly important in that case to make
sure that what we're creating is not locked in to a particular platform.
How would you archive a document which depends on eight CMS plugins to
work? How sustainable is a journal that requires multiple CMS plugins?
I'm not saying the folks working on tools now are not thinking about
these issues, just emphasising that we will be thinking about hard about
separating tools from formats and considering interoperability at the
workshop. That includes 'interop with the future' AKA digital
preservation.)

In scope for the *format* Scholarly HTML:

-   **Articles, theses, reports, lab notebooks, blog posts**, which
    reference associated stuff such as data and provenance and anything
    else that makes research reproducible and/or able to be validated.
    Peter Murray-Rust contributed this:

    > It is critical that the tool [I think he should have said *format*
    > rather than *tool* here] supports easy aggregation and publication
    > of data as part of the article. This includes the following - in
    > text
    >
    > -   tables in some accepted format (CSV, \*.tex are most common)
    >
    > -   bit-map images (micrographs, gels, galaxies...)
    >
    > -   vector graphics (SVG, ?WMF, etc.). Plots, apparatus, etc.
    >
    > -   maths - equations, variables, code
    >
    > -   chemistry - CML and other Open markup languages (PubchemXML?0
    >
    > -   maps (GML, coordinates)
    >
    > -   supplemental files. All the above and more
    >
    > \
    > \

-   **Structure and semantics for document contents**, like headings,
    being able to label parts <span class="spCh spChx2013">–</span> like
    <span class="spCh spChx201c">“</span>This bit is a *Method<span
    class="spCh spChx201d">”</span>* where *Method* is well defined
    using a URI and extensible methods for describing relations between
    and within objects.

-   Ways to **represent citations in an unambiguous machine readable
    way** so that readers can have them presented in ways of their own
    choosing.

-   **Techniques for embedding domain semantics**.

-   **Packaging** so that research objects can be moved around, saved,
    posted, etc. This is going beyond HTML, I know, but it's one of the
    great unsolved problems of the web. I've [talked about this
    before](http://ptsefton.com/2010/08/13/epub-as-a-way-of-packaging-scholarly-resources.htm)
    <span class="spCh spChx2013">–</span> and [Martin Fenner has picked
    up the Epub ball and taken it for a good
    run](http://blogs.plos.org/mfenner/2011/01/23/beyond-the-pdf-%E2%80%A6-is-epub/).
    More soon on this but just as a teaser, I'm now thinking of
    proposing that a minimal scholarly HTML package might consist of a
    zip file with at least one file at the root, index.html, which can
    link other pages if it wants. This is inspired by Eprints and by the
    simple standards such as
    [Bagit](https://confluence.ucop.edu/display/Curation/BagIt)
    developed at the California Digital Libraries. This is a minimum
    <span class="spCh spChx2013">–</span> the package could also be an
    ePub and have a formal ORE manifest etc. Chris Rusbridge [mentioned
    the importance of packaging over on Peter Murray-Rust's
    blog](http://blogs.ch.cam.ac.uk/pmr/2011/03/08/scholarly-html-hackfest/#comment-94093).

    > <span class="spCh spChx2026">…</span> My concern re Scholarly HTML
    > relates to the difficulty in saving an article in HTML and then
    > accessing it later (one of PDF<span
    > class="spCh spChx2019">’</span>s big advantages is that it does
    > this simply and reliably). Safari does this well with .webarchive
    > but it<span class="spCh spChx2019">’</span>s non-standard and no
    > other browsers support this. Most use a really clumsy convention
    > with a .html file and an associated directory; not very easy to
    > manage.
    >
    > So my suggestion to help Scholarly HTML would be a plugin (eg for
    > Firefox) or filter that converts Scholarly HTML articles to .epub
    > (eg see mfenner<span class="spCh spChx2019">’</span>s plugin for
    > epub from WordPress).

Related to the format, but not actually part of Scholarly HTML:

-   **Annotations on the above**, where annotation is taken in the
    broadest possible sense. Scholarly HTML needs to worry about anchors
    for annotation. Annotation can be used for peer and open review,
    inline discussion at all stages of a research object life cycle,
    adding formal semantics and lots of other scholarly processes.

-   **Tools, tools tools.** Word, WordPress and anything else that
    starts with W, maybe even some things that don't. I want to be able
    to work on papers in OpenOffice and post them to collaboration
    spaces <span class="spCh spChx2013">–</span> including WordPress, so
    I think a lot of the hackfest should be about interop.

-   **Authoring tricks and techniques.** Stuff like
    [KCite](http://wordpress.org/extend/plugins/kcite/) where you can
    add citations in any-old editor using text [ [cite
    source='pubmed']17237047[/cite], and my approach of using links to
    embed document semantics, like this assertion that I am the author
    of this post:

    <span property="http://xmlns.com/foaf/0.1/foaf:name"
    resource="http://trove.nla.gov.au/people/541658">[Peter
    Sefton](http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_o=http://trove.nla.gov.au/people/541658)</span><span
    style="color:#333333; font-size:9.75pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none;"><span
    class="T5">.</span></span>\
    \

-   **Browser-side plugins to make declarative Scholarly HTML come
    alive**. There are some problems with browser-side code,
    particularly when various scripts get in each other's way, but one
    of the big pluses is that it can work across more than one system
    really easily, so you don't just get a WordPress plugin, you get
    something that can be added to any system or turned into an app for
    offline use.

Important properties of scholarly HTML:

-   **It's declarative**. That is if we are linking a document to, say,
    a map then the document will contain:

    -   At least, a link to the map, which must be in a standard format.
        The link will be labelled in some way to say <span
        class="spCh spChx201c">“</span>I am a link to a map<span
        class="spCh spChx201d">”</span>, maybe with further attached
        semantics.

    -   Optionally a static placeholder image for the map so that any
        old web browser can be used to at least show something.

    Systems for rendering Scholarly HTML will know how to interpret the
    semantics that there is a map, or a molecule on the end of the link
    and do something useful. A web page containing Javascript tied
    directly to Google Maps doesn't qualify <span
    class="spCh spChx2013">–</span> it's not portable. (But as Phillip
    Lord pointed out in email, if the basic declarative stuff is there
    then it should be OK to have the script as well.)

    Another example of where a declarative spec is important is
    citations. Scholarly HTML will have a way to represent citations
    <span class="spCh spChx2013">–</span> there's a really [useful
    discussion going on of the issues around
    this](https://groups.google.com/group/wordpress-for-scientists/msg/d5ab1ba17fde62d6)
    on the wordpress-for-scientists@googlegroups.com list. Martin Fenner
    is committed to working on a tool that can find citations in text
    and format them, this [will be a web
    service](http://blogs.plos.org/mfenner/2011/03/07/the-trouble-with-bibliographies/).
    I think we can use the workshop to [progress work on microformats
    for citation](http://microformats.org/wiki/citation) and at least
    consider some of the questions about what are reliable end points
    for citations and how much potentially redundant bibliographic data
    to store in the Scholarly HTML.

-   It has a **simple structural backbone**, using HTML 5 elements to
    give the basic hierarchy with optionally much more detail. Using the
    [HTML article
    element](http://dev.w3.org/html5/spec/Overview.html#the-article-element),
    it should be possible to identify the bounds of a work, and separate
    it from navigation and branding.

Copyright

<span property="http://xmlns.com/foaf/0.1/foaf:name"
resource="http://trove.nla.gov.au/people/541658">[Peter
Sefton](http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_o=http://trove.nla.gov.au/people/541658)</span>,
2011. Licensed under Creative Commons Attribution-Share Alike 2.5
Australia. \<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>\
\
<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en;"><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><!-- --></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/03/scholarly-html_filesm40ca94ba.png.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>

</div>

</div>
