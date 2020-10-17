---
Title: "Publish Everywhere? Not from word processors..."
Slug: publish_everywhere
Date: 2006-09-23

---
<div>

Tim Bray reckons that you should be able to publish to the web, via
ATOM, from anywhere:

> Here’s the Atom dream: A “Publish” button on everything. On every word
> processor and email reader and web browser and cellphone and PDA and
> spreadsheet and photo-editor and digicam and outliner and sales-force
> tracker. Really, everywhere. If it doesn’t have a “Publish” button,
> it’s broken.
>
> <http://www.tbray.org/ongoing/When/200x/2006/09/14/Why-Atom>

Wouldn't that be nice.

But there's one ongoing problem, which has been a constant theme on this
blog. Word processors don't typically produce usable reliable good
quality HTML, let alone XHTML. Adding a button that says 'Publish' is
not going to change that.

Why? Because it is not possible to map everything you can do in your
word processor to HTML. The word processor that Sun sells and gives
away, for example, does a particularly awful job of producing HTML, and
does not come with a default template that helps **at all**. And to feed
stuff to a web site via Atom you **need HTML**.

For years word processors have had HTML export, and for years everyone
seems to have been happy to accept that HTML export is awful and always
will be. People just say “Word produces crappy HTML” and leave it at
that, like it's a law of nature.

But it doesn't have to be that way. By using styles and adding some
style-aware scripts to your word processor you can make word processors
more productive and produce good HTML at the same time. The creators of
these products could have encouraged people to use styles by shipping
great templates and making the HTML export work with them.

Instead Microsoft have buried styles and templates under more and more
layers of obfuscation and unhelpful automation.

OpenOffice.org Writer at least doesn't bury styles, the quirky interface
is easy enough to find. But sun doesn't ship a sensible default template
and its HTML export is really, really appalling. For example it doesn't
even re-size images, just dumps them out at full resolution and adds
height and width attributes to the `img` tag. And don't get me started
on lists. Not again.

Here's
[ one](http://ptsefton.com/blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)
of my previous rants on the subject.

[See
also](http://ptsefton.com/blog/2006/03/21/writely,__meet_the_ice_template)
what happens when  you try to feed OpenDocument Formatted documents to
the web via Writely.

To be able to publish to the web from your word processor you either
have to:

1.  Suss out which features export properly to HTML and stick to those.
     Plain paragraphs should work OK.

    Microsoft are actually documenting this for Word 2007 so you can
    produce simple HTML by sticking to a subset of Word's features and
    clicking the blog button. They don't seem to want to take this all
    the way and support styles. I asked, but no response.

    (You also need to avoid things that are broken – like row and
    columns spanning in tables in OOo Writer which  has a [long standing
    bug.](http://qa.openoffice.org/issues/show_bug.cgi?id=60238)Would
    any of you care to visit the OOo site and vote that bug up so it
    gets fixed? Tim can't get his publish everywhere button working
    properly without it.)

2.  Set up an environment with a template, some styles, custom export
    scripts etc etc.

    We've done that at USQ with the [ICE
    project](http://ice.usq.edu.au/). ICE doesn't do ATOM yet, but there
    is no reason that it couldn't, and no reason that its free code
    could not be turned into stand-alone plugins for OpenOffice.org and
    Word so they really can publish to the web.

As always I invite you to take a look at the way this works here on this
site. All my posts are produced using OpenOffice.org Writer (I now use
NeoOffice as well) with ICE.

</div>
