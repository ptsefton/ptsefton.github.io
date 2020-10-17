---
Author: ptsefton
Comments: true
Date: 2008-02-05 02:13:52+00:00
Slug: mini-websites-of-supporting-material-for-scholarly-articles

Title: Mini websites of supporting material for scholarly articles
Wordpress_id: 83
---

<div>

<div class="page-toc">

</div>

<div>

Via [First Author](http://www.firstauthor.org/blog/?p=159), I see that
BioMed Central has added the ability for authors to include extra web
material with a paper:

> ... to make it possible to upload collections of files that can be
> conveniently navigated in the web browser - essentially a miniature
> website associated with the article. This functionality has now been
> added to the BioMed Central publication system.
>
> The [BioMed Central
> homepage](http://blogs.openaccesscentral.com/blogs/bmcblog/entry/additional_material_gets_additional_features)
> offers instructions for uploading these <span
> class="spCh spChx2018">‘</span>mini-websites<span
> class="spCh spChx2019">’</span> as a ZIP file. Readers of the
> published article will have a choice of whether to download the ZIP
> file to view locally on their own machine, or alternatively they can
> follow a link to view the contents of the ZIP file via the BioMed
> Central website...
>
> <http://www.firstauthor.org/blog/?p=159>

There's a link there to an article about butterflies, with some extra
material in HTML.

This sounds like something that [ICE](http://ice.usq.edu.au/) could do
really well. ICE has lets you create <span
class="spCh spChx201c">“</span>mini-websites<span
class="spCh spChx201d">”</span> complete with internal navigation with
an export to ZIP. The ZIP files exported by ICE are actually IMS
packages, designed to slot into learning management systems, but they
work as stand alone websites. You can see
[examples](http://ocw.usq.edu.au/course/view.php?id=7) at the USQ open
courseware site, see the automatically generated navigation at the left?
This could be a good way to package materials. You can tie just about
anything together into a package using ICE, and we're working hard right
now to make sure that there are tools to help embed data visualizations
into documents as seamlessly as possible.

I'm working on a paper at the moment about exporting HTML from word
processors. One of the things I've been doing is [documenting some of
the issues with the built-in HTML
export](http://del.icio.us/ptsefton/xhtmlchallenge) in widely available
software pacakages. I was just going to link to the blog, but one idea
would be to include all these blog posts and a set of sample documents
as a package to go along with the paper. Whether or not a publisher
would be set up to take it is another matter.

Another packaging mechanism that might be useful given tools to support
it would be METS pacakages. We saw first hand at our [repository interop
workshop](http://ice.usq.edu.au/blog/?p=105) how APSR developed an
Australian METS profile for packaging journals, to enable automated
depost from a journal management system into a repository. But who knows
how to make a METS package? Apart from geeks like the ICE team, or some
speical repository-rats[<span style="vertical-align: super;"><span
class="footnote">1</span></span>](#ftn0), that is. BioMed Central's
choice of ZIP is sensible. No fancy metadata required, just make sure
your ZIP has an entry point named index.html. But it could do more if it
knew how to deal with IMS content packages or a METS profile as well.

> To submit such a 'mini-website' as an additional material file, all
> you need to do is to ensure that the homepage is named index.html, and
> sits in the root folder of the content you wish to submit. Then
> convert the folder hierarchy into a ZIP archive, and upload this ZIP
> file using the regular manuscript submission system, which will
> recognize and process it automatically. Full guidelines are provided
> in each journal's Instructions for Authors (example).
>
> <http://blogs.openaccesscentral.com/blogs/bmcblog/entry/additional_material_gets_additional_features>

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote">[1](#ftn0-text) Dorothea Salo, <span
class="spCh spChx201c">“</span>A Messy Metaphor,<span
class="spCh spChx201d">”</span> *Caveat Lector* , Blog, January 9, 2006,
http://cavlec.yarinareth.net/archives/2006/01/09/a-messy-metaphor/</span>

</div>

</div>

</div>
