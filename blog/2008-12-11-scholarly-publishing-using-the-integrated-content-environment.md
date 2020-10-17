---
Author: ptsefton
Comments: true
Date: 2008-12-11 13:45:13+00:00
Slug: scholarly-publishing-using-the-integrated-content-environment
Title: Scholarly Publishing using the Integrated Content Environment
Wordpress_id: 264
---

<div>

<div class="page-toc">

-   [1 Orientation](#id1)
-   [2 Introduction](#id2)
-   [3 About ICE](#id3)

</div>

<div>

2008-12-11

<span class="meta-familyname">Peter Sefton </span>

University of Southern Queensland

<p>
<script type="text/javascript">
<!--
h='&#x75;&#x73;&#x71;&#46;&#x65;&#100;&#x75;&#46;&#x61;&#x75;';a='&#64;';n='&#x73;&#x65;&#102;&#116;&#x6f;&#110;';e=n+a+h;
document.write('<a h'+'ref'+'="ma'+'ilto'+':'+e+'" clas'+'s="em' + 'ail">'+e+'<\/'+'a'+'>');
// -->
</script>
<noscript>
sefton at usq dot edu dot au
</noscript>
</p>
# <span id="id1"></span><!--id1--></a>1 Orientation

This is another blog post based on a presentation. What I've been doing
lately is working on each presentation as a document with embedded
slides before I give it. I think that working this way makes for a more
coherent delivery and I can take a bit of time to edit the thing into
something a bit more useful than a PowerPoint presentation[<span
style="vertical-align: super;"><span
class="footnote">\*</span></span>](#ftn1). Of course it's only ever half
done by the time I give the talk so I have to come back and finish it
off and edit to make it reflect what I think I actually said.

Here's the notes for my talk at the recent [Open Access Publishing
workshop run by APSR](http://www.apsr.edu.au/open_access_publishing/).
The website bills it as <span class="spCh spChx201c">“</span>A two-day
Public Knowledge Project Workshop<span class="spCh spChx201d">”</span>,
while the program says it was a <span class="spCh spChx201c">“</span>a
PKP User Group Workshop<span class="spCh spChx201d">”</span>, either way
the idea was to talk about issues around the mission of and the software
produced by the PKP project. Website says:

> The Public Knowledge Project is a research and development initiative
> directed toward improving the scholarly and public quality of academic
> research through the development of innovative online publishing and
> knowledge-sharing environments. [More...](http://pkp.sfu.ca/node/1410)

This was the last APSR event and I'd like to take the opportunity to say
thanks to the APSR crew, particularly Margaret Henty for all the APSR
events of various kinds over the last few years. These events got us
started in the repository business, APSR events helped bootstrap the
RUBRIC project.

I started with this abstract:

**Abstract:** The Integrated Content Environment (ICE) is an open source
software application and service-platform for word processor based
academic authoring, originally built to support the University of
Southern Queensland's flexible-delivery courseware but now expanding
into more general scholarly publishing.

We will show a myriad of ways that ICE can be used in the academy.
Starting from document creation, ICE uses generic word processing
templates which capture the structure and semantics of scholarly
documents. The system manages collaborative works in progress using a
distributed version-controlled repository, and can publish works to
HTML, PDF and domain-specific XML schemas. It has been integrated with
several other systems, including the Moodle Learning Management System
and DSpace, ePrints and Fedora repositories.

Specific examples will include an journal which uses the ICE publishing
system, demonstrations of semantic-web publishing for theses (an outcome
of the JISC-TheOREM ICE project) and institutional repository
integration.

# <span id="id2"></span><!--id2--></a>2 Introduction

The Integrated Content Environment (ICE) is an open source software
application and service-platform for word processor based academic
authoring, originally built to support the University of Southern
Queensland's (USQ's) flexible-delivery courseware but now expanding into
more general scholarly publishing.

ICE is a product of a software development team now located in the
Australian Digital Futures Institute
([ADFI](http://www.usq.edu.au/adfi)) at USQ. The Institute is involved
in a research and development projects in eLearning and eResearch.

When I first wrote up this talk, I thought it might come out a bit
negative. I had this paragraph:

> This presentation I will show-off ICE and talk about how some of its
> modules can be used in and mashed-up with other systems.
> Unfortunately, the conclusion to this presentation is not <span
> class="spCh spChx201c">“</span>and they all lived happily ever
> after<span class="spCh spChx201d">”</span>. After showing some of what
> ICE can do, a lot of which I believe is very important to the
> scholarly enterprise, I will go on to talk about the challenges that
> lie ahead. All we have to do is change the entire scholarly publishing
> model and along the way make our publishing systems much more flexible
> and far reaching.

But actually, the tone of the meeting made it a bit hard to summon the
doom and gloom. We had a very productive exchange on how we might mesh
our technologies and experience with the PKP systems.

# <span id="id3"></span><!--id3--></a>3 About ICE

I kicked off with some credits. ICE is a team effort, I make the most
noise but I don't do the most work.

<div class="slide">

# Credits (in random order)

-   Ron Ward

-   Pamela Glossop

-   Oliver Lucido

-   Daniel de Byl

-   Bron Chandler

-   Linda Octalina

</div>

ICE is more than one thing. See the [website](http://ice.usq.edu.au/).

<div class="slide">

# ICE components

-   Word processing templates (MS Word and OpenOffice.org)

    Easy to use, generic, extensible structured editing.

-   A web application for converting word processing documents into HTML
    and PDF, packing and disseminating them.

    (This normally runs on the desktop <span
    class="spCh spChx2013">–</span> one copy per user)

-   A set of APIs so that ICE components can be used in other systems.

</div>

The templates are at the heart of the ICE system. They provide a simple
generic way to structure word processing documents. It is well known, if
not a scientifically documented fact, that using a word processor to
create web pages typically results in, shall we say sub-optimal web
sites.

ICE is style-driven, not as in fashion conscious, but as in
styles-as-named-bundles of-formatting which have structural or semantic
significance.

<div class="slide">

# ICE is style driven

About the only styles your word processor can export to a web page are
Heading 1 and family.

So ICE defines styles for:

1.  **Headings** <span class="spCh spChx2013">–</span> with and without
    outline numbering.

2.  **Lists** <span class="spCh spChx2013">–</span> lots of flavours
    including bullets and definition lists and various was of counting
    enumerations.

3.  **Blockquotes** and **preformatted** text.

</div>

To convert word processing documents to HTML and PDF ICE uses
OpenOffice.org. ICE converts Word documents to the OpenDocument Format
behind the scenes, a step which is not necessary with OOo Writer. And
from there there's code to turn ODF into HTML. ICE uses Writer to
generate web-ready images from the various graphic formats, equations
etc.

ICE can be used in lots of ways. It started life as a courseware
authoring system. At USQ we have a decades-long tradition of producing
printed distance education materials, and for the last decade or so of
making the same content available on the web, with added webbish
goodness.

<div class="slide">

# ICE for courseware

<http://ocw.usq.edu.au/course/view.php?id=13>

<span
style="display: block"><a name="Object1"></a>![Object1](htt%0Ap://ptsefton.com/wp-content/uploads/2008/12/69b284ecs443x314.jpg)</span>

</div>

Starting from document creation, ICE uses generic word processing
templates which capture the structure and semantics of scholarly
documents. The system manages collaborative works in progress using a
distributed version-controlled repository, and can publish works to
HTML, PDF and domain-specific XML schemas. It has been integrated with
several other systems, including the Moodle Learning Management System
and DSpace, ePrints and Fedora repositories.

<div class="slide">

# ICE for theses

ICE can manage book-length content like theses quite well:

-   Creates HTML and PDF

-   Annotations for supervisor comments

-   Integrated data visualizations

-   Automated repository deposit

</div>

While ICE can be used to manage thesis drafting it doesn't really manage
the other processes that go on, Particularlty the examination process
where PKP's Open Journal Systems (OJS) might help <span
class="spCh spChx2013">–</span> OJS is used at USQ to manage the thesis
review process for *some* theses.

Speaking of journal systems I showed an example of journal which was
published using the ICE publishing system:

<div class="slide">

# A Journal

<http://www.usq.edu.au/electpub/e-jist/docs/vol10_no1/default.htm>

ICE gave no help with the journal workflow, but it did create HTML and
PDF renditions of all articles

</div>

There's very little overlap between ICE and OJS.

<div class="slide">

# ICE wrt OJS

<a name="Object2"></a>![Object2](/wp-content/uploads/2008/12/bd1fb1ds402x160.jpg)

</div>

I was able to demonstrate some work that Linda Octalina has been doing
to integrate ICE conversion services into OJS. She's added a basic
feature where you can upload an ICE document and instead of treating is
as a monolithic word processing file, OJS fires it off to ICE to be
converted into other formats, and then shows them to you:

<a name="graphics1"></a>![graphics1](/wp-content/uploads/2008/12/m58c8a5fds554x275.jpg)

In the above screenshot you can see how OJS now has an HTML and PDF
rendition for each file, If we could make this work then OJS would be
able to use ICE features like embedding data such
as[chemistry](http://ice.usq.edu.au/presentations/demos/cml_ice_ice.htm)
or inline annotations. Here's a screenshot that covers a few ICE
features:

<a name="graphics2"></a>![graphics2](/wp-content/uploads/2008/12/m384dbd62s554x370.jpg)

<div class="slide">

# ICE lessons

What would these mean for the PKP tools?

-   **Feedback** early and often.

-   We need '**bundle aware**' content stores so we had to build one.
    (Disseminators, Fedora Commons style are another option)

-   People **can and will** structure their documents if there is a good
    reason for them to do so.

-   Learning structured word processing is a **key skill**<span
    style="font-weight:normal; "><span class="T3"> </span></span>for
    academics <span class="spCh spChx2013">–</span> why are we not
    teaching them how?

-   We have done the work to define a **generic structured document
    profile on top of ODT** (didn't realise that's what we were doing!)

</div>

The final point above, about a generic structured document profile
seemed to resonate with MJ Suhonos from PKP. We've corresponded for a
while about getting ICE and his Lemon8-XML project better aligned. Now
that we've met s and had a couple of glasses of wine that should be a
bit easier.

If MJ decides to use ODF we'll be there to help with the process of
getting the Open Document Format word processing format (ODT) plugged
into Lemon8-XML as a back-end, a byproduct of which will be what I was
hoping for in my previous post, [a way to bring unstructured documents
into the ICE
fold](http://ptsefton.com/2007/12/12/lemon8-xml-more-information.htm).

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote">[\*](#ftn1-text) As I always say a used
PowerPoint (particularly without speaker notes) is about as much use as
a used condom. Fun for those who were there, maybe, but lacking appeal
for those who were not.</span>

</div>

</div>

</div>
