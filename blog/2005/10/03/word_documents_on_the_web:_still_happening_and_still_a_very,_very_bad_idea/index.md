---
Title: "Word documents on the web: still happening and still a very, very bad idea"
Slug: word_documents_on_the_web:_still_happening_and_still_a_very,_very_bad_idea
Date: 2005-10-03

---
<div>

As the team at USQ get the RUBRIC (Regional Universities Building
Research Infrastructure Collaboratively | [del.icio.us tag:
destrubric](http://del.icio.us/tag/destrubric)) project started I have
noticing a disturbing amount of documentation to do with sustainable
repositories and related projects published in Microsoft Word format on
the web. One would hope that people in this field would at least be
putting up PDF. And HTML would be handy as well. This is the web after
all, not some circus (you know; full of Acrobats).

In 2005 people can still not easily get good quality HTML and PDF
versions of their word processing documents onto the web without fuss.

Why? Why are we still putting word documents on the web? That's a
recurrent theme here – and the short answer is that you need two things
that are not widely deployed.

1.  You need authors to use a known set of styles that map to HTML, ie a
    template. No generic 'save as HTML' will ever work, because the
    structure of an arbitrary word processing document can't be mapped
    to HTML reliably and 'nicely' without styles. There are things you
    can do in your word processor (but should not if you want long-life
    no-fuss documents) - that can't be done in HTML.

2.  You need software infrastructure to catch documents and make HTML
    and PDF – even the [ICE project](http://ice.usq.edu.au/) I'm working
    on is not quite there yet, but it is at least now letting me work in
    a word processor for this weblog.

    While it does make web publishing easier blogging is not the answer
    here – that's typically done with web-only software which is usually
    not integrated with word processors well if at all.

But back to Word on the web.

Before I give some examples, lets go over why Word on the web is a bad
idea:

-   It's not open access. Word is not available everywhere there's a web
    browser.

    Think about Linux, mobile phones, Sony PSPs etc.

-   Word documents can contain history you probably don't want to
    publish for others to see. In some cases other people can
    reconstruct the entire editing history of your document, or worse,
    find traces of other documents that you might not want to publish.

-   Word documents are typically much bigger than HTML documents and
    they are hard to integrate with web sites using hyperlinks.

-   Word is not considered an archival format in a lot of repository
    projects, so putting word on the web is not good behavior for
    leaders in the field to be modeling.

-   Microsoft have made their web Windows web browser load Word when you
    hit a Word document from the web. Maybe they think people won't
    notice, but it can be disconcerting. If you accidentally change a
    document then try to go back, Word wants to save it, for example.

Now the bad news about how people who are working in the sustainable
digital repository field seem to be stuck with Word.

I want to be clear here that I am not blaming individuals. I am
commenting on the lamentable state of the art in web publishing tools
that make it too much trouble to get decent HTML rendition from a Word
document.

Last Monday I attended a meeting of the Australasian Digital Theses
([ADT](http://adt.caul.edu.au/)) project. Amongst the presentations were
a couple of instances of Word on the web. This is odd – given that
theses on the web are usually in PDF format.

Last Tuesday I went to a round-table ([Open Access, Open Archives and
Open
Source](http://www.humanities.org.au/Events/NSCF/CurrentRT/Current.htm).
National Scholarly Communication Forum) on open access research. One of
the recurrent threads was about making research papers openly available.

In presentations there I saw PowerPoint slides with links pointing to
Word documents on the web, from senior people involved in research
infrastructure and policy.

But my favorite example is RUBRIC-related. The announcement from the
Australian Government was done in a Word document. The URL for the
document is:

> <http://www.dest.gov.au/sectors/research_sector/policies_issues_reviews/key_issues/australian_research_information_infrastructure_committee/documents/outcomes_call_for_proposals_doc.htm>

This looks like a URL for an HTML page, doesn't it? But it actually
points to a Word document. On my setup that means it downloads, and I
have to open it to read it – hardly a seamless browsing experience.

Last time I looked (2005-09-21) there is an HTML version of this
document as well, which is undated. I am guessing that someone in the
DEST web team had to convert it by some copy-paste-convert process from
the original.

The web version contains some very basic HTML code. While it is
impossible to tell how it was created, like the word document that
spawned it, it does not carry any structural information, such as
headings. So instead of this heading being coded as such is is merely
formatted with bold tags.

> **B. TECHNICAL DEVELOPMENT AND DEPLOYMENT PROJECTS**
>
>     <P><B>B.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TECHNICAL DEVELOPMENT AND DEPLOYMENT PROJECTS</B></P>

This format-driven approach is common, and I suppose it's not a huge
issue if you are dealing with short documents like this, or lost-dog
flyers, but for a longer document, like (say) a thesis you'd want to be
using headings and other styles. [Use
styles](http://ptsefton.com/blog/2005/03/02/use_styles).

The fact that a document announcing important infrastructure grants
could not be put on the web as a web page immediately is a strong
endorsement of the need for DEST to fund our project, because one of our
goals in the RUBRIC project is to be able to provide researchers (and
DEST, if they want) with word processor based tools that will give them
HTML and PDF from a single source. Like this document. If you want a PDF
version of this you can have one for \$99.97 Australian including GST.

(And yes, I am aware that I have a couple of fixups to do on this site
to make the HTML really good quality).

</div>
