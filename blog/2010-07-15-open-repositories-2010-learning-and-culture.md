---
Author: ptsefton
Comments: true
Date: 2010-07-15 01:10:27+00:00
Slug: open-repositories-2010-learning-and-culture

Title: Open Repositories 2010 - Learning and Culture
Wordpress_id: 574
---

<div>

<div class="page-toc">

-   [<span>Issue: packaging</span>](#id2)
-   [<span>An idea for USQ</span>](#id3)

</div>

<div>

The last couple of days of the Open Repositories conference were devoted
to the user-group streams, splitting the community into the Duraspace
crowd and the ePrints devotees. You can move between them, of course,
but some of the stuff that's in those sessions is not really software
specific, and I think that it would be good to have a bit more
cross-fertilisation between the software platforms (assuming they don't
all end up under one big foundation :). But I know from talking to a
couple of people from the program committee over dinner that streaming
this conference is a very difficult balancing act. Some people will only
come for 'their' software sessions, and others only want the general
sessions.

I attended a few talks on the use of repositories in eLearning (in
Dspace and in ePrints) and on using ePrints for creative-arts outputs. I
was interested to see what others are doing, as these are both areas
where our team is working very actively at USQ. What I saw really
reinforced for me that the work we're doing at ADFI is on the right
track.

In this post I want to talk briefly about one of the main issues that
repository designers are facing as they move away from hosting mainly
articles, mainly in PDF, into learning and creative-arts resources; the
need for packaging and its impact on repository architecture, and then
look to the opportunities that we have at USQ to apply some of our
repository expertise <span class="spCh spChx2013">–</span> which has
mostly been on the research-outputs side <span
class="spCh spChx2013">–</span> to learning resources.

# <span id="id2"></span><span></span></a>Issue: packaging

**Packaging is important**; learning resources and creative-arts outputs
need to be organised into ordered , hierarchical sets or resources that
people can click through in a comfortable way. A screen-full of PDF
files to download is not optimal.. In the learning world that's why
there are standards like IMS content packaging and SCORM. And for the
creative arts there are lots of use-cases around organising things into
exhibitions and portfolios. Exhibitions might travel around, and have
different makeup in different places. Not to mention complexities like a
photo in your repository that depicts more than one painting, all of
which Duncan Dickinson at ADFI has been looking at modelling using CCO:
<span class="spCh spChx201c">“</span>[<span>Cataloging Cultural
Objects</span>](http://www.vraweb.org/ccoweb/cco/partone.html)<span
class="spCh spChx201d">”</span>.

The thing is, this business of packaging things is putting pressure on
the data models inherent in IR software like Eprints and DSpace which
grew up around discrete 'items' that have a metadata page, with
click-to-download files. When we start looking at an exhibition of
photographs this model is put under a fair bit of strain.

In the session on [<span>Kultur
</span>](http://kultur.eprints.org/)<span
class="spCh spChx2013">–</span> the Eprints extension for creative arts
output; Stephanie Meece showed some of the extensions that improve the
metadata page in Eprints for exhibitions. While it does provide a basic
way to show-off a large number of images, I think her talk showed up
some of the architectural issues really well <span
class="spCh spChx2013">–</span> she noted that sometimes the repository
manager has to add circa fifty images files to an 'exhibition' item,
using an interface that requires a lot of scrolling backwards and
forwards. I talked to her afterwards, and found that there is no real
way, yet, to deal with exhibitions that change over time, or to re-use
items across portfolios (the Eprints team did say that there is a
collections feature now that could be used for this). One thing that
Kultur did achieve is to work out the basis for metadata for
creative-arts metadata; work that has been re-used in Australia. This is
informing our work at USQ, and we have helped disseminate it via CAIRSS.

Back in the day, on the RUBRIC project, I was a vocal critic of the
notion of 'hard' collections I don't like the way DSpace was designed
around 'communities' and 'collections' and I argued that for most of the
use-cases people were talking about then were better served by 'soft'
metadata-driven collections. If you want to look at all your theses, for
example that should just be a 'slice' of the repository based on a query
not some process of hand-curating a list, or having to deposit items
into a particular collection.

But as I noted above there are cases where you do need to hand-curate
sets of items.

In our current work on The Fascinator, Duncan Dickinson is leading the
team in efforts to capture creative-arts outputs, partly for the ERA
assessment where exhibitions are particularly important. Bron Chandler
is managing the media repository project, where courseware media objects
(video, audio that sort of thing) that need to be grouped into
course-materials packages along with the traditional long-form course
books for which USQ is famous. This work has led us to create a flexible
architecture where you can either:

1.  Add a manifest/table of contents to a single compound repository
    item containing lots of stuff; for example we have pre-populated a
    repository with all of USQ's current course offerings from ICE and
    each course can be considered one item.

2.  Group several discrete items together into a package.

Oh, and you can package packages too <span
class="spCh spChx2013">–</span> something we're going to have to think
about very hard when it comes to user-interfaces.

One output of this work is some web-interface code for navigating and
managing packages, called Paquete. Paquete can build a table of contents
and forward/back links to a set of web resources using a simple JSON
table of contents. It's like having a pure web-based eBook or IMS
package reader. We're thinking it could be deployed in all sorts of
places, such as on top of ePrints, or in WordPress, and, of course in a
learning management system. One use would be in
[<span>Jorum</span>](http://www.jorum.ac.uk/)Open, the DSpace-based OER
repository which is in need of a way to view IMS packages. It would be
easy to add an IMS organiser support to Paquete, or produce a standalone
tool to add a Paquete manifest to an IMS content package.

You can see a simple demo of an early version Paquete at our demo site.
Note that each part of the package, which behind the scenes is a
separate HTML page, has a proper URL, so I can send you direct to
the[<span>
intro</span>](http://demo.adfi.usq.edu.au/paquete/demo/#module01.htm),
or to the bit about
[<span>JSON</span>](http://demo.adfi.usq.edu.au/paquete/demo/#module02.htm).
The idea is that on an HTML 5 device like an iPhone, you could use 'save
as App' to grab a copy of an entire resource, via the HTML 5 manifest,
and the stable URLs mean we can combine it with our annotation software
that allows tags and discussion to take place in-line.

Using Paquete, it won't matter to users whether the resources on show
are spread out across several repository items or all jammed into one
big item. So, for an exhibition, you could put ALL the pictures into a
single ePrints object, then make multiple new items which consisted of
slightly different packages representing variants of the exhibition. Or,
each picture could be a first-class item with a number of exhibition
items that simply reference them.

There's lots more we can do with this viewer with a bit more coding<span
class="spCh spChx2013">–</span> to make it show pictures and videos
gracefully, and to work in presentation mode like PowerPoint. Speaking
of PPT, why not render each slide as a JPEG and then let people flip
through them there in the repository without having to download? (We're
very close to this in our work on The Fascinator). It could also be made
easier to use on mobile devices, mimicking the tap-to-page-turn
behaviour of eBook apps like Stanza or Kindle [<span>along the lines of
this thing that Russell Beattie
did</span>](http://www.russellbeattie.com/blog/making-an-ipad-two-column-magazine-layout-using-jquery).
Contributions are welcome if any of this sounds like something you can
do. I'd be really happy if someone with some Eprints skills was able to
do a plugin that can recognize where there's a Pacquet or IMS manifest
present and show the HTML resource in-line.

There's **a lot more to say about this packaging stuff,** and how we
might be able to use the ePUB format to ship repository content around,
I'll come back to this in a future series of posts.

# <span id="id3"></span><span></span></a>An idea for USQ

One of the repositories on show at OR10 in a session led by Yvonne
Howard was an effort at Southampton to provide an open platform for
sharing: [<span>EdShare</span>](http://www.edshare.soton.ac.uk/). This
is an ePrints repository that's being built-in behind the Learning
management System / Virtual Learning Environment they use at
Southampton. I think the idea is that eventually, there will be seamless
integration with BlackBoard so that resources can show up as part of the
course-experience there, but be sitting in an open content repository
behind.

There's an interesting design pattern here; a sharing oriented
repository that's also hooked in to an access-controlled learning
environment. At Southampton the emphasis is on low-barrier to
participation so that lecturers can get stuff up as quickly as possible,
with the downside that some of the metadata provided can be a bit
lacking and many of the resources end up being quite fragmented. For
example in the [<span>HumBox</span>](http://humbox.ac.uk/) site for
sharing humanities resources last Friday, the latest uploads were a
bunch of individual PDF files that didn't mean much on their own. Fom my
point of view as someone discovering stuff I would have preferred them
to be in one bundle so I could begin to make sense of them.

At USQ, on the other hand, where a large number of our courses go
through a production process in which many people collaborate with the
course writer to bake-in pedagogy, get the referencing right, and deal
with licensing for readings and other supplementary materials, we are
well on the way to having v**ery well-described well-organised materials
already in a repository**. It would be so easy to tag a course as 'ok
for Open Access' and have it flow through to an externally-facing site
as a high quality Open Educational Resource (OER).

There are lots of reasons that we might want to go open, even just a
little bit. I'll rehearse them here, yet again:

1.  **For prospective students:** I bet high-quality courseware would
    bring lots of traffic from people searching for stuff . Some of them
    might enrol, particularly if we lower the barriers to participation.

2.  **For staff:** open resources can be good for a lecturer's profile
    <span class="spCh spChx2013">–</span> even better if we can work out
    a way to build in a genuine peer review process that helps some
    kinds of resources also count as research outputs (which = \$\$\$\$
    and prestige in a way that learning resources currently just don't).
    OERs would mean that you get to take your work with you to the next
    institution.

    There are some things to think about re copyright, too. At the
    moment USQ owns the courseware, but in new models there might be
    ways to let authors keep their copyright, with an agreement that
    they license it openly.

3.  **For USQ** there's that thing about [<span>many
    eyeballs</span>](http://en.wikipedia.org/wiki/Linus'_Law). Back when
    we first looked at open courseware, some senior people wondered if
    we wanted to expose some of the content. A bit of sunlight should
    work wonders if there are substandard bits of courseware (I'm not
    saying there are). Feedback and re-use has the potential to help us
    improve our materials.

    When we first launched our minimal set of OERs at USQ Prof. Jim
    Taylor was working on a project to get volunteer tutors (focusing on
    retired academics) to help learners in an LMS environment. That
    project didn't come off, but I am wondering if there might not be
    some people willing to review courseware<span class="footnote"
    style="vertical-align: super;">[<span>1</span>](#ftn1 "1I know one retired physics lecturer, for example who can't resist pointing out, er, issues with the way physics is presented to students. Why in Year 12 he once 'marked' an entire textbook I'd been set; the textbook didn't do very well.")</span>.

Those are just some of the reasons we might open our courseware, there
are other stories about why we might use stuff created elsewhere.

It sounds silly, but at the moment **we can't even share our own
courseware with our own students**. As I said not long ago, [<span>we
should at least open up all the resources to our existing
students</span>](http://ptsefton.com/2010/05/17/cheap-laugh-1-suggest-opening-up-courseware-just-a-little.htm)
so they can (a) go back to prerequisite stuff they missed or forgot and
(b) discover new things to enrol in.

To bring this back to Open Repositories <span
class="spCh spChx2013">–</span> there's a research project around the
idea of having two channels into our course materials, one via the
existing institutional systems we use for students and staff; the Moodle
LMS and the course production systems, but with a public-facing
discovery system that lets us expose at least some of our resources
under open licenses so we can see if the potential benefits are realised
and work out what the various stakeholders can do with openly licensed
quality-controlled learning materials.

Copyright Peter Sefton, 2010. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<[<span>http://creativecommons.org/licenses/by-sa/2.5/au/</span>](http://creativecommons.org/licenses/by-sa/2.5/au/)\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><span></span></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2010/07/m40ca94ba1.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project and published to
WordPress using [<span>The
Fascinator</span>](http://fascinator.usq.edu.au/desktop/desktop.htm).

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote-defined">[<span>1</span>](#ftn1-text)I know one
retired physics lecturer, for example who can't resist pointing out, er,
issues with the way physics is presented to students. Why in Year 12 he
once 'marked' an entire textbook I'd been set; the textbook didn't do
very well.</span>

</div>

</div>

</div>
