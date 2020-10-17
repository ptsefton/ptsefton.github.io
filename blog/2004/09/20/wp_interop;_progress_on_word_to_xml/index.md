---
Title: "WP Interop; Progress on Word to XML"
Slug: wp_interop;_progress_on_word_to_xml
Date: 2004-09-20

---
I have been making some progress on Word to XML conversion, essential to
the [WP Interop project](blog/2004/08/23/style). This was originally
supposed to take place *after* I released a sample template for
OpenOffice.org Writer, but [Rick Jelliffe's observation about Word in
XML projects](http://www.oreillynet.com/pub/wlg/5326) following from the
Open Publish conference in Sydney got me thinking that I should publish
on this matter. Rick says:

> If I were to pick a theme or meme, it was that the decision on whether
> and how to support Word was the by far the most critical decision for
> most large XML deployments.

He goes on to talk about how some users are entrenched in Word. But I
think can empower them to transcend its limitations, and maybe help them
to move to 'better' tools. The problem is, the better tools are not
really here yet, as noted by Tim Bray and discussed here
[before](blog/2004/08/09/futureoffice).

So, the first substantial release from my WP Interop project will be a
Python script, with commentary about how it works, for generating
well-formed XML from Microsoft's deservedly much maligned 'Save as Web
Page ...' format. Stay tuned for details about how I used libxml2 to do
most of the heavy lifting.

Once we have a Word template using the [WP Interop
styles](wp-interop-styles) and an XHTML stylesheet to turn documents
into real XHTML, I should even be able to use it to write for this site,
when James Tauber releases [Leonardo](http://james.tauber.name/leonardo)
0.4 with its new architecture.
