---
Author: ptsefton
Comments: false
Date: 2011-04-12 23:16:35+00:00
Slug: some-questions-about-epub-wordpress-tools

Title: Some questions about EPUB, WordPress, tools
Wordpress_id: 735
---

<div>

<div class="page-toc">

-   [<span>If you publish EPUBs now, what tools do you
    use?</span>](#id2)
-   [<span>What's considered best practice for EPUBs?</span>](#id3)
-   [<span>JISC project people: What do you have to do to get your
    reports up in JISCPress?</span>](#id4)

</div>

<div>

[This is a repost from the jiscPUB project <span
class="spCh spChx2013">–</span> please comment, but do so over
[<span>there</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/12/some-questions-about-epub-wordpress-tools/%20)]

I have a couple of questions for discussion in this jiscPUB project,
please any and all of you, [<span>use the
comments!</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/12/some-questions-about-epub-wordpress-tools/%20)

# <span id="id2"></span><span></span></a>If you publish EPUBs now, what tools do you use?

I asked jiscPUB team member Liza Daly via email what she uses to make
EPUBs, and she said
[<span>asciidoc</span>](http://www.methods.co.nz/asciidoc/index.html).

Asciidoc lets you create documents in your text editor of choice using
one of a [<span>family of lightweight wiki-style text formatting
languages</span>](http://en.wikipedia.org/wiki/Lightweight_markup_language).
Unlike Wiki formats, though, asciidoc is designed to create richly
structured documents, as [<span>discussed on this
page</span>](http://www.mzlinux.org/node/269). This [<span>post from an
O'Reilly author
explains</span>](http://www.apeth.net/matt/iosbooktoolchain.html) how it
works to create multiple output files. I'll do a post on how these tools
work with EPUB.

Now, I am interested in who uses what?

-   Anyone else use asciidoc?

-   Are there [<span>pandoc</span>](http://johnmacfarlane.net/pandoc/)
    users reading this? Bruce D'Arcus , have you made EPUB? I tried, but
    it does not support intra-document links.

-   Are some of you [<span>hand-crafting HTML like Mark
    Pligrim</span>](http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition)
    then feeding through something like Calibre?

-   Anyone use their word processor to make HTML and get EPUB from that?

(And just on the off chance, has anyone done a pandoc/markdown to
asciidoc converter?)

# <span id="id3"></span><span></span></a>What's considered best practice for EPUBs?

I have been making EPUBs by feeding things through various processors.
Different tools are using different levels of styling by default.

What's best practice, in terms of what level of CSS styling to put in
and so on? The top hit I got on Google for this was an Adobe page from
2008 that didn't actually tell me anything useful.

I think that when we're talking about word processing documents being
transformed for the web what often works best is to have consistent
styling for headings and plain paragraphs but authors do need some
control over what goes on in tables, for example. This will require some
figuring out for EPUB <span class="spCh spChx2013">–</span> I know the
team at USQ had problems with large and complex tables in their testing
with USQ courseware, mainly using iOS devices.

# <span id="id4"></span><span></span></a>JISC project people: What do you have to do to get your reports up in [<span>JISCPress</span>](http://jiscpress.org/about/)?

[<span>JISCPress</span>](http://jiscpress.org/about/) is a site where a
variety of project output documents can be annotated by the community.
It uses the [<span>digress.it</span>](http://digress.it/) comment system
to allow paragraph-level annotation. It says on the site: <span
class="spCh spChx201c">“</span>We are currently operating JISCPress on a
trial basis, with a view to making it a fully fledged JISC service if
the trial goes well.<span class="spCh spChx201d">”</span>

I wondered if anyone reading this has used it, and what the experience
of contributing to it is like. This is both relevant to this project and
to potential future explorations of how something like JISCPress might
work in an environment where some people might be commenting on
documents using ebook reader software and some using the plain-old web
<span class="spCh spChx2013">–</span> with some way of aggregating both.

When I called for sample documents for this project, Owen Stephens
([<span>@ostephens</span>](https://twitter.com/#!/ostephens)) sent me a
test document, I am still working on making a nice EPUB out of it,
fiddling with the tool as I go. He tells me it was 'converted by hand'
to go on [<span>this
site</span>](http://www.open.ac.uk/blogs/telstar/remit-toc/remit-why-integrate-reference-management/),
which is not quite like jiscPress but does allow comments.

Anyway, I am wondering:

-   How much effort are people putting in to getting JISC project
    outcome documents on the web?

-   I know there are templates for JISC reports, which seem pretty light
    and simple but what about JISC deliverables, like toolkit documents
    etc?

-   Assuming most of this kind of output is written in Word or other
    word processors, would people be interested in a template (and
    tools) that had:

    -   Embedded metadata that could be used by machines to process
        documents.

    -   A way to preview your work quickly and easily to make sure that
        the final output is going to be OK?

    -   Enough styling cues to create good web pages, maybe ebooks via
        automated uploads.

        There's a trade-off here between having something that's easy
        for authors to use, like treating the word processor like a
        typewriter (which is usually more costly in the long run) and
        getting people to invest in learning tools.

Comments?

[This is a repost from the jiscPUB project <span
class="spCh spChx2013">–</span> please comment, but do so over
[<span>there</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/12/some-questions-about-epub-wordpress-tools/%20)]

Copyright <span rel="http://purl.org/dc/elements/1.1/creator"
resource="http://trove.nla.gov.au/people/541658"><span
property="http://xmlns.com/foaf/0.1/name"
resource="http://trove.nla.gov.au/people/541658">Peter
Sefton</span></span>, 2011-04-12. Licensed under <span
rel="http://creativecommons.org/licence">Creative Commons
Attribution-Share Alike 2.5 Australia</span>.
\<http://creativecommons.org/licenses/by-sa/2.5/au/\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><span></span></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/04/m40ca94ba2.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project.

</div>

</div>
