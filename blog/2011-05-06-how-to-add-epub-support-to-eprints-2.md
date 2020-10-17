---
Author: ptsefton
Comments: false
Date: 2011-05-06 00:31:19+00:00
Slug: how-to-add-epub-support-to-eprints-2

Title: How to add EPUB support to EPrints
Wordpress_id: 767
excerpt: Putting EPUB into EPrints as-isWhat does the repository need to do?In a previous post here on the jiscPUB project I said it would be good for the EPrints repository software to support EPUB uploads. I#8217;d love to do something with hellip; a href=quot;http://ptsefton.com/?p=758quot;Continue reading span class=quot;meta-navquot;rarr;/span/a a href=quot;http://jiscpub.blogs.edina.ac.uk/?p=183quot;Continue reading span class=quot;meta-navquot;rarr;/span/a a href=&amp;amp;amp;quot;http://jiscpub.blogs.edina.ac.uk/?p=204&amp;amp;amp;quot;Continue reading span class=&amp;amp;amp;quot;meta-nav&amp;amp;amp;quot;rarr;/span/a &amp;amp;lt;a href=&amp;amp;quot;http://jiscpub.blogs.edina.ac.uk/?p=214&amp;amp;quot;&amp;amp;gt;Continue reading &amp;amp;lt;span class=&amp;amp;quot;meta-nav&amp;amp;quot;&amp;amp;gt;&amp;amp;amp;rarr;&amp;amp;lt;/span&amp;amp;gt;&amp;amp;lt;/a&amp;amp;gt; &amp;lt;a href=&amp;quot;http://anotar.ptsefton.com/?p=305&amp;quot;&amp;gt;Continue reading &amp;lt;span class=&amp;quot;meta-nav&amp;quot;&amp;gt;&amp;amp;rarr;&amp;lt;/span&amp;gt;&amp;lt;/a&amp;gt; &lt;a href=&quot;http://anotar.ptsefton.com/?p=310&quot;&gt;Continue reading &lt;span class=&quot;meta-nav&quot;&gt;&amp;rarr;&lt;/span&gt;&lt;/a&gt;
---

<div>

<div class="page-toc">

</div>

<div>

[This is a repost from the JISCPub project <span
class="spCh spChx2013">–</span> please comment over there
[<span>http://jiscpub.blogs.edina.ac.uk/2011/05/03/how-to-add-epub-support-to-eprints-8/</span>](http://jiscpub.blogs.edina.ac.uk/2011/05/03/how-to-add-epub-support-to-eprints-8/)
]

In a [previous post here on the jiscPUB projec<span
style="color:#000000; "><span
class="T1">t</span></span>](http://ptsefton.com/2011/04/12/metadata-in-word-processing-monographs.htm)<span
style="color:#000000; "><span class="T1"> I sai</span></span>d it would
be good for the EPrints repository software to support EPUB uploads.

> I<span class="spCh spChx2019">’</span>d love to do something with a
> repository <span class="spCh spChx2013">–</span> I<span
> class="spCh spChx2019">’</span>m thinking that it would be great to
> deposit theses in EPUB format <span
> class="spCh spChx2013">–</span> and the repository could provided a
> web-based reader, along the lines
> of [<span>IbisReader</span>](http://ibisreader.com/), which Liza Daly
> and company created. I<span class="spCh spChx2019">’</span>m looking
> at you, Eprints! Eprints already almost supports this, if you upload a
> zip file it will stash all the parts for you in a single record. All
> we would need would be something like this[<span> little reader my
> colleagues at USQ
> made</span>](../little%20reader%20my%20colleagues%20at%20USQ%20made).
> It would just be a matter of transforming the EPUB TOC into JSON, and
> loading the JavaScript into an Eprints page.

I Called Les Carr's attention to the post and he responded:

> [<span>lescarr</span>](https://twitter.com/#!/lescarr)
> [<span>@ptsefton</span>](https://twitter.com/#!/ptsefton) just tell us
> what to do and we'll do it.

OK. Here goes with my specification for how EPrints could add at least
basic support for EPUB.

# <span id="id2"></span><span></span></a>Putting EPUB into EPrints as-is

To explore this, I ran the [<span>EPrints live
CD</span>](http://wiki.eprints.org/w/EPrints_Live_CD_Help)
(livecd\_v3.1-x.iso) under VirtualBox on Windows 7 <span
class="spCh spChx2013">–</span> this worked well when I gave it a decent
amount of memory <span class="spCh spChx2013">–</span> it didn't manage
to boot in several hours at 256Mb. (Note that no repositories were
harmed in the making of this post <span class="spCh spChx2013">–</span>
I did not change the Eprints code at all.)

The EPUB format is a zipfile containing some XHTML payload documents, a
manifest, and a table of contents. On one level EPRINTS already supports
this, in that there is support for uploading ZIP files. I tested this
using Danny Kingsley's thesis (as received, with no massaging or adding
metadata apart from tweaking the title in Word) [<span>converted to
EPUB</span>](http://dl.dropbox.com/u/24994372/Formatted_PhD_12May09.epub)
via the ICE service [<span>I have been working
on</span>](http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/doc).

The procedure:

1.  Generated an EPUB using ICE.

2.  Changed the file extension to .zip.

3.  Uploaded it into EPrints.

The result is an EPrints item with many parts. If you click on any of
the HTML files that make up the thesis then they work as web pages <span
class="spCh spChx2013">–</span> ie the table of contents (if you can
find it amongst the many files) links to the other pages. But there is
no navigation to tie it all together you have to keep hitting back <span
class="spCh spChx2013">–</span> each HTML page from the EPUB is a stand
alone fragment.

<span
style="display: block"><a><span></span></a>![graphics1](/wp-content/uploads/2011/05/ma53f402_643x400.jpeg)</span>Illustration
1: The management interface in EPrints showing all the parts of an EPUB
file which has been uploaded and saved as a series of parts in a single
record.

At this point I went off on a side trip, and [wrote this little tool
<span class="spCh spChx2013">–</span> to add an HTML view to an EPUB
file](http://ptsefton.com/2011/04/15/introducing-epub2html-adding-a-plain-html-view-to-an-epub.htm).

# <span id="id3"></span><span></span></a>Putting enhanced EPUB into Eprints

Now, lets try that again with [<span>the
version</span>](http://dl.dropbox.com/u/24994372/Formatted_PhD_12May09.epub)
where I added an HTML index page to the EPUB using the new demo tool,
epub2html. I uploaded the file, clicked around semi-randomly until I
figured out how to see all the files listed from the zip, and selected
index.html as the 'main' file. From memory I thought the repository
would do that for me but it didn't. Anyway, I ended up with this:

<span
style="display: block"><a><span></span></a>![graphics3](/wp-content/uploads/2011/05/5fc3b428_643x332.jpeg)</span>Illustration
2: The details screen that users see - clicking on the description takes
you to the HTML page I picked as the main file.

<span
style="display: block"><a><span></span></a>![graphics2](/wp-content/uploads/2011/05/m629e91b8_643x417.jpeg)</span>Illustration
3: A rudimentary ebook reader using an inline frame.

If I click on the link starting with Other, there we have it <span
class="spCh spChx2013">–</span> more-or-less working navigation within
the limits of this demo-quality software. All I had to do was change the
extension from .epub to .zip and select the entry page, and I had a
working, navigable document.
The initial version of epub2html used the unsupported epubjs as a web
based reader-application <span class="spCh spChx2013">–</span> but Liza
Daly suggested I use the more up to date Monocle.js library instead. I
tried that but I'm afraid the amount of setup required is too much for
the moment so what you see here is an HTML page with an inline frame for
the content.

# <span id="id4"></span><span></span></a>What does the repository need to do?

So what does the EPrints team need to do to support EPUB a bit better?

-   Add EPUB to the list of recognised files.

-   Upon recognising an EPUB...

    -   Use a service like epub2html that can generate an HTML view of
        the EPUB. I wrote mine in Python, Eprints is written in Perl but
        I'm sure that can be sorted out via a re-write or a web service
        or something<span class="footnote"
        style="vertical-align: super;"><span
        id="ftn1-text">[<span>\*</span>](#ftn1)</span></span>.

    -   Allow the user to download the whole EPUB, or choose to use an
        online viewer. Could be static HTML, frames (not nice), or some
        kind of JavaScript based viewer.

    -   Embed some kind of viewer in the EPrints page itself, or at
        least provide a back-link in the document viewer to the EPrints
        page.

Does that make sense, Les?

[This is a repost from the JISCPub project <span
class="spCh spChx2013">–</span> please comment over there
[<span>http://jiscpub.blogs.edina.ac.uk/2011/05/03/how-to-add-epub-support-to-eprints-8/</span>](http://jiscpub.blogs.edina.ac.uk/2011/05/03/how-to-add-epub-support-to-eprints-8/)
]

Copyright <span rel="http://purl.org/dc/elements/1.1/creator"
resource="http://trove.nla.gov.au/people/541658"><span
property="http://xmlns.com/foaf/0.1/name"
resource="http://trove.nla.gov.au/people/541658">Peter
Sefton</span></span>, 2011-04-15. Licensed under <span
rel="http://creativecommons.org/licence">Creative Commons
Attribution-Share Alike 2.5 Australia</span>.
\<http://creativecommons.org/licenses/by-sa/2.5/au/\>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project.

------------------------------------------------------------------------

<div class="footnote-defined">

<span id="ftn1">[<span>\*</span>](#ftn1-text)</span> Maybe there's a
Python interpreter written in Perl?

</div>

</div>

</div>
