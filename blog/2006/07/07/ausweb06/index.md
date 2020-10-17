---
Title: "Yet another untitled post"
Slug: ausweb06
Date: 2006-07-07

---
<div>

On June 29<span class="T1">th</span>  I gave a demo of ICE at an event
called [The Successful
Repository](http://www.apsr.edu.au/successful/successful.htm).

Andrew Treloar, who says he is in charge of generating acronyms for
projects named after pointy objects ([ARROW](http://arrow.edu.au/) and
[DART](http://dart.edu.au/)), asked me a couple of questions. It happens
that Andrew is the program chair for the AusWeb conference, where I gave
my [paper](http://ausweb.scu.edu.au/aw06/papers/refereed/sefton/)about
ICE.

AusWeb paper sessions are a bit unusual – instead of everyone talking
for half an hour or so on their paper, with a few minutes for questions
if you're lucky, presentations are much shorter. Three or four
presenters talk for 10 minutes or so each, and then form a sort of a
panel, and discussion starts. I have seen this work really well.

So for my presentation on my ICE
[paper](http://ausweb.scu.edu.au/aw06/papers/refereed/sefton/) at Ausweb
I thought I might do a demonstration of ICE, using this very document.
You can see the final presentation [on my
site](http://ptsefton.com/files/ausweb06.slide.htm) . It is generated
from the same source document as this blog post.

By the way, ICE is now using a system called
[Slideous](http://goessner.net/articles/slideous/slideous.html) for web
presentations which is apparently inspired by
[Slidy](http://www.w3.org/Talks/Tools/Slidy/). Bron Dye of the RUBRIC
project did the work to set up Slideous ICE templates.

If you're reading this that means I was not torn to pieces by other
AusWeb delegates.

<div class="slide">

# About this demo

The demo will:

1.  Show how I use ICE to write multipurpose documents.

2.  Show-off ICE's new slide [presentation
    features](http://ptsefton.com/files/ausweb06.slide.htm).

    (which I wrote about
    [earlier](http://ptsefton.com/blog/2006/05/23/presenting_slidy_ice))

3.  Answer Andrew Treloar's questions.

    And any more questions that came up...

</div>

# <span id="id860780"></span>Andrew's questions

<div class="slide">

# Why Python?

ICE is written in Python because:

1.  The Java programmers in our team at USQ were not confident of
    writing a cross-platform application.

2.  Python ships with OpenOffice.org.

    At this stage we use a different Python version, but some ICE code
    could be used with OOo in future...

3.  Python can be compiled into stand alone executables for Mac OS X and
    Windows.

4.  Python has all the libraries we need.

</div>

<div class="slide">

# I don't write courseware. Do I need ICE?

I use ICE to look after my stuff (that is back it up, and keep track of
document versions).

Which stuff?

Home

:   -   This weblog.

    -   A couple of book-proposals.

    -   Admin stuff like tax spreadsheets.

</div>

<div class="slide">

# More stuff in ICE: RUBRIC project

-   Board documents and meeting packages.

    (book and web versions)

-   Technical reports

-   Papers like my [AusWeb
    paper](http://ausweb.scu.edu.au/aw06/papers/refereed/sefton/)

    Complete with automated link footnotes

-   Administrivia like forms

-   Coming soon – RUBRIC [web site](http://rubric.edu.au/).

</div>

<div class="slide">

# More stuff in ICE: ICE project

-   All the doco for ICE

-   The ICE [web site](http://ice.usq.edu.au/).

</div>

# <span id="id863170"></span>More discussion from the AusWeb session

The two other papers in the session with mine
([RikWik](http://ausweb.scu.edu.au/aw06/papers/refereed/roe/paper.html)
and
[DotWikIE](http://ausweb.scu.edu.au/aw06/papers/refereed/rees/paper.html))
were wiki systems, so there was a bit of discussion about 'horses for
courses'; how we need to have a variety of systems for different kinds
of documents. A word processor is useful for longer documents, while
Wikis are useful for note-style communal pages, such as the contacts
page we keep for our proejct.

<div class="slide">

# But how do you enforce high quality?

A fair bit of discussion was about how to keep standards high when ICE
does not do content validation.

-   ICE is an enabler not a constrainer.

    -   An XML system with a validating editor did not catch on with USQ
        lecturers.

    -   A word processor based system seems more likely to succeed, but
        cannot do strict validation.

-   Schematron validation could be used to help 'health check' content.

-   A strict system can be very costly when exceptions are needed.

</div>

<div class="slide">

# More on quality

-   Quick feedback via automated XHTML formatting teaches people to [use
    styles](http://ptsefton.com/blog/2005/03/02/use_styles).

-   Complete course templates including the all major elements that
    should be there help most people to do an acceptable job.

-   USQ still has editorial services available for distance materials.

</div>

<div class="slide">

# Image handling in ICE?

ICE deals with bit map images like this JPEG of me and Spensa...

<span
id="graphics1"></span>![graphics1](/blog/2006/07/07/ausweb06/1.png)

... but vector graphics remain a huge problem for word processing in
general. SVG support is missing from both Microsoft Word and Writer.

</div>

</div>
