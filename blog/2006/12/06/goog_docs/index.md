---
Title: "Google Docs and collaboration"
Slug: goog_docs
Date: 2006-12-06

---
<div>

One of the main design goals for [ICE](http://ice.usq.edu.au/) was to
let people **write courseware** (and now research) in an **ordinary
offline word processor.** This makes sense for book-length content, and
gives you access to stuff like outliners, mutliple windows onto the same
content, bibliography management tools like EndNote.

But there are times when an **online** editor would be good too. I
realised this when I made the switch to using Gmail for all my mail;
Gmail's interface and search suits me better than Apple's Mail or
Entourage – I get red-squiggly spell checking for nothing courtesy of
Firefox 2 and integrated calendaring that mostly understands my exchange
calendar too (I just include my Gmail account in meetings), a trick I
never managed with iCal. The web experience is better than any other
toolset I've tried on the Mac. Maybe Chandler will change the whole game
though.

The mail setup I'm using now should be the subject of another post but
it made me realize that an online word processor for some tasks might
not be as far off for me as I thought, provided it can do the same stuff
as, or integrate with, ICE; organizing sets of documents into mini web
sites, decent HTML and PDF from the same source, interop with other word
processing users on different toolsets.

I was thinking about this issue this week, when by chance, a couple of
the Maths & Computing people here at USQ announced a seminar; [*Using
Google Docs to Collaborate on Papers and Study
Books*](http://www.sci.usq.edu.au/research/seminars/?seminarID=132).

> Researchers and Lecturers have many software options to write papers
> and course material on their own, but fewer options when they want to
> collaborate with others.  USQ has developed some systems (eg GOOD and
> ICE) that can be used by non-technical persons, each having strengths
> and weaknesses.  In this seminar we present our findings on using
> Google Docs (formerly Writely.com) and compare it to other approaches.
>  A live demo of Google Docs is included in the seminar.  In addition,
> we demo an extension to the system that we developed to generate
> high-quality output.
>
> [http://www.sci.usq.edu.au/research/seminars/?seminarID=132](http://www.sci.usq.edu.au/research/seminars/?seminarID=132#null)

I've [looked at Writely (now Google Docs)
before](http://del.icio.us/ptsefton/ptsefton+writely) and been
disappointed; I hate the interface that is larded with formating tools –
and I wish I could use a more structurally oriented editor that just
edits plan-old HTML. Headings, blockquotes, lists, that kind of thing. I
never, ever want to make arbitrary font changes to parts of my documents
– fonts are always, always tied to styles.

Anyway, Stijn and Richard do a wonderful trick with Google Docs -  they
collaborate on documents then feed them through a web service that turns
them into LaTeX to get a PDF. Stijn demoed a simple form where he fed in
a Google Doc and some LaTeX gobbledygook and made one and two column PDF
renditions from a single source.

But they identified the same issues as me: the format of a Google Doc
with a few bullet points or bits of formatting is too messy to use as
the input to a structured converter without significant work, so their
processor ends up looking for only the simplest structures, such as
paragraphs, and in the end they won't try to deal with the word
processor features of Google Docs.

The plan is to use Google Docs as a collaborative text editor and just
do LaTeX over the web  - nice and simple if you know LaTeX or work in a
community where people will work with you in LaTeX.

I wondered if the same approach might work with wiki text formats which
I believe to be less complex than LaTeX, if no more intuitive. Lots of
users have become familiar with wiki text recently, including some of
our RUBRIC team members, 'cos they have had to learn it to get the
considerable benefits of a wiki.

A great Web 2.0 mashup would combine Google Docs for highly concurrent
editing by multiple people with a decent HTML output (which you do not
get from the current monster). I think over at the ICE team we should
pick a wiki format and start building it in to the ICE code base, as
this would begin to allow this kind of mashup with ICE docs.

We should explore Google Docs and similar systems on the ICE-RS project;
it's important not to too much on ICE just 'cos we wrote it. If other
software can do the job with a reasonable business case for using it
then we'll use it.

And just as I was about to post this, Jon Udell [writes
again](http://www.infoworld.com/article/06/11/29/49OPstrategic_1.html)
about the need for a “universal canvas”. The
[phrase](http://weblog.infoworld.com/udell/2006/12/05.html#a1572) he
borrows; *We found the version control, collaboration and invite system
outweighed the limited feature set* could have come from Stijn and
Richard's presentation.

</div>
