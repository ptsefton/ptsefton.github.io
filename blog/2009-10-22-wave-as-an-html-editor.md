---
Author: ptsefton
Comments: true
Date: 2009-10-22 01:49:11+00:00
Slug: wave-as-an-html-editor

Title: Wave as a Scholarly HTML editor
Wordpress_id: 382
excerpt: I did a series of articles here a while back  about trying to use various
  word processors and editing tools to write scholarly works for publication in HTML.
  Then this year, I looked in more detail at what Scholarly HTML might be like.  Now
  it&apos;s Google Wave&apos;s turn.
---

<div>

[Update: immediately after publishing I changed the title a little bit]

<div class="page-toc">

-   [Formatting](#id1)
-   [Citations](#id2)
-   [Conclusion](#id3)

</div>

<div>

I did a [series of articles here a while back ** about trying to use
various word processors and editing tools to write scholarly works for
publication in
HTML](http://delicious.com/ptsefton/ptsefton+xhtmlchallenge). Then this
year, I looked in more detail at what [Scholarly
HTML](http://delicious.com/ptsefton/ptsefton+scholarlyhtml) might be
like.

Now it's Google Wave's turn. I got my invitation (thanks Jim) and
immediately had a look at how it might be used for collaborative
authoring for papers. I'll cover two things here; (a) document structure
and formatting tools and (b) citations. I won't say too much about the
collaborative aspects until we have tried it out, but they seem to work
as advertised, a few of us were able to muck around in a document
together without too much trouble.

# <span id="id1"></span></a>Formatting

The first thing I do with any editor is see how it structures documents.
Wave has a slightly weird (to me) set of choices. It has headings, which
is a start, and a whole lot of direct formatting tools, which is
disappointing, and lacks both numbered lists and block-quotes which is a
real pity.

But the really interesting (to me) part is the way it handles bullet
lists.

If I put in a little list like this:

-   List 1

    -   List 2

    -   List 2

-   List 1

Then the HTML it produces is like this:

    <pstyle="margin-left: 14px;" class="simulated-li bullet-type-0">List 1<br></p>

    <pstyle="margin-left: 28px;" class="simulated-li bullet-type-1">List 2<br></p>

    <pstyle="margin-left: 14px;" class="simulated-li bullet-type-0">List 1<br></p>

Not a list-element in sight! It uses plain-old paragraphs with a mixture
of classes (which is fine by me) and direct formatting which is a bit
less so: "margin-left: 28px;". This will probably get some people
riled-up, but actually I think it is a reasonable approach for an
editing environment, provided one can export to proper HTML later and
make something like this:

    <ul>

    <li><p>List 1</p>

    <ul>

    <li><p>List 2</p></li>

    <li><p>List 2</p></li>

    </li>

    <li><p>List 1</p></li>

    </ul>

Why is this approach of using plain-old paragraphs reasonable? It's
because of the mess that most editors get into when editing lists. All
the in-browser editors I have seen have major problems making sensible
structure, they let you do stupid meaningless things like have two
adjacent bullet lists, but don't let you collapse them. I last wrote
about this [looking a Mozilla Seamonkey
Composer](http://ptsefton.com/2008/02/21/xhtml-challenge-mozilla-seamonkey-composer-is-not-suitable-for-writing-academic-papers.htm),
which is a desktop tool.

The Wave approach is very similar to what we do in
[ICE](http://ice.usq.edu.au/). ICE uses styles in a word processor (MS
Word or OpenOffice.org Writer) to *imply* structure. In an ICE document
the above list would be made using styles, shown here in braces. The ICE
Toolbar has buttons just like the Wave ones <span
class="spCh spChx2013">–</span> to toggle bullets and promote and
demote.

-   {li1b} List 1

    -   {li2b} List 2

    -   {li2b} List 2

-   {li1b} List 1

So, provided there is a way in Wave for us to add an export as HTML
feature like the one in ICE which I'm sure there is, then I'm happy with
the flat-paragraph approach. I would really love to see blockquotes
supported and custom styles would be really great. But even if
blockquotes aren't supported we can look for indented paragraphs and map
them to blockquote elements.

# <span id="id2"></span></a>Citations

The other thing that's essential for writing a paper is good reference
and citation support. I asked on Twitter if there was a Zotero gadget
yet, and Bruce Darcus pointed me
to[Igor](http://blogs.nature.com/wp/nascent/2009/07/igor_a_google_wave_robot_to_ma.html),
which doesn't support Zotero, but does connect to PubMed, Connotea or
Citeulike. It works by looking for text like:

> (cite sefton 2006)

Then inserting a reference and updating the bibliography. I have not
tried Igor but it looks like it is limited to one citation style.

All I would want would be a plugin to look for links to an online Zotero
account like this: <http://www.zotero.org/ptsefton/items/77278> or to a
DOI, [as I described back in
April](http://ptsefton.com/2009/04/07/scholarly-html-simple-rational-modern-citations-using-links.htm)
and provide a variant of the Zotero word processor plugin feature to
format citations and bibliographies. One issue might be that as I
understand it parts of the Zotero citation code depend on Firefox
specific libraries, so can't be made to function across-browsers.

# <span id="id3"></span></a>Conclusion

I think Wave shows some promise as a collaborative editing tool, but
it's only going to be useful for simple documents to start with, what
with the lack of table and numbered list support. I'd be surprised if
Zotero support doesn't manifest soon, but if it doesn't then we'll
probably get around to that in my team at some stage.

Of course there's lots more to talk about with the potential for
embedding scientific objects etc, as [discussed in this
post](http://blog.openwetware.org/scienceintheopen/2009/07/19/sci-bar-foo-etc-part-iii-google-wave-session-at-scifoo/).
I'll come back to that.

</div>

</div>
