---
Title: "Why not use styles for blogging in Word 2007 and really leap the chasm"
Slug: chasm_crossing
Date: 2007-02-27

---
<div>

What a shame it is that some of the bestest geeks use Emacs. Off the top
of my head, blogs I am subscribed to include those written by Emacs
users [Norm Walsh](http://norman.walsh.name/) and [Tim
Bray.](http://www.tbray.org/ongoing/) I bet there are lots of others.
I've used this quote from Tim Bray before:

> Geeks like me are fine with writing in Emacs, but lots of people seem
> to like writing in word processors,
>
> <http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice>

Why is it a shame they use Emacs? 'Cos if they wrote using word
processors like OpenOffice.org Writer or Microsoft Word then there would
be good ways to use those word processors to create HTML.

Another favourite blogger, who's more of a journalist than the other two
is Jon Udell. He uses Emacs too, but he's also thinking about the other
99.9999% of the world. Recently he wrote about [Blogging with Microsoft
Word 2003, crossing the
chasm](http://blog.jonudell.net/2007/02/19/blogging-from-word-2007-crossing-the-chasm/).

Jon's latest piece is about metadata and doesn't mention the word
**style** once, but I know that he understands the value of styles.

Last year, when Microsoft were talking about the new blogging feature in
Word 2007 [I
tried](http://blogs.msdn.com/brian_jones/archive/2006/06/08/621325.aspx#622812),
via Brian Wilson's blog to get a conversation started about styles in
Word, and how a standard set of styles for common formatting in Word
could really, really improve their HTML export. Not just for blogging
but for 'Save as web page...' as well. I was frustrated that this
blogging feature was seen as quite separate from general web export,
that Word doesn't come with a single template with a decent
comprehensive HTML compatible stylesheet, and that nobody had the time
to explain why Word has three different ways of expressing[style on a
list item](http://ptsefton.com/blog/2006/06/13/list-samples) (same
problems over at Sun, re OpenOffice.org).

Word could **so easily ship with a 'use HTML compatible styles' mode**,
that turned off all the formatting buttons and had a nice clean
interface that only did HTML exportable things, all using styles. I know
this, because I can do this with Word, although for short documents I
usually fly NeoOffice.

In Word at at the moment saving as HTML will turn Heading 1 into an h1
element, Heading 2 into an h2 element and for the rest, your guess is as
good as mine. Some formatting choices will result in nice(ish) HTML
others will be horrific, or worse. Sadly, [using
Styles](http://del.icio.us/ptsefton/usestyles), which is generally
considered to be A Good Thing in word processing doesn't buy you
anything unless you have a bit of custom software, like, um, say,
[ICE.](http://ice.usq.edu.au/)

Also last year Jon Udell was kind enough to say, about ICE:

> Peter Sefton [has integrated
> Slidy](http://ptsefton.com/blog/2006/05/23/presenting_slidy_ice)into
> the University of Southern Queensland's ICE courseware system. ICE, by
> the way, is a noteworthy example of how wordprocessor stylesheets --
> for OpenOffice.org and MS Word -- can provide the integration glue for
> single-source and multi-output content management.
>
> <http://weblog.infoworld.com/udell/2006/05/23.html>

Noteworthy!  Jon Udell said that ICE is noteworthy! (Ron Ward, Daniel de
Byl and Pamela Glossop did the integration, I just proved the concept.)

So, Jon Udell, who is now working for Microsoft, recognizes that
stylesheets can provide the glue for multi-output content management. He
describes his new work on manipulating Word 2007 files:

> To that end, I<span class="spCh spChx2019">’</span>m developing some
> Python code to help me wrangle Word<span
> class="spCh spChx2019">’</span>s default .docx format, which is a zip
> file containing the document in WordML and a bunch of other stuff. At
> the end of this entry you can see what I<span
> class="spCh spChx2019">’</span>ve got so far. I<span
> class="spCh spChx2019">’</span>m using this code to explore what kind
> of XML I can inject programmatically into a Word 2007 document, what
> kind comes back after a round trip through the application, how that
> XML relates to the HTML that gets published to WordPress, and which of
> these representations will be the canonical one that I<span
> class="spCh spChx2019">’</span>ll want to store and process.

And Jon Udell notes formatting problems:

> Note: There will be formatting problems in this HTML rendering which,
> for now, painful though it is, I am not going to try to fix by hacking
> around in the WordPress editor.

Here's an idea. ICE has a [set of
styles](http://ice.usq.edu.au/ice-guide/study-modules/module06.htm)
which are designed to map to HTML.  ICE has a bit of [Python
code](http://ice.usq.edu.au/trac/browser/ice/trunk/apps/xhtml-export/ooo2xhtml/ooo2xhtml.py),
with quite a few
[tests](http://ice.usq.edu.au/trac/browser/ice/trunk/apps/xhtml-export/ooo2xhtml/convertionTests.py),
that does ODF -\> HTML, making it possible to write HTML using not just
Word 2007, but basically any word processor with styles. **Would anyone
care to adapt it** to use Word's OOXML? Wouldn't be hard, as it really
only needs to work with paragraphs, spans and style-names; the hard work
on a state-machine framework to drive the transformation is already
done. Thanks Ron Ward. (There's also some legacy XSLT code that could be
adapted, but it has performance problems and a couple of long standing
bugs and it's hard to maintain.)

And the ICE style names are just one set. If Microsoft or Sun, or
preferably both, backed a differently named set that did the same job
we'd adapt instantly.

**We chose short names**, like `h1`, `h1n`, `li1b`, `pre1`, `bq1` so
they' d be easy for style-geeks to type if they needed to, but we do
provide a non-geek accessible menu, [which is soon to be
improved](http://ice.usq.edu.au/trac/wiki/IceOpenSource/TemplateToolbar2Spec).

We chose short names so they would **show up in the left margin** of the
page in Word's Normal view.

We chose short names that are easy for machines to parse so we could
automate HTML and other conversion.

**We chose style names that are not part of the meager set** of
semi-default styles that ship with word processors and we chose to make
all other styles in Word go RED, to help with document conversion.

</div>
