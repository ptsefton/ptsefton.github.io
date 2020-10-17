---
Author: ptsefton
Comments: true
Date: 2008-02-21 01:00:22+00:00
Slug: xhtml-challenge-mozilla-seamonkey-composer-is-not-suitable-for-writing-academic-papers

Title: 'XHTML Challenge: Mozilla Seamonkey Composer is not suitable for writing academic
  papers'
Wordpress_id: 87
---

<div>

<div class="page-toc">

</div>

<div>

I have written a few posts about [trying to write HTML, peferably XHTML,
with various word processing
tools](http://del.icio.us/ptsefton/ptsefton+xhtmlchallenge). Today was
reminded of the Mozilla Seamonkey project by this post about [open
source alternatives to proprietary software
packages](http://whdb.com/2008/the-top-50-proprietary-programs-that-drive-you-crazy-and-their-open-source-alternatives/).
(Some things on the list are sensible, but suggesting that
'[DocBook](http://docbook.org/)' might be a replacement for FrameMaker
is a stretch. DocBook aint a software package it's a lifestyle.)

Remember Netscape Navigator, which came with email and an editor and all
bundled together? That's what Seamonkey is. I grabbed a copy of
Seamonkey for the Ubuntu Linux machine I'm using at the moment and tried
out the Composer application.

How would one go writing an academic paper with it?

Some technical stuff follows, but the conclusion is in the title of this
post.

The first thing I looked at is how I might mark up a quote. There's no
obvious way to get a blockquote element. If you hit the indent button,
then it does produces code like this:

> `<h1>Here's a heading</h1>And the first paragraph.<br><br><div style="margin-left: 40px;">Now this is a quote<br>More quote.<br></div>More text.<br>`

This is garbage. There are no paragraphs, only line breaks `<br>` and
instead of a blockquote element we have the semantically null
`margin-left: 40px; `what I want from my editor is what the [ICE
toolbar](http://ice.usq.edu.au/instructions/templates/using_the_ice_toolbar.htm)
for OpenOffice.org and Microsoft Word delivers, if I indent (demote) an
ordinary paragraph it gives me a quote, hit the same button when I'm on
a heading and it will give me a lower-level heading (ie h1 -\> h2).

And the list editing is like most other HTML editors I have looked at
recently, unintuitive and wrong.

Take this for example. The lists are not nested correctly (the `ol`
should be inside the first `li`). And what's that br doing at the end of
my second bullet item?

> `<ul`\>` <li>Bullet</li>`` <ol>    <li>Numbered</li>    <li>Numbered</li> </ol>    <li>Bullet<br>    </li></ul>`

This editor doesn't think hard enough about what you might mean. It is
easy to produce all sorts of terrible markup. IIf you click the toolbar
buttons in the wrong order then you can produce very wrong code. Why
should it be different if I change to numbered list format then indent
(which is what I did in the above example), rather than indent then
change to numbered list format (below)?

> `<ul> ... <li>Bullet</li></ul><ol style="margin-left: 40px;"> <li>Numbered</li> <li>Numbered</li></ol><ul> <li>Bullet<br></li></ul>`

What I meant was this, but I have yet to see an HTML editor that can do
this properly (note, I don't look at HTML editors much, I tend to
specialize in complaining about word processors.):

> `<ul> ... <li>Bullet   <ol>     <li>Numbered</li>     <li>Numbered</li>    </ol> </li> <li>Bullet</li></ul>`

So, the bottom line is that even thought Mozilla Seamonkey composer
comes with a button to fire the document off to a validation service it
would be useless for writing a paper, even before we get to the issue of
how you might make a PDF version, or deal with your bibliography.

</div>

</div>
