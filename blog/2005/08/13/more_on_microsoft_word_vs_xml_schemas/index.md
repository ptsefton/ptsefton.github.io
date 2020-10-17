---
Title: "More on Microsoft Word vs XML Schemas"
Slug: more_on_microsoft_word_vs_xml_schemas
Date: 2005-08-13

---
I have been puzzled for some time about the purpose of the validating
editor that is embedded in Microsoft Word 2003, the bizarre feature that
lets you mix schema-controlled XML content in amongst Word's own
structure. I may have been jetlagged when I wrote
[this](blog/2005/07/26/i'm_back):

> I'm not convinced. This looks like high-cost, fragile development to
> me, particularly with a new format coming. I think a better
> alternative is to use a 'microformat' approach, and embed information
> in something like a table, with a known structure, so that it can be
> found and processed. I have been doing this for years with educational
> content, using simple mechanisms like two-cell tables to mark-up
> content such as activities or readings. This is the approach we are
> taking in ICE.

What I was trying to say was that if you are going to use a word
processor why not use the built-in word processing features and layer
your semantics on top of them? Use the methods already provided for
expressing your own semantics. Method number one is styles. Method
number two is tables. This approach will work in versions of Word that
don't have XML export, and with forthcoming Word formats that have been
announced but not released and with other word processors that save in
XML such as OpenOffice.org Writer.

And this week, I found that [Bryan
Wilhite](http://www.kintespace.com/rasxlog/), has been probing Brian
Jones of Microsoft about how this XML support is supposed to work.

Here's part of Brian Jones'
[response](http://blogs.msdn.com/brian_jones/archive/2005/07/08/436973.aspx)
in the comments on his site:

> We designed the XML support so that you could leverage both WordML and
> your XML together. If there are features such as formatting, lists,
> and tables that Word already supports, then you don't need to mark
> that up. Instead you can just take the subset of your schema that
> isn't already represented by Word functionality, and only mark up with
> that.
>
> Then you can just transform on the way out into your schema. At one
> point I had an example of doing this for DocBook, but I can't seem to
> find it anywhere. I'll post it if I ever dig it up.

I think that if you're looking at embedding "the subset of your schema
that isn't already represented by Word functionality" into Word then you
should probably look for another authoring package. How are users going
to fare trying to use obscure markup features of Word to do stuff Word
doesn't do natively (assuming they have a version of Word that can even
undestand this stuff). And who's going to pay for the programming you
have to do to write your own interface.

And this hand-waving 'just transform on the way out' is NOT helpful.
Let's be clear about this, features such as formatting, lists and tables
are going to be found in any document schema you name, but trivialising
the conversion process with a glib 'then you can just transform on the
way out into your schema' is very misleading. Formatting, list and table
models are NOT built on some kind of universal grammar that allows
painless transformation from one to the other.

I'd like to see Brian Jones' mislaid DocBook converter. I can't imagine
such a thing working without at least a good set of styles, and in the
case of something as big and complex as DocBook, maybe some fairly heavy
duty macros as well.

My favorite conversion challenge is lists. How might we map from Word to
XHTML lists?

Lists in Word have their own, complex representation in WordML (I
thought it was called WordProcessingML), but there is no way that you
could reliably map one to another without:

-   Creating some kind of guideline or template to control the way lists
    are expressed in Word.

<!-- -->

-   Writing complex software to map the way lists work in WordML to the
    way they work in XHTML.

I did a quick experiment to see what lists look like in WordML. Took a
bit longer than I had planned, 'cos I was unable to find 'Save XML' in
Word 2004 on the Mac, and I had to go to Windows, but the result is
nothing like XHTML, I can assure you. The good news, though, is that if
you have defined styles for your formatting that do map to XHTML then
you can write software to do the mapping from the styles without
worrying about the way WordML handles lists at all, and it will only be
complex if you try to do it in XSLT. [Use
styles](blog/2005/03/02/use_styles).

PS The way WordML handles lists is much more rational than the way it's
done in OpenOffice. In Word a paragraph is the main container and
properties like lists are referenced through the charmingly named w:pPr
element. That is lists are implied structures.

(If you want to talk about w:pPr you can try [John R. Durant's
weblog](http://blogs.msdn.com/johnrdurant/archive/2004/02/18/75595.aspx))

And did I mention [Use styles](blog/2005/03/02/use_styles)?
