---
Title: "Rick Jelliffe looks at Open Office XML formats on Wikipedia"
Slug: ooxml
Date: 2007-01-23

---
<div>

I thought about calling this post <span
class="spCh spCh0x201c">“</span>Rick Jelliffe sells out<span
class="spCh spCh0x201d">”</span>, but then I would have had to explain
that I was joking. Joking. Got it?

In [this
post](http://www.oreillynet.com/xml/blog/2007/01/an_interesting_offer.html),
Rick considers whether to take some money to fix up the Wikipedia entry
on Microsoft's Open Office XML format.

Me, I think that the arguments about standards are entertaining, but I'm
interested in a broader point of view. We need working implementations
of the standards too. Take this statement from [the page comparing the
formats](http://www.oreillynet.com/xml/blog/2007/01/an_interesting_offer.html):

> OpenDocument is similar to XHTML, while MS XML is not. OpenDocument
> uses mixed content and marks styles in a similar way. This makes it
> easier to transform data accurately between OpenDocument and XHTML,
> and also simplifies the reuse of existing skills.

Even at the standards level parts of this paragraph are dubious, but
when you look at the implementations they're definitely suss.
OpenDocument has a very different list model and quite a different table
model to XHTML. And what matters to me and my colleagues is how the
major application implementing ODF behaves. With tables, the behaviour
is appalling. OpenOffice.org implements some kinds of cell-merges in
tables using sub-tables. This means that to correctly transform from ODF
to XHTML the transforming application has to correctly understand every
detail of the table rending, so it can work out which cells are supposed
to line up with each other. The bug list for OOo seems to contain
multiple overlapping issues around this area, but it's not at all clear
to outsiders when the thing will be fixed. It's the application that is
at fault, but what good is a Standard if there is no working
implementation?

The ICE team have a list of dos and don'ts that give you 'safe' tables
across Word and OpenOffice.org. Sad, but necessary. They're not in the
[Tips and tricks
document](http://ice.usq.edu.au/ice-guide/study-modules/module05.htm),
yet.

I've [covered lists
here](http://ptsefton.com/blog/2006/10/20/list_formatting_in_ooo_writer),
all too often, as regular readers will know. For those of you have not
been hanging on every word, the hierarchical model in ODF does not allow
the kind of free form mixing and matching of nested content that XHTML
allows. If anything the flat OOXML approach is closer to XHTML, although
neither of them are really anything like it.

For us its not about the standards, it's about practicalities of
implementing stuff on top of them.

What I expect to happen is that Word will eventually do an 90% job of
reading and writing ODF and OpenOffice.org will do an 86.5% job of
reading and writing OOXML, and users who stick to the 60% of the overlap
that maps to XHTML sensibly, and use styles, will prosper. Meanwhile
people like Rick working to make the Standards as clear as possible and
to skewer some of the FUD are my heroes. The comments look interesting.

[I wrote and posted this at the airport in LA, been up for 26+ hours
with only a few minutes of shut-eye, trying to stay awake for another 6
or so hours and then magically synchronize to San Antonio time, sans
jetlag in time for the [OR07](http://openrepositories.org/) conference
tomorrow.]

</div>
