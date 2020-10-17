---
Title: "Why do I keep going on about HTML export from word processors?"
Slug: why_do_i_keep_going_on_about_html_export_from_word_processors?
Date: 2005-10-31

---
<div>

I spend a lot of time on this site going on about HTML, particularly
XHTML export from word processors[using
styles](http://ptsefton.com/blog/2005/03/02/use_styles). Why? Surely in
2005, when the mainstream use of the web is 10 years old, this is a
solved problem?

It's not solved.

If you're using Microsoft Word or OpenOffice.org, or working with a
community that uses both, can  you fire up the word processor, type out
a document and export it as XHTML, or click a button to send it to your
blog in useful XHTML?

If you can, I'd love to know how you do it.

I can, using the [ICE](http://ice.usq.edu.au/) software we're building
at USQ – give or take a few teething problems. But for non ICE users?

Microsoft Word doesn't pretend to have XHTML export, so lets look at
OpenOffice.org writer which does pretend. And I do mean pretend.

## <span id="id1309675"></span>OpenOffice.org Writer (X)HTML export

My first experiment with OOo Writer was to try using the XHTML export on
a document I had written using the ICE template. It had lots of lists in
it. The XHTML export was awful, with list numbering all over the place.
Why? Because the export stylesheet could not divine the structure
implied by my styles and map that structure to XHTML. (And writer has
this horrible mixture of list structures and paragraph styles that are
sort-of tied together and very hard to work with in a consistent way.)

Oh, and the XTHML export that comes with OpenOffice doesn't do anything
with image export. If you want the images then the best approach seems
to be to also save as HTML, which gives you a result very very far from
XHTML, then match the images between the two files (and resize the
images, too, if you want reasonable performance because the HTML export
pumps them all out at full-size and lets the browser do the resizing. We
do it that way in the ICE project using Python code. Really.)

So the XHTML export didn't like my stylesheet. How would I go with the
default template that comes with Writer?

I turned off my ICE template (File / Templates / Organize, select the
templates folder and from the commands drop-down choose reset default
template) and made a new document with the default. A bit of poking
around and I found 'HTML styles' in the stylist. That looked promising.
There were styles for `Heading 1...6`, `Preformatted Text,`
`Quotations`. But what about lists? There's a thing called
`List Content`. Apply that and you get not very much happening. Welcome
to the wonderful world of lists in OpenOffice.org. You have to switch to
the list styles that come built in. There are four list styles with
bullets, List 1...4 the names don't tell you what kind of bullets you
might get. There are four numbered list styles, Numbering 1...4 four of
which are numbered 1...n and one of which is uppercase Roman numbering.
How you would nest these lists inside each other is anybody's guess.

Got that? To apply a list style first apply List Contents from the
paragraph styles, then switch to viewing  the list styles and guess
which list might have the formatting you want. It would take me hours
and hours to work out how to make decent XHTML using these crappy
styles, and I'm a very patient, very experienced user of word
processors.

Weirdness abounds. I can't begin describe to you the chaos that ensues
when you start clicking on the list toolbar. Apply Numbering 4 style and
you get something that starts with II (dunno why, since it is the first
item) and then choose “Down one level” from the list toolbar and you get
a sub-list that starts with III. It goes on and on, and you would need
to do lots of exporting and peering at the result to work out what works
and what doesn't.

I have no idea how to get these lists to nest, or to embed a list in a
quote or embed preformatted text in a  bulleted list item. About all I
could figure out quickly was that there is a button on the list toolbar
that adds another paragraph to a list item.

The XTHML export was a bit better on this test document but instead of
the problem being it not understanding my stylesheet it was the other
way round.

## <span id="id1310486"></span>OpenOffice.org XHTML support sux

I'd like someone to prove me wrong on this, but when Tim Bray [said last
year](http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice):

> It turns out that OpenOffice already comes with a doohickey that will
> produce an XHTML approximation of most documents (Lauren tells me it’s
> shaky on tables)

> <http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice>

he was really stretching credibility. I know Tim Bray doesn't spend much
time in a word processing environment, but if he thought about it, he'd
work out that no single stylesheet can map from something as flexible as
the OpenDocument format to XHTML reliably. How could it possibly do
something sensible with my custom stylesheet? And how on earth are
 users supposed to use the built-in list styles? And what about images?

## <span id="id1310514"></span>The good news (if you're a geek)

So what can you do to make XHTML from OpenOffice.org Writer (version 2)
documents right now? (If you're technically minded and don't mind
working with incomplete software):

1.  Get the ICE template; `ice.ott.` You'll find it under the downloads
    section at
     [http://ice.usq.edu.au/browser/ice/downloads/.](http://ice.usq.edu.au/browser/ice/downloads/)
    The current latest version is:

    <http://ice.usq.edu.au/file/ice/downloads/0.2/beta/templates/ice.ott>

    The ICE template works with styles, available from a `Styles` menu,
    which is organized into things like headings, lists, inline
    (character) styles. In most cases you need only apply a single
    paragraph style using this menu.

2.  You can use the style sheets from ICE, by adding them as an export
    filter.

    1.  Download the XSLT stylesheets and save them in a directory
        together somewhere.

    2.  Set up a new export filter in Writer. (Won't do images but it
        will work better than the built in one)

        -   From the Tools menu, choose XML Filter Settings...

        -   Click New to create a new filter.

            Filter name
            :   test

            Application
            :   OpenOffice.org Writer

            File extenstion
            :   xhtml

    3.  Point the new filter at the `XSLT for Export `on the
        `Transformation` tab.

    4.  OK that. (You don't need to specify a DTD for this project, you
        can still validate because the stylesheet takes care of the XML
        declaration that declares the document to be XHTML).

    5.  Click the `Test XSLTs `button and then `Current document`  to
        see the result of the transform (which is just the same as
        running the `office2html.xsl` stylesheet at this stage).

Or, you can grab the ICE stylesheet now and start working, then get ICE
in a few days when we release Mac OS X 10.4 and Windows compatible
binaries. ICE can sit there watching a directory of content for you, and
keep it under version control using Subversion.

Or, wait a bit longer until we, or some other kind team, package just
the OpenDocument to XHTML part of ICE as a stand-alone bit of code.

****

</div>
