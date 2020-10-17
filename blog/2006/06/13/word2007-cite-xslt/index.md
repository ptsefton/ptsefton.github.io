---
Title: "Word 2007 bibliographies and XSLT"
Slug: word2007-cite-xslt
Date: 2006-06-13

---
<div>

More archeology on Word 2007 from Bruce D'Arcus [shows that it uses
XSLT](http://netapps.muohio.edu/blogs/darcusb/darcusb/archives/2006/06/09/citation-formatting-in-word-2007)
to format bibliographies.

This is good news. It's not Bruce's [Citation Style
Language](http://xbiblio.sourceforge.net/csl/), but it is an open
standard.

Bruce has some concerns about the complexity and size of the XSLT
involved, but I don't think that matters so much -what matters is that
XSLT is involved. All that's required is an CSL to XSLT compiler. Feed
CSL in one end and get a Word 2007 compatible stylesheet out the other.
This could be done with a stand alone tool.

OK, that's not completely trivial and it is more than one afternoon's
work, but it's doable, I'm sure. The trickiest bit is sorting the
bibliography, and it appears that there are separate stylesheets Word to
do this.

Bruce suggests porting CSL to XSLT – but I don't think that's necessary.
I do agree that CSL offers significant advantages, though.

> But what this does suggest to me is that it ought to be easy to swap
> in citeproc, or for Microsoft to port it to XSLT 1.0 if they like. The
> benefits to using a domain language like CSL for styling are
> significant. It becomes easy for users to create new styles, and for
> developers to create tools for it.

Last year I
[suggested](http://bibliographic.openoffice.org/servlets/ReadMsg?list=dev&msgId=2239530)
a similar approach to Microsoft's on  the OpenOffice.org bibliography
dev list. I thought that getting citation and bibliographic support in
OpenOffice.org might be easier if the scope were smaller, and I
suggested that a general mechanism might be the way to go – a generic
XSLT process that could run across any document and change it.

> .. maybe it would be possible to shipXSLT with an OD document. So
> instead of including a CSL spec, onecould ship an XSLT derived from a
> CSL spec that would operate on thecontent. So OOo would not have to
> know about CSL, just have amechanism for running an XSLT stylesheet
> across the content of adocument to produce a new version. Obviously
> there would need to besome conventions for feeding in bibliographic
> data for it to work uponand OD should still know about citations and
> bibliographies, just notthe styling language.
>
> XSLT plugins would be a mechanism that might have other uses. In
> ourpublishing system, for example I'd love to be able to ship an
> XSLTstylesheet that would normalize a document by removing
> unwantedformatting and rationalizing lists.
>
> <http://bibliographic.openoffice.org/servlets/ReadMsg?list=dev&msgId=2239530>

Questions remain:

-   How do you 'register' a new stylesheet. Is there a GUI for this?

-   Where is a the developer documentation for making new stylesheets?

-   Will there be one or more central repositories of stylesheets?

And I'm still dubious about the value of having the bibliographic
software built into Word 2007; Microsoft's site clearly states that if
you load a file with citations in it into an earlier version of Word
they will be converted to plain text. This means that the feature will
not be usable in a real-world context for several years. People have to
collaborate with others, work from home and in internet cafes; we can't
mandate Word 2007 in all those places.

I would rather see an add-in that can work with not only Word 2007 but
earlier versions of Word, Macintosh versions of Word and other software
like OpenOffice.org.

I know that with the [ICE project](http://ice.usq.edu.au/) we can expect
to see users running version of Word going back to 2000, and maybe 97.
We don't need to turn those users away; but if we started relying on
features that are only in Word 2007, which as far as I know is
Windows-only then we would loose a lot of users, as we would if we
insisted on OpenOffice.org version 3 if and when it comes out.

</div>
