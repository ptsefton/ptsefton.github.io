---
Title: "A first try of Zotero's Word integration for citations and bibliographies"
Slug: zotero_word_processor
Date: 2007-03-05

---
<div>

[Zotero](http://www.zotero.org/) is an open source bibliography
management system - think EndNote embedded in your browser - that seems
to be coming along very nicely even if there are
[concerns](http://netapps.muohio.edu/blogs/darcusb/darcusb/archives/2007/01/27/zotero-and-the-bazaar-what-zotero-should-learn-from-successful-open-source-projects)that
it is not very open to external contributions. Oh, and the browser has
to be Firefox.

It's important for the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project that we
have a good referencing application, and Zotero now looks pretty certain
to be it.

I have been sort-of using Zotero for a while now to collect references,
but its word processor integration only recently appeared and I only got
around to looking at it today.

Here's a few notes on how Zotero works with Microsoft Word 2004 on the
Mac.

1.  I downloaded the disk image, opened the template, and went
    `File / Save as...` - Word helpfully offered to save in a templates
    directory so that worked fine <span class="spCh spChx2013">–</span>
    it's just not what you're meant to do. I should have put it in the
    startup folder for Word as described in the instructions.

2.  There's a little toolbar with only three buttons. One inserts a
    citation, one inserts a bibliography and the other sets a single
    preference. That's abut the right number of buttons.

3.  Citations get inserted like this: Sefton 2006() - think there must
    be a little formatting bug there.

4.  My explorations didn't last long because it started complaining that
    it could not talk to Firefox, even after I restarted both Word and
    Firefox. I think it has problems if you try to include citations
    with incomplete data, or delete things from the database and leave
    them in the document.

As far as I can tell almost all the work is done by Zotero. The Word
macro uses AppleScript to make web (SOAP) calls to Firefox / Zotero
behind the scenes. This looks very promising for ICE integration; should
be easy to call Zotero with a list of citations and ask it to make a
bibliography.

But, while I'm prepared to accept the limitations of new software, such
as a small number citation styles for the Word plugin, **there's one
thing I really don't like**. Zotero uses Word fields to store citation
information. Those **fields do not work** when you open the document in
OpenOffice.org. That's a complete show-stopper for us. Of course we
could just make a new version of the macro that uses a more
interoperable citation format, but I've attempted to [start a discussion
on the Zotero
forums:](http://forums.zotero.org/discussion/500/format-for-embedding-citations-in-word-processors/#Item_0)

> My initial experiments indicate that citations embedded in Word using
> Fields are lost when the .doc file is opened in OOo. So, can we look
> at using a mechanism for carrying citation information that will be
> preserved. One approach would be to use bookmarks rather than fields.
> I have also considered looking for hyperlinks, matching those against
> URLs in Zotero and inserting appropriate citations.
>
> What's the current thinking on this issue within the Zotero team?

Zotero can recognize some kinds of metadata embedded in web pages and
automatically import it. At the moment in doesn't recognize [USQ's
Eprints](http://eprints.usq.edu.au/), even though it has Dublin Core
metadata in the head element. It looks like adding support of our
ePrints would be easy enough. There's an incomplete how-to on the site
explaining how. We'll definitely look into teaching Zotero about ePrints
and the other repositories we deal with in RUBRIC.

# <span id="id5"></span>

</div>
