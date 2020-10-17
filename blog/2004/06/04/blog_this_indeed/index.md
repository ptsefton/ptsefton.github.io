---
Title: "Don't just blog this"
Slug: blog_this_indeed
Date: 2004-06-04

---
> Geeks like me are fine with writing in Emacs, but lots of people seem
> to like writing in word processors, and as of this week, I think that
> any word processor without a "Blog This" button is just broken.

Geeks like who? [Geeks like Tim
Bray](http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice).
Other people prefer
[vi](http://www.oreilly.com/news/zenclavier_1299.html) over Emacs, and
James Tauber thinks [Eclipse will be the next
contender](http://www.jtauber.com/blog/2004/04/05/eclipse_is_next_emacs).
I prefer to write prose in a word processor, but then I'm not a geek.

Here are my thoughts on blogging from a word processor, and how this
might work with Atom, which [does not look promising at this
stage](http://www.tbray.org/ongoing/When/200x/2004/06/02/AtomMeetingReport#p-22).

I like Tim Bray's idea of the "blog this" button, but I think we can do
even better than that. As of today *I* think any word processor without
a

-   make me an XHTML version of this content,
-   check with me how much metadata I would like to add,
-   help me provide an abstract by pulling out the first paragraph or
    two,
-   stick it in the corporate content store,
-   keep the original so it can be re-edited,
-   check if I want all of it — or a short bloggish summary — to appear
    in a blog,
-   ask if I want a PDF rendition,
-   and work out what distribution it should have,

button is just broken. Two clicks to just blog an item as is, a few more
to slot it into a knowledge base where it can find others like itself on
the basis of more than just the posting date. If I'm writing minutes
from a meeting I probably want to store the full minutes and blog a
summary but also be able to search by document type or by meeting. A
good general purpose content management system can run a blog, but a
blogging system is a just a web logging system. I want both.

In [the OpenOffice.org application suite](http://www.openoffice.org/),
about which geek Tim Bray is talking in his post, my button looks easy
enough to add, given a place to store the content and run the blog and
so on. OpenOffice already has a nice way of keeping all its bits and
pieces including images in one place, a zip file. It also has a barely
acceptable export to HTML, which can be [tidied to make it into
XHTML](http://tidy.sourceforge.net/). I am looking to see if OpenOffice
can be scripted to add PDF, and HTML stuff to this container so it can
be thrown around as a single object.

In MS Word the problem is somewhat different. From Word 2000 onwards
there is a 'Save as Web' feature that gives you all of your content in
an accessible format, including an HTML-ish version that's relatively
easy to transform into XML, from where you can transform it easily to
XHTML based on your styles. You even get web-ready versions of all your
images and other component objects. But Word lacks an omnibus format
that bundles them all together (yes I know about the Microsoft download
that is supposed to do this but it doesn't work for me), and a built in
PDF renderer. [The Ace scripting language has round-trip-functions for
Word HTML](http://www.teratext.com.au/get/page/directory/browser) that I
helped design. See this [presentation in PDF I gave with Timothy
Arnold-Moore](http://www.planetmarkup.com/xmlarena/xap/Thursday/WordtoXML.pdf).

The bad news is that at this stage there is no way to do build this
button and use Atom to add it to a blog without multiple posts. Tim Bray
[again](http://www.tbray.org/ongoing/When/200x/2004/06/02/AtomMeetingReport#p-22):

> A crucial decision point seems to be whether you try to package up
> multiple pieces in one message, or not.

If Atom doesn't let you package multiple pieces in one message then I
won't use it for posting to a repository. I don't understand all the
technical stuff involved here — I naively thought of using a zipped
bundle for multi part entries — but I don't want to have to manage
multiple calls to a repository to do what should be a single
transaction, and then have to manage rollback if something goes wrong.
Been there.
