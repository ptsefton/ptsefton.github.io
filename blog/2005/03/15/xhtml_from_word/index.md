---
Title: "XHTML from Word"
Slug: xhtml_from_word
Date: 2005-03-15

---
I have been prompted by Bryan Wilhite to respond to some questions he
posed in [this blog
entry](http://www.kintespace.com/rasxlog/index.php?p=35) about Word to
XHTML export. I have to admit that I don't understand all of what Bryan
covers in his article on [XHTML Schemas in Word 2003
Documents](http://songhaysystem.com/document.php?cmd=getDoc&get=24). But
here's what I think.

I am very dubious about the usefulness of Word 2003's XML support in
both the 'native' XML export and the use of schemas inside Word, but for
a much broader, and infinitely better informed critique of XML in MS
Office than mine, see Simon St. Laurent's [Holes in Microsoft Office
XML](http://www.onlamp.com/pub/wlg/6649).

Word's XML export using WordprocessingML is less useful in the context
in which I work than the 'export to HTML and transform to XML' approach
that I covered in my [Word to XML
article](http://www.xml.com/pub/a/2004/12/08/word-to-xml.html).

The WordprocessingML schema is very complex, with its own table model
etc. So for most purposes something closer to HTML is a better bet. My
assumption is that the Word team originally wrote the HTML export from
Word 2000 as a true XML export but were forced to dumb it down for some
strategic reason while they worked on a truly proprietary, much less
useful solution.

I admit to not having explored Word's XML structured editing and schema
support very much but I have looked into it a couple of times and was
not moved to take it further (Bryan's report of the problems involved
helped to scare me off). I would expect that true structured editing is
likely to be a nightmare because of all the other features of Word
getting in the way. Structured editing is hard enough for most authors
using an XML editor that doesn't have Word's extensive legacy, and the
possibility of confusing matters with structured and non structured
parts intermingling.

I'm sure that there are people using these schema-driven editing
features, but I'm equally sure that it's costing them dearly in
development and support time.

But that said, if there was an example of a mature XHTML editing
environment built on Word 2003 I'd love to give it a try. I can't find
one, though.

So, for broad-scale use I think the answer is: [use
styles](http://ptsefton.com/blog/2005/03/02/use_styles), and plug into a
content management solution that can generate web documents from your
styled documents.

As Simon puts it in [Holes in Microsoft Office
XML](http://www.onlamp.com/pub/wlg/6649):

> Word's XML functionality isn't integrated with its existing style
> functionality.
>
> Users, at least some users, understand the style drop-down and
> applying styles. The XML task pane is new and additional. Creating XML
> documents in Word that look like you want them to look can require
> using both styles and XML. My advice to people who want to use Word to
> create XML: forget about the XML tools, unless you need lots of
> precise nesting and attributes. Use styles instead, and then extract
> the information from WordprocessingML. (Yes, I know that's painful.)

To which I would add skip the WordprocessingML and use the HTML export
(transformed to XML) - less painful, but not pain-free. And I have had
pretty good results with nesting in XHTML using a carefully designed
style-set. More on that soon.

And as for Bryan's questions:

> Would he welcome the ability to automatically markup Word documents
> with XHTML using the robust automation features of Office System 2003
> and/or Visual Studio .NET?

Well maybe, but I don't really understand how you would do this and make
it usable. I've got a pretty workable solution using styles at the
moment. I don't think most of the authors I work with would take well to
further complexity. (I assume the authors would not be expected to use
Visual Studio).

> Would he find routing nodes of XHTML through a Web service from Word
> useful?

I don't understand the use-case for this.

> What about saving bits of a Word document as XHTML by selecting text
> and sending it marked up to the Clipboard?

That would be useful, but again, it would be *most* useful if it was
style driven, and didn't require the author to deal with XML Word's
bastard environment. I guess I can see how that could be done using
styles, feeding the selection to Word (or OpenOffice.org), then running
it through a process to save as XML and map styles to XHTML.
