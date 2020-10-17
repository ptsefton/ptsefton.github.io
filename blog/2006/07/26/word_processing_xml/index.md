---
Title: "Comparing XML word processing formats"
Slug: word_processing_xml
Date: 2006-07-26

---
<div>

Rick Jelliffe has [another informative
post](http://www.oreillynet.com/xml/blog/2006/07/comparing_xml_office_document_1.html)on
OpenDocument format vs Office Open XML.

I have left a comment there questioning some of the detail, but I like
the conclusion:

> Which is why I think it is better to consider the bottom line: can all
> the information be round-tripped, even if with effort? That is the
> information that anyone with archiving and data conversion
> requirements should be considering more than initial eye-rolling,
> however understandable, I think
>
> <http://www.oreillynet.com/xml/blog/2006/07/comparing_xml_office_document_1.html>

Rick is saying that  the important thing is interoperability, both with
current tools and with the future.

To which I add, if  you care about document processing now and into the
future and you're working with word processing documents **use styles**
to mark the bits of your document that have structural and semantic
significance. If you use styles then the task of converting from one
format to another becomes much easier; you can forget all the discussion
about wrapper elements and work from the style names (even if they
happen to be a bit obfuscated by the file format as in ODF).

I have [noted
before](http://ptsefton.com/blog/2005/12/12/ice:_interchange_comes_easily)
that we have already achieved some of this interoperability with the ICE
template, and an alternative implementation by Ian Barnes.

</div>
