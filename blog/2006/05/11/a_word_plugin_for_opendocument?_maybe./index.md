---
Title: "A word plugin for OpenDocument? Maybe."
Slug: a_word_plugin_for_opendocument?_maybe.
Date: 2006-05-11

---
<div>

Some people from something called [The OpenDocument
Foundation](http://opendocument.us/) say they have developed an
OpenDocument read/write plugin for Microsoft Word. But they don't say it
on their own website (and their website is actually a frameset pointing
to another very unimpressive site at
[http://www.theequityexchange.com](http://www.theequityexchange.com/)).

I read about this on
[Groklaw](http://www.groklaw.net/article.php?story=20060504015438308),
via [SolidOffice](http://www.solidoffice.com/archives/282).

The claim published on Groklaw says, in part:

> The testing has been extensive and thorough. As far as we can tell
> there isn't a problem, even with Accessibility add ons, which as you
> know is a major concern for Massachusetts.

> <http://www.groklaw.net/article.php?story=2006050401543830>

I'm skeptical.

Why? There is, as Microsoft has repeatedly claimed, a mismatch between
the features in Microsoft Office and OpenDocument. **There is definitely
such a mismatch** between Word and the most-used application that uses
OpenDocument which is OpenOffice.org. That is, there are things that
won't map between the applications.

For example, **OpenDocument has styles for lists and Word doesn't**. The
OpenOffice.org solution to this involves creating new list styles like
`WW8Num1` when you load a word document, even if that document was
created three minutes ago in OpenOffice.org and used a list style called
`li1n`. This is causing us lots of trouble on the [ICE
project](http://ice.usq.edu.au/svn/ice/downloads/latest/documentation/packages/ice-guide/ice-guide_template.zip),
but we will write macros and other code to fix the problem because we
use paragraph styles to carry the important information about our ICE
document. Paragraph styles are similar enough between word processors
that they do tend to interoperate pretty well.

So what will this magic plugin do when you open an
OpenOffice.org-created document in Word? I'd love to see.

**Going the other way**, Word has an outline feature the lets any
paragraph participate in an outline whereas in OpenOffice.org you are
restricted to using a single set of heading styles. I did check the
OpenDocument spec and it appears to me that this limitation is built in
to the format.

There are lots, lots more examples that will come up and keep coming up,
but the ICE team will keep on finding solutions and working on the
documentation (you can download a zip
[here](http://ice.usq.edu.au/svn/ice/downloads/latest/documentation/packages/ice-guide/ice-guide_template.zip)
– but it will soon be online).

In ICE, we don't care so much about **full interoperability** between
Word and OpenOffice.org Writer, we care are about knowing what is the
set of features that you can to **allow interoperability**. So I'd love
to get my hands on the OpenDocument Foundation's plugin if and when they
decide to release it.

(Yes I know there are supposed to be other [word processors that support
OpenDocument](http://en.wikipedia.org/wiki/List_of_applications_supporting_OpenDocument)
but for now OpenOffice.org is the one that matters to the people I'm
working with. Try following the links to IBM to see if you can find out
anything about their word processor, if there is one. I gave up after a
few minutes of reading the same uninformative stuff repeated on
different pages.)

</div>
