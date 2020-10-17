---
Author: ptsefton
Comments: true
Date: 2007-12-12 05:13:42+00:00
Slug: lemon8-xml-more-information

Title: Lemon8-XML more information
Wordpress_id: 21
---

<div>

<div class="page-toc">

</div>

<div>

Some time ago, around the time there was [some discussion on why
repositories use PDF and not
HTML](http://cavlec.yarinareth.net/archives/2007/08/13/another-xml-publishing-tool/)
there was this thing called Lemon8-XML announced <span
class="spCh spChx2013">–</span> at the time there was very little
information available. I tried to get on the mailing list but nobody got
back to me. This week we're having an invitation-only workshop at USQ,
*<span>Connecting Repositories to Authoring Tools</span>*, and I went
back to have another look. Turns out that there is now an
[FAQ](http://www.lemon8.org/pages/docs#faq%20). And a test site <span
class="spCh spChx2013">–</span> which ICE collaborator Ian Barnes knew
about.

L8X comes from [PKP,](http://pkp.sfu.ca/) same place as the Open Journal
Systems ([OJS](http://pkp.sfu.ca/?q=ojs)).

The bit of the FAQ I'm interested in is, of course, about [using
styles](http://del.icio.us/ptsefton/usestyles).

> Q: does it rely on authors choosing styles?<span
> class="spCh spChx2028"> </span>
>
> A: not at this point, although we have considered developing (or
> adopting) a standard set of styles to help provide the document parser
> more information to work with. We would be glad to hear from anyone
> willing to help collaborate on a standard style template for authors.
>
> <http://www.lemon8.org/pages/docs#faq>

We at the [ICE project](http://ice.usq.edu.au/) **would be delighted**
to work with the developers from PKP on a *standard style template*. We
have lots and lots of experience at developing styles and[cross
platform, easy to use interfaces to apply
them](http://ice.usq.edu.au/instructions/templates/using_the_ice_toolbar.htm).
We also have pretty well developed code to go from our generic styles to
XHTML. It should be possible to adapt this to target the XML format used
by L8X either by writing a whole new converter, or by converting via
XHTML-plus-microformats.

I retried registering my interest and I've now made contact with MJ
Suhonos, who is looking forward to talking more, as am I.

If we were to provide ICE-style templates for OJS then one **potential
workflow scenario** could run like this:

1.  The **hard working Journal manager** makes a template available
    using ICE-like styles.

2.  A **careless author** ignores or misuses the template.

    This is normal for journals. There is typically lots of reformatting
    to do at the end of the process. I know from the questions people
    frequently ask about ICE that many people believe that authors
    cannot be induced to use styles properly, but our experience at USQ
    is that if you provide a feedback loop so people can see their
    document converted to HTML, then they **do use and even like
    templates**. See my post, [Why ICE
    works](http://ptsefton.com/blog/2007/08/10/09-25-10.681066/) for my
    take on this.

3.  **Careless author uploads** a document to OJS for the first time.

4.  OJS sends the doc to L8X, which **tries to find the structure** as
    best it can.

    L8X has a four-tab interface where you can see how it went:

    1.  Extracting metadata

        (another thing we're working on this week is how to embed
        metadata in ICE documents so it is easy to extract it reliably
        <span class="spCh spChx2013">–</span> if we can get people to
        use styles then this becomes **much** easier)

    2.  What it thinks the structure of your document is.

        (We find in ICE that showing a table of contents, generated from
        headings gives people really strong feedback.)

    3.  Extracting citations

        (In ICE we're working on Zotero integration, so that citations
        are formatted automatically <span
        class="spCh spChx2013">–</span> this should make it much easier
        for L8X to recognize them)

    4.  And a preview in HTML and PDF

5.  L8X then round-trips the document back into a word processing doc
    using ICE styles and passes it back to OJS. The quality of the
    document has just improved!

6.  OJS uses the styled doc from then on. If the author adds content, or
    metadata about another author then there is a good chance that
    they'll do it correctly, if the template makes it easy. We've
    already got a toolbar that tries as hard as it can to format things
    using styles, we could extend that to have buttons such as 'add
    another author' just by using autotext.

(I tried out the Lemon8-XML demo site, using the styled [Word version of
my paper from Ausweb
'06.](http://ausweb.scu.edu.au/aw06/papers/refereed/sefton/paper.html)
There were several problems, which you'd expect from alpha software like
this <span class="spCh spChx2013">–</span> I have reported the bugs on
the wiki.)

</div>

</div>
