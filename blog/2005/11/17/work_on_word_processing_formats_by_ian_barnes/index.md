---
Title: "Work on word processing formats by Ian Barnes"
Slug: work_on_word_processing_formats_by_ian_barnes
Date: 2005-11-17

---
<div>

On Wednesday I was a guest at the **Australian Partnership for
Sustainable Repositories** ([APSR](http://www.apsr.edu.au/)) planning
day, which helped me get my head around the diverse projects coordinated
under the APSR banner. We're going to be talking a lot with APSR at the
[RUBRIC](http://www.rubric.edu.au/) project where I work.

The highlight for me was a talk by [Ian
Barnes](http://www.bloglines.com/blog/barnes) of
[ANU](http://www.anu.edu.au/) on Sustainability in word processing
formats. He was looking at how you can take a word processing document
and turn it into an archive-quality XML document.

I liked his presentation partly because Ian is working with our
[ICE](http://ice.usq.edu.au/) templates, developed at USQ. This is
interesting because it means that our **open source project is
working**:

1.  we have **more smart people** testing and extending the styles, and

2.  the ANU work is trying **new things**.

Ian said that for a sustainable format you need something that is:

1.  XML

2.  Non proprietary, and open. (Ian said non-commercial)

Here was the list of contenders for an archival document format:

-   [DocBook](http://www.docbook.org/)

-   [TEI](http://www.tei-c.org/)

-   XHTML

-   Custom schemas

Ian voted off these two:

Custom schemas
:   Because of the costs and obvious unsustainability involved

XHTML
:   Because it is essentially flat. While XHTML does allow nesting, if
    you start using particular conventions for nesting elements then
    that's a custom schema, Ian argued. I'll come back to this point.

Ian **picked DocBook** for his demonstration system, and as a likely
contender for long term document storage, because of the **existing
toolchain**.

Using OpenOffice.org Writer, he was able to demonstrate a **complex
ICE-based test document** that had all sorts of nested lists, block
quotes and pre-formatted text and images. Saved it into a directory and
was able to show via a Java-based web server (Cocoon) the original
OpenDocument Format document (the XML), a **DocBook version** and then
an **XHTML version**. It also does **PDF**.

I **liked** the new direction, and the idea of plugging into the
**DocBook toolchain** because of all the stuff you get for nothing, but
later discussions indicate there **might be some problems**,
particularly with documents that mix numbered and un-numbered headings,
and with jumps between heading levels (like putting heading 4
immediately after heading 1. What do you put in your archival format in
a case like that where the author wants the feel of small divisions with
a low-level heading, but the schema may insist that that is not allowed?

Which brings me to one of the **constraints on this exercise** – if
you're going to be capturing with a word processor you need to live with
what it's capable of, and your software will always have to build any
nested structure out of a flat series of paragraphs and lists, so I'm
not convinced that using DocBook buys all that much more than using
existing tools, which could, in time be written for a constrained
version of XHTML. But I am intrigued, and also am all for using existing
software where possible so I'd like to **see how far** Ian and the ANU
team can take this.

I got the chance to go into more detail with Ian after lunch (thanks
APSR). He's got **a nice set of chained XSLT stylesheets** that turn the
ICE styles in a word processing document into DocBook by doing one bit
at a time. This is a more manageable approach that the one I took with
the original ICE XSLT; at that stage I thought we'd need to have a
single XSLT because I had this (very wrong) idea that the export system
in OpenOffice.org was worth using.

But even with Ian's much simpler chain of stylesheets it's at the limits
of the useful range for XSLT, it might be better to **switch to a
procedural version** using a 'normal' language like Java or Python.
There's someone else working on this that I know of, but no release yet.

****

</div>
