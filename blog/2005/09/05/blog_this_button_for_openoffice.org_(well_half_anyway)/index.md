---
Title: "Blog this button for OpenOffice.org (well half anyway)"
Slug: blog_this_button_for_openoffice.org_(well_half_anyway)
Date: 2005-09-05

---
<div>

Last year Tim Bray wrote about OpenOffice.org, and suggested that,

> Geeks like me are fine with writing in Emacs, but lots of people seem
> to like writing in word processors, and as of this week, I think that
> any word processor without a “Blog This” button is just broken.

> <http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice>

I'm one of those people who likes writing in word processors. See, I
told you I wasn't a geek.

As far as I know most word processors are still broken (is there a "Blog
this!" button available for Word, AbiWord, OpenOffice.org etc? Google
search for '"blog this" button word processor' gets you my site so maybe
not.) But I finally made myself a "Blog this!" button.

I have been working with a team from USQ on a system called
[ICE.](http://ice.usq.edu.au/) ICE is an open source content management
system designed mainly to work with courseware. It can take a bunch of
OpenOffice.org Writer files that happen to be under
[Subversion](http://subversion.tigris.org/) control (Subversion is a
version control system used mainly by programmers) and automatically
generate HTML renditions for each document. It can organize packages of
content so they can be published as stand-alone, or for deliver through
a Learning Management System, but it can also just take a directory of
word processing documents and turn them all into HTML.

This document is the first one I wrote for my blog in OpenOffice and
published with the 'Bog this!' button. Here's what I did.

1.  Today I added a few lines of code to an ICE configuration file so
    that any item of content can be sent to the
    [Leonardo](http://jtauber.com/leonardo)-powered site you're looking
    at. This was really simple; I just copied the 'draft' form straight
    out of Leonardo and added it my site. Five minutes work for any
    competent programmer. About half an hour for me. This will show up
    in ICE when it's properly sorted.

2.  Tonight when I got home I added a blog directory to my subversion
    working copy I keep for all my articles, half written songs and so
    on. This means that I can get to it on any of my computers, or check
    it out at work over the 'net. ICE can take care of the subversion
    commands for you but I typed this:

        $ mkdir blog
        $ svn add blog
        A         blog

3.  I opened Writer and started a new document. Because I have the ICE
    template installed I can format stuff using the styles set up in ICE
    and have my documents come out as XHTML. (Did I mention before that
    it's a good idea to [Use
    Styles](http://ptsefton.com/blog/2005/03/02/use_styles)?)

    For example this paragraph is in style `li1p` – that's a paragraph,
    `p` that's part of a first level list item, `li`. The above
    paragraph is `li1n` where the `n` is for number. Above that we have
    `pre2`, for preformatted text. I can apply all these styles either
    through a custom menu, like the one I [wrote about on
    xml.com](http://www.xml.com/pub/a/2005/01/26/hacking-ooo.html) or
    using the keyboard.

    You can check for yourself if you're interested in this stuff that
    the XHTML is pretty neat, although it may have some stray namespace
    declarations that don't belong because of the way I hooked this all
    up.

4.  I typed this out, saved it in my blog directory, then used my local
    ICE site to view it as HTML. ICE runs as a local web server. When I
    was happy, after seeing the web preview a few times, I clicked the
    "Blog this!" button and it presented me with a pre-filled form that
    sent the content to my Leonardo blog site. There it became a draft
    and I had only to look it over and click one more button.

5.  I rejoiced. I'd much rather work in a word processor than muck
    around with wiki formatting.

Future improvements in ICE will mean I could work in Microsoft Word
using the same set of styles. I might choose to do this for longish
documents with complex heading structure 'cos Writer's outliner is
terrible, but otherwise Writer is fine. And I would definitely choose
Writer for book-length content where I want to use master documents to
tie-together small pieces, and get PDF renditions for free without
mucking around with add-ins. It's probably possible to put the 'Blog
this!' button into Office, but I'm happy with where it is on my ICE web
site, where I can preview my content.

Future developments in Leonardo will add support for the Atom Publishing
Protocol, then I won't have to steal a form from Leonardo. When I get
around to writing it I will be able to use a standard bit of code to
talk to any Atom-compliant blogging software.

****

</div>
