---
Title: "Cutting off your word processor's tail"
Slug: cutting_off_your_word_processor's_tail
Date: 2005-11-10

---
<div>

Jon Udell makes a [return to the subject of word
processors](http://weblog.infoworld.com/udell/2005/11/10.html#a1337).

He wonders about distilling, sorry reducing, the functionality of a word
processor:

> Suppose we boiled down a large sample of office documents to their
> constituent elements and ranked them by frequency. We'd find
> paragraphs, lists, tables, images, links, basic styling, and then a
> long diminishing tail of rarely used features.
>
> <http://weblog.infoworld.com/udell/2005/11/10.html#a1337>

Yes! (Sounds like something culinary – a *reduction of Microsoft Word*)

I discussed this a lot, last year when I kicked off the [WP Interop
project](http://del.icio.us/ptsefton/ptsefton+wpinterop). While Jon's
dream of a well-oiled word processor without a long tail is appealing,
it's something that will take significant effort, [according to Tim
Bray](http://www.tbray.org/ongoing/When/200x/2005/11/09/Lightweight-Authoring):

> Well, yeah, but... authoring software is hard. I’ve used a lot of
> different programs over the years, and written some myself, and I’ve
> never seen software, designed for use by human authors, that has good
> usability and isn’t a great big honking monster. And usually, they’re
> not only big, but they take years and years to get working properly.
> So I really hope Jon’s right, but I’m not holding my breath.

> <http://www.tbray.org/ongoing/When/200x/2005/11/09/Lightweight-Authoring>

So Tim Bray's not holding his breath waiting. Just as well because then
he wouldn't be able to be a cheerleader for
[openoffice.org](http://openoffice.org/).

I'm not holding my breath either. I decided to build Jon Udell's
'reduction of word processor', not on top of 'web 2.0' or 'the Internet'
but on top of Word and OpenOffice.org.

What?

Well, the wait could be a long one, and I can't write an authoring
application. But what I can do, and have done for ten years or so is
design good, simple templates that do Udell's 'paragraphs, lists,
tables, images, links, basic styling'. We're well on the way to having
this working in the ICE project, where the same set of simple styles can
be used in Microsoft Word and OpenOffice.org Writer reasonably
interchangeably to produce, usable, reusable documents efficiently. ICE
documents can be automatically published as XHTML (via OpenOffice.org
and some XSLT and Python) or PDF (via OpenOffice.org) and [maybe to
DocBook](http://www.bloglines.com/blog/barnes?id=17) via work done by
Ian Barnes for long term archiving and more publishing options.

Even in the absence of a good lightweight authoring tool we need to do
something to promote efficiency and sustainability and reusability. And
the people who work in this way (basically the ones who [use
styles)](http://ptsefton.com/blog/2005/03/02/use_styles%20) will be
ready for the new lightweight world, whereas some of the less considered
word processor users will have a hard time migrating to a new tool.

The application Jon Udell wishes for could well be based on a slice of
XHTML. There was a bit of [talk of such an
application](http://ptsefton.com/blog/2004/08/09/futureoffice)last year,
but it died down, and I have heard of no real progress, except, of
course my dogged pursuit of the [word processor
interoperability](http://del.icio.us/ptsefton/ptsefton+wpinterop)
stylesheets.

The [ICE project](http://ice.usq.edu.au/)has an OpenOffice.org v2
template, which you can have a[look
at](http://ice.usq.edu.au/file/ice/releases/0.2/beta/templates/ice.ott)
in the downloads section for our 0.2 release. A word template is coming
in the next couple of weeks – email me if you're impatient to try one.
To convert documents to HTML you need to install ICE because the export
in OpenOffice.org (and Word) is so woeful as [discussed
here](http://ptsefton.com/blog/2005/10/31) last week. There are ICE
binaries available, but unless you are particularly adventurous maybe
wait a bit until we get some more instructions published.

****

</div>
