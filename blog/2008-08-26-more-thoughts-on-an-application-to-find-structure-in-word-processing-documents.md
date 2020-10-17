---
Author: ptsefton
Comments: true
Date: 2008-08-26 03:24:02+00:00
Slug: more-thoughts-on-an-application-to-find-structure-in-word-processing-documents

Title: More thoughts on an application to find structure in word processing documents
Wordpress_id: 187
---

<div>

<div class="page-toc">

</div>

<div>

In my [last post I said I'd write
more](http://ptsefton.com/2008/08/26/a-courseware-authoring-dashboard-using-schematron.htm)
about how Ian Barnes' S*tructure Guesser* AKA S*tructure Sniffer[<span
style="vertical-align: super;"><span
class="footnote">1</span></span>](#ftn1)* might work, and how it might
be able to leverage
[Schematron](http://en.wikipedia.org/wiki/Schematron).

The sniffer is part of Ian's [Digital Scholar's
Workbench](http://www.apsr.edu.au/word/) concept, where you can upload
an unstructured word processing document, and use the workbench to add
explicit structure in as automated a way as possible. Explicit structure
really helps in being able to convert the document to other formats such
as HTML for the web, or structured PDF with a table of contents, but
also for preservation formats that might keep the words and other
content for posterity without necessarily worrying about exact
formatting. Ian has looked at using [DocBook](http://docbook.org/) for
this, but I reckon HTML might be good enough, and I know others are
thinking the same thing<span class="T5">[<span
style="vertical-align: super;"><span
class="footnote">2</span></span>](#ftn0)</span>.

Ian's looked at the statistical approach to guessing structure used by
in the [Lemon8-XML](http://pkp.sfu.ca/lemon8) project, found that
particular implementation wanting and is now thinking about more of a
machine learning approach.

I too have been thinking about how this application might work for a
while now and I'm getting increasingly enamored of the idea of using an
HTML interface, something like this:

1.  **Upload** a word style-free processing document to a web site.

2.  You see an **interactive preview of an HTML version of the
    document**, complete with a full table of contents (so you can see
    where the sniffer application thought the headings were).

    Interactive? Hover the mouse over a top level (h1) heading in the
    preview and see some details about why the machine formatted it that
    way, such as <span class="spCh spChx201c">“</span>Paragraphs at 18pt
    (10 instances) and 19pt (1 instance) Helvetica look like Heading
    1<span class="spCh spChx201d">”</span>. You'd be able to correct the
    machine, either on a case by case basis or wholesale.

    Another area where some interaction might be needed would be in
    disambiguating various kinds of indented text, some indentation
    might mean *block-quote* some might be example while other text
    might just be, you know, indented. We had to add an indent style in
    addition to the `bq1` (block-quote) style to ICE to support this
    because some authors just, you know, want to indent stuff.

3.  Once you were happy with the HTML view of the document, there would
    be an option to **improve your original by adding styles** without
    changing its presentation too much (Did I mention? You too should
    [use styles](http://delicious.com/ptsefton/usestyles).) or you could
    just use the rendition and leave the original alone. Either way, the
    choices you made would constitute feedback to the learning system.
    So even if you don't choose to use styles, the next time it sees the
    same document it will be able to handle it better.

So where does Schematron come into this? Well, leaving aside the (very)
hard problem of actually writing the learning system, that system could
**generate Schematron rules**, which could be used to annotate the
original document with suggested styles for each paragraph. Having done
that, you could then feed the document into the existing ICE HTML
formatter, which is style-driven and it could use the suggested styles
to render the document.

These rules can be hierarchical meaning that based on certain cues
different sets of rules might apply. For example, there might be a
family of documents which all come from a user who uses Palatino 11pt
for the main text, and makes use of an idiosyncratic mixture of
formating and styles <span class="spCh spChx2013">–</span> the learner
could derive rules for that situation. I know nothing about this kind of
thing, I wonder if it would be like the [Na<span
class="spCh spChxef">ï</span>ve Bayseian in the Old
Bailey](http://digitalhistoryhacks.blogspot.com/2008/05/naive-bayesian-in-old-bailey-part-1.html)
where a machine is trained to classify trials.

Using Schematron rules would mean that they could also be written or
tweaked by humans. Returning to the example before, a human could add a
rule that if a bit of text is indented relative to the text around it
and it contains something that looks like a citation <span
class="spCh spChx2013">–</span> which could mean either that it uses
something like a Zotero field, or is formatted like a citation with
brackets or a footnote <span class="spCh spChx2013">–</span> then it's a
blockquote.

This would be a nice modular approach. Chances are we're going to be
looking at Rick Jelliffe's in-zip Schematron for use on Open Document
Format documents, so the sniffer could piggyback on that<span
class="T5">[<span style="vertical-align: super;"><span
class="footnote">1</span></span>](#ftn2)</span>.

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote">[1](#ftn1-text) Also know as that by **me** , at
least.</span>

</div>

<div style="font-size: .9em;">

<span class="footnote">[2](#ftn0-text) And no, OOXML and ODF are not
necessarily the answer for preservation although they are important,
I'll expand on this in a future post as I think about a presentation for
[Open Standards 08](http://www.open-standards.com/) .</span>

</div>

<div style="font-size: .9em;">

<span class="footnote">[1](#ftn2-text) Actually there is an issue with
this, it's not that simple to write rules that work on the formatting in
an ODT file, cos it uses these automatically defined styles that
introduce a layer of indirection. We could consider a pre-processor that
*remembers* these automatic styles between documents, it would also
probably need to annotate docuents with some kind of weighted score like
they use in Lemon8-XML.</span>

</div>

</div>

</div>
