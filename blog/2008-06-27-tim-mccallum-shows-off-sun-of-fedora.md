---
Author: ptsefton
Comments: true
Date: 2008-06-27 07:12:09+00:00
Slug: tim-mccallum-shows-off-sun-of-fedora

Title: Tim McCallum shows off Sun of Fedora
Wordpress_id: 152
---

<div>

<div class="page-toc">

</div>

<div>

Here in the Repository Services group at USQ we have been working on a
project funded by [ARROW](http://www.arrow.edu.au/) and in partnership
with the [National Library of Australia](http://nla.gov.au/). It's a bit
of repository software originally designed to explore the [Apache
Solr](http://lucene.apache.org/solr/)search application.

We looked at Solr last year at USQ, and [I blogged about it as part of a
consulting
job](http://aanro-repo.blogspot.com/2007/10/solr-demo-is-up.html) to
compare [VTLS Vital](http://vtls.com/products/vital),
[Fez](http://espace.library.uq.edu.au/view.php?pid=UQ:11924) and
[Muradora](http://drama.ramp.org.au/). Since then, Muradora and Fez have
both started using Solr, there is a plugin for Fedora's standard text
search package to use Solr. As far as I know VTLS have not announced
anything to do with Solr apart from their Visualizer product.

The goal of the current project is to create a simple interface to
Fedora that uses a single technology <span
class="spCh spChx2013">–</span> that's Solr <span
class="spCh spChx2013">–</span> to handle all browsing, searching and
security. This contrasts with solutions that use RDF for browsing by
'collection',
[XACML](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xacml)
for security and a text indexer for fulltext search, and in some cases
relational database tables as well. We want to see if taking out some of
these layers makes for a fast application which is easy to configure. So
far so good.

This is not a replacement for [VTLS
Vital](http://vtls.com/products/vital), and is not intended to replace
the [NLA's ARROW Discovery service](http://search.arrow.edu.au/) which
is also based on Solr.

We now have a working demonstration with content pulled from a number of
repositories, and are able to show the main things we set out to
achieve. Administrators can set up a new portal which shows a subset of
the main index with a few clicks, and we have a security model which can
restrict access to metadata and data based on group roles.

I will post some more information about the emerging architecture of the
application soon, but for now Tim McCallum has put together a [demo
screencast](http://www.youtube.com/watch?v=NLVRjh2af1Y), which had him
slaving over a hot video editor over the weekend (forgive any glitches,
it's his first time). Or [you can try it out for
yourself](http://rspilot.usq.edu.au:8080/sun-of-fedora/) (Demo URL may
not work after October 2008). If you want to log in contact me for a
password.

Thanks to Oliver Lucido who did most of the development, building on
work he did for the FRED project last year with David Levy. Tim has also
been assisting, with project coordination from Bron Chandler and
stake-holding from Neil Dickson at ARROW and Alison Dellit at the NLA.

</div>

</div>
