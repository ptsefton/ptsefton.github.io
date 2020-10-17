---
Author: ptsefton
Comments: true
Date: 2009-08-24 05:52:26+00:00
Slug: ice-for-theses-thesice-where-we-are-we-up-to

Title: ICE for theses (ThesICE) , where we are we up to?
Wordpress_id: 376
---

<div>

<div class="page-toc">

-   [About ICE and theses](#id2)
    -   [Why use ICE?](#id5)
-   [Getting things done](#id7)
    -   [Using ICE-classic](#id8)
    -   [Using ICE-Server](#id9)
    -   [Using ICE with other services](#id10)
-   [Conclusion](#id11)

</div>

<div>

Danny Kingsley who is the Manager, Scholarly Communications and
ePublishing at the Australian National University, emailed me to ask
about ICE and theses. I asked Danny if she minded making her question
and my reply public, and she's OK with that, so I will use this as an
opportunity to summarize where we are at with ICE for Theses, in my
usual long-winded way.

Danny asked:

> We are trying to plan some processes for electronic submission of
> theses and trying to work out ways of getting a thesis to an examiner
> that they can annotate without printing it out. The ICE process came
> up in discussion so I have a couple of questions:
>
> -   Does the output allow for any annotation?
>
>     [PS: Yes, but the annotation in ICE is designed for the
>     drafting/authoring stage, we have not done the work to make an
>     annotation system that could be used by examiners, with all the
>     privacy issues etc sorted out. More below on options on how to
>     proceed.]
>
> -   What form can ICE take as input <span
>     class="spCh spChx2013">–</span> I needed to make sure my Word
>     document was properly styled <span class="spCh spChx2013">–</span>
>     how much leeway is the system able to cope with (if a student puts
>     hard formats into the document what happens)?
>
>     [PS: Hard formatting inline and in tables is preserved, but when
>     converting to HTML, ICE should discard any paragraph level format
>     that's added, like making a whole paragraph italic or
>     hand-formatted headings. For PDF all formatting is preserved. We
>     do require the use of ICE styles for headings and bullets etc, but
>     if ANU has a house style you could (a) adapt ICE or (b) write a
>     conversion macro. ICE styles are also extensible so if new ones
>     are required that's easy and cheap.]
>
> -   Are there other inputs that the ICE system can take?
>
>     [PS: ICE takes .doc, .docx and .odt for documents, but it also has
>     a plugin architecture for other file formats so it could be used
>     to render wiki markup (kept as text files), LaTeX (we have a LaTeX
>     plugin already but LaTeX is not standardized well enough to
>     reliably convert aribitraty markup to HTML), or anything else for
>     which you can get commandline conversion software we can plug in.
>     We have a growing list of things it can handle, like chemical
>     markup language, text to speech for documents.]
>
In summary the rest of this post says that:

-   ICE needs support, which should be doable at ANU.

-   The released version is designed for use on the desktop, which may
    not be ideal for many candidates and/or supervisors.

-   There is a web-only version of ICE but it is not stable enough to
    release yet, we would have to scope this.

-   We don't have solution for managing theses past the authoring stage,
    with annotation and structured comment by external examiners, I
    suggest a couple of leads below and note that eventually our work on
    The Fascinator should yield these features, but not for a while.

That's the summary, now some more detail. I will look at this from the
beginning, covering:

-   What ICE offers for thesis writing and why you might want to use it,
    or not use it.

-   What do we have now that could be used and what you'd need to
    support it.

-   Potential future developments.

# <span id="id2"></span></a>About ICE and theses

ICE, the [Integrated Content Environmen](http://ice.usq.edu.au/)t was
developed by a team at USQ under my direction for the purpose of
creating web and print courseware from the same source files, using a
word processor as the editor. It's now a core system of the university,
and it's freely available as an open source product, but it's a product
that would need to be supported.

I put up an
[example](http://ptsefton.com/files/packages/honours/default.htm) of an
ICE-formatted thesis here ages ago, my BA Honours thesis in
computational linguistics from 1990 <span
class="spCh spChx2013">–</span> note that there are some issues with the
images because it was done with obsolete software on the Mac, but you
get the idea of what a thesis looks like in HTML rather than the
standard approach of sticking PDF files on the web.

Since then we have converted a few more theses to ICE after the fact,
and we have some people writing theses in ICE, but not a very
concentrated effort.

Looking to the future, my group recently completed a project with Peter
Murray-Rust's group at Cambridge, to look at thesis workflows for
chemical theses with live-links to data embedded in the document. We
looked at issues like chapter-level embargo and suggested a repository
architecture where there would be research office repository that
managed examination processes and embargo, with the institutional
repository continuing to handle open access. Have a look at the document
Jim Downing and I [presented](http://eprints.usq.edu.au/5248/) about
ICE-TheOREM, a joint USQ/Cambridge project at Open Repositories 2009.
You can click through to the [HTML
view](http://eprints.usq.edu.au/5248/1/ice-theorem-paper-OR09.htm) of
the document, which was created with ICE, of course. You can also look
at it as a [slide
presentation](http://eprints.usq.edu.au/5248/1/ice-theorem-paper-OR09.slide.htm)
or as [PDF](http://eprints.usq.edu.au/5248/1/ice-theorem-paper-OR09.pdf)
all automatically generated from the same word processing document.

ICE consists of a few components.

1.  A toolbar, which works with a standard set of style names to give a
    consistent way to author documents. The toolbar can be used in
    Microsoft Word on Windows, or with OpenOffice.org on Mac OS X, Linux
    or Windows. The toolbar can work with templates, which can be set up
    to match any requirements that a university might have for thesis
    formatting.

2.  An application which can turn ICE-formatted documents into web-ready
    content, and automate the production of PDF. The application can run
    in a few modes:

    1.  **The standard 'classic' mode**, which installs as an
        application on your PC (Mac, Windows, Linux). It shows you the
        stuff you're working on (like a course, or a thesis) in your web
        browser, and it will backup and version control your content to
        a remote repository using Subversion.

    2.  **Server-mode** where you interact with ICE as a web-site,
        uploading documents and data flies and media via a web form;
        this is potentially a really good model for research students
        writing theses, and it could possibly be used to but the
        software is not released yet, which means I can't simply
        recommend it to ANU.

    3.  **As a service**, where ICE runs quietly in the background. This
        is normally relevant only for embedding ICE in other
        applications, but it can be used if you want to just use the ICE
        Toolbar/templates and use ICE to convert your documents for the
        web. As far as I know there only person doing this is Peter
        Murray-Rust who uses ICE to blog. This service could be
        integrated with some other system like SharePoint or the Open
        Journal Systems, or Sakai.

## <span id="id5"></span></a>Why use ICE?

Assuming that you have the resources to support ICE, which I'll cover
below there are a few reasons why an institution might want to use it
for theses specifically.

-   It provides a **well tested general purpose way to design
    templates**, with a standard set of style names, so even if none of
    the other features appeal ICE templates might. Of course everyone
    writing a thesis should be using a template; I think at ANU they
    actually have official templates. Here at USQ, although we have made
    some test ICE templates for the house style they're not officially
    endorsed. We don't have a *Manager, Scholarly Communications and
    ePublishing* either,maybe we should.

    (The main potential drawback with ICE templates is that we have used
    non-standard names for headings. Instead of Heading 1 we have h1 and
    for numbered headings it's h1n. The reason I designed it this way is
    that in a 'standard' template Heading 1 may or may not be numbered,
    and if you do attach outline numbering to Heading 1, Heading 2 etc
    then how do you head-up a non-numbered section? I've been waiting
    for someone to argue this out with me over this for years, but so
    far nobody has complained.)

-   You can present theses in **HTML as well as PDF**. This is something
    that strikes me as a blindingly obvious thing to want to do, but we
    have not been overrun with people wanting to get this happening at
    their university.

    It is possible to deposit from ICE into a repository via [SWORD
    APP](http://swordapp.org/); we have plugins for ePrints and Fedora
    only at the moment, not for Dspace which is what they use at ANU.

-   It provides **annotation services**, so the answer to Danny's
    question <span class="spCh spChx201c">“</span>Does the output allow
    for any annotation?<span class="spCh spChx201d">”</span> is yes, but
    it depends what you mean by *output*. If you are running ICE either
    from a desktop or the server version then you can collaborate via
    paragraph-level annotations, but at the moment we don't have a way
    to do the workflow that would be required to allow examiners to do
    this.

    <a name="graphics1"></a>![graphics1](/wp-content/uploads/2009/08/7f96103a.png)

-   You can **integrate data** into a document via links, making it
    Linked Data <span class="spCh spChx2013">–</span> at least, we have
    proved the concept on the ICE-TheOREM project, but this would need
    to be worked out discipline by discipline.

# <span id="id7"></span></a>Getting things done

So, if there is a reason to use ICE, in what circumstances might it make
sense?

## <span id="id8"></span></a>Using ICE-classic

Using ICE in the standard way would be a sensible approach to writing a
thesis, and getting comments from supervisors, just as a couple of
hundred authors at USQ use it to write book-length courses. This could
work for on-campus students given some support staff, up to the point
where the thesis goes off for examination. As I said, we don't handle
documents past the authoring process, we have button for repository
deposit, but you don't get to self deposit a thesis without having it
examined.

## <span id="id9"></span></a>Using ICE-Server

Using the ICE server could work well, except that it's not stable enough
for us to be comfortable releasing it. We are using it in internal
trials with PhD candidates, but we're not really dedicating enough time
either to helping them or to fixing up the software, and I have to say
that I'm not sure that we will fix up the software as it currently
stands; it may be that the future for ICE will be to build its
conversion services into our eResearch Desktop / Institutional
Repository project, [The Fascinator](http://fascinator.usq.edu.au/).

## <span id="id10"></span></a>Using ICE with other services

ICE is designed to play nicely with other software, so one approach to
getting a thesis written and commented on by a supervisor and examined
would be to mash-up ICE with other software. We have looked at doing
this with the Open Journal Systems, which has review features, if not
annotation, and which in the past has been used at USQ for thesis
review. That would be a modest development project, [which I outlined
early this
year](http://ptsefton.com/2009/01/06/potential-projects-2-integrating-ice-with-the-open-journal-systems.htm).

Another thing I have had a quick look at for this post, is
[digress.it](http://digress.it/), which is being used in a JISC
supported project. It has similar inline annotation features to ICE with
one huge advantage, it is built on WordPress which means that it's easy
for people to install, I got it up and running in about half an hour at
my hosting service, and had my first document in there for comment
minutes later. Now this is not suitable for examination, out of the box
as the comments are in the open, but it could possibly be used for
earlier stages of thesis writing, such as getting supervisor comments. A
candidate could use the ICE template, post to a word press 'blog'
periodically, with each new post creating a new entry for comment by the
supervisors and potentially peers.

If you'd like to have a look at it, see my test site where [I put up a
recent blog post for
testing](http://comment.ptsefton.com/archives/4.html).I was impressed by
how easily I could get digress.it going, but I didn't like the way it
removed my document formatting, still, I have joined the developer list
and the lead developer said he'll look at a mode that does not strip
formatting.

Another option would be to go ahead and build another one of my ideas, a
[general purpose
annotation](http://ptsefton.com/2009/01/05/potential-projects-1-a-general-purpose-document-annotation-system.htm)
system to supplement ICE. We have a lot of the pieces, so between us I'm
sure that ANU and USQ could make this happen given a business a case,
and getting the resources.

# <span id="id11"></span></a>Conclusion

Looking at where we are at with theses in ICE makes it clear to me that
we have a lot of potential, but very little action. So, I'm going to try
to get things moving again at this end, with what we have called the
ThesICE project. This will involve:

-   An ADFI project concept outline to work out how we can start really
    driving ICE theses at USQ, including talking to our research office
    about stuff like officially supported ICE templates.

-   A conversation with Danny Kingsley about the requirements at ANU.

-   With Jim Downing, updating the paper we gave at OR09 for submission
    to the proceedings, which will be a chance to outline further work
    required and talk about further joint projects with Cambridge.

</div>

</div>
