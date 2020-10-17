---
Title: "WP Interop Project: First documentation"
Slug: style
Date: 2004-08-23

---
[Last time I wrote](blog/2004/08/16/wordprocessorinterop) about a
project to set up a system for making Word and OpenOffice work together
to do genuine content management - and to give us [Tim Bray's 'blog
this'](http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice)
button for Word and OpenOffice.org. This is the first part of that
project.

Today I have [put up some preliminary documentation](wp-interop-styles).
This is all about word processing's one redeeming feature, styles.
Styles are names that you can give to paragraphs: "Main heading",
"Ordinary paragraph", "Quote", "Title". Stuff like that.

Example: you can tell the word processor that all the stuff you label
with the style name "Main heading" should be made really big, say three
inches high, in some really baroque font. And then you can come to your
senses and choose a classic understated font in more modest size; and
your entire oeuvre could be changed in a few seconds, because you always
used styles and never just applied the dreaded direct formatting to make
your document look right.

In the web world, if you use styles you're considered to be pretty
classy. (For those of you who are not web-geeks that's a joke; the same
system of naming things applies, but the names are called classes. And
the system is called Cascading StyleSheets, CSS.)

The solution I'm going to build for the word processor interoperability
project is to use styles to drive everything, based on tried and tested
style systems developed at Standards Australia, RMIT and NextEd.

If you are going to try to get a wide variety of people to use this
system then it may be challenging to get them all using styles. I have
been involved in a few large-ish scale projects where we have
successfully assisted people to use styles, but I hear from people
involved in larger scale more distributed projects, working with general
web content (particularly at RMIT) that they are thinking of relaxing
the styles-only rule and trying to figure things out by interpreting
formatting.

I also [have more extensive notes on why I am sticking with
styles](style-basics) for this project.

This document is a work in progress and will change, as I add more
detail. Remember - we are going to add custom processing to both
applications to get good, consistent XHTML output, leveraging but not
*relying on* their built in features, so it matters not if the style
sheet is output as good XHTML out of the box, it matters only that we
can make good XHTML.
