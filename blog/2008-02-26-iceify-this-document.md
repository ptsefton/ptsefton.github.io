---
Author: ptsefton
Comments: true
Date: 2008-02-26 06:05:21+00:00
Slug: iceify-this-document

Title: ICEify this document!
Wordpress_id: 91
---

<div>

<div class="page-toc">

</div>

<div>

I have been working on some proposals to get us a some interesting
projects (with attendant money) for the Learning Futures Institute,
where I work. To do this I have to work with other people's templates,
which is fine, but it could be so much better if I could use some of the
tools we've developed on[the ICE project](http://ice.usq.edu.au/).

What happens is, when I open up one of these templates that people
supply, I still have my ICE toolbar sitting there ([see the
demo](http://ice.usq.edu.au/presentations/demos/html_from_ooo.htm) if
you don't know what I mean). Out of habit, I reach for the shortcut keys
for ICE, or hit the toolbar buttons if my hand happens to be on the
mouse. So when I want to whack in a bullet list it's Esc 8 or Esc \*. I
really like the ICE toolbar interface. Really. I use it all the time.

( I first thought about building it in about 1996, only took 11 years
for me to get around to suggesting it to my team last year. Why take so
long? Afraid of macros, once you write them then you are stuck with
maintaining them. But it was worth it.)

I'm using an Ubuntu Linux machine at the moment which means the word
processor is OpenOffice.org Writer, a reasonable if uninspiring word
processor but the same thing applies on the Mac or Windows using
Microsoft Word.

Now the ICE toolbar is pretty smart, so even though the document is not
an ICE document, it goes ahead and creates a style for me, in this case
`li1b` for List Item level 1, with a bullet. If the template designer
has bothered with styles for list bullets they might be called
`List Bullet 1`, but then again they might not. There are no standards
for this stuff.

What I'm thinking is that most of these funding bodies (or even many
journals) don't really care about the styles in their documents, so long
as they look right, so it would be great to be able to get the ICE
toolbar to adapt a document to the ICE styles automatically, to ICEify
it as it were.

In a lot of cases this would involve renaming `Default` or `Normal` to
`p,` and `Heading 1` to either `h1` or `h1n` depending on whether it is
numbered or not (I'm going to write on the subject of heading numbering
soon for the ICE FAQ if you're interested in why we did it the way we
did). Actually a better way to do it would be to create new styles that
are based on the existing ones and then search and replace from the old
to the new.

I'm not sure how interactive the process would need to be, but the idea
would be to try to disturb the supplied template as little as possible,
while making it possible to take advantage of the ICE toolbar, not to
mention automated conversion to HTML and PDF and even possibly the
ability to embed slides, if you're going to have to present your
proposal. You could even post it to a blog and have it come out in
perfect HTML, although I'm not too sure how many funding bodies would
appreciate that. (And if one of the proposals I'm working on comes off
you will be able to submit a completed application to a repository, for
long term preservation).

I covered the [manual steps involved in ICEifying a
document](http://ptsefton.com/blog/2007/05/15/etd_paper/) last year, I
might have to have a look-see at how hard it would be to write a simple
ICEifier.

Another trick might be for it to put the styles back the way they were
when you're done.

</div>

</div>
