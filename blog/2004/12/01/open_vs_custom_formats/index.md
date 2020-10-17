---
Title: "General purpose document formats, again"
Slug: open_vs_custom_formats
Date: 2004-12-01

---
Emacs-addicted geek Jon Udell, who is not to be dismissed lightly has
returned to the topic of [open document
formats](http://weblog.infoworld.com/udell/2004/11/30.html#a1123) vs
custom schemas and where XHTML fits in. I have been working with the
software development team at USQ's Distance and e-Learning Centre on
this issue, and we are looking at bridging the gap between
generic/general purpose and custom formats.

Jon revisits Tim Bray's
[piece](http://www.tbray.org/ongoing/When/200x/2004/06/17/CustomSchemas)
suggesting that XHTML might be a better choice than a custom XML dialect
in many situations:

> No, I'm not saying that everyone should use XHTML or the
> OpenOffice.org formats for every document in the world. But I do think
> that the cost of rolling your own is a lot higher than you think, and
> you should really try to avoid doing that if you possibly can.

Jon's conclusion:

> I'm not ready to go along with the other conclusion he reaches in that
> posting -- that custom schemas are a red herring. But I agree that
> XHTML is more valuable than most people think. For the vast majority
> of useful documents, it can have as much structure as we need, and for
> the rest it can be extended internally with namespaced inclusions. But
> the real power arises from its hypertextual nature. For me,
> increasingly, there is no office, and there is no desktop, there is
> only a network of linked documents. A successful open document format
> will have to be supremely well-adapted to that environment, as XHTML
> is.

I have written on this matter numerous times and [started the
slow-moving Word Processor Interoperability project](wp_interop_project)
(which does at least have a template to download now) to look into a
practical implementation of Tim Bray's idea.

I am now investigating this in new context. At USQ there is a custom
schema for courseware for print, web and CD delivery, known as GOOD
(Jacek Radajewski will present a
[poster](http://www.cs.mu.oz.au/~alistair/adcs2004/program.html) on GOOD
at the Ninth Australasian Document Computing Symposium (ADCS 2004),
December 13 in Melbourne).

We are considering doing both: maintaining the custom schema at the back
end, with a more flexible front-end system for creating content.
Obviously, a generic general-purpose document format is more permissive
than the back-end GOOD, so there will be some intervention to get
documents from the authoring system 'up the
[hill](blog/2004/05/03/potentialenergy)' into GOOD. I think we have a
few tricks that will minimize the manual conversion process, though.

The GOOD system is a custom schema (expressed as a DTD) - with
chapter-level elements that structure the overall flow of course
materials in a standard way across a large corpus of offerings, and a
content model that is appropriate for educational content. It also has
an assessment module that can drive both print and computerized quizzing
with hooks into the University grade-book at the back end, in
PeopleSoft.

GOOD is now used in the Distance and e-Learning Centre, and by a some
course leaders. It produces print, web and CD offerings automatically
from the XML source. To get it into wider use I have been asked to look
at an easy-to-approach, cross-platform editing system. One thing that we
are exploring is to use XHTML as the basis of an easier-to edit format,
with the target remaining the GOOD system for production.

It is early days yet, but these are the ingredients we are considering
for the new system (and we *will* be seeking further input and pilot
users from the university):

-   A word processing template. Related to [the one in the Word
    Processor Interoperability project](wp_interop_project) based on
    OpenOffice.org, with a Microsoft Word version as well.

<!-- -->

-   Fragmentation. Rather than trying to author an entire course in one
    document each 'chapter' will have its own document. This will allow
    broad control over the content of parts, by using different template
    variants for different parts of the course, e.g. providing for
    quizzes in study modules but not in the introduction.

<!-- -->

-   Ways of consistently marking-up pieces of content such as reading
    activities using word processing devices like tables so they can be
    mapped to the GOOD schema.

<!-- -->

-   A web-based content management application to manage the fragments
    of a course. This application will take on the role of a schema
    *above* the chapter level, controlling the way the pieces are
    assembled and acting as a hub for the *network of linked documents*.
    This will also map to the IMS Manifest format for packaging course
    materials, although that format has some problems with
    hypertextuality as I have [noted
    here](blog/2004/08/06/implementingims).

<!-- -->

-   XHTML templates for those who want to work in their favourite HTML
    editor.

<!-- -->

-   Some human intervention from experienced editorial staff to help raw
    documents achieve GOODness.

It is important to remember that at the low level of granularity there
would be a relatively free form 'canvas' to draw on, using something not
too far from XHTML, with its generic heading, table and list elements,
but with domain specific extensions for things like activities, or
learning outcomes. The extensions would be implemented in the Word
processor using the least-ugly hacks available. At a higher level, there
would be a schema-like content system that would stitch the smaller
granules together according to domain specific rules, so you would be
able to specify the top level structure of a course and have it drive
the content management system; at least that level would be guaranteed
to comply with the house schema.

I know that such a system, with high-level schematization that ties
together loosely structured granules can work well, as we used it in
NextEd's Continuous Publishing System (CPS), described here in this
[poster paper for
AUSWEB04](http://ausweb.scu.edu.au/aw04/papers/edited/sefton2/paper.html),
but the CPS was not trying to map to a complex schema. How much human
intervention will be required to map word processor-produced or edited
content, where it is virtually impossible to enforce constraints on
structure, back to the GOOD structure is an open question; we will have
to find out from trials.

\$LastChangedDate: 2004-12-01 01:29:05 -0600 (Wed, 01 Dec 2004) \$
\$Rev: 108 \$
