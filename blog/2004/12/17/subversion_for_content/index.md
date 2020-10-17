---
Title: "Subversion for content"
Slug: subversion_for_content
Date: 2004-12-17

---
James Tauber
[speculates](http://jtauber.com/blog/2004/12/04/structured_tag_naming_in_subversion)
on how [Subversion](http://en.wikipedia.org/wiki/Subversion) (it's a
version control system, used mainly by programmers) might be used to
manage the code for his web publishing application, Leonardo, which
powers this site. No updates, so maybe he has had no feedback.

I have nothing to offer regarding code in Subversion, but I have been
using Subversion to manage the content, as opposed to the code, here. A
few observations and speculations of my own follow.

[will\_be\_able](update:_leonardo_<a_href=)\_to\_do\_all\_the\_things\_i\_want"\>Update:
Leonardo [will be able](blog/2004/12/21/leonardo_and_subversion) to do
all the things I want

### Background

The Subversion book says to set up a project like this:

-   /branches

<!-- -->

-   /tags

<!-- -->

-   /trunk

So I did, when I put the content for this website under version control,
but it makes no sense for my content. I think what we need for content
is more like:

-   /drafts

<!-- -->

-   /published/projects

<!-- -->

-   /published/blog

At the moment I work on files in Leonardo's draft's directory and
preview them through the web application. Leonardo works by mapping
requests to text files in a wiki format, which it turns into HTML before
serving them to you, so you can just give it text files in special
places, or use a web interface to manage the files.

I edit the content from a Linux machine at home using XEmacs, and on the
ISP's site via SSH using Emacs, and sometimes on a Windows machine at
work using XEmacs. Subversion keeps all this in sync. If I make a change
at home I can commit it, then update on the web server to see the
change, but I could just as easily run a version of the website at home
as well for content development.

When I'm ready to publish, I use a |svn move| to send a file to the blog
or a permanent home in the site.

### Goals

I'm happy enough with Leonardo + Subversion at the moment, but what else
to I want?

I want to work on content in a variety of tools and formats for
different jobs: plain text, 'wiki' text, html, and OpenOffice.org and/or
Word for longer structured documents. I want to have a drafts area that
is portable across different machines, (Subversion is perfect for
this).I want to be able to browse my drafts as they will appear in HTML
via a preview area on the website, as I can with Leonardo, but with more
structure to the drafts area.

I also want to be able to have the same piece of content show up on more
than one path in a site, for example a document like this could appear
both in the blog 'stream' and as reference documentation in a projects
area. The reference version of this content might then change, under
version control of course, but I would likely leave the blogged version
pretty much alone except for a pointer to the new version.

I want full-text search.

And a tagging system like [del.icio.us](http://del.icio.us), possibly
with smart synchronization to my delic.ious.account, so that stuff I tag
there propagates to my local system, and public resources tagged locally
end up on del.icio.us automatically.

I want to be able to generate dynamic index pages automatically based on
a query, say ask for a list of titles and summaries for all the blog
entries tagged with OpenOffice.org.

I want to be able to work locally on a draft, commit it and have the
website automatically update its drafts area when I refresh the preview.

I want. I want. I want.

I'd better build it then, eh.

### Implementation

Managing revisions would probably be done by copying an existing
published document back into drafts, revising it there, then
re-publishing using a copy. In the case I mentioned above, where a piece
of reference content might go in the weblog and under a timeless path,
the new version would go to the reference path, and a the system should
then be able to add a pointer to the old blog entry to show where there
is a new version.

Bits of Subversion I think look promising for implementing the above
include:

-   The ability to use *properties* to store stuff like renditions, or
    even the images that go with a page. So original content could be in
    wiki format, or a word processor, or HTML, or whatever, and a
    normalized rendition could be stored for each item. Although if I
    stick with Leonardo, it will just use directories to accomplish
    this.

<!-- -->

-   *Cheap copies* of content, so publishing to multiple paths in a site
    becomes manageable.

<!-- -->

-   The *hooks* that can fire-off when you commit in Subversion could be
    used to full-text index pages, and presumably this could be made
    smart enough that multiple copies of an item would not show up as
    multiple results. I would also like to be able to set up special
    indexes that would pull out content
    [fraglets](blog/2004/04/28/platform_for_udell/) from documents and
    index them for retrieval on their own. These indexes could be
    specified using XPath or full-text (or XQuery I guess).

<!-- -->

-   *Properties* could also be used for content tagging. I don't think
    you can query on properties using Subversion (eg ask 'list all the
    docs with the XHTML tag'), but the full-text indexer could take care
    of that kind of index as well. Outside resources such as web pages
    would need a stub-record so they could have properties attached.

\$LastChangedDate: 2004-12-22 07:23:05 -0600 (Wed, 22 Dec 2004) \$

Site version: \$Rev: 144 \$
