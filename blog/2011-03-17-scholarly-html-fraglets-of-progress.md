---
Author: ptsefton
Comments: true
Date: 2011-03-17 17:00:17+00:00
Slug: scholarly-html-fraglets-of-progress

Title: 'Scholarly HTML: Fraglets of progress'
Wordpress_id: 698
---

<div class="tf-content-block">

[update 2011-03-18 Fixed some typos]
<div>

<div class="rendition-links">

<span class="pdf-rendition-link">[PDF
version](cml-tool-first-look.pdf "View the printable version of this page")</span>

</div>

<div class="page-toc">

-   [Preamble](#cml-tool-first-look-id2)
-   [Example](#cml-tool-first-look-id3)
-   [Summary](#cml-tool-first-look-id4)

</div>

<div class="body">

<div>

# <span id="cml-tool-first-look-id2"></span><!--id2--></a>Preamble

I have been in Cambridge for 10 days [working
on](http://scholarly-html.okfnpad.org/1) Scholarly HTML with Peter
Murray-Rust and team, plus assorted remote participants. I think the
emerging consensus says that Scholarly HTML is a set of practices and
conventions for using the web for scholarship [in a] way that will
reduce friction for people and machines. The nascent format Scholarly
HTML is the pivot point for tools that will be used to create documents,
package research objects and consume content.

Scholarly HTML (should it take off) is relevant for publishers who
create content for the web <span class="spCh spChx2013">–</span> making
it more useful to their readers. It's relevant to authors who want to
produce the highest quality meaningful documents they can and reduce the
time and effort they spend re-working content and re-entering metadata,
and it's relevant to scholars who are trying to deal with vast amounts
of material out there on the open web, and behind various paywalls and
barriers, including the often impenetrable prison of the PDF format.

In this post I wanted to report some progress on simple tools for
creating Scholarly HTML. I will focus on Chemistry. I ask:

-   How do I refer to a molecule described using Chemical Markup
    language in a way that a reader will get a nice view of the
    molecule, while a machine can tell that what I am linking to is
    chemistry?

-   How do I do this declaratively, so that I am not baking-in to my
    document any particular behaviour? I will describe some progress
    towards tools below?

-   What tools would help?

Before getting to the examples, a bit of more general discussion.

We are in the process of defining some [core
guidelines](http://okfnpad.org/schtml-core), and setting out conventions
for dealing with scholarly semantics such as
[citations](http://okfnpad.org/schtml-citations). The techniques we're
documenting have been drawn from lots of previous work, particularly
RDFa and micro-formats. Martin Fenner has [a blog post setting out some
of the
benefits](http://blogs.plos.org/mfenner/2011/03/15/discussing-science-with-microformats/)
<span class="spCh spChx2013">–</span> I have minor quibbles with the
examples he has chosen but he articulates some of the benefits clearly.

There has been some push-back for example:

> [**<span>TAC\_NISO</span>**](https://twitter.com/#!/TAC_NISO)<span
> style="color:#444444; font-size:11.25pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none;"><span
> class="T2"> </span></span><span
> style="color:#999999; font-size:9pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none;"><span
> class="T9">Todd Carpenter</span></span><span
> style="color:#444444; font-size:11.25pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none;"><span
> class="T2"> </span></span>
>
> Sorry @rtennant I just don't see value here, apart from duplicating &
> rebranding work already done <http://bit.ly/gEoNg0>
> <http://bit.ly/hCTIgH>

And:

> [**<span>TAC\_NISO</span>**](https://twitter.com/#!/TAC_NISO)<span
> style="color:#444444; font-size:11.25pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none;"><span
> class="T4"> </span></span><span
> style="color:#999999; font-size:9pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none;"><span
> class="T10">Todd Carpenter</span></span><span
> style="color:#444444; font-size:11.25pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none;"><span
> class="T4"> </span></span>
>
> If all Scholarly HTML is to take DCMI terms, existing ontologies &
> layer upon \#HTML5, what's the "there" there? Value being added?
> @rtennant

I don't think we're duplicating work but trying to make it easy to find,
packaging it into a single set of guidelines and providing a locus for
tool builders. For example, this morning we have been talking about how
to take the Object Reuse and Exchange spec and provide a single, simple
way to use that in an HTML page so that page can aggregate resources
into a scholarly object. Frankly ORE needs all the help it can get to
drive adoption.

A lot of what we are doing amounts to providing guidelines. Writing
guidelines that tell people how to apply existing RDFa techniques in a
particular way is not 'duplication' it's documentation. Maybe we could
think of this effort not as <span class="spCh spChx201c">“</span>HTML
for D---ies<span class="spCh spChx201d">”</span> but <span
class="spCh spChx201c">“</span>HTML for Scholars<span
class="spCh spChx201d">”</span>.

The way I see it we are taking the opposite approach to the one taken by
Perl where Larry Wall's mantra was <span
class="spCh spChx201c">“</span>There's more than one way to do it<span
class="spCh spChx201d">”</span>. On the web, there certainly is, but for
Scholarly HTML to succeed I think we need to say to people:

-   There's one good (enough) way to do it.

-   Here's a meaningful way to do it.

-   Here's a simple way to do it.

We meed to make things easy for people to copy and paste examples into
their blogs, easy for developers to code tools, and easy to document.
So, Scholarly HTML is not RDFa, which is hard and very broad and very
complicated, but it does use fragments of RDFa that should make sense to
RDFa processors (at least when RDFa 1.1 arrives with support for full
URIs in properties and relations etc).

# <span id="cml-tool-first-look-id3"></span><!--id3--></a>Example

So, to the example.

I want to include some chemistry in my blog. Now, remember this is just
one tool-chain. We know it won't be suitable for everyone, and we're
hoping that our friends at Microsoft Research and the WordPress blogging
tool community can make all this much easier for users. With that in
mind let's go through two cases which would be suitable for
early-adopters who want to embed a molecule in their blog in a way that
should interoperate with other systems, and not cause problems in the
future. Two cases:

1.  Where I am using plain-old WordPress or similar,.

2.  Where I am using a Scholarly-HTML-ready publishing system (which I
    am here).

We start out the same in both cases. Here's what you do:

1.  Grab the
    [Crystalize.me](javascript:(function()%7Bwindow.open('http://ontologize.me/?tl_p=http://www.xml-cml.org/convention/crystallographyExperiment&triplink=http://purl.org/triplink/v/0.1&tl_o='+location.href);%7D)();)
    bookmarklet. Drag the link to your bookmarks bar.

2.  Go to some Chemical Markup Language you want to talk about. Anything
    I am likely to say about it will be meaningless, of course as I was
    kicked out of chemistry 101. As I am sponsored by the Murray-Rust
    group I get my
    [CML](http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml)
    from Crystaleye.
    <http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml>

3.  While the CML is showing in your browser, click the Crystalize.me
    bookmarklet. Don't click it now, or you will create a bad thing
    something claiming to be chemistry that is actually a blog post. The
    result is something like this (plain-text 'cos if I link to it the
    tool-chain turns it into CML): I have
    http://ontologize.me/?tl\_p=http://www.xml-cml.org/convention/crystallographyExperiment&triplink=http://purl.org/triplink/v/0.1&tl\_o=http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1\_II/dn3132sup1\_II.complete.cml.xml

    1.  If you resolve the above URI, you are looking at a page at my
        ontologize.me site. From here you can copy and paste a bit of
        HTML to include in your blog post if you know how to do that.

        > `<span rel='http://www.xml-cml.org/convention/crystallographyExperiment' resource='http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml'><a href='`[`http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml`](http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml)`'>Insert text here</a></span>`

    2.  Or of you're using a scholarly HTML aware tool like the Beyond
        The PDF demonstrator you can create a document with the link in
        it, and the Scholarly HTML preprocessor in the tool will unpack
        the information encoded in the link, and insert a span just like
        the one above.

4.  So now you have an HTML document with some semantics embedded in it.
    If you happen to have a browser plugin that understands the
    semantics, or you have a penchant for reading the source of web
    pages then you might be able to do something useful with it.

    I think a more sensible use case is that you use a delivery system
    that knows about Scholarly HTML.

    So, using a test plugin, for example this blog can now show you
    chemistry. Like so: <span
    rel="http://www.xml-cml.org/convention/crystallographyExperiment"
    resource="http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml">[http://ontologize.me/?tl\_p=http://www.xml-cml.org/convention/crystallographyExperiment&triplink=http://purl.org/triplink/v/0.1&tl\_o=http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1\_II/dn3132sup1\_II.complete.cml.xml](http://wwmm.ch.cam.ac.uk/crystaleye/summary/acta/c/2010/01-00/data/dn3132/dn3132sup1_II/dn3132sup1_II.complete.cml.xml)</span>

    You can try out the very simple plugin if you can work out what to
    do:

         

        hg clone 

        https://bitbucket.org/wwmm/schtml/

# <span id="cml-tool-first-look-id4"></span><!--id4--></a>Summary

What does all this mean? Why is it important?

What I have demonstrated here is a way of embedding some semantics in a
scholarly document in a way that builds on existing practice and serves
as a example for conventions for other disciplines. Instead of embedding
a JMOL viewer in my blog post by pasting in a lot of script-code, I can
cause a JMOL to be shown in appropriate circumstances. I will post a
more generic demo of reference and citation handling soon and there is
much more to Scholarly HTML to talk about, including packaging for
scholarly objects.

We have a few things happening here:

-   **We have a format:** a scholarly HTML convention designed to work
    in any web-processing environment or browser and to be as
    interoperable as possible, including supporting that important kind
    of interop, preservation, AKA <span
    class="spCh spChx201c">“</span>interop with the future<span
    class="spCh spChx201d">”</span>.

-   **We have tools:** in the last couple of days I have been able to
    put essentially the same Javascript call into three different web
    systems with little effort. The advantage of this approach is that
    if JMOL stops being supported, then we can replace our scripts with
    new ones that invoke a new molecule viewer, without having to touch
    the scholarly works that include chemistry. We are thinking about
    how to make a configurable master Scholarly HTML javascript library
    that can do useful things with citations, licenses and so on, and be
    extended to deal with stuff like chemistry.

-   **But we need better tools:** the tool chain I have shown here is
    probably viable for people who really really need to do this, or
    like playing with code, but we can do better. I can imagine tools
    built into Word and WordPress and so on that make this easy and
    transparent for authors.

And finally, yes Todd Carpenter this is partly a branding exercise, like
the Linked Data movement but we think it is for a good cause. If we can
get this right we can help the web be what it was meant to be from the
start, a platform for scholarship.

Copyright Peter Sefton, 2011. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en;"><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><!-- --></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/03/cml-tool-first-look_filesm40ca94ba.png.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content](http://ice.usq.edu.au/)
[Environment](http://ice.usq.edu.au/) project and published to WordPress
using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>

</div>

</div>
