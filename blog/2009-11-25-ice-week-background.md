---
Author: ptsefton
Comments: true
Date: 2009-11-25 01:52:26+00:00
Slug: ice-week-background

Title: ICE Week, background
Wordpress_id: 450
---

<div class="rendition-links">

<span class="pdf-rendition-link">[PDF
version](/wp-content/uploads/2009/11/ICEWeek1.pdf.pdf "View the printable version of this page")</span>

</div>

<div class="page-toc">

-   [History](#id1)
    -   [FrameMaker](#id2)
    -   [LaTeX](#id4)
    -   [Lessons?](#id5)
    -   [GOOD](#id6)
    -   [CPS](#id10)
    -   [ICE](#id13)
-   [Future directions?](#id17)
-   [Working parties](#id19)
-   [References](#id21)

</div>

<div class="body">

<div>

This week at the [Australian Digital Futures
Institute](www.usq.edu.au/adfi) we're taking a look at ICE: the
[Integrated Content Environment](ice.usq.edu.au/), an open source
software system which is now part of the core infrastructure at USQ.

The ADFI team are spending all week exploring new stuff and considering
what ICE 3 might look like and how it might fit with or merge with our
other project, [The
Fascinator](fascinator.usq.edu.au/desktop/desktop.htm).

The week kicked off with a couple of sessions with the USQ community.
The first session was by invitation, we asked a number of USQ staff who
have engaged with ICE over the last few years along, including some who
have been vocal critics. The second session was an open-invitation ADFI
event. In both cases we went through this agenda:

-   How did we get here? (and what did we learn?)

-   Your concerns

-   What should we do next?

Bron Chandler has [summarised some of the points
already](ice.usq.edu.au/blog/2009/11/23/ice-the-future.html), It's half
way through the week now and I have been jotting down my thoughts in
this post since Monday. This is a bit long winded, but I hope it is a
useful record of some of the lessons learned from the last few years of
content-creation systems at USQ. It's on my blog, so it's my opinion,
comments are welcome to expand, clarify, correct or argue.

Remember that USQ is a distance education-specialist and produces lots
of courseware, book-length study materials that are delivered in
print/PDF and/or HTML to thousands of students. Teaching and learning is
not all about courseware, of course, but courseware is a big part of
what we do, and that's what ICE was developed for.

# <span id="id1"></span><!--id1--></a>History

## <span id="id2"></span><!--id2--></a>FrameMaker

Adobe FrameMaker has been used since the 1990s at USQ to produce
courseware for print. It's still used for some print-only courses
(largely ones with lots of maths I think). The problem with our use of
FrameMaker is all the manual steps involved. Authors submit manuscripts
in Word, these are converted to Frame by operators, largely by hand, and
then proofing is done by the academics in Word with track changes, or on
paper with corrections. Staff in Electronic Publishing Services then
have to update the Frame documents change-by-change. This legacy process
is being phased out, but these things take time.

USQ has never had a fully automated web-conversion process for
FrameMaker documents although there have been a couple of attempts, and
there is now a process for converting to ICE in a semi-automated way. In
a decidedly un-automated process from 1999 or so until 2003-ish USQ used
to send FrameMaker documents over to NextEd at the USQ Toowoomba campus
to have courses converted to HTML by hand. This was a process which I
recall costing circa \$5000 US per course payable every semester,
because of the almost complete lack of automation they had to be redone
with each offering. Apparently some of the HTML courses from the NextEd
days are still extant and being maintained using DreamWeaver and the
like.

Bron Chandler and Ron Ward and I from the current ADFI team all worked
for NextEd, and we still go to the support-group meetings from time to
time but I think we're getting better.

At NextEd I devised a word-processor based publishing system built
around FrameMaker which would have slashed the cost of producing courses
for both print and HTML at USQ. The system used Frame's structured
editing mode using XHTML as a document model, so you could produce high
quality print documents and export them straight to the web <span
class="spCh spChx2013">–</span> and because it used styles in FrameMaker
you could import word processing documents and have FrameMaker
automatically add structure. NextEd got a pilot system up in a few
weeks, with help from [Allette Systems](allette.com.au/). I thought it
was rather a good idea but USQ was not interested in that, or our other
publishing system the CPS, because they had other plans, in the form of
an XML system.

## **<span id="id3"></span><!--id3--></a>Lessons learned?**

I think it was pretty broadly recognised that all the manual work
involved in producing courseware this way was not sustainable and not
sensible which is why USQ tried to build an XML publishing system. The
main lesson here is that systems change can take a long time in a
university and document conversion is always slow and expensive, which
is why we still have some FrameMaker documents.

## <span id="id4"></span><!--id4--></a>LaTeX

Before looking at the XML world, though, there's another legacy system,
LaTeX.

-   Used in some technical disciplines.

-   No universal web conversion (really, there isn't).

There's not a whole lot to say about this, the people who know how to
use it continue to do so to produce courseware, and it continues to make
no inroads into other disciplines, I hear, though, that in engineering
they are starting to get new staff who don't know LaTeX. The problem is
that Word and OpenOffice.org are not great when it comes to very large
amounts of Maths, and ICE uses OpenOffice.org to make PDF, which is a
bit buggy for maths so there is still a place for LaTeX, even if it is
embedding LaTeX in word processing documents and automatically rendering
the maths at least until further investments are made in ICE to improve
its MathML support. USQ needs to work this out.

Participants in the sessions this week emphasised some of the good
points of LaTeX:

-   BibTex referencing is vastly superior to anything else, we heard.
    (I'm not an expert but I believe (via Bruce Darcus) if this is true
    it is only so for some scientific disciplines. ICE works with the
    university supported EndNote and with the open source Zotero).

-   LaTex's rendering is better than we produce using ICE/FrameMaker.
    (Certainly true for maths, probably not that important for most of
    the rest of what we do <span class="spCh spChx2013">–</span> but
    even if you can produce PDF with links is that enough? For web use
    I'd like to see more usable fluid materials like the stuff we did in
    ICE-TheOREM with live, interactive chemical models embedded in web
    pages, or interactive maps for documents with geographical
    references, easy in HTML and not possible in PDF.)

We had a follow-up meeting about LaTeX (and online document editors,
more of which later) and reached the conclusion that ICE might be able
to help manage LaTeX files and bundle them as courses, if communities of
users could agree on which LaTeX stlyes or macros to use. Some people
insist that for maths-heavy courseware the only practical delivery
medium is PDF.

## <span id="id5"></span><!--id5--></a>**Lessons?**

We've learned that where a community is using a tool that meets their
requirements it is best to leave them to it. Apparently, though there is
pressure on some of the LaTeX users to use ICE as per USQ policy. Me, I
think the policy should be based on performance outcomes not mandating
how people should achieve the outcomes. I'd love to see a
competitor/successor to ICE emerge from someone who's a bit feral and
won't use the corporate tools (but it aint going to be LaTeX-based).

## <span id="id6"></span><!--id6--></a>GOOD

The GOOD system (Generic Online Offline Delivery) was USQ's was a very
big, complicated bespoke XML system which never realised its claimed
potential. The idea was to build a semantically aware highly structured
courseware production system.

There were several issues with GOOD:

-   Converting content from FrameMaker was a very **costly, slow
    process.**

-   Despite the best efforts of the team to design the one true Document
    Type Definition (a DTD was an ancient kind of document schema they
    had back in the twentieth century) for USQ courseware, there was
    **exception after exception** as more disciplines came on board and
    wanted different conventions, referencing systems, extensions to the
    table model and so on and so on, with every discussion ending up in
    a big meeting to see whether a change was needed. Being a university
    we didn't count the cost of those meetings, but I bet it added up,
    let alone the cost of all the changes.

-   It was slow to render documents, so changes like sorting out
    pagination or fixing typos were very painful.

-   But the biggest issue was that **almost none of the lecturers used
    it, see below**.

### <span id="id8"></span><!--id8--></a>**Lessons?**

There were lots of things that USQ should remember from the GOOD
experience, most of which were well understood in the XML/SGML community
before the project started, but there's nothing like experiencing these
things for yourself:

-   **Top-down mandating of system is risky**, particularly if the
    people you're telling what to do are academics in an Australian
    university. They're not process workers who will take orders.

-   **Don't build a big system without sorting out basic issues** like
    what editor you are going to use and testing to see whether the user
    community will be able to use it and actually do so.

-   The system produced HTML and PDF from the same source document
    alright but then so did the demo system we built at NextEd using
    FrameMaker at about 100^th^ of the cost. I think maybe GOOD would
    have had more traction i**f all that semantic markup had been used
    to better effect**, so people could see the point of the extra work
    and cost involved. When I joined USQ I worked with the GOOD team
    (particularity Oliver Lucido who now works with us in ADFI) to demo
    some of the potential but our proposals never made it into the
    learning management system which the students used.

## <span id="id10"></span><!--id10--></a>CPS

The NextEd Continuous Publishing System was my baby at NextEd, sponsored
by another current USQer Cameron Loudon who ran the conversion team. It
was a word processor based HTML publishing system which many of our
clients used and which was used for the company intranet. But even when
customers didn't fully embrace it for courseware, we were able to use it
internally to dramatically cut costs.

-   Server based like ICE server.

-   Used an earlier version of ICE templates (inherited from Standards
    Australia where I helped set them up for writing standards).

-   No print output.

-   Banned at USQ's Distance and e-Learning Centre. (True, even though
    there was a small user community who liked it, and it was open
    source it was considered a risk to use. I think one of the issues
    was whether the open source code was truly clean-room open, and then
    there was the GOOD system with which the CPS competed (except for
    the lack of print output)).

### <span id="id12"></span><!--id12--></a>**Lessons**?

The CPS worked pretty well. Ron Ward did most of the work on the later
versions, and together we learned a lot about modern software
development and how to keep things as simple as possible. For example
lots of the features we thought we needed it turned out we didn't and
even with the simplest possible model we could think of for
document-reuse across semesters it was too hard for most users to get
their heads around.

It was eventually made open source, but too late, meaning that all that
work died with most of NextEd's business. I resolved that if I worked on
software for other people again I would either (a) get paid substantial
amounts of money or (b) get to release the software under an open source
license so I could build on it in future, never mind the other potential
benefits of open source software.

The big thing that I miss about CPS which is so far not present in ICE
is that it was very much driven by metadata, which means that courses
self-assembled as you uploaded and described parts of a course. This is
an area we are exploring with our
ICE/[Fascinator](fascinator.usq.edu.au/) mashup which we hope will be
used to serve all the universities policies and procedures in a faceted,
browse/search interface before too long.

## <span id="id13"></span><!--id13--></a>ICE

Regulars here probably know more than they want to about ICE and you can
read about it on the website, and in various papers (Sefton et al. 2009;
Sefton 2006; Sefton 2007).

-   Originally called GOOD-lite (2004) for (internal) marketing reasons
    and changed immediately to The Integrated Courseware Environment for
    (external) marketing reasons. (Then we changed Courseware to Content
    to go after a grant.)

-   Approved within DeC without the benefit of the kind of USQ
    governance we now have.

-   Grew organically from a user-base of one.

-   Core system in 2009.

### <span id="id15"></span><!--id15--></a>Lessons?

Lots of lessons, but we're still working out what they are. The big ones
for me are:

-   Trying to build a replicated version controlled content management
    system as well as the core ICE function which was to make HTML and
    PDF courseware from word-processing files was a big mistake, cost us
    a lot for limited benefit. My fault, I think for getting carried
    away with [architectural
    space-travel](www.joelonsoftware.com/items/2008/05/01.html). We're
    going to see if we can get away without using Subversion or anything
    remotely like it for future versions and focus on the things that
    ICE does that no other system does, mainly having good generic word
    processing templates and turning them into HTML. Yes it is strange
    that no other open system does this but no, we don't know of
    anything comparable.

-   The agile, organic approach worked well to make the actual software
    but because we started the project under local governance, just
    before a big project to centralise uni IT services, by the time it
    was ready to roll out there was a whole new governance framework in
    place and it took longer than it should to navigate that. Future
    projects need to move into core mode much more smoothly.

# <span id="id17"></span><!--id17--></a>Future directions?

I put up a slide for discussion with some bullet points, some brief
notes here on each point:

-   **Concept Maps? ([Bron's
    summary](ice.usq.edu.au/blog/2009/11/25/ice-concept-maps.html))**

    Mark Phythian and co (Phythian & Das Gupta 2008) have been trialling
    Concept Maps as a learning and teaching aid. Mark started by
    wondering if Concept Maps could provide a navigation aid for
    courses, then started looking at how they might help learners. We
    had a meeting on Tuesday which affirmed that ADFI will keep helping
    with this line of research, with a view to building open tools for
    the use of concept maps in learning, teaching and research as
    indicated by ongoing evaluations like Mark has been doing.

    We also heard about Mind Maps (don't get me started on that one) and
    something called Argument Maps which were new to me . Duncan is
    exploring how [work on Aus-e-Lit](www.aus-e-lit.net/%5C) might be
    used in our tools to build concept-map-like navigation or
    aggregation in our tools.

-   **Efficiency:**

    There were a few points that came down to ICE efficiency and
    performance; there are already processes under way to make ICE more
    responsive by getting some of the large video content out of it and
    into more suitable repositories, building towards university-wide
    media and courseware repository and discovery services. ADFI may
    have a role to play in developing some of this infrastructure, and
    we are gearing up to build and pilot some software along these lines
    in 2010.

    -   **Media repository?**

        Yep, we know we need it and there are people looking at this. It
        is clear that we need some kind of repository of course content
        to remember what we served up to students; Bron Chandler is
        looking at the new version (2) of the Moodle learning management
        system to see how repository-like it is.

    -   **Drop versioning from ICE?**

        It seems that the versioning is not one of ICE's most used
        features and people would be happy to sacrifice it for extra
        speed. Some of the maths and computing people would lament the
        loss of subversion, but I figure they know how to type:
        `svn add *; svn commit -m 'Finished for semester one!'`

    -   **Syncing?**

        Ditto.

-   **GoogleDocs and other online editors?**

    We had a group looking at online editors today. Stijn Dekeyser is
    particularly interested in either working with Google Docs and its
    APIs to do some ICE integration, or better yet designing a
    collaborative structured semantically aware editor. The latter
    sounds fun, but it would be a huge project and I think would be well
    beyond us without a very strong partner. We will look at
    opportunities for work in this area where we can. Via Anna Gerber I
    got a tip to look at Google Docs Base editor which uses the Google
    Docs APIs:

    > [<span
    > class="Strong_20_Emphasis">AnnaGerber</span>](twitter.com/AnnaGerber)
    > <a name="status_star_6002880028"><!--status_star_6002880028--></a>
    >
    > @[ptsefton](twitter.com/ptsefton) Have you seen Google Docs Base
    > Editor? [code.google.com/p/gdbe/](code.google.com/p/gdbe/)

-   **Google Wave (no)**

    See my [recent
    critique](ptsefton.com/2009/11/17/wave-as-a-scholarly-document-editor-not-promising-at-this-stage.htm).

-   **More LaTeX support?**

    I wrote about this above. If the LaTeX users can organise
    themselves, there might be a case for extending ICE's limited
    support for LaTeX to help with the course-management side of things.
    Look, if someone is telling a mathematician to dump LaTeX and use
    Word or openoffice.org just because university policy is to 'use
    ICE' then I think that's wrong and I'm happy to help them fight
    their case. But I'm also going to fight against everyone who wants
    to just put PDF on the web and not take advantage of the web in
    every possible way, so I support PDF-only courses only where they
    are so maths-heavy there is no other practical way to deliver them
    right now.

-   **Ebook delivery**

    I have been using and loving an ebook reader on my android phone,
    which experience I will go into in more detail soon. There was
    interest in adding eBook publishing to ICE from both the library,
    where ex RUBRIC colleague Alison Hunter emphasised the importance of
    being able to deliver electronic books as part of the library of the
    future and from the Learning and Teaching Support Unit, where
    Michael Sankey thought eBook delivery would be important for open
    educational resources. (Which reminds me, need to make some more
    [noise about Open Courseware and other open things we could be
    doing](ptsefton.com/2009/05/05/three-big-hairy-audacious-goals-for-an-open-usq.htm).)

    Linda Octalina and Cynthia Wong got ICE packaging books in EPUB
    format in less than a day and we're ironing out bugs and testing in
    Stanza on the iPhone and Aldiko on Android. When that's done we will
    had the plugin over to Michael at LTSU and see if we can get some
    trials going.

-   **SiteCore/SharePoint?**

    These are the corporate web CMS and intranet systems. It would be
    nice if they could understand ICE documents; we're not going to
    tackle these this week, but I hope that USQ gets around to it one
    day. Given that we can produce high-quality HTML pages for courses
    from the tool that most people use for documents authoring (MS Word)
    it seems a pity not to extend that to more corporate documents.
    There is the forthcoming policies and procedure site which will show
    just how much **better ICE documents are** than standard ad-hoc
    unstlyed word documents.

-   **Moodle tie-in?**

    This is a big one, for which we don't have a lot of data yet. Bron
    chandler is investigating Moodle 2.

-   **Theses?**

    Nothing much to report since
    [August,](ptsefton.com/2009/08/24/ice-for-theses-thesice-where-we-are-we-up-to.htm)
    but I hope to talk more with people at ANU about theses, as I write
    this my honours thesis is not function in ePub format, possibly
    because the title it too long: *MAKING PLANS FOR NIGEL: Defining
    interfaces between computational representations of linguistic
    structure and output systems: Adding intonation, punctuation and
    typography systems to the PENMAN system.*

-   **Journals (OJS)?**

    There's a project to get OJS up at USQ, and we have had a long
    running dialogue with the PKP folks about ICE integration, but
    nothing new to report at this stage.

-   **Annotations!!**

    There was strong support for taking the kind of in-document
    in-browser annotation we have in ICE as an authoring service and
    making it more generally available. Ron Ward is working with Duncan
    Dickinson to see if we can get the open
    [Dannotate](metadata.net/sfprojects/dannotate.html) system going in
    our systems with a view to having rich discussions in-context as
    part of the teaching and learning process. We are keen to get
    annotations going for eResearch too, for peer review, and for public
    participation in research in our work with the Public Memory
    Research Centre.

-   Various contributions about potential functionality from Michael
    Sankey (thanks!): syndication of audio and video content from
    YouTube, Facebook, inline quizzes, infopath/Sharepoint forms
    integration. Implementation of a global glossary and integration
    with and Mahara.

    We're going to find out more about Mahara and how we might bridge
    between it and ICE and media repositories and Eprints and our
    eReserve system and library catalogue and so on.

# <span id="id19"></span><!--id19--></a>Working parties

And we have 4 mini 'sprint' developments/investigation happening in the
tech team this week. These are designed to explore some of the many
things that were brought up by our colleagues where we think we can get
something to show quickly that will advance ICE significantly:

1.  **Annotations:** Ron Ward & Duncan Dickinson. The point here is to
    look for generic annotation services for academia covering comment,
    discussion, notes for personal use, peer review, marking and so on,
    using a common web based system across multiple web applications.
    The basis for this is
    [Dannotate,](metadata.net/sfprojects/dannotate.html) to which we are
    adding some user-interface tweaks

2.  **ePub-format books**: Linda Octalina and Cynthia Wong have this
    mostly working <span class="spCh spChx2013">–</span> we'll post some
    examples soon.

3.  **Packaging of arbitrary collections of resources** (ICE, flickr,
    images, data) using The Fascinator: Oliver Lucido is looking at a
    proof of concept here; to show a possible ICE-future.

4.  **Moodle 2 integration possibilities**: Bron Chandler. This is
    fact-finding at this stage, but if we can hook in any of the above
    into a demo then we will.

# <span id="id21"></span><!--id21--></a>References

Phythian, M.W. & Das Gupta, J., 2008. Hyperlinked concept map
enhancements for electronic study materials. Available at:
http://eprints.usq.edu.au/4776/ [Accessed November 24, 2009].

Sefton, P., 2007. An integrated approach to preparing, publishing,\
 presenting and preserving theses. In *ETD 2007*<span
style="font-style:normal;"><span class="T5">. Uppsala. Available at:
http://eprints.usq.edu.au/archive/00002653/ [Accessed July 2,
2007].</span></span>

<span style="font-style:normal;"><span class="T5">Sefton, P., 2006. The
Integrated Content Environment for Research and
Scholarship.</span></span> *ICE Website*<span
style="font-style:normal;"><span class="T5">. Available at:
http://ice.usq.edu.au/introduction/ice\_rs.htm [Accessed April 30,
2007].</span></span>

<span style="font-style:normal;"><span class="T5">Sefton, P., Downing,
J. & Day, N., 2009. ICE-theorem - end to end semantically aware
eResearch</span></span> <span style="font-style:normal;"><span
class="T5">infrastructure for theses.</span></span> *University of
Southern Queensland*<span style="font-style:normal;"><span class="T5">.
Available at:
http://eprints.usq.edu.au/5248/1/ice-theorem-paper-OR09.htm [Accessed
August 24, 2009].</span></span>

Copyright Peter Sefton, 2009. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<[creativecommons.org/licenses/by-sa/2.5/au/](creativecommons.org/licenses/by-sa/2.5/au/)\>

[<!-- -->![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2009/11/ICEWeek1_filesm40ca94ba.png.png)](creativecommons.org/licenses/by-sa/2.5/au/)

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>
