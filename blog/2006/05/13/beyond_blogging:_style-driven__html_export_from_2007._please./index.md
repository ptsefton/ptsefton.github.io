---
Title: "Beyond blogging: style-driven HTML export from 2007. Please."
Slug: beyond_blogging:_style-driven__html_export_from_2007._please.
Date: 2006-05-13

---
<div>

Via [Brian
Jones](https://rubric-central.usq.edu.au/projects/trac/rubric/timeline?ticket=on&wiki=on&max=50&daysback=90&format=rss),
who writes about the new Office XML formats for Microsoft, I welcome the
news from Joe Friend that there will be built-in[blogging in Word
2007](http://blogs.msdn.com/joe_friend/archive/2006/05/12/595963.aspx).

This is good news not so much for the blogging bit but for the way that
Word will be able to make clean HTML from styles. Joe Friend only
[mentions](http://blogs.msdn.com/joe_friend/archive/2006/05/12/595963.aspx)
a couple of styles (h1 and, I assume, quotes, or does he mean any
paragraph enclosed in quote marks and indented?):

> Go ahead, click View, Source in your browser and look at the HTML
> starting with "Word is a great tool..." We really are going pretty
> basic here. Bold become \<strong\>, Italic becomes \<em\>, Heading 1
> become \<h1\>, Quotes become \<blockquote\> and on it goes. There are
> definitely kinks in Beta 2. For example we are encoding smart quotes
> incorrectly so I had to turn off that feature in Word, but the goal is
> to output just what is needed to make your blog post clean and
> readable (code and rendered HTML).

That's fine, but what about lists, and pre-formatted text embedded in
quotes and so on? (And actually I think bold should map to \<b\>, or
nothing, and you should use a style called 'strong' if that's what you
want).

Well at the ICE project we have developed a stylesheet that can drive
clean HTML output, and we have templates for both Word and
OpenOffice.org – so I can post to this blog from Microsoft Word or any
OpenDocument aware application, like OpenOffice.org. I have covered this
in a number of previous posts. So look
[here](http://ptsefton.com/blog/2005/09/18) for an example, and
[here](http://ptsefton.com/blog/2005/09/05/blog_this_button_for_openoffice.org_(well_half_anyway))
for some stuff about the ICE approach to blogging from a word processor,
and in the [pre-print of the
paper](http://eprints.usq.edu.au/archive/00000697/) I'll be giving on
ICE at Ausweb 06 for some more detail about how the mapping works. I'll
quote that paper here:

> The core styles are listed below.

<div class="Table48" align="left">

Family

Type

Style names

Paragraph (p)

p

Heading (h)

h1

h2

h3

h4

h5

Heading (h)

Numbered (number)

h1n

h2n

h3n

h4n

h5n

List item (li)

Numbered number)

li1n

li2n

li3n

li4n

li5n

List item (li)

Bullet (bullet)

li1b

li2b

li3b

li4b

li5b

List item (li)

Uppercase Alpha (A)

li1A

li2A

li3A

li4A

li5A

List item (li)

Lowercase Alpha (a)

li1a

li2a

li3a

li4a

li5a

List item (li)

Lowercase Roman (i)

li1i

li2i

li3i

li4i

li5i

List item (li)

Lowercase Roman (I)

li1I

li2I

li3I

li4I

li5I

List item (li)

Continuing paragraph (p)

li1p

li2p

li3p

li4p

li5p

Blockquote (bq)

bq1

bq2

bq3

bq4

bq5

Definition List

Term (dt)

dt1

dt2

dt3

dt4

dt5

Definition List

Description (dd)

dd1

dd2

dd3

dd4

Dd5

Pre formatted

(pre)

pre1

pre2

pre3

pre4

Pre5

Metadata: title

(title)

Title

</div>

**Table of style names for paragraph styles in ICE.**

> The set of style names is designed to be different to those that ship
> by default with major word processors in order to emphasize that this
> is a self-contained system. For example, a first level heading is
> called h1, rather than Heading 1 in Word or OpenOffice.org while a
> first level bulleted list item would be li1b for “list item, level 1,
> bullet”.
>
> In the default style-sets that come with other word processors this
> kind of list item might be “List 1” in OpenOffice.org, or “List Bullet
> 1” in Word. The Word style name is more readable than the ICE style,
> but at the cost of being so long that it can be difficult to work with
> in Word itself, when trying to view style names in the left margin (a
> feature denied to users of OpenOffice.org).

So, what if Word 2007 finally shipped with the Normal template
containing a complete set of styles, like the ICE styles, that would
cover pretty much the same territory as HTML? Not just headings, but
different flavours of numbered list, definition lists, pre-formatted
text and blockquotes in a number of levels that could be combined.
Something a bit better than the feeble, incomplete set of styles
Microsoft has been shipping for years.

Hey Joe, you can [contact me](mailto:pt@ptsefton.com) if you'd like some
help – I've been **working on this issue for ten years**.

(And what if the much hyped new clean Word interface defaulted to using
styles for its formatting? Imagine if pressing those little list-icons
have you not only list-like formatting but style-driven list-based
formatting. That would mean that you could **export clean HTML** and
**really interoperate with other packages**.)

Given a decent set of styles then finally the default `Save as HTML...`
in Word could produce nice clean HTML. Please, please, Microsoft don't
tell us that you've continued to bury and de-value styles, and make
templates even harder to find in the interface.

For example, it Word's HTML export system saw a paragraph with the style
`List Bullet 1` followed by `List Bullet 2`, it would know how to output
nested list in HTML. At the moment **HTML export in any word processor
is severely handicapped** by having to divine good mappings to HTML from
a completely open-ended formatting palette, with the result that clean
export is pretty much impossible. You can read about my frustrations
with the OpenOffice.org Writer application
[here](http://ptsefton.com/blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F).

And going a bit further wouldn't it be great if OpenOffice.org and
Microsoft Word and Google's Writely (see my
[post](http://ptsefton.com/blog/2006/03/21/writely,__meet_the_ice_template))
all understood the same set of styles and could make clean HTML from
them? (They all agree on “Heading 1, Heading 2” but that's as far as it
goes).

Ok, so maybe Microsoft and Sun and Google don't care. But
[**we**](http://ice.usq.edu.au/) do so we'll continue in our struggle to
provide good word processor interoperability even if we have code it
ourselves. It would just be so much easier if the vendors helped the
community.

</div>
