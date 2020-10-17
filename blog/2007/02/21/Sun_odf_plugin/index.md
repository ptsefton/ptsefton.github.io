---
Title: "ODF plugin for Word is available"
Slug: Sun_odf_plugin
Date: 2007-02-21

---
<div>

# <span id="id47"></span>The plugin

*Sun ODF plugin for Microsoft Office now available*! says [<span
class="Internet_20_link">this
page</span>](http://www.sun.com/software/star/staroffice/index.jsp). It
is a thing that makes Microsoft Word 2003 understand OpenDocument files,
sort of anyway. I did a [quick round-up of document
converters](http://ptsefton.com/blog/2007/02/09/odf-converters) last
week but this one was not available.

You have to register and agree to a license which I think is non Open
Source.

# <span id="id48"></span>Testing

My initial tests were pretty positive so I started writing this page
using the new plugin, in Microsoft Word. Things did go downhill, though.

First up, lets have a picture I took of a sad elephant sculpture by
Bharti Kher. In the Queensland Art Gallery, it's covered in [<span
class="Internet_20_link">bindi</span>](http://www.indianlink.com.au/?q=node/2335).

![graphics1](/blog/2007/02/21/Sun_odf_plugin/1.png)

(inserted via Writer on the Mac cos that<span
class="spCh spChx2019">’</span>s where the photos are)

And a Word drawing of a clipart toilet saying <span
class="spCh spChx201c">“</span>Hmm<span class="spCh spChx2026">…</span>
<span class="spCh spChx201c">“</span>

![Object1](/blog/2007/02/21/Sun_odf_plugin/2.gif)

This drawing survived the round-trip bit it cannot be edited in
NeoOffice, only Word. So it's not really in ODF.

# <span id="id49"></span>The verdict?

More tests below, for document format geeks to admire, but what do I
think, with my [ICE](http://ice.usq.edu.au/) project hat on?

1.  It's SLOOOOOW. About as slow as the way-too-slow Microsoft funded
    [converter](http://sourceforge.net/projects/odf-converter). Like a
    minute or so to open this little document slow. But it 's nicer to
    use because it uses Word's native open and save features.

2.  If you switch between Word and OpenOffice templates get detached.
    Easy to reattach in Word, and for OpenOffice you can <span
    class="spCh spChx2018">‘</span>repair<span
    class="spCh spChx2019">’</span> the document using ICE. I had minor
    issues with the repair functions but we can fix those.

3.  There were some formatting issues, noted below.

4.  It all worked relatively smoothly, albeit slowly, and did I mention
    slowly?

5.  Until...

    ...It stopped working.

    What I put the document through:

    -   Edited in Word 2003 (Windows)

    -   Viewed but not changed in OpenOffice.org 2.0 (Windows)

    -   Edited in NeoOffice on the Mac (after repairing in ICE)

    -   Edited in Word 2003 on Windows

    -   Opened in Word 2003 on Windows again <span
        class="spCh spChx2013">–</span> and the document was completely
        messed up <span class="spCh spChx2013">–</span> only a couple of
        paragraphs showing so I didn't save it.

    -   Edited in OpenOffice.org 2.0 (Windows)

    -   Viewed in Word 2003<span class="spCh spChx2013">–</span> Headers
        and footers had become embedded in the page in the wrong place.

    -   Edited in NeoOffice on the Mac, worked fine apart from lists
        needing to be repaired again.

    -   Opened in Word 2003 on Window, headers and footers still astray.

    -   Pubished via ICE on the Mac.

Bottom line?

**Well maybe**, if it can be made to work about 100 times faster than it
does now. That is it may be usable for ICE, where we [use
styles](http://del.icio.us/ptsefton/usestyles) to carry all important
document structure and can therefore fix conversion bugs and mismatches
by reapplying styles and rebuild those pesky list structures in Word. In
the wild it would be frustrating indeed to work with complex documents
using this thing, just as it is with OpenOffice.org's Word support, upon
which I understand this software relies.

By the way, have you seen [the
list](http://odf-converter.sourceforge.net/features.html) of things that
are different between the two formats, courtesy of the Microsoft funded
Open Source project. The Sun funded non Open Source project doesn't seem
to offer any list of known problems that I could see.

This is just my blog, and I have not yet done the same tests both
available converters, just followed my nose...

# <span id="id50"></span>Style tests

This all works <span class="spCh spChx2013">–</span> except that at one
point bullets became boxes when opened in NeoOffice and one list decided
to start at the wrong place when opened in Word. Thing is, in the ICE
system documents can be 'repaired' in both Word and writer; lists re
rebuilt and reapplied; so minor issues like this don't really bother us.

Here<span class="spCh spChx2019">’</span>s a bit of a workout for the
list formatting.

Definition lists
:   These don<span class="spCh spChx2019">’</span>t use any list
    functions, and they work fine.

Bullet lists
:   This is a definition list with:
    -   A bullet list in it

    -   With two bullets

        How about a Blockquote in here:

        > <span class="spCh spChx201c">“</span>This is quoted text.<span
        > class="spCh spChx201d">”</span>

    -   And a third bullet

Numbered lists

:   1.  This is a numbered list

            SOME PREFORMATTED TEXT EMBEDDED IN THE LIST.

            USE THIS FOR PROGRAM CODE

    2.  With two numbers

        1.  And an embedded Roman-numbered list

        2.  With two items in it

    3.  Make that 3 numbers

        1.  We need to check that this list restarts correctly when

        2.  It is round tripped

:   

</div>
