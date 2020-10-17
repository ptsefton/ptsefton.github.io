---
Author: ptsefton
Comments: false
Date: 2011-07-15 04:52:47+00:00
Slug: the-repository-is-watching-automated-harvesting-from-replicated-filesystems
Category: ScholarlyHTML
Title: 'The repository is watching: automated harvesting from replicated filesystems'
Wordpress_id: 931
---

<div>

<div class="page-toc">

-   [<span>Managing a thesis</span>](#id2)
-   [<span>Demonstration</span>](#id3)
-   [<span>Installation notes</span>](#id4)

</div>

<div>

<span style="font-style:normal; "><span class="T2">[This is a repost of
</span></span>[<span style="font-style:normal; "><span
class="T2">http://jiscpub.blogs.edina.ac.uk/2011/07/15/the-repository-is-watching-automated-harvesting-from-replicated-filesystems-2/</span></span>](http://jiscpub.blogs.edina.ac.uk/2011/07/15/the-repository-is-watching-automated-harvesting-from-replicated-filesystems-2/)<span
style="font-style:normal; "><span class="T2"> please comment over
there]</span></span>

<span style="font-style:normal; "><span class="T2">One of the final
things I'm looking at on this jiscPUB project is</span></span> <span
style="font-style:normal; "><span class="T2">a demonstration of a new
class of tool for managing academic projects <span
class="spCh spChx2013">–</span> not just documents. For a while we were
calling this idea the <span
class="spCh spChx201c">“</span></span></span>[<span
style="font-style:normal; "><span class="T2">Desktop
Repository</span></span>](http://ptsefton.com/2011/02/16/another-look-at-desktop-repositories.htm)<span
style="font-style:normal; "><span class="T2"><span
class="spCh spChx201d">”</span>, the idea being that there would be
repository services watching your entire hard disk and exposing all the
content in a local website with repository and content management
services <span class="spCh spChx2013">–</span> that's possibly a very
useful class of application for some academics, but in this project we
are looking at a slightly different slant on that idea.</span></span>

The core use case I'm illustrating here is thesis writing, but the same
workflow would be useful across a lot of academic projects, including
all the things we're focussing on in the jiscPUB project <span
class="spCh spChx2013">–</span> academic users managing their portfolio
of work, project reporting and courseware management. This tool is about
a lot more than just ebook publishing, but I will look at that aspect of
it, of course.

In this post I will show some screenshots of The Fascinator repository
in action, talk about how you can get involved in trying it out, and
finish with some technical notes about installation and setup. I was
responsible for leading the team that built this software at the
University of Southern Queensland. Development is now being done at the
University of Central Queensland and the Queensland Cyber Infrastructure
Foundation where Duncan Dickinson and Greg Pendlebury continue work on
the [<span>ReDBox research data
repository</span>](http://code.google.com/p/redbox-mint/) which is based
on the same platform.

I know Theo Andrew at Edinburgh is keen to get some people trying this.
So this blog post will serve to introduce it and give his team some
ideas <span class="spCh spChx2013">–</span> we'll follow up on their
experiences if there are useful findings.

# <span id="id2"></span><span></span></a>Managing a thesis

The short version of how this thesis story might work is:

-   The university supplies the candidate with a dropbox-like shared
    file system they can use from pretty much any device to access their
    stuff. But there's a twist <span class="spCh spChx2013">–</span>
    there is a web-based repository watching the shared folder and
    exposing everything there to the web.

-   The university helpfully adds into the share a thesis template
    that's ready to go, complete with all the cover page stuff, margins
    all set, automated tables of contents for sections and tables and
    figures and the right styles <span class="spCh spChx2013">–</span>
    and trains the candidate in the basics of word processing.

-   The candidate works away on their project, keeping all their data,
    presentations, notes and so on in the Dropbox and filling out the
    thesis template as they go.

-   The supervisor can drop in on the work in progress and leave
    comments via an annotation system.

-   At any time, the candidate can grab a group, which we call a package
    of things to publish to a blog or deposit to a repository at the
    click of a button. This includes not just documents, but data files
    (the ones that are small enough to keep in a replicated file
    system), images, presentations etc.

-   The final examination process could be handled using the same
    infrastructure and the university could make its own packages of all
    the examiners reports etc for deposit into a closed repository.

The result is web-based, web-native scholarship where everything is
available in HTML, not just PDF or application file formats and there
are easy ways to route content to other repositories or publish it in
various ways.

Where might ebook dissemination fit into this?

Well, pretty much anywhere in the above that someone wants to either
take a digital object 'on the road' or deposit it in a repository of
some kind as a bounded digital thing.

# <span id="id3"></span><span></span></a>Demonstration

I have put a copy of Joss Winn's MA thesis into the system to show how
it works. It is [<span>available in the live
system</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/detail/2fcd657c012eb2d4f5f011a37b1d33fb/#22cc9a7fae17e01c1c699c970858ecf0)
(note that this might change if people play around with it). I took an
old OpenOffice .sxw file Joss sent me and changed the styles a little
bit to use the ICE conventions, I'm writing up a much more detailed post
about templates in general, so stay tuned for a discussion of the pros
and cons of various options for choosing style names and conventions and
whether or not to manage the document as a single file or multiple
chapters.

<span
style="display: block"><a name="graphics2"><span></span></a>![graphics2](/wp-content/uploads/2011/07/1772b368_643x287.jpeg)</span>Illustration
1: The author puts their stuff in the local file system, in this case
replicated by Dropbox.

<span
style="display: block"><a name="graphics7"><span></span></a>![graphics7](/wp-content/uploads/2011/07/m6338db22_643x323.jpeg)</span>Illustration
2: A web-view of Joss Winn's thesis.

\
The interface provides a range of actions.

<span
style="display: block"><a name="graphics9"><span></span></a>![graphics9](/wp-content/uploads/2011/07/m74679952.png)</span>Illustration
3: You can do things with content in The Fascinator including blogging
and export to zip or (experimental) EPUB

The EPUB export was put together as a demonstration for the Beyond The
PDF effort by Ron Ward. A the moment it only works on packages, not
individual documents, and it is using some internal Python code to
stitch together documents, rather than calling out to Calibre as I did
in [<span>earlier work on this
project</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/).
The advantage of doing it this way is that you don't have Calibre adding
extra stuff and reprocessing documents to add CSS <span
class="spCh spChx2013">–</span> but the disadvantage is that a lot of
what Calibre does is useful, for example working around known bugs in
reader software, but it does tend to change formatting on you, not
always in useful ways.

I put the EPUB into the dropbox so it is [<span>available in the demo
sit</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/detail/fac25c6c6183ffe6c1b874d02e0fe620/)e
(you need to expand the Attachments box to get the download <span
class="spCh spChx2013">–</span> that's not great usability I know). Or
you can [<span>go to the
package</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/detail/2fcd657c012eb2d4f5f011a37b1d33fb/#22cc9a7fae17e01c1c699c970858ecf0)
and export it yourself. Log in first, using admin as a username and a
the same for a password.

<span
style="display: block"><a name="graphics8"><span></span></a>![graphics8](/wp-content/uploads/2011/07/m32aa0aef_643x329.jpeg)</span>Illustration
4: Joss Winn's thesis exported as EPUB.

I looked a [<span>different way of creating an EPUB book from the same
thesi</span>](http://jiscpub.blogs.edina.ac.uk/2011/05/25/making-epub-from-wordpress-and-other-web-collections/)s
a while ago which will be available for [<span>a while here at the
Calibre server I set
up</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/).

One of the features of this software is that more than one person can
look at the web site <span class="spCh spChx2013">–</span> and there are
extensive opportunities for collaboration.

<a name="graphics5"><span></span></a>![graphics5](/wp-content/uploads/2011/07/m15505cf3_643x239.jpeg)Illustration
5: Colleagues and supervisors can leave comments via inline annotation
(including annotating pictures and videos)

<span
style="display: block"><a name="graphics6"><span></span></a>![graphics6](/wp-content/uploads/2011/07/m60f1be58.png)</span>Illustration
6: Annotations are threaded discussions

<span
style="display: block"><a name="graphics3"><span></span></a>![graphics3](/wp-content/uploads/2011/07/m70dddee9_643x350.jpeg)</span>Illustration
7: Images and videos can be annotated too. At USQ we developed a
Javascript toolkit called Anotar for this, the idea being you could add
annotation services to any web site quickly and easily.

This thesis package only contains documents, but one of the strengths of
The Fascinator platform is that it can aggregate all kinds of data,
including images, spreadsheets, presentation and can be extended to deal
with any kind of data file via plugins. I have added another package,
modestly calling itself [<span>the research object of the
future</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/detail/35ef5a6c8a43f8946e6480c52b9e8d87/#81ad16c49c0f7b7284edb82872eef547),
using some files supplied by Phil Bourne for the Beyond the PDF group
The Fascinator makes web views of all the content <span
class="spCh spChx2013">–</span> and can package it all as a zip file or
an EPUB.

<span
style="display: block"><a name="graphics10"><span></span></a>![graphics10](/wp-content/uploads/2011/07/2c8aa7f2_643x355.jpeg)</span>Illustration
8: A spreadsheet rendered into HTML and published into an EPUB file
(demo quality only)

This includes turning PowerPoint into a flat web page.

<span
style="display: block"><a name="graphics11"><span></span></a>![graphics11](/wp-content/uploads/2011/07/m578316a1_643x397.jpeg)</span>Illustration
9: A presentation exported to EPUB along with data and all the other
parts of a research object

# <span id="id4"></span><span></span></a><span style="font-style:normal; "><span class="T2">Installation notes</span></span>

<span style="font-style:normal; "><span class="T2">Installing The
Fascinator</span></span>  <span style="font-style:normal; "><span
class="T2">(I did it on Amazon's EC2 cloud on Ubuntu 10.04.1 LTS) is
straightforward. These are my notes <span
class="spCh spChx2013">–</span> not intended to be a detailed how-to,
but possibly enough for experienced programmers/sysadmins to work it
out.</span></span>

-   Check it out.

        sudo svn co https://the-fascinator.googlecode.com/svn/the-fascinator/trunk /opt/fascinator

-   Install Sun's Java

        sudo apt-get install python-software-properties

        sudo add-apt-repository ppa:sun-java-community-team/sun-java6

        sudo apt-get update

        sudo apt-get install sun-java6-jdk

    [<span
    class="Source_20_Text">http://stackoverflow.com/questions/3747789/how-to-install-the-sun-java-jdk-on-ubuntu-10-10-maverick-meerkat/3997220\#3997220</span>](http://stackoverflow.com/questions/3747789/how-to-install-the-sun-java-jdk-on-ubuntu-10-10-maverick-meerkat/3997220#3997220)<span
    class="Source_20_Text"><span
    style="background-color:transparent; color:#000000; font-size:10.5pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
    class="T7"> </span></span></span>

-   Install Maven 2.

        sudo apt-get install maven2

-   [<span>Install
    ICE</span>](http://code.google.com/p/integrated-content-environment/wiki/InstalIICEServiceOnUbuntu)
    or point your config at an ICE service. I have [<span>one running
    for the jiscPUB
    project</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/api/convert)
    <span class="spCh spChx2013">–</span> you can point to this by
    changing the `~/.fascinator/system-config.json` file.

-   Install Dropbox or your file replication service of choice <span
    class="spCh spChx2013">–</span> a little bit of work on a headless
    server but there are instruction linked from the Dropbox.com site.

-   Make some configuration changes, see below.

-   To run ICE and The Fascinator on their default ports on the same
    machine add this stuff to /etc/apache2/apache.conf (I think the
    proxy modules I'm using here is non-standard).

        LoadModule  proxy_module /usr/lib/apache2/modules/mod_proxy.so

        LoadModule  proxy_http_module /usr/lib/apache2/modules/mod_proxy_http.so

        ProxyRequests Off

        <Proxy *>

        Order deny,allow

        Allow from all

        </Proxy>

        ProxyPass        /api/ http://localhost:8000/api/

        ProxyPassReverse /api/  http://localhost:8000/api/

        ProxyPass       /portal/ http://localhost:9997/portal/

        ProxyPassReverse /portal/ http://localhost:9997/portal/

-   Run it.

        cd /opt/fascinator

        ./tf.sh restart

Configuration follows:

-   <span style="font-style:normal; "><span class="T2">To set up the
    harvester, add this to the empty jobs list in
    </span></span>`~/.fascinator/system-config.json`

<!-- -->

    "jobs" : [
                       {
                           "name": "dropbox-public",
                           "type": "harvest",
                           "configFile":
    "${fascinator.home}/harvest/local-files.json",
                           "timing": "0/30 * * * * ?"
                       } 

*And change* /harvest/local-files.json to point at the Dropbox directory

    "harvester": {

            "type": "file-system",

            "file-system": {

                "targets": [

                    {

                        "baseDir": "${user.home}/Dropbox/",

                        "facetDir": "${user.home}/Dropbox/",

                        "ignoreFilter": ".svn|.ice|.*|~*|Thumbs.db|.DS_Store",

                        "recursive": true,

                        "force": false,

                        "link": true

                    }

                ],

                "caching": "basic",

                "cacheId": "default"

            }

To add the EPUB support and the red branding, unzip the skin files in
this zip file into the portal/default/ directory:
[<span>http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/download/551148ce6d80bfc0c9c36914f9df4f91/jiscpub.zip</span>](http://ec2-50-19-86-198.compute-1.amazonaws.com/portal/default/download/551148ce6d80bfc0c9c36914f9df4f91/jiscpub.zip)

    unzip -d /opt/fascinator/portal/src/main/config/portal/default/ jispub.zip

<span style="font-style:normal; "><span class="T2">[This is a repost of
</span></span>[<span style="font-style:normal; "><span
class="T2">http://jiscpub.blogs.edina.ac.uk/2011/07/15/the-repository-is-watching-automated-harvesting-from-replicated-filesystems-2/</span></span>](http://jiscpub.blogs.edina.ac.uk/2011/07/15/the-repository-is-watching-automated-harvesting-from-replicated-filesystems-2/)<span
style="font-style:normal; "><span class="T2"> please comment over
there]</span></span>

Copyright <span rel="http://purl.org/dc/elements/1.1/creator"
resource="http://trove.nla.gov.au/people/541658"><span
property="http://xmlns.com/foaf/0.1/name"
resource="http://trove.nla.gov.au/people/541658">Peter
Sefton</span></span>, 2011-07-12. Licensed under <span
rel="http://creativecommons.org/licence">Creative Commons
Attribution-Share Alike 2.5 </span><span
rel="http://creativecommons.org/licence">Australia</span>.
\<http://creativecommons.org/licenses/by-sa/2.5/au/\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1"><a name="graphics1"><span></span></a>![graphics1](/wp-content/uploads/2011/07/m40ca94ba1.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project.

</div>

</div>
