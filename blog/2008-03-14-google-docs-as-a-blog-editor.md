---
Author: ptsefton
Comments: true
Date: 2008-03-14 02:51:01+00:00
Slug: google-docs-as-a-blog-editor

Title: Google Docs as a blog editor?
Wordpress_id: 96
---

<div>

<span class="pdf-rendition-link">[View as
PDF](/wp-content/uploads/2008/03/google-docs-blogging.pdf)</span>
<div class="page-toc">

</div>

<div>

Last post here was [another complaint about Google
Docs](http://ptsefton.com/2008/02/27/google-claims-to-support-odf-over-ooxml-but-google-docs-has-awful-odf-support.htm)
and its terrible OpenDocument Format support. I've been very sick for
the last little while and it turns out purely by coincidence that the
next post I feel strong enough to write is another complaint about
Google Docs. I promise I'll complain about something else next, and then
maybe say something nice when I'm feeling particularly strong.

Via [OUseful Info](http://blogs.open.ac.uk/Maths/ajh59/) I found out
about [how Google Docs can be used as a blog
editor](http://bavatuesdays.com/publishing-google-docs-to-your-blog/),
where the author says:

> I wanted to test it out, so this morning I tried pulling in the
> outline of a presentation I will be doing with Jerry and Andy at ACCS
> this Friday in order to see how clean it is <span
> class="spCh spChx2014">—</span> let me tell you something, it is very
> clean!
>
> <http://bavatuesdays.com/publishing-google-docs-to-your-blog/>

It did indeed seem like Google Docs was producing clean code in the
examples cited so I went to check it out. Here's what I found:

1.  There's no ATOM Publishing Protocol (APP) support. This is a big
    disappointment. To publish to WordPress you have to use the
    antiquated Movable Type API.

2.  Google Docs was still not producing good clean HTML for me, either
    in the editing interface or when the document was pushed to my blog.
    When I use it I get `br` tags in between my paragraphs rather than
    proper `p` elements. How did those other people get it to output
    proper paragraphs? I finally figured out that you need to select
    your paragraphs and apply the Style `Normal paragraph`. That's a
    small amount of progress.

    <span
    style="display: block"><a name="graphics1"></a>![graphics1](/wp-content/uploads/2008/03/af482a9s143x194.jpg)</span>

3.  List nesting is still not correct even when you manage to get
    nesting to happen (and it's easy to end up with non-nested lists
    without meaning to). What I *think* is happening here is that the
    examples cited above are on WordPress and it has an HTML
    cleaner-upper that is fixing Google's broken HTML.

    So, I'm still disappointed, but I am wondering if we can work out
    some way to support Google Docs as an editor for
    [ICE](http://ice.usq.edu.au/)by inserting a cleaner-upper somewhere
    in the toolchain. Google docs has spectacularly good collaboration
    support. But I think we'd be wanting APP support before we tried
    that. Maybe it's time to look in to the Google Docs APIs...

</div>

</div>
