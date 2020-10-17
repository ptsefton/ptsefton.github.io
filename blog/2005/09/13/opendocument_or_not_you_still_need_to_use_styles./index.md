---
Title: "OpenDocument or not you still need to Use Styles."
Slug: opendocument_or_not_you_still_need_to_use_styles.
Date: 2005-09-13

---
<div>

There is discussion going on about the State of Massachusetts in the USA
proposing to mandate the OpenDocument format for Government documents.

Simon Phipps of Sun has some useful links. He emphasizes that it is all
about the document format not about OpenOffice.org vs Microsoft Word:

> All these (and more, watch for it now I've mentioned it) want you to
> approach the discussion from the perspective this is Microsoft vs
> OpenOffice.org, Microsoft vs Sun, Microsoft vs Free Software - in
> other words, they want to frame the conversation as company
> competitive when it's nothing of the sort. Massachusetts are not
> mandating OpenOffice.org or any other specific product.

> <http://blogs.sun.com/roller/page/webmink?entry=a_study_in_framing>

There's also Microsoft's Brian Jones' who is [stunned by the
move](http://blogs.msdn.com/brian_jones/archive/2005/08/31/458879.aspx)
(but read the skeptics writing in the comments) and offered
[more](http://blogs.msdn.com/brian_jones/archive/2005/09/05/461143.aspx)
that still doesn't satisfy the skeptics.

Me, I think Massachusetts is doing the right thing, and it's likely more
Governments will follow.

But on another level I'm concerned that the technopolitics will obscure
other issues with document formats. It would be easy to get the
impression that switching to an open format is all you need to do.

If you want documents to be accessible and useful even in the short term
you need to be able to render them to PDF, which is an option for any
word processor, or HTML which no word processor can do reliably unless
you constrain the way it is used.

(Another way of look at this which may make sense to the XML crowd is
that using your word processor like styles is a bit like doing
well-formed XML instead of using a schema .)

I'll say that again. It doesn't matter whether you are using MS Word,
OpenOffice.org, Adobe FrameMaker, or any other general purpose WYSIWYG
program, it cannot render good HTML output from arbitrary input. Take
the OpenDocument format, for example, it's available in PDF format or
OpenOffice.org format (not OpenDocument). Not HTML.

This is where styles come in.

Using styles you can format a document in your word processor that will
both print well and make a good web page (given software that knows
about your styles), and in the process save time, ensure consistency
with other documents and make re-use much easier. There's more about
this on my [word processing site](http://trac.officecontent.net/) and
there will be practical applications coming out of the [ICE
project](http://ice.usq.edu.au/).

HTML output is not the only reason to use styles either. Ad hoc use of
any complex tool costs you dearly in wasted time in document creation
and re-use and in the lack of consistency in materials produced.

For those of use who have been using styles in our communities of
authors switching between Word and OpenOffice.org Writer (for example)
is trivial - even where Writer messes up stuff imported from Word it is
easy to fix programmatically because the document structure is in the
styles.

For people who have not been using styles, or using styles that use
particularly 'edgy' features in Word migration could be real headache.
This works in Microsoft's favor. Even where a government says “Use the
OpenDocument format” there will be plenty of important existing material
that won't go easily.

So, whichever format you use now do yourself a favor and use styles.
Feel free to share ours, which you can read about on
[trac.officecontent.net](http://trac.officecontent.net/).

</div>
