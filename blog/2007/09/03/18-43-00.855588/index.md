---
Title: "ICE is atomized!"
Slug: 18-43-00.855588
Date: 2007-09-03

---
<div>

[View this page as PDF](/blog/2007/09/03/18-43-00.855588/100.pdf)

ICE is getting increasingly service-oriented. At the moment it's a great
big application with a lot of dependencies, but we're going to make all
the bits usable so other services can use them.

One major step in this direction is the addition of an Atom Publushing
Protocol (APP) client. ICE users (on the bleeding edge only for now) can
now compose posts in the comfortable ICE template and post to ATOM-aware
blogs.

I've just [posted over at blogspot](http://aanro-repo.blogspot.com/) for
the new AANRO project we're doing at USQ. I wrote the post in an ICE doc
and hit the publish button to send it. It just works. (OK, that's not
pure ATOM, but we do standard APP as well).

What does this mean?

Well as far as I'm aware this is the first ATOM client for a word
processor that works with styles, so it can produce valid HTML. I have
yet to write up my experiences with the blog functionality in Word 2007,
but it's pretty much like Word itself, and the [Sun
weblog](http://ptsefton.com/blog/2006/10/20/sun-weblog) plugin is
subject to all the limitations of OpenOffice.org, which has particularly
awful HTML export. (See my [ongoing invesigations into HTML generation
from out-of-the-box word
processors](http://del.icio.us/ptsefton/xhtmlchallenge)).

Tim Bray [has this dream that everything should have a 'publish this'
button on it](http://www.tbray.org/ongoing/When/200x/2007/03/22/Atom):

> Once again, here<span class="spCh spChx2019">’</span>s the dream:
> Everything should have a <span
> class="spCh spChx201c">“</span>Publish<span
> class="spCh spChx201d">”</span> button. Your browser, your
> spreadsheet, your word processor, your feed reader, your camera, your
> phone, your email client, your calendar client; I mean everything. APP
> isn<span class="spCh spChx2019">’</span>t the whole solution, but
> it<span class="spCh spChx2019">’</span>s a necessary piece of the
> platform you need to build such a future on.

And once again I point out that if you just hook up the button to a
standard word processor you're going to get junk HTML. To get really
good HTML from a word processor, ICE is one solution. We're well on the
way to realizing Tim's dream, by doing what Microsoft and Sun and Google
should have done, and providing a usable word processing template that
you can adapt to your own look, but which comes with software to create
proper web pages. Have a [look at the
demo](http://ice.usq.edu.au/media/videos/quick_ice_demo.swf) which shows
a silent Daniel de Byl creating a document in ICE, using OpenOffice.org,
using the ICE toolbar to apply styles by clicking dead simple buttons,
then rendering his document to HTML and PDF. Works **exactly** the same
with Word and documents are interchangeable between Word and Writer.

Next step for ICE is to build an extension for OpenOffice.org Writer
that contains the new APP button, and a 'Save as HTML' that works using
ICE styles. Once that's done we'll work out a way to call that code from
Word, with Writer acting as a server, either on your own machine or
remotely. (If anyone knows how to package Python applications for Writer
can you [drop me a line](mailto:pt@ptsefton.com)?)

I'm going to have to make a choice now whether to stick with
[Leonardo](http://jtauber.com/leonardo/) for this blog, as it looks like
James Tauber is working towards making Leonardo talk APP. Or should I
use ICE, running the new server-based version and teaching it how to
blog?

As for the APP work, so far we don't handle images, or post the PDF or
slideshow versions of documents, but that's next <span
class="spCh spChx2013">–</span> we should be able to include this in the
ICE release some time in the next few weeks.

</div>
