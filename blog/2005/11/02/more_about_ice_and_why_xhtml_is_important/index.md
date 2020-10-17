---
Title: "More about ICE and why XHTML is important"
Slug: more_about_ice_and_why_xhtml_is_important
Date: 2005-11-02

---
<div>

Peter Albion of USQ has responded to my [last post on XHTML
export](../../blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)
from word processors.

There are a few points I think that need to be cleared up because I seem
to sending the wrong message about [ICE.](http://ice.usq.edu.au/) (Peter
also has a theory on my motivations for obsessing on HTML export but
I'll deal with that separately with more detail about why it is
important for usability and for ensuring the long term-sustainability of
our content).

Peter [says](http://edux.usq.edu.au/~albion/weblog/?p=117):

> Unless I’m missing the point, both ICE and GOOD are being developed
> primarily to enable academics to prepare well presented course
> materials that can be published equally well on paper or
> electronically on the web or CD-ROM. I think, though not having
> prepared a course that way I’m not sure, that each of the electronic
> formats includes a PDF version of the material to facilitate printing
> by students.

Yep. That's the idea. This will involve PDF for printing and HTML for
browsing, with all the materials packed up in IMS package format; that's
the standard for interchanging webs of course content between content
management (CMS) and learning Management Systems (LMSs).

This is important. ICE lets academics work in a word processor
(OpenOffice.org Writer this week, and Microsoft Word within a few more
weeks) and will automatically create both HTML and PDF. The PDF is
currently manually generated if you want it – a painless process.

ICE is not going to be painful to use, not as painful as trying to
create the same quality of output without an application like ICE to
help, anyway. There is no need to export HTML and clean up the results.
ICE does that. There is no need to worry about building navigation or
packaging as an IMS package. ICE does that for you. There will be no
need to export each document as PDF. ICE will do that for you. There
will be no need to back up your files. ICE will do that for you. No
problem working from home. ICE won't do that for you though!

Dr Albion [continues](http://edux.usq.edu.au/~albion/weblog/?p=117):

> If that is the case, then why bother with all the conversion from Word
> (or the Open Office equivalent) to XML and thence via XSLT to XHTML
> and/or PDF? Word, especially if used on a Mac where PDF capability is
> built into MacOS X, can easily enough generate PDF directly.

Why indeed. That's what my article was about but I obviously didn't make
myself clear. We need to work on systems to export HTML because it is
impossible to make a system export any given word processing document to
HTML, that's because HTML is more constrained than Word or the
OpenDocument format used by OpenOffice.org. And the vendors don't ship
standard templates or stylesheets that are any use, preferring to focus
on other areas of functionality.

-   **HTML** is important because that's what the web is made of, not
    PDF, or Word documents on the 'net. I'll write more on this, but
    that's the summary.

-   **PDF** is important because it is the best portable print-ready
    format. Yes you can print HTML and read PDF and in some cases you
    may even want to, but ICE is designed to produce both. It will make
    HTML courseware where each course is a richly-linked HTML package,
    and it will make PDF in a couple of flavours.

Ultimately each course in ICE will have:

-   **Authoring** in a familiar **word processor** complete with spell
    checking and other delights.

    (Peter could use an HTML editor instead if he wanted, but he
    wouldn't get the PDF because we will use OpenOffice.org to generate
    that – maybe Word too in future).

-   A stand-alone transportable web site for the course, which is
    **standards compliant** and usable as pure HTML.

-   **Easy linking** between parts of a course (which is basically
    impossible to do if you're working in Word and/or generating PDF).

-   Nicely **printable PDF** versions of each **part** of the course; so
    far we have been chunking courses into modules – roughly equivalent
    to chapters in a book.

-   **A complete 'book'** PDF of the whole course complete with a table
    of contents and cross references that match the links that are in
    the HTML version.

-   Embedded **interactive components** that are currently impossible or
    costly for most people to include in their courses.

NOTE: Not all the functionality described above exists yet but we have
made a good start.

Peter [suggests](http://edux.usq.edu.au/~albion/weblog/?p=117%20):

> Start with a good set of templates and you could get near enough to
> the same outcome for a fraction of the effort. The technology might
> not be so neat but it does work and would do the job.

> <http://edux.usq.edu.au/~albion/weblog/?p=117>

Um, yes – that's what we're doing, starting with **good set of
templates,** using whatever software we can and tying it together with
the smallest possible application to make it easy to use. Templates and
styles [are worth doing
even](http://ptsefton.com/blog/2005/03/02/use_styles) when there's no
web publishing involved, and if that's all that ICE achieves then we're
still ahead.

While we we're expending effort we will be saving many times that effort
for others and, we hope, improving the technical side of courseware
delivery by enabling more people than ever to create seamlessly
integrated web and print courseware without lots of mucking around.

My point in the [previous
post](http://blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)is
that if you start with a good set of templates you still need to a fair
bit of work to customize the HTML output of any word processor to
produce reasonable HTML. (Hands up who hasn't seen the awful results of
HTML export from Word.) I don't know what Peter thinks is near-enough
but what comes out of my version of Word or OpenOffice.org when I export
stuff that I've made using my template is not near enough.

Yes there has been some effort put into HTML export in the ICE project,
but not that much, we used prior work both from outsiders and from my
previous efforts elsewhere (basically I arrived at USQ a year ago with
working code that forms the basis of the conversion code in ICE, under
the free GPL license, and that code has now passed into USQ ownership,
and the template design we're using has been in use for ten years across
a number of organizations).

A lot of the effort in ICE is going into building infrastructure for
distributed authoring with version control and making the IMS packaging
process seamless.

The ICE team is currently working on easy creation of interactive
quizzing and easy embedding for multimedia, and doing so in a way that
will integrate with other USQ systems and provide the best possible
compromises for print and web delivery (such as allowing for transcripts
of audio for the print version, and automatically creating answers up
the back of the book for formative quizzes in the PDF version, while the
HTML version will be interactive).

So, I think while he understands the essence of what ICE is setting out
to do, maybe Peter Albion is missing part of the point. We are investing
some programmer time in this, but we have active pilot users who we hope
will help us make software that solves their problems, and allow USQ
(and others) to generate top quality courseware in HTML and PDF with
minimum effort, not just “near enough”. If we can save 100 people a few
hours or days per semester for the next few years by automating
previously manual conversion and re-formatting tasks that's worth doing
isn't it? If we can improve the flexibility of USQ's hybrid-delivery by
allowing Print, web and CD delivery with a format for every occasion and
taste from the same source, that's worth doing as well, isn't it?

And finally – Peter, and anyone else at USQ if you'd like a demo, email
<sefton@usq.edu.au> or call me on +61 (07) 4631 1640.

****

</div>
