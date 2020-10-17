---
Title: "A bout the RUBRIC project Trac wiki"
Slug: wikis
Date: 2006-09-05

---
<div>

Kate Watson of the University of the Sunshine Coast is one of the RUBRIC
project managers. She's writing a paper on wikis, and is collecting
various perspectives on the wiki we use on the [RUBRIC
project](http://rubric.edu.au/).  We have a closed wiki for the RUBRIC
central team at USQ and our network of partners, each of which
instiution has a project manager.

With Kate's permission, I'm posting my answers here.

# <span id="id868731"></span>1. What are the group's needs for collaborative group knowledge creation?

The RUBRIC project is all about collaborative construction of knowledge,
initially amongst partner institutions. At the end of the project we'll
be publishing some reports and information kits that aim to help other
institutions build institutional repository infrastructure.

There's an information lifecycle at work. The extended RUBRIC team uses
highly interactive knowledge construction to come up with solutions that
will then be packaged into a toolkit that can be used by others.

We need to keep track of a lot of technical documentation and software
configuration as well as vast amounts of literature on the subject.

# <span id="id838722"></span>2. What tools are available to the group to enable collaborative group knowledge creation?

Knowledge resides in individuals, everyone has to construct it for
themselves.

The tools and practices we use, in roughly decreasing order of
interactivity:

-   Face to face meetings.

-   Teleconferences.

-   Email, both one to one and via lists.

-   Del.icio.us bookmarks, as described in a [previous
    post](http://ptsefton.com/blog/2005/09/07/del.icio.us_rubric_bookmarks).

-   Job tickets in our Trac project management system.

-   Wiki pages.

-   Documents such as reports for publication on the website.

    RUBRIC central uses ICE for these, meaning we can get both HTML and
    PDF versions and compile book-length content easily.

# <span id="id838837"></span>3. Why a wiki?

The initial impetus for getting a Wiki was that it came as part of the
[Trac](http://trac.edgewall.org/) system. I first used Trac on the [ICE
project](http://ice.usq.edu.au/), where we picked it for its integration
between [Subversion](http://subversion.tigris.net/) version control and
job-tickets.

On RUBRIC  we chose Trac for internal use. I did not try to push it to
the broader RUBRIC team, partly because the 'official' USQ system is
Microsoft Sharepoint (does nothing for me, particularly on a Mac).  We
made the project managers aware of it. Gradually the RUBRIC partners
adopted Trac and its wiki and the wiki has turned out to be useful for
jointly constructed pages where interactivity is important.

So our use of the wiki evolved organically, it was not part of a
pre-meditated project methodology. Having used it though, I think I
would recommend it for future RUBRIC-like projects. This means we'd
better document how we use it. (I think Kate's paper will do this).

# <span id="id838783"></span>4. Technical Information?

We use the open source Trac system running under Apache on Red Hat Linux
on a virtual machine running on VMWare ESX running on Dell hardware,
plugged in to a SAN.  User authentication is via LDAP. Backups are via
ESX  ranger running on another (Windows) Dell machine. Backups go to
hard disk, and then to tape, and the tapes are sent off site.

Trac has proven to be a stable, low maintenance piece of software.

Trac's wiki is perhaps more useful than a stand-alone wiki in that it is
tightly integrated with a version management system, Subversion, and a
job-ticket system.

We use some Trac macros developed at USQ by Sally Macfarlane to help
with Task estimation. This is not an important part of RUBRIC's work,
but it is useful in the ICE content management system. If you want them
contact me.

# <span id="id838433"></span>5. How has the wiki supported collaborative group knowledge creation?

(Experience and Comments from an administrators point of view.)

I don't have a lot to say from an administrative point of view. Trac
'just works' once one has the users set up.

A wiki is like a garden. It needs pruning sometimes, and weeding, and
the harvest needs to be gathered. The harvest in our case is material
that is ready to move to published document form and go on our public
website.

# <span id="id869280"></span>6. Administration issues

Trac has no major administrative issues, apart from the fact that it
does not come with any user authentication – that has to be handled via
the Apache web server.  For use in a large institution this is probably
a good thing: it allows for the software to use existing service
infrastructure, for smaller stand-alone projects it could be a problem.
We had to set up our LDAP server but that was a useful learning
experience.

Remember that our wiki is closed and we have a civilised project team so
there are no issues with spam or vandalism.

# <span id="id868036"></span>7. Administrator opinion on Pros/Cons/Benefits/Limitations

The Trac wiki system has a few quirks, using some wiki formatting that
is less than natural. Attachments to Wiki pages are also less than ideal
– they are not version controlled as far as I know, but given that Trac
included subversion they easily could be.

The Trac ticket system is a little bit clumsy, and for general project
use, rather than on a development project, it could be better integrated
into a Personal Information Manger (PIM) application, such as Microsoft
Outlook.

I think other wiki systems might be good for RUBRIC style work, but Trac
is adequate. It's more than adequate for development projects like ICE.

The biggest strenght of Trac is its integration with Subversion. I'd
love to explore similar integration with ICE so that documents written
in wiki format could migrate to a word processor and the other way
round, one could edit word processing documents using a wiki syntax.

</div>
