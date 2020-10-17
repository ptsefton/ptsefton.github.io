---
Author: ptsefton
Comments: true
Date: 2010-03-30 06:34:57+00:00
Slug: my-obsession-with-wordpress

Title: My obsession with WordPress
Wordpress_id: 522
---

<div>

<div class="page-toc">

-   [Why WordPress in particular](#id2)
-   [What's not to like?](#id3)

</div>

<div>

My team received some interesting, thoughtful and detailed feedback this
week from one of the computer programmers in one of our sister-teams at
USQ. One thread in this missive was to do with the superiority of
general purpose content management applications,and Joomla! In
particular over mere blogs. Oh, and the email contained the phrase <span
class="spCh spChx201c">“</span>I don<span
class="spCh spChx2019">’</span>t understand your obsession with
WordPress<span class="spCh spChx201d">”</span>. I wasn't the only
recipient, but I thought that now might be a good time to explain **my
own** supposed obsession with WordPress, and why, as the head of the
team that produces the [Integrated Content
Environment](http://ice.usq.edu.au/) and is building our repository
toolkit [The Fascinator](http://fascinator.usq.edu.au/) I have made sure
that our software are able to interoperate with WordPress in particular
and blogging software in general.

Actually, I'm not obsessed. I do use WordPress to run this blog[<span
style="vertical-align: super;"><span
class="endnote">i</span></span>](#ftn2) and the reason for that is
pretty much the same reason we support it and use it at ADFI (for the
[main blog](http://adfi.usq.edu.au/blog/) and for a more technical
[developers blog](http://intranet.adfi.usq.edu.au/dev_blog/)). It's one
of the most commonly used web publishing applications. And it's big in
academia. Our job is to build tools for academics and we use it for the
same reason they do. It's like a Commodore or a Falcon or a Camry, well
understood by mechanics, cheap, and easy to find spare parts, even if
it's not the best bit of engineering or it uses more fuel than we'd
like. As with such utilitarian transport WordPress is not the
interesting bit, it's where it can take you that counts, and academic
users are taking themselves all sorts of places with it.

There has been a lot written on this topic, and I'm not an expert, but
my impression is that one reason that blogging has worked well in the
academy is that the basic model of blog posts that don't change much is
very similar to journal articles. You publish, others comment on or
reference what you published. This used to happen at glacier-speed via
journal processes and letters and reviews and so on and now it an
happens fast, but it's essentially the same kind of discourse as we've
had for some centuries.

# <span id="id2"></span></a>Why WordPress in particular

One of the main reasons we chose to use and extend WordPress a few years
ago is that it has AtomPub support that works. This means that you can
post a document, like, say, this one, along with images and maybe other
stuff such as alternative renditions, using a standard protocol. Other
blogging software we tried a couple of years ago Just Didn't Work. We
have a few bugs in our AtomPub support, which we'll look at.

And it's obvious that WordPress is really widely used in academia. Off
the top of my head, here are just a few of the many, mostly recent
things I know are going on in the crowd that I follow in Google Reader
<span class="spCh spChx2013">–</span> I didn't subscribe to any of these
because of some predilection for WP, I follow this stuff because it's
interesting:

-   JISC in the UK have funded [JISCPress which produced the
    Digress.it](http://jiscpress.blogs.lincoln.ac.uk/2009/11/18/digress-it-version-2-3-was-released-last/)
    system for turning WordPress into a paragraph-level discussion
    system. Very important work for public review of all kinds of
    documents.

-   Joss Winn [squeezes all sorts of stuff out of
    WordPress](http://joss.blogs.lincoln.ac.uk/2010/02/22/wordpress-beyond-blogging/)[<span
    style="vertical-align: super;"><span
    class="endnote">ii</span></span>](#ftn0).

-   The [Code4Lib
    journal](http://journal.code4lib.org/process-and-structure) is
    powered by WordPress.

-   Tony Hirst is [full of useful tips for using
    WP](http://ouseful.wordpress.com/2010/03/25/viewing-wordpress-posts-in-chronological-order/).
    Tony pointed out to me that you can extract the content from a WP
    page using a single-page feed, making WP blogs ideal for integration
    with other services.

-   Peter Murray-Rust [has written about the shortcomings of
    WordPress](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=896) as he
    tries to force it to do data-rich publishing and was [trying our ICE
    templates with it last
    year](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=1720).

And:

-   When I was looking at referencing systems I was able to [make my
    blog Zotero compatible in three minutes
    flat](http://www.zotero.org/support/dev/wordpress).

-   [Ditto](http://lackoftalent.org/michael/blog/ore-wordpress-plug-in/)
    for when [I was exploring
    ORE](http://ptsefton.com/2008/10/14/what-the-oai-ore-protocol-can-do-for-you.htm).

Point is, there are so many plugins that when you need one, someone has
usually done it for you.

Look, I don't have stats on this, but it is clear that this is the
system to support first. I don't see all this activity around other
systems in the stuff I follow, which is biased towards the Open Access
Scholarly Publishing and repository communities.

So, we're making a WordPress plugin for our Anotar discussion/annotation
system; there's a huge audience who might (a) like to use it to allow
paragraph-anchored discussion, and eventually image-region anchored
discussion etc and (b) if enough people adopt it, then they might help
us build Anotar by extending the Anotar client, which we will be using
in other systems as well, such as Moodle.

# <span id="id3"></span></a>What's not to like?

To finish up, there **are** some aspects of WordPress that I really,
really hate[<span style="vertical-align: super;"><span
class="endnote">iii</span></span>](#ftn1)

-   **The key one is this 'river of news' format** which is the default.
    Go to a default WordPress home page and you get the latest article,
    and you have to scroll and scroll to see the next article. I reckon
    that for all but very specialised link blogs or twitter-like blogs
    this is incredibly poor usability <span
    class="spCh spChx2013">–</span> how am I supposed to know what's
    actually there?

-   **The default search behaviour is the same.** Look at [this search
    on Tony's
    blog](http://ouseful.wordpress.com/?s=word+press+single+post+rss).
    There's a reason Google doesn't do this. I was trying to find
    something that I know he wrote about getting the content of a post
    via an RSS feed but I get an incredibly long page containing several
    posts.

-   The **default theme mangles basic HTML** like bullet points for no
    apparent reason.

-   The **default behaviour of making the title of a post link to the
    'permalink' is silly** <span class="spCh spChx2013">–</span> I
    particularly loathe pages that link to themselves (not that I have
    bothered to change this on my site).

-   There's this fundamental **hard-wired distinction between 'posts'
    and 'pages'**. Ugh. It would be so much nicer if a document was a
    document, and it had metadata, such as 'document-type' and then you
    could configure how you wanted things displayed <span
    class="spCh spChx201c">“</span>on the home page give me abstracts of
    the last 6 posts, most recent first<span
    class="spCh spChx201d">”</span>. But then, you know it would be
    Drupal, not good ole WordPress.

Copyright Peter Sefton, 2010. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1"><a name="HTTP:::DBPEDIA.ORG:SNORQL:?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%"></a>![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2010/03/m40ca94ba4.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="endnote">[i](#ftn2-text) When PHP was born I hated it, the
way it mixed code and output formatting, but you know, modern PHP apps
have grown up a lot, and WordPress has a reasonably respectable, if
extremely poorly documented, way to write extensions. I avoided using it
for years, but it's actually OK, if you don't try to edit using the
stupid web-based editor.</span>

</div>

<div style="font-size: .9em;">

<span class="endnote">[ii](#ftn0-text)I am still trying to get over the
way he deposited a thesis in ePrints via an RSS feed.</span>

</div>

<div style="font-size: .9em;">

<span class="endnote">[iii](#ftn1-text) I'm not sounding obsessive am
I?</span>

</div>

</div>

</div>
