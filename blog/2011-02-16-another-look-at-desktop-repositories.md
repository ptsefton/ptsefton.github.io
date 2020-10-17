---
Author: ptsefton
Comments: true
Date: 2011-02-16 05:19:18+00:00
Slug: another-look-at-desktop-repositories

Title: Another look at desktop repositories
Wordpress_id: 679
---

<div>

[Update: There were a few issues with this post, I forgot the reference
list, and a couple of formatting bugs - hand fixed it]

<div class="rendition-links">

<span class="pdf-rendition-link">[PDF
version](/wp-content/uploads/2011/02/desktop-repos-again.pdf.pdf "View the printable version of this page")</span>

</div>

<div class="body">

<div>

This post is a refresh on where we are at with the idea of Desktop
Repositories, sparked by a discussion I had this week with people from
[Intersect](http://www.intersect.org.au/), the NSW eResearch
organisation where they are working on the next version of
[FieldHelper](http://acl.arts.usyd.edu.au/index.php?option=com_content&task=view&id=178&Itemid=211),
tool that originated at The University of Sydney. I met with Anne
Cregan, Chris Kenward and Raul Carrizo on Monday 2001-02-14 (I wonder
what it was about their building, which seems to house a lot of
insurance companies. There were lots of couriers delivering roses, and
blokes carrying bunches of same. The place reeked of romance. Strange.)

The idea of FieldHelper is to allow field workers (archaeologists,
linguists, anthropologists etc) to manage and describe their data and
get it off their hard drives in to 'staging repositories'. The new round
of work on FieldHelper will be funded under the Australian National Data
Service (ANDS) data capture program. I wanted to make sure that the
Intersect team were aware of the work we've been doing towards similar
aims, and to let them know about the software we've built. My team at
USQ is funded by ANDS to work on software for managing metadata about
research data, the [ReDBox
application](https://fascinator.usq.edu.au/trac/wiki/Projects/ReDBox).
This work is under the ANDS metadata stores program, and is therefore
focussed on describing captive data rather than the process of capture,
but my team has had an interest in data mustering for a while, and we
have done some small pilot projects. My thinking is that if there is
enough of a match, then our work might give the new FieldHelper a bit of
a head-start. If not, that's useful data too.

**First, some history.** I [proposed the idea of a desktop
eResearch](http://ptsefton.com/2009/03/05/desktop-eresearch-revolution.htm)
repository in 2009, inspired by FieldHelper and by metadata-aware
consumer tools for media-data management like Picasa and iTunes. I was
also inspired by some comments from Mr Eprints himself, Les Carr. This
was picked up by a few people and I [talked to people in Sydney about
the
ideas](http://ptsefton.com/2009/03/31/trip-report-intersect-and-university-of-sydney.htm).
I posted [an early view of what the architecture might look
like](http://ptsefton.com/2009/06/12/desktop-repositories-smashing-up-powerpoint.htm).

In summary, the idea was to provide a platform for researchers that
would:

1.  **Watch their hard disk** (on the laptop, desktop, fileshare or
    instrument) for new files.

2.  Show them the files in a web browser - emphasising that even though
    the files are still private, and local **the web is everything**.

3.  Provide **a plug-in framework for handling any kind of file**,
    extracting technical metadata, indexing it to death, and making it
    web-viewable.

4.  Allow the researcher to **organise and classify** the files using
    both formal and informal metadata and send collections of stuff off
    to be backed up, preserved or disseminated.

The ADFI team, in a project led by Duncan Dickinson did some work with a
researcher at USQ, Leonie Jones, on a Vietnam War history project
exploring what a media-rich desktop repository for history research
might look like, and demonstrating how some of the content she's working
with can be pushed up to the World Wide (as opposed to desktop) Web for
a community of veterans to interact with the materials Leonie has
collected; tagging and geolocating photos, identifying people in
pictures using the official roll held at the Australian War Memorial,
and reconstructing the official history. This is covered in a couple of
conference presentations from eResearch Australasia [1]. And you can
[buy the DVD](http://www.awm.gov.au/shop/item/100035589/). We didn't
help make the DVD, mind, but we would like to help manage the resources
that went into making it and future productions.

All this work has been on hold at ADFI, as we work on the ReDBox
application for research metadata, but we have restarted some of it in
the wake of [Beyond the
PDF](https://sites.google.com/site/beyondthepdf/). Very soon we'll
launch [a little site which allows people to put stuff in Dropbox and
then see it with in a few minutes on the
web](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#2e8e42f5db150edfc4e3d9ed5a271b78).
Oops. Looks like that was a launch, of sorts. That
[link](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#2e8e42f5db150edfc4e3d9ed5a271b78)
is to a package I made out of the sample files from the BTPDF workshop,
which [Anita de
Waard](http://www.elsevier.com/wps/find/newsroomhome.newsroom/bio_anitadewaard)
refers to as "The Bourne Corpus". All I did was drop them in Dropbox,
wait a minute or two for them to sync and then I was able to browse to
the files thru the web interface, select them, click to package the
selected files, and then drag-n-drop them into the order I wanted them.

So, the package contains a bunch of stuff including some draft versions
of the document, meaning it is a bit of a mess, but it does show how we
can publish stuff like the [supporting
data](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#3cc347184b4aafb7c780d3b3d6071b80)
or [info about the
data](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#3d307f1c16ec00d6b9a58363859ae56d)
or
[stuff](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#1546bb2186444297660d5f6459e87d35)
[about the
grant](http://dev-win.adfi.usq.edu.au/btpdf/default/detail/e96e2301302fdbbe418aedace234354f/#1546bb2186444297660d5f6459e87d35).
Log in with any old OpenId and you can make your own packages. If you'd
like to try the system on your own files, drop me a line and I will
share the Dropbox with you. The demo will probably be around until mid
2011 - these links are not guaranteed persistent. There are bugs.
Batteries not included. If you want your own, stay tuned and I'll post
when we have installation instructions.

Copyright Peter Sefton, 2011. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en;"><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"><!-- --></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/02/desktop-repos-again_filesm40ca94ba.png.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

1\. 2009 Nov 10 [Conference paper] Dickinson D, Sefton P. Creating an
eResearch desktop for the Humanities. Presented at: eResearch
Australasia 2009 Sydney: 2009. Available from:
http://eprints.usq.edu.au/6090/

\
\

</div>

</div>

</div>
