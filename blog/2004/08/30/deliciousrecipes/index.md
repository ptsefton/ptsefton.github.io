---
Title: "Delicious recipe markup"
Slug: deliciousrecipes
Date: 2004-08-30

---
If you have been following this weblog you will have seen me talking
about a so-far imaginary content store called the
[Fragletorium](blog/2004/04/28/platform_for_udell), marking up web pages
with classes to show where special content (like
[recipes](blog/2004/06/02/recipe_schema)) resides so you can do sematic
querying, rather than fumbling around with full text searches, and most
recently, the magnificent communal bookmark system called
[del.icio.us](http://del.icio.us/).

This time I am going to talk about all of these.

Jon Udell showed [early in
August](http://weblog.infoworld.com/udell/2004/08/11.html#a1057) how he
automatically built del.icio.us bookmarks for his weblog by adding
'tags' (categories) to each post and then harvesting them and using the
del.icio.us API to create the bookmarks.

Late in August I got around to doing the same trick on my site - with
one difference. I'm too lazy to tag my posts so I have just added a tag
'ptsefton' to every post. And I have leveraged another resource; the
markup I added to some, er, actually one so far, post to show that part
of it was a recipe.

As mentioned before I am slowly writing code to build a full-text and
XPath indexed content store (the aforementioned
[Fragletorium](blog/2004/04/28/platform_for_udell)) with every item
having an XHTML rendition, regardless of its origin. I have some test
code that harvests the wiki-style source documents for this site, turns
them into XHTML and stores them in an XML repository where I can do
XPath queries for my own amusement. Minutes of fun there, I can assure
you.

Here's my del.icio.us trick, based on Jon Udell's code.

As I process each item, using Python, in which I am still barely
literate, I do an XPath query to find recipes:

    recipes = fraglet.xhtmlDoc.xpathEval("//*@class='recipe'")

If I find any then I can add a tag "recipe" to that item and post it
using the del.icio.us site, using curl, just like Jon. But when he says
he's generating a batch file, he must be targeting an operating system
other than Windows. On Windows you need to escape the % characters
otherwise they try to mean something.

    print 'curl -u xxxxx:xxxxx "%s"' % re.sub('%','%%',post)

I have now done this to my site, and the results are here: [all the
content](http://del.icio.us/petey/ptsefton) and all the
[recipes](http://del.icio.us/petey/ptsefton+recipe). (You can even
subscribe to the RSS feed on that page if all that keeps you coming back
is my recipes. Coming up sometime this financial year: chunky loquat jam
and PT's infallible tomato and basil salad).

This trick would work wonders for a bigger site with better semantic
markup, like, you guessed it, Jon Udell's. See his stuff about XPath
search [with semantic markup in class attributes with multiple
space-separated
values](http://weblog.infoworld.com/udell/2004/02/09.html). Using the
technique I have outlined here, one could pull out all the classes,
maybe just going for ones starting with some magic string like 'tag' (as
I am proposing in my [Word Processing Interoperability
project](wp-interop-styles)) and do one or more of the following:

-   Add tags to del.icio.us or similar that point you right to the
    content you seek rather than the top of the document (like I did
    with my recipe).

<!-- -->

-   Yank out the whole element that's been marked, full-text index it
    separately and give it is own URL on your site. This would be great
    for educational content where you might want to pull out all the
    objectives, or the activities or whatever, not to mention finding
    the word 'loquat' in the ingredients list of a recipe which may well
    be embedded in an incomprehensible technical babble-fest like this
    one.

<!-- -->

-   Do this recursively, so you index an entire document, then grab the
    recipes as separate docs, and then the ingredients from them, and so
    on.

I'm still excited about full-on XPath indexing, but I think this
approach may be more generally useful and probably much cheaper to run;
you define some useful queries at index time. If more queries occur to
you, or your users invent them then simply define them and re-index.
(This is how [TeraText](http://www.teratext.com.au/index.html) works.
It's a great XML-aware text indexing content manager of awesome power,
and not inconsiderable cost that I use when I can justify it).
