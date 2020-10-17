---
Title: "(X)HTML as a universal document format"
Slug: xhtmlasuniveraldocumentformat
Date: 2004-06-18

---
This web site was not conceived as a fanzine for Tim Bray and Jon Udell,
but they do insist on saying such clever things. What's a boy to do?
I'll keep linking to them. The really fun part of this post is that Tim
Bray, recent Sun recruit, appears to be sort-of endorsing Microsoft's
Office suite, although he doesn't know it. How could this be? Read on…

Bray and Udell have been discussing Office document formats [with the
latest from Tim
Bray](http://www.tbray.org/ongoing/When/200x/2004/06/17/CustomSchemas)
proposing that XHTML is a pretty good general purpose document format. I
have been working in this mode for years, since before XHTML existed, in
several generations of publishing systems, starting with the one I
helped develop at TAFE New South Wales (a big state-wide vocational
education institution), followed by [Standards
Australia](http://www.standards.com.au), and more recently at NextEd. In
all of these systems the key has been to develop a broadly useful word
processing template, with similar coverage to HTML, and to use it for
more than one document-type, rather than building a complex, expensive,
vertically integrated schema for each family of documents.

I learnt my lesson from the experience of trying to implement a
publishing system for the TAFE Gazette using Microsoft's now long buried
SGML add-on for Word. It was engaging, ludicrous and lots of fun to
develop but it went nowhere. It soon became apparent to me that the
simple word processing templates developed by the technical writing team
in which I was working were much more sensible. And we could use then
for technical bulletins, user guides, newsletters, as well as
courseware. Using various combinations of Word Basic, Perl, and free
stuff from [James Clark](http://jclark.com/) and [David
Megginson](http://www.megginson.com/Background/) and a thing called a
'[Rainbow](http://xml.coverpages.org/publicSW.html#rainbow) Maker'
(thanks!) we managed to create web pages too.

(I remember very fondly the gentlemen from the hospitality school, who
had great course books for cookery, which we put on line using humble
word templates and very expensive SGML publishing software obtained on
trial. You just had to get them before lunch, when they could still
remember where they had stashed their floppy disks. After lunch they
wanted to talk about automated generation of learning materials from a
database, based on user profiling. "I'm a Lebanese Australian woman, I
want to learn Kosher Japanese cooking, and by the way I'm visually
impaired and allergic to fish". Righto, the system would say, and whip
you up a personalised programme.)

At Standards we built a simple word processing template which on the
evidence of the web site is still used to create the monthly magazine,
the news releases *and* the
[standards](http://committees.standards.com.au/) themselves. It has
styles for a few levels of heading, some special legal-ish numbering,
and not much else, but it works well enough for publishing the roster of
Australian Standards, with a few exceptions.

In my current gig, we do similar tricks with a Word template that we
offer to courseware authors, and it works in OpenOffice.org too. This
system is great for courseware with distributed authorship, low training
budgets, and low expectations for print delivery.

Last year, frustrated with Word's continuing inability to manage
multi-part documents, we developed a solution using XHTML as the schema,
and Adobe FrameMaker as the editor and PDF renderer. It was a reasonably
cheap project to implement, compared to a full-on custom schema, and
carried on the tradition of working with generic schemata, and using off
the shelf tools with comprehensible interface for rendering to print,
rather than expensive options such as developing XSL Formatting Objects
stylesheets. [Allette systems](http://www.allette.com.au) assisted as
consultants and trainers.

However, for your average office document, Microsoft Word is in my
opinion closer to Tim Bray's vision than the sun-sponsored
OpenOffice.org. Why? In a rare stroke of (near) genius, Microsoft Word
2000 and upwards (is that version 8?) offers a 'save as html' option
which is nearly but not quite XML but is also a complete Word document.
It's a [few simple transforms, described in this
PDF](http://www.planetmarkup.com/xmlarena/xap/Thursday/WordtoXML.pdf%0A)
to turn the office html format into XML. It would be less than a hundred
lines of script in Perl or Python. Once you have it in XML, you can take
it to XHTML, and use the web ready image renditions that Word has also
generated for you. Or, you can change your original document or generate
a new one and round-trip the XML back to that weird Microsoft format. As
far as I'm concerned this is more useful than WordML, and more practical
that custom XML schemas. I can get good web pages out of it, and make
changes to, or create, documents. If my Word template maps to XHTML then
I have everything I need for most publishing systems. As Tim Bray [puts
it](http://www.tbray.org/ongoing/When/200x/2004/06/17/CustomSchemas#p-16):

> No, I’m not saying that everyone should use XHTML or the
> OpenOffice.org formats for every document in the world. But I do think
> that the cost of rolling your own is a lot higher than you think, and
> you should really try to avoid doing that if you possibly can.

In summary, and in the grand tradition of Usenet. Me too!
