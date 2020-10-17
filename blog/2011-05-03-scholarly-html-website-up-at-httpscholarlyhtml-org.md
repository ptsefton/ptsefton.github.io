---
Author: ptsefton
Comments: true
Date: 2011-05-03 06:45:32+00:00
Slug: scholarly-html-website-up-at-httpscholarlyhtml-org

Title: Scholarly HTML website up at http://scholarlyhtml.org
Wordpress_id: 760
---

<div>

<div class="page-toc">

</div>

<div>

I have set up a website for [<span>Scholarly
HTML</span>](http://scholarlyhtml.org/) at
[<span>http://scholarlyhtml.org</span>](http://scholarlyhtml.org/). The
site is intended to hold some key documents about Scholarly HTML, what
it is, lists of tools etc. It will be populated as time allows. I will
announce this on the [<span>Scholarly
HTML</span>](https://groups.google.com/group/scholarly-html?hl=en)
mailing list now, and invite people from [<span>Beyond the
PDF</span>](https://groups.google.com/group/beyond-the-pdf?hl=en) when
it is a bit more mature.

We are going to continue with document authoring taking place over on
the EtherPads provided by the Open Knowledge Foundation <span
class="spCh spChx2013">–</span> I will call for people to review and
update documents from time to time, and when there is consensus I will
post them to the site. I am happy to give other responsible adults those
powers as well if they want them. The EtherPad entry point is:
[<span>http://scholarly-html.okfnpad.org/1</span>](http://scholarly-html.okfnpad.org/1).

I am trying out a WordPress deployment pattern I have been thinking
about for a while to use the WordPress 'stack of posts' as a version
control mechanism <span class="spCh spChx2013">–</span> every version of
every document is a post, and is intended to be immutable (that's a
governance issue). There will be a WordPress *page* for each node in the
site, but it won't have any content, rather it will run a query to find
the last post (as opposed to page) from a particular category. For
example, The faq page at
[<span>http://scholarlyhtml.org/faq/</span>](http://scholarlyhtml.org/faq/)
runs a query to find the latest post labelled as faq <span
class="spCh spChx2013">–</span> eg
[<span>http://scholarlyhtml.org/2011/03/25/faq-2011-03-25/</span>](http://scholarlyhtml.org/2011/03/25/faq-2011-03-25/).
The point of this is to get a full revision history in a simple way.

My experience with EtherPad is that it is great for collaboration and
awful for formatting, so I am proposing to use wiki-style markup in the
pad <span class="spCh spChx2013">–</span> making the job of publishing
much easier. There are [<span>a number of such
formats</span>](http://en.wikipedia.org/wiki/Lightweight_markup_language).
I was introduced to
[<span>asciidoc</span>](http://www.methods.co.nz/asciidoc/) recently. It
has rich formatting for technical documents and an established toolchain
for creating HTML, PDF and EPUB. It is a bit finicky and I'm not sure if
it is the best candidate for a format to support authoring of Scholarly
HTML but it does seem to be more complete than many. Rending EtherPad
documents is as easy as this:

> `curl http://okfnpad.org/ep/pad/export/schtml-core/latest?format=txt | asciidoc -vs - > core.html`

That creates a core.html file. To post it to the site I can use this
command to push the content to WordPress as an unpublished document with
the category 'core':

> `blogpost.py -vu -d html -t "Scholarly HTML core" -c core  post  core.html`

As I get time I will change the markup in the EtherPads over to asciidoc
and invite the collaborators back to work on them <span
class="spCh spChx2013">–</span> happy to discuss alternative formatting
arrangements if anyone objects to asciidoc.

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

</div>

</div>
