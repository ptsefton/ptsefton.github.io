---
Author: ptsefton
Comments: false
Date: 2011-04-12 00:11:57+00:00
Slug: metadata-in-word-processing-monographs

Title: Metadata in word processing monographs
Wordpress_id: 731
---

<div>

<div class="page-toc">

-   [<span>Introduction – why worry about metadata?</span>](#id2)
-   [<span>Thesis workflow</span>](#id3)
-   [<span>Thesis metadata</span>](#id4)
-   [<span>Summary</span>](#id6)
-   [<span>Where now?</span>](#id7)

</div>

<div>

[This is a repost of a document I posted to the jiscPub blog <span
class="spCh spChx2013">–</span> posting here as well to reach more
people but please use the comments [<span>over
there.</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/11/metadata-in-word-processing-monographs-2/)]

# <span id="id2"></span><span></span></a>Introduction <span class="spCh spChx2013">–</span> why worry about metadata?

I have been working on a simple service to take word processing
documents <span class="spCh spChx2013">–</span> Word and OpenOffice.org
mainly <span class="spCh spChx2013">–</span> and create mobile-readable
EPUBs from them. One of the issues in this process is metadata: how do
we get quality metadata into the EPUB format?

EPUB readers, like music applications use metadata to provide browse and
search access to content.

<span
style="display: block"><a name="graphics1"><span></span></a>![graphics1](/wp-content/uploads/2011/04/m65a205f3_643x396.jpeg)</span>Illustration
1: Calibre's metadata-driven management interface

Obviously, for books to be useful to readers, and to store-owners,
publishers and repositories, metadata is an issue.

But it's not just for ebook delivery that this is an issue. A thesis has
to be submitted for examination, and sent to an institutional
repository, and maybe to a discipline repository or a publisher. And
papers are often submitted to multiple sites over their lives <span
class="spCh spChx2013">–</span> conference management systems, journal
management systems, repositories and so on. The current state of
scholarship is that every time you make such a submission you have to
re-enter metadata. Upload a paper to a conference site, and chances are
you will have to enter the author names into a form, even if they are
already on the paper. Not to mention that every time you type in a name,
you are generating low-quality string-based non-linked data. Some of
us[<span> think there is a slow revolution happening in
metadata</span>](http://cairss.caul.edu.au/blog/2010/08/05/i-only-have-uris-for-you-vicki-and-peters-adventures-in-linked-data-land/),
using URIs and making links.

So one of the things I would like to consider for this project is how to
embed metadata within documents so that the various applications that
process them can do all the hard work. And I want to think not just
about strings but high-quality linked-data metadata. To discuss this I
will work through one of the use cases for the jiscPUB project and look
at the life-cycle of a thesis.

# <span id="id3"></span><span></span></a>Thesis workflow

The aspect of workflow we're interested in here is that:

1.  If the candidate is lucky the university or supervisor provides them
    with a template for writing up their thesis.

2.  The candidate writes up the thesis and sends it to their supervisor
    and possibly other reviewers during this process.

3.  Depending on the quality of the template there is work to do for
    submission, generating tables of contents, making PDF files <span
    class="spCh spChx2013">–</span> maybe, probably, in future, making
    web and mobile-ready versions.

4.  Someone deposits the thesis file into (at least) the repository at
    the university, maybe also other databases, entering metadata about
    it who knows how many times.

5.  Also in the future making sure all the provenance for all claims is
    available via data that is linked to or bundled with the thesis.
    (Out of scope for this post, but I will come back to it).

In this post I am going to look at 1-4 above, looking at how template
design might aid in preparing a thesis for mobile delivery. I've been
thinking for a few years now that the university should not just provide
a template but pre-fill as much of it as possible with machine-readable
metadata. And note that there's probably a much more compelling case for
machine readable metadata in articles, which tend to be submitted to
more places.

# <span id="id4"></span><span></span></a>Thesis metadata

The university of Edinburgh, host of this jiscPUB project via
[<span>EDINA</span>](http://edina.ac.uk/), has a word template for PhD
theses on its wiki. I showed in the last post that if you feed that
template, sans any content, through the experimental Word to EPUB
converter I've been working on, then it more or less worked, but without
very much metadata (it was also dropping heading numbering, which I have
now, sort-of, kinda, fixed).

To add the metadata that *should* be in the EPUB you would have to type
it in somewhere. Either I could add fields to the conversion service, or
you could use something like
[<span>Calibre</span>](http://calibre-ebook.com/), but the thing is,
most of the metadata you need is in the document <span
class="spCh spChx2013">–</span> it's just not marked as such. The title
page has the Title (in `AUTHOR` style) the author's name, and the name
of the institution, degree and date in the footer.

<span
style="display: block"><a name="graphics2"><span></span></a>![graphics2](/wp-content/uploads/2011/04/m367b9320.png)</span>Illustration
2: Thesis metadata is there - in the text, just not marked as such

So <span class="spCh spChx2013">–</span> it should be possible, given
that this metadata is all there to mark it in such a way that downstream
processing systems can recognise it. One of the best places to start is
with the document metadata fields. The Edinburgh template does use
document metadata for the title.

<span
style="display: block"><a name="graphics3"><span></span></a>![graphics3](/wp-content/uploads/2011/04/m57000384.png)</span>Illustration
3: Document metadata in Word 2010

But it could go one step further, and instead of requiring the author to
enter the same thing in two places, use a field to show the title on the
title page. In Word 2010 the field function is hiding in the Ribbon
under Insert, Quick Parts.

<span
style="display: block"><a name="graphics4"><span></span></a>![graphics4](/wp-content/uploads/2011/04/75372ee3.png)</span>Illustration
4: Adding a field so the title entered in the document metadata can be
placed on the title page without re-typing.

Now the title is linked to the document properties, and any application,
such as search engine can extract that metadata. But there is a cost
<span class="spCh spChx2013">–</span> you have to be able to explain to
your authors that they need to set the title in the properties, and how
to do it, for the different word processing applications they're using.

The same thing works for the author field as well. That's OK for theses
but it is less useful for other kinds of scholarly content where there
are often many authors. Word 2010 supports multiple authors in its
metadata<span class="spCh spChx2013">–</span> but the fields don't <span
class="spCh spChx2013">–</span> all you can get using a field is a
semicolon separated list of authors, which is not useful for laying out
the content. An approach I think is useful for scholarly templates in
general is to embed the metadata in-line.

Some colleagues and I wrote up some of the approaches for embedding
inline metadata for the Journal of Digital Curation<span
class="T2">1</span>. The short version of that is that the most reliable
cross-platform way of adding semantics like metadata in-line to
documents is to use styles, or a new technique I have been developing
since that work, using links. Both styles and links are supported by
major word processors, so they tend to survive being loaded into
different word processors or different versions of the same word
processor. I will give examples of both approaches here.

Styles are fiddly to apply if you are expecting people to manage the
process for themselves, but in the case of a template like this one for
theses they should be robust enough <span
class="spCh spChx2013">–</span> thesis candidates are not going to be
changing the title page except to fill in their details. Even better
<span class="spCh spChx2013">–</span> why doesn't the university do it
for the candidate? I'll come back to this idea. Using tables for
metadata like the one on the top of this document is also a reliable
approach the metadata can be identified using style, or just text in a
cell adjacent to each metadata item.

So <span class="spCh spChx2013">–</span> to demonstrate the use of
styles for metadata in the Edinburgh thesis template, I:

1.  Used style p-meta-author instead of AUTHOR so the ICE conversion
    system would recognise it.

    <span
    style="display: block"><a name="graphics5"><span></span></a>![graphics5](/wp-content/uploads/2011/04/c775b0c.png)</span>Illustration
    5: Applying the style p-meta-author the author name in the template.
    This dialogue box is a bit hard to find, good luck.

2.  Added an inline/character style for the date i-date. [TODO: get this
    working or remove from post]

    <span
    style="display: block"><a name="graphics6"><span></span></a>![graphics6](/wp-content/uploads/2011/04/2646dc13.png)</span>Illustration
    6: The inline style for the date, i-meta-date. It has no special
    formatting.

Getting both of these to work required a bit of hacking on ICE itself,
as this metadata handling was only partially implemented.

The result is that both author and date are now included in the metadata
for the EPUB file.

There is a problem with this approach, though, in that it is not giving
us very high quality metadata in a linked-data sense. The author name is
just a string, which as we know is not a good way to uniquely identify
an author. More than one person might be identified by a string, and
more than one string often identifies an author<span
class="T2">2</span>. It would be much better if we could give the Author
an HTTP URI. That is to name them using a URL that will be stable and
unambiguous whether they are called <span
class="spCh spChx201c">“</span>Name of Author<span
class="spCh spChx201d">”</span> or <span
class="spCh spChx201c">“</span>Author, N<span
class="spCh spChx201d">”</span> or they change their name to <span
class="spCh spChx201c">“</span>Nom de Plume<span
class="spCh spChx201d">”</span>, which might occur as a string like
<span class="spCh spChx201c">“</span>de Plume, N<span
class="spCh spChx201d">”</span> or many other variants.

There's a big project coming, ORCID, which will aim to give researchers
URIs, but an university could easily give each candidate a URI now, and
match up with ORCID later.

I have included a demonstration of how to identify a party, the
Publisher, using a URI. Here's a walk-through of a possible technique
for including URIs for metadata in a template. Remember, only the
template designer has to do this, not the poor candidate. And if we
wanted to use this technique for personal names we could automate it and
use a university-assigned URI for each candidate:

1.  I chose a URI for the university:
    [<span>http://www.ed.ac.uk/</span>](http://www.ed.ac.uk/) . Just
    using that as a link does not amount to metadata though. Instead I,

2.  Visited [<span>http://www.ed.ac.uk/</span>](http://www.ed.ac.uk/) -
    which redirects to
    [<span>http://www.ed.ac.uk/home</span>](http://www.ed.ac.uk/home)

3.  Clicked my
    [<span>Publisherize.me</span>](javascript:(function()%7Bwindow.open('http://ontologize.me/?tl_p=http://purl.org/dc/terms/publisher&triplink=http://purl.org/triplink/v/0.1&tl_o='+location.href);%7D)();)
    bookmarklet.

4.  Copied the resulting link <span class="spCh spChx2013">–</span>
    which is encodes an RDF statement/triple, and wrapped it around the
    text in the template.

    > `http://ontologize.me/?``tl_p=http://purl.org/dc/terms/publisher&triplink=http://purl.org/triplink/v/0.1&tl_o=http://www.ed.ac.uk/home`

5.  Now, when documents using that template are fed through ICE,
    including the[<span> word-processing-to-EPUB
    service</span>](http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/doc)
    I have been prototyping, ICE recognises the metadata, extracts it
    into a data structure so it can be passed-on to Calibre, which makes
    the EPUB.

    > ebook-convert ... --title "Title of Thesis" --authors
    > "Author-name" --publisher "The University of Edinburgh
    > (http://www.ed.ac.uk/home)" --pubdate "2011-05-01"

    But wait, there's more! ICE also embeds the metadata in the HTML it
    produces, like so (I did edit out some cruft that it should not be
    producing):

    > `<span rel="http://purl.org/dc/elements/1.1/publisher" resource="`[`http://www.ed.ac.uk/home`](http://www.ed.ac.uk/home)`">`
    >
    > `<span property="http://xmlns.com/foaf/0.1/name" resource="`[`http://www.ed.ac.uk/home`](http://www.ed.ac.uk/home)`">`
    >
    > `<a href="http://ontologize.me/?tl_p=http://purl.org/dc/terms/publisher&amp;triplink=http://purl.org/triplink/v/0.1&amp;tl_o=http://www.ed.ac.uk/home">The University of Edinburgh`
    >
    > `</a>`
    >
    > `</span></span>`

    This is intended to be compatible with RDFa 1.1, and this approach
    for embedding metadata in scholarly documents is on of the
    approaches we're promoting in the nascent [<span>Scholarly
    HTML</span>](http://scholarlyhtml.org/) movement.

# <span id="id6"></span><span></span></a>Summary

In this post I have looked at three ways to embed metadata in a word
processing document, so that when people *use* the template the metadata
they or the template designer, enter can be machine-processed from then
on.

1.  Using the metadata fields in the document: good for very basic
    metadata like titles, but limited and not particularly interoperable
    for other kinds of metadata.

2.  Using styles: flexible but fragile, and requires that each
    processing system knows about the styles you are using.

3.  Using my proposed way of making linked data metadata statements
    encoded in links; triplinks, as seen on my demo site:
    [<span>http://ontologize.me</span>](http://ontologize.me/). This is
    potentially quite robust, and could be supported by tool-chains that
    are much easier to use than the current half-baked infrastructure
    provided by yours truly.

Here's a final screenshot showing how the embedded metadata has made its
way from the sample template using those three methods to the EPUB
metadata, as seen in the Firefox EPUB plugin.

<span
style="display: block"><a name="graphics7"><span></span></a>![graphics7](/wp-content/uploads/2011/04/74c35190_643x180.jpeg)</span>Illustration
7: Metadata from the thesis template demo, in the Firefox EPUB plugin.

All three of these require that software systems know how to find and
process metadata <span class="spCh spChx2013">–</span> what we're trying
to achieve over at the [<span>Scholarly
HTML</span>](http://scholarlyhtml.org/) site (when I get time to add
pages on conventions for encoding metadata) is to document common ways
of doing this so that tool-builders can create interoperable systems.

To try this out for yourself:

1.  Go here in your browser:
    [<span>http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/doc</span>](http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/doc)

2.  Either:

    -   [<span>Download</span>](http://dl.dropbox.com/u/24994372/Edinburgh-ThesisSingleSided-plus-inline-metadata.doc)
        this document and upload, or

    -   paste in this URL:
        [<span>http://dl.dropbox.com/u/24994372/Edinburgh-ThesisSingleSided-plus-inline-metadata.doc</span>](http://dl.dropbox.com/u/24994372/Edinburgh-ThesisSingleSided-plus-inline-metadata.doc)
        and click Convert.

        <span
        style="display: block"><a name="graphics8"><span></span></a>![graphics8](/wp-content/uploads/2011/04/d7cebc_620x220.jpeg)</span>Illustration
        8: Converting the test thesis doc to EPUB via a URL.

The default check-boxes at that service will make you an EPUB <span
class="spCh spChx2013">–</span> if you don't have an EPUB reader you can
change the file extension to .zip, open it up and have a look. If you
do, you'll see something like this:

<a name="graphics9"><span></span></a>![graphics9](/wp-content/uploads/2011/04/m61bdf872_643x579.jpeg)Illustration
9: Test thesis template in Adobe Digital Editions - note the title and
author have been automatically extracted from the Word document.

# <span id="id7"></span><span></span></a>Where now?

There's potential here to test some of this stuff out with the folks who
support thesis candidates and their supervisors, or in journal
templates.

-   I will keep working on the Edinburgh template <span
    class="spCh spChx2013">–</span> to show how we might add to it in
    ways that increase the utility of the documents it produces, by
    making it easier to build ebooks. My thinking is to provide demos of
    what can be done for Word, OpenOffice.org/LibreOffice both using
    generic styles, or for people prepared to invest a little more time
    using the ICE styles.

-   I'd love to do something with a repository <span
    class="spCh spChx2013">–</span> I'm thinking that it would be great
    to deposit theses in EPUB format <span
    class="spCh spChx2013">–</span> and the repository could provided a
    web-based reader, along the lines of
    [<span>IbisReader</span>](http://ibisreader.com/), which Liza Daly
    and company created. I'm looking at you, Eprints! Eprints already
    almost supports this, if you upload a zip file it will stash all the
    parts for you in a single record. All we would need would be
    something like this [<span>little reader my colleagues at USQ
    made</span>](http://demo.adfi.usq.edu.au/paquete/demo/#module01.htm).
    It would just be a matter of transforming the EPUB TOC into JSON,
    and loading the JavaScript into an Eprints page.

-   There are improvements to be made to ICE <span
    class="spCh spChx2013">–</span> currently the style-based metadata
    does not produce Scholarly HTML / RDFa output, and is in a separate
    part of the code from the link-based metadata; these could be
    brought together.

-   Is it worth adding Scholarly HTML / RDFa metadata support to Calibre
    so it can auto-detect metadata in HTML input?

Longer term I would like to see:

-   A properly resourced end-to-end thesis project looking at how an
    institution could provide technical resources to candidates and
    supervisors, from templates, and a content, data and annotation
    management system . I will be showing demo service of some of this
    later in the project, but at the moment the demos are just toys
    <span class="spCh spChx2013">–</span> we need some real users and
    some institutional commitment to trying this stuff out.

-   A journal and conference paper service where authors can write once
    and then submit to multiple journals. This idea comes from <span
    rel="http://purl.org/dc/elements/1.1/subject">Timo Hannay</span> who
    I met when I was in the UK <span class="spCh spChx2013">–</span>
    he's worked with Nature <span class="spCh spChx2013">–</span> where
    there is a 95%-ish rejection rate, so a service that could
    automatically re-work your document for you and submit would be
    really useful. Also sounds a bit like the Repository Junction
    project that Theo Andrew is involved in.

<span class="T10">1. Sefton P, Barnes I, Ward R, Downing J. Embedding
Metadata and Other Semantics in Word Processing Documents.
</span>*International Journal of Digital Curation*<span
style="font-style:normal; "><span class="T6">. 2009;4(2). Available at:
http://www.ijdc.net/index.php/ijdc/article/view/121. Accessed October
22, 2009.</span></span>

<span style="font-style:normal; "><span class="T5">2. Salo D. Name
Authority Control in Institutional Repositories - Cataloging &
Classification Quarterly. </span></span>*Cataloging & Classification
QuarterlyWhere*<span style="font-style:normal; "><span class="T5">.
2009;47(3 & 4):249 - 261. Available at: Accessed September 9,
2009.</span></span>

[This is a repost of a document I posted to the jiscPub blog <span
class="spCh spChx2013">–</span> posting here as well to reach more
people but please use the comments [<span>over
there.</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/11/metadata-in-word-processing-monographs-2/)]

Copyright Peter Sefton, 2011. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<[<span>http://creativecommons.org/licenses/by-sa/2.5/au/</span>](http://creativecommons.org/licenses/by-sa/2.5/au/)\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><span></span></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/04/m40ca94ba1.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project.

</div>

</div>
