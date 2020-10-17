---
Title: "More news on Word to HTML export"
Slug: more_word_export
Date: 2006-07-14

---
<div>

There's more on lists and XHTML export at Brian Jones' blog, and a post
about a new WordprocessingML to HTML conversion project.

First the list handling. Guest Zeyad Rajabi
[writes](http://blogs.msdn.com/brian_jones/archive/2006/07/12/662552.aspx):

> Word 2007 provides you with a rich editing experience that allows you
> to create a multitude of different types of lists, from simple
> standard one level lists, multi-level lists, to custom defined bullet
> and numbering lists.
>
> Given the time and resource constraint for our blogging feature we
> decided to take a more simplistic route with lists. Our blogging
> feature only outputs two types of lists: unordered and ordered lists
> (we do not support definition lists). That is, we are only relying on
> \<ul\> and \<ol\> HTML elements to render the look of lists, which
> will give full power to the host browser for rendering.

> <http://blogs.msdn.com/brian_jones/archive/2006/07/12/662552.aspx>

I am disappointed in this. I'd love to see Microsoft supply a decent
style-driven system that worked not just for blogging but for HTML
export in general. Failing that, how about a general-purpose
style-driven export system that can be customized with XSLT?

I'm getting tired of writing about his over an over, so see my [recent
posts](http://del.icio.us/ptsefton/ptsefton+wpinterop+lists) on list
support in Word and OpenOffice.org.

Which brings me to a [recent
post](http://blogs.msdn.com/brian_jones/archive/2006/07/13/664720.aspx)
from Brian Jones, pointing to this simple Word to HTML converter. It
really is simple, nothing in there about tables for example. And is it
mapping paragraphs in Word to `div` elements in HTML or am I misreading
it? (I'll join up and ask)

But remember folks: it is not possible to write a generic Word to HTML
converter because Word lets you do a lot more stuff than HTML does.
That's why I keep going on about using styles. If you use an HTML-ready
stylesheet like the one in the [ICE](http://ice.usq.edu.au/)templates
then you can make lovely HTML.

Over at ICE we have an OpenDocument to HTML XSLT stylesheet that could
be adapted to WordprocessingML, and I'm sure someone will get around to
that task at some stage, maybe after there is more boilerplate code
available for doing things like tables, but don't forget that
transforming the textual part of a document is just one part of the
puzzle – you also need to be able to export all the images in
appropriate web formats.

So, Microsoft, or the community I'd like to see an export framework in
Word like the (not very useful) one in OpenOffice.org but please can it
have some configuration options that tell Word how to export various
image formats?

</div>
