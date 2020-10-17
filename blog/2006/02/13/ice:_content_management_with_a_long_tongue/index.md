---
Title: "ICE: Content Management with a long tongue"
Slug: ice:_content_management_with_a_long_tongue
Date: 2006-02-13

---
<div>

Tim O'Reilly has posted a piece about [the long
snout](http://radar.oreilly.com/archives/2006/01/the_long_snout.html),
which is about engaging with the people working on the leading edge of
technology change, and about making pre-release books available via
automated publishing systems.

In my new role I get to work with [Institutional
Repositories](http://en.wikipedia.org/wiki/Institutional_repository) and
in that domain they talk about 'ingest' which is the bit where the
repository swallows your data. One of the things we're looking at in the
[RUBRIC](http://rubric.edu.au/) project is ingest using
[ICE](http://ice.usq.edu.au/), the Integrated Content Environment.

These things are clearly related. A long snout is good for snuffling-out
and ingesting tasty morsels that animals with lesser snouts won't reach.

Tim O'Reilly describes a publishing system used for the O'Reilly hacks
books:

> Rael decided that we needed a lightweight "Web 2.0" toolset for
> building the hacks books -- something that would allow for
> collaborative, web-based authoring and editing, but would also
> eliminate the complex conversions that were now required by our siloed
> production process. He christened the tool aardvark -- an animal noted
> for having both a long snout and a long tail -- and put it to work
> building some of the latest hacks books. It's a wiki-based
> collaborative editing front end that emits DocBook as its back-end
> repository format. Sweet.

> <http://radar.oreilly.com/archives/2006/01/the_long_snout.html>

The aardvark system is a response to the complexity of their publishing
systems:

> Each of our business units had developed its own systems for
> developing content, and while we'd made big strides towards
> integration -- starting with the development of
> [DocBook](http://www.docbook.org/) as an SGML repository format back
> in the late 80's (and then migrating that format to XML) -- getting
> data into the ultimate XML content repository that drives Safari
> required a lot of convoluted format conversions. And the development
> process was always designed to be tools-agnostic, creating a lot of
> complication. We've let authors develop books in troff, teX, Microsoft
> Word, Quark, Framemaker, InDesign, POD, WordPerfect, Microsoft Word --
> and even directly in DocBook -- providing complex tools to convert
> back and forth from our ultimate XML repository format.

> <http://radar.oreilly.com/archives/2006/01/the_long_snout.html>

The ICE publishing system has similar aims, so as you would expect it is
evolving along similar lines to the aardvark application.

ICE stands for the “Integrated Content Environment”, but it also has a
long snout, or at least a long tongue. ICE is engineered to be able to
ingest documents as early as possible in their development.

My colleague Cameron Loudon is working within
[USQ](http://www.usq.edu.au/) to see if he can get interest in a project
to ICE-ify some research areas so that their papers, presentations and
other documents can be seen by other people within the university:

1.  The research office, who can help get funding.

2.  The marketers and PR people who want to know what's going on so they
    can tell the market, sorry, the customers, I mean potential
    students.

3.  Support people who can assist researchers in working as efficiently
    as possible with their authoring tools.

ICE is built around the idea of interoperability via templates for
ordinary office-software users. I'll talk a bit about how it might
become more aardvarkesque below.

ICE already works with OpenOffice.org and Word by using a set of common
style names and some fix-up macros that help work around the
limitations, bugs and stupidities that are present in both word
processors. It produces consistent XHTML and PDF using OpenOffice.org as
a conversion engine, giving us a publishing system that can be used for
a lot of the course publishing at USQ.

The ICE team are working on Framemaker integration as well. If that
works (and I bet it will) ICE will be able to slurp-up hundreds of
well-styled Framemaker books produced by USQ and allow everyone in the
production process to collaborate directly on the source-documents using
their choice of Microsoft Word or OpenOffice.org writer.

On the DocBook front, Dr Ian Barnes of ANU, working with the DEST-funded
[APSR project](http://www.apsr.edu.au/) has created stylesheets for ICE
documents that generate DocBook XML. The demonstrator system, the
*Digital Scholar's Workbench* generates XHTML and PDF using free DocBook
tools, and the latest version even has a button to put your document
directly into the institutional repository. See this Powerpoint
[presentation](http://www.apsr.edu.au/Open_Repositories_2006/barnes_yeadon.ppt)
from Ian and Scott Yeadon, from the recent [Open Repositories
conference](http://www.apsr.edu.au/Open_Repositories_2006/conference_program.htm).

While I haven't seen O'Reilly's aardvark, it isn't hard to imaging
plugging ICE into O'Reilly's publishing process – authors could work in
Word, OpenOffice.org writer or any other word processor that can read
and write word docs, RTF or OpenDocument, provided they use the ICE
template that maps so nicely to profiles of DocBook and XHTML, and
provided they stick to middle of the road features that work across
applications.

ICE is also designed for collaboration. It uses the Subversion version
control system underneath to manage distributed authoring and to store
various renditions (PDF, XHTML) of documents as properties.

## <span id="id766992"></span>What ICE and the ICE templates do now

Make web pages
:   ICE makes web content out of MS Word and Writer documents including
    recent pages on this site, a growing amount of USQ courseware and
    our team Intranet at work.

Make PDF 
:   ICE makes PDF for whole books using OpenOffice.org writer's master
    documents, if you set one up, and for individual chapters using the
    OpenOffice.org PDF export feature.

Make DocBook documents
:   (If you manage to get your hands the Digital Scholar's Workbench.)

Manage small team-intranets. 
:   We use it on the RUBRIC project to keep track of all our stuff.
    Everybody has a copy of everything, even when out on the road, or
    otherwise offline, and when online we can synchronize at the click
    of a button.

Keep working documents safe. 
:   I have my life in a Subversion repository hosted at home and I have
    copies of all my stuff synchronized across multiple machines. When
    the Mac Powerbook has to go back to the shop to be fixed *again*, it
    is simple to keep working using a Windows PC from home and Linux at
    work.

## <span id="id768448"></span>What ICE will do soon or might do with a slightly longer snout

Capture undergraduate work
:   Imagine the very first day of a humanities course that you are
    handed a copy of ICE (or the URL to an online version). There in
    front of you are not only folders for all the courses you have
    enrolled in, but there are blank documents ready to fill out for
    Assignement 1, major essay etc.
:   You open the document, type away and hit sync to send a copy to
    secure, version-controlled, backed-up storage at the university, and
    you have a complete portfolio at the end of your course, not just a
    bunch of word documents, but a linked-up web site, with PDF versions
    as well. And since ICE can handle multimedia, it would not just be
    for text.
:   (This would also mean that the submission process would have a
    long-snout, the markers would just check out the version of your
    work that was current at the submission date.)

Paragraph-level annotation and discussion
:   Commenting is planned for documents at all stages of their life
    cycle, from draft to published to archived.
:   Imagine working on your thesis, clicking 'sync' and having in-line
    comments back from your supervisor the next day.
:   The IT support team would be able to see the PDF and HTML versions
    developing as you went and step in to help you use styles and so on,
    making sure that the automated tables of contents would work.

Wiki-style editing
:   This might need to be done using a sub-set of ICE formatting, but it
    should be possible to start a document using a wiki format from a
    browser, then continue its development using a word processor.

## <span id="id767998"></span>See ICE in action

To see ICE in action you can [download it from the
website](http://ice.usq.edu.au/) and run it using its local web server
(http://localhost:8000 by default). That will let you browse around some
sample content. You can also switch repositories to look at the ICE
documentation, which is kept in Subversion on the ICE site.

Or, to get a feel for how much it can already do, download the ICE
documentation, which comes in a [zip
file](http://ice.usq.edu.au/svn/ice/downloads/latest/documentation/packages/ice-guide/ice-guide_template.zip).
Inside there's a complete web site with both HTML and PDF versions of
the manuals in IMS package format. You can look at the source documents
that were used to create that book by looking at the Subversion
repository for the project [via the
web](http://ice.usq.edu.au/svn/ice/downloads/latest/documentation/packages/ice-guide/study-modules/).
These are in OpenDocument format, but the system does work with Word
documents as well. The documentation is organized a bit like a USQ
course, into modules, but you could call them chapters or sections, or
whatever you like.

As usual, I note that ICE is pre-version one, suitable for brave and/or
resourceful people only (and our well-supported pilot users at USQ). If
you have trouble or want to know more, please [drop me a
line](mailto:pt@ptsefton.com).

</div>
