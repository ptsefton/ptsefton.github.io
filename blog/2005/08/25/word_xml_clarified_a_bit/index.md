---
Title: "Word XML clarified a bit"
Slug: word_xml_clarified_a_bit
Date: 2005-08-25

---
Brian Jones of Microsoft has [continued our conversation on Word to
XML](http://blogs.msdn.com/brian_jones/archive/2005/07/08/436973.aspx#452483)
in the comments on his blog. I am very pleased to be having this
discussion, and I'm pleased that Brian is willing to follow-up on some
of the points I raised. I have pulled a few quotes from his response.

> The first point is that our main scenarios weren't about turning Word
> into an XML editor.

That's reassuring, because that would have been a disaster, but I'm not
sure that it's clear to most people just what the Word/XML story is.

And this:

> There is a huge market that exists today for custom Office solutions.
> People customize the Office applications in all kinds of ways to try
> to get more out of their documents. By adding the support for custom
> defined schemas, we made it much easier to build semi-structured
> solutions on top of Word. Rather than rely on hacks with styles or
> bookmarks, folks could create a simple schema and add some XML tags
> into their existing document solutions.

There certainly is a big market for custom Office solutions. Personally,
I wonder how much the worst end of this kind of development costs
business. It's easy to build great apps, but also pretty easy to waste a
lot of time and produce ongoing maintenance headaches that last for
years. MS Office based developments is one of the biggest time-sinks
I've ever found, with some very serious deployment issues. Distributing
and maintaining templates is a nightmare! But in fairness OpenOffice.org
is much worse than MS Office in the template department.

And I don't think of styles as hacks - like classes in HTML I think they
are a good, accessible way to add domain specific semantics on top of a
standard publishing system. Flexible, well implemented, easy to deal
with for both users and programmers. What's not to like? [use
styles](http://ptsefton.com/blog/2005/03/02/use_styles), that's what I
say. If Microsoft wanted to they could ship Word with a standard
stylesheet that mapped to XHTML with no problem and add an XHTML export,
and offer advice about how to extend the stylesheet to make a 'custom
Office Solution'. I'd be happy to help with that.

And finally, Brian offers to follow up on a couple my issues:

> I think the points you raise are great, and there are a couple of
> things I'll try to follow-up on. I'll try to see if we have any good
> XSLTs for mapping our lists into XHTML lists. I'll also try to get a
> more complete description of the goals behind our XML support in
> Office.

Firstly, I'm really interested in list mapping; my thoughts are that you
need to add styles to the picture to be able to do reliable WordML to
XHTML, but I could be wrong. I offer [my work on list
styles](http://trac.officecontent.net/wiki/WpInteropStyles) and the code
we developed for OpenOffice.org writer to XTHML lists (I'll announce an
ICE release soon).

Secondly, I think a more complete description of the goals behind XML
support in Office, posted as publicly as possible would be a great step
forward for the increasingly communicative Microsoft we're seeing
lately. It would also be good to have a map of which versions of Word
(and on which platforms) will support which bits of the XML picture. And
how will things change when the new Word 12 XML format is out? Will the
mix-n-match with arbitrary XML still work? What will happen if you load
it in Word 2000? There are big questions here...

Finally, a summary of how we are going to approach word processing to
XHTML, via XML in the [ICE
project](http://www.usq.edu.au/dec/staff/ice.htm).

-   We're starting with OpenOffice.org Writer and, which has its quirks,
    some serious limitations and its challenges but which is *much*
    easier to deal with than Word in the context in which we're using
    it.

<!-- -->

-   I am continuing work on my (still) favourite way of getting XML in
    and out of Word, which is via the Save as Web functionality
    available in all versions since 2000; I will soon release a .NET
    assembly that can be used to do it from the command line or embedded
    in another application, and we will look at adding the [Python
    code](http://www.xml.com/pub/a/2004/12/08/word-to-xml.html) I wrote
    for xml.com to ICE.

<!-- -->

-   I am sure we'll add ICE support for the new MS Office XML formats
    when they are out. I hope it's not too hard to produce web-ready
    renders of embedded objects reliably, though. Last time I checked
    you were not meant to run Word on a server, so how will we do XML to
    HTML conversion and get all the images and equations and so on to
    look right?

