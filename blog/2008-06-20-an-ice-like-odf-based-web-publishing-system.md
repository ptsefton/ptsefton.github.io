---
Author: ptsefton
Comments: true
Date: 2008-06-20 05:55:10+00:00
Slug: an-ice-like-odf-based-web-publishing-system

Title: An ICE like ODF based web publishing system
Wordpress_id: 146
---

<div>

<div class="page-toc">

</div>

<div>

From Kay Ramme at the GullFOSS blog at Sun comes [this
demo](http://blogs.sun.com/GullFOSS/entry/odf_www_an_odf_wiki) of a
wiki-like system using ODF as a document format and OpenOffice.org as an
editor.

It seems to be using WebDAV to allow users to edit documents on a
server, then convert them to HTML automatically when they load the
document in a browser.

Good idea to have the user change a document and automatically render it
to HTML on request.

Same idea, in fact as the [ICE system.](http://ice.usq.edu.au/)

Some differences with ICE:

-   ICE doesn't use WebDAV because, well, it doesn't work with Windows
    reliably and it doesn't work with the Mac too well either.

-   ICE doesn't rely on OpenOffice's native save as HTML feature which
    will produce awful results on all but the simplest text documents. A
    few of several reasons not to use it:

    -   It gets list formatting badly wrong.

    -   It exports photos at full resolution and puts height and width
        attributes on them to resize them meaning that you end up
        shipping megabytes when you should be shipping kilobytes.

    -   It is not styles-based so you have no way of configuring it to
        do things like use pre formatted text in the right places.

-   ICE is styles-driven which means it produces very clean HTML
    compared the rubbish that office suites spit out.

-   ICE uses templates to help people apply styles.

-   ICE can deal with Microsoft Word documents and has cleanup code to
    correct some of the interop issues with OpenOffice.org.

-   ICE has a version-controlled back end courtesy of Subversion so it
    can be used by distributed teams.

-   ICE can create IMS content packages for courseware.

-   ICE has an Atom Publishing Protocol button which can send stuff to a
    blog <span class="spCh spChx2013">–</span> and do a much better job
    of formatting than the Sun Weblog Publisher addin too.

-   ICE has a plugin architecture and a growing number of hooks for
    integrating other content types like chemistry data.

-   ICE doesn't deal with spreadsheets, but we could add that pretty
    easily.

-   ICE doesn't have a mechanism to create new pages by linking to a
    target that doesn't exist <span class="spCh spChx2013">–</span> if
    we add that we'll make it a bit smoother than what's shown in the
    demo.

-   ICE can be used as a conversion service by other systems.

I could go on.

If you like the demo, check out [some of
ours](http://ice.usq.edu.au/presentations/demos/index.htm) although I
note that we don't have a really basic one that shows what Kay shows in
hers. We'll get on to that.

</div>

</div>
