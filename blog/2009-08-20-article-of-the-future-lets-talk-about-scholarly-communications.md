---
Author: ptsefton
Comments: true
Date: 2009-08-20 23:11:30+00:00
Slug: article-of-the-future-lets-talk-about-scholarly-communications

Title: Article of the future? Let's talk about scholarly communications.
Wordpress_id: 374
---

<div>

<div class="page-toc">

</div>

<div>

It has taken me a while to get to commenting on the [Article of the
Future examples](http://beta.cell.com/) from Elsevier and Cell Press. If
you look at their two prototype articles you will see an attempt to
sex-up the presentation of a research articles, with a few social-web
trimmings via a share/save button. I already know how to tweet or
delicious-tag an article all by myself, but OK maybe it's useful. I'd be
more impressed if the delicious tagging thing put in a DOI/Handle
instead of the URL of the page I'm looking at, though.

I can't match the level of detail in Paul Carvill's piece; [Elsevier's
'Article of the Future' resembles websites of the
past](http://onlinejournalismblog.com/2009/07/27/elseviers-article-of-the-future-resembles-websites-of-the-past/)
which I will quote from here. My conclusion is that the Article of the
Future is merely a distraction from the real issues so I would not
bother dissecting the thing in detail even if Carvill had already not
already eviscerated it:

> these <span class="spCh spChx201c">“</span>Articles of the Future<span
> class="spCh spChx201d">”</span> are not tools, and they are no more
> innovative than using a page layout application to alter the
> appearance of some printed matter.  Hyperlinking and the ability to
> add media files to a page have existed since the web was created, and
> these articles add nothing more to that basic paradigm of linked data
> files [PS: I don't think this is a reference to Linked Data in the
> Berner's Lee semantic-web sense].  There are some nods towards current
> trends, with a comment feature and social bookmarking links.  But
> overall the feel is clunky, lacking research and distinctly amateur.
>
> <http://onlinejournalismblog.com/2009/07/27/elseviers-article-of-the-future-resembles-websites-of-the-past/>

Read the whole critique, there are lots of good points in there.

My first reaction was that most of what is presented in the prototypes
is interface trickery that is being driven by the XML structure behind
the articles. The most obvious example is that there is a kind of
tab-driven Table of Contents (ToC); I guess that is a compact way to
present a ToC if you have a small enough number of main headings, but
it's a trivial programming exercise and I'm guessing that if the idea
had legs it would be in wider use; and it's masking a deeper concern.
Carvill notes that you simply can't access the prototypes without
Javascript turned on and I agree this is very bad. There is no reason
that these articles could not be presented in purely declarative,
semantically rich HTML, as per my post describing a potential [Scholarly
HTML](http://ptsefton.com/2009/03/31/scholarly-html.htm), with the
interface trickery loaded in on browsers that support it, for users that
want it. Not exposing the complete structure of the article in one go,
or with plain links is an effective way of blocking machine processing
of the text and data (if data happens to be linked, which does not seem
to be the case here), not to mention potentially blocking reader's
ability to archive the page in a tool like Zotero or save it for later
reuse.

This brings me to some of the bigger issues. When interviewed for a
recent [Times Higher Education article on scientific
communication](http://www.timeshighereducation.co.uk/story.asp?sectioncode=26&storycode=407705&c=2),
[Peter Murray-Rust](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=2214)
points out that publisher policies on the use of tools to process online
papers are a drag on scientific communications:

> "You are actually barred from using modern techniques to enhance your
> science ... it has taken us back ten years in the use of scientific
> information,"

Peter is talking about policy there, but he has also campaigned against
locking up publications in PDF which is a technological approach to the
same end. What we see here is potentially a way to lock up HTML, too. I
don't know whether this is a deliberate *policy* or not, but the lack of
emphasis on data and the lack of a one-page HTML and/or XML view point
to a maybe unconscious attempt to keep up the divide I pointed out in
the paper I [posted here
yesterday](http://ptsefton.com/2009/08/19/towards-scholarly-html.htm#id2),
the gap between author's versions of papers and those held by the
publisher. I said there:

> <a name="id2"></a>To illustrate the potential divide between the
> author<span class="spCh spChx2019">’</span>s version and the
> publisher<span class="spCh spChx2019">’</span>s, consider that
> Elsevier, the publisher of this journal, recently ran a competition,
> Article 2.0 to show the future of a scientific article. The
> competition winner shows that a journal article may be the Web locus
> for discussion, annotation and semantic relationships, but this
> competition was built on XML source documents which are created and
> held by the publisher, so there is no way that a typical institutional
> repository could easily provide the same services. This is a case
> where the publisher is shaping scholarly communications, or at least
> exploring how to do so, but a lack of tools means that repositories
> are unlikely to be able to do likewise. This creates a distinct divide
> between the publisher<span class="spCh spChx2019">’</span>s more
> richly marked-up version and the version held by the author in word
> processing format or the typesetting system LaTeX, neither of which
> allow high quality HTML unless the author has used a particular set of
> templates and/or macros and has access to specific conversion
> software.
>
> [[doi:10.1016/j.serrev.2009.05.001](http://dx.doi.org/10.1016/j.serrev.2009.05.001)]

What we really need, I think, is Scholarly Communications 2.0, not
Article of the Future or Journal 2.0. Articles and Journals are
constructs that we may not end up needing. To find out, we should work
out the new model for research that a number of those interviewed in the
Times Higher Education article were talking about. My article suggests
some ways that USQ might proceed, recommending that we (a) start with
research theses and (b) build from our strength in flexible educational
delivery to build a new scholarly communications process around the
scholarship of teaching and learning.

</div>

</div>
