---
Title: "Missed opportunities in opening up Microsoft Word"
Slug: missed_opportunities_in_opening_up_microsoft_word
Date: 2006-05-15

---
<div>

Rick Jelliffe
[writes](http://www.oreillynet.com/xml/blog/2006/05/good_technical_blogs_at_micros.html)
of his ongoing frustration with Microsoft Word's lack of openness (this
is not a negative post from Rick, though):

> I welcome both [OpenDocument format and Mirosoft OpenXML] but have a
> big eyeroll thinking of the **twenty years of missed opportunities**
> which Microsoft has cheated its users out of by not providing an XML
> interface until recently: I remember trying out their appalling SGML
> Author for Word more than a decade ago and wishing they just had a
> simple mini-SGML version of RTF instead, like the Rainbow DTD. I hope
> the “Open” in “Open XML” refers to a change of thinking in MicroSoft
> management in favour of agressive interoperability.)
>
> <http://www.oreillynet.com/xml/blog/2006/05/good_technical_blogs_at_micros.html>

A big eyeroll from me too. I too dealt with the terrible SGML Author
thing.

I'd like to go on about one particular missed opportunity in the history
of Word. There was the 'almost but not quite XML' nearly full-fidelity
round-trip export feature in Word 2000. I seem to remember that this
feature came after some mentions that Word 2000 was going to have XML
export; which in the end it didn't.

This round-trip Save as HTML... feature uses an unholy mishmash of HTML
and islands of XML which is deliberately broken in all sorts of weird
ways. But going on a lead from something Jon Udell wrote, I worked out
that you could transform it into 'real' well-formed XML to get something
very like the Rainbow format to which Rick alludes; a useful document
interchange format.

I gave the idea to the team from
[TeraText](http://www.xml.com/pub/a/2004/12/08/word-to-xml.html),
because I wanted to use it on the project we had running at Standards
Australia. They built it in to their Ace scripting language (now there's
another missed opportunity. That was by far the most complete and
comfortable XML / SGML programming language I have used until .NET and
C\# came along – you can still get yourself a [free (beer)
copy](http://www.teratext.com.au/get/page/directory/browser;)).

I wrote an article about this for
[xml.com](http://www.xml.com/pub/a/2004/12/08/word-to-xml.html),
complete with a little Python / XSLT script to do the transform. Problem
is, I wrote it at least four years too late. Now there's Word 2003's XML
format and the new OpenXML formats to look forward to, not to mention
using OpenDocument, via OpenOffice.org, which is what we do in the [ICE
application](http://ice.usq.edu.au/).

I think this was a missed opportunity for the XML publishing community –
I wish I'd been more vocal in promoting the idea beyond my own small
circle, because we could have had ourselves a lot more Word mashups a
lot sooner had the technique been better known and it might have broken
Word's formats open sooner.

I have always wondered what went on in Microsoft in 1999. The export
format they produced was *this* close to being XML. I have always
imagined that somewhere **in the lab it was well formed XML**, and the
poor old programmers were made to dumb it down. I like to think that
someone inside Microsoft was trying to make Word as open as possible and
it was up to us, as a community to find the crack they left for us to
crawl through.

Now I think it is the OpenDocument crowd who are largely responsible for
the new openness at Microsoft because they provided an alternative to
Microsoft's ubiquitous but largely closed and/or lame systems and forced
Microsoft to compete.

Anyway – If I had to work with Word right now I would either:

-   Use OpenOffice.org to convert documents via the ICE code.

-   use Word 2000's save as HTML and [transform it to
    XML](http://www.xml.com/pub/a/2004/12/08/word-to-xml.html).

And kids, don't forget to [use
styles](http://ptsefton.com/blog/2005/03/02/use_styles).

</div>
