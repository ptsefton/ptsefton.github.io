---
Author: ptsefton
Comments: true
Date: 2009-12-23 00:42:29+00:00
Slug: bye-bye-word-2007-custom-xml

Title: Bye Bye Word 2007 Custom XML ?
Wordpress_id: 478
---

<div>

<div class="page-toc">

</div>

<div>

I have argued here repeatedly that building applications using Microsoft
Word's Custom XML feature is a spectacularly bad idea, but it turns out
that I missed the best reason of all not to use custom XML: **It may
well be going away very soon**, because, I gather, [it infringed
someone's patent](http://blogs.zdnet.com/microsoft/?p=4835). In reaction
to this news, [Tim Bray is reiterating his case that rolling your own
XML is a bad
idea](http://www.tbray.org/ongoing/When/200x/2009/12/22/On-Custom-XML):

> People like me, who had experience with the extreme difficulty of
> doing this kind of customization, the extremely limited number of
> places where it made sense, and the high proportion of failure among
> people who tried to do it, shouted <span
> class="spCh spChx201c">“</span>That<span
> class="spCh spChx2019">’</span>s a bug!<span
> class="spCh spChx201d">”</span> Given that the number of organizations
> that deploy Office is huge, I bet Microsoft can trot out a few
> customers who<span class="spCh spChx2019">’</span>ve got good results
> with Custom XML. But I also bet that, first of all, the proportion who
> try is tiny and, second, that among those who do, few succeed in
> getting much business value.

I'm one of these people like Tim and like him, I told you so. Let's
revisit some of this:

-   [Earlier this year I agreed with Glyn Moody that using custom
    XML](http://ptsefton.com/2009/03/16/opening-up-microsoft.htm) in a
    collaboration between Science Commons and Microsoft was promoting
    lock-in to Word 2007 and later versions. If the feature is removed
    from future versions then would MS Research like to consider the
    [suggestion I made in
    Marc](http://ptsefton.com/2009/03/27/more-on-microsoft-collaboration-and-word-processor-interop.htm)h
    to embed ontological annotations using links. The ontology plugin in
    question used the simplest of schemas, so simple that there was
    really no need for custom XML at all.

-   I have also expressed doubts about the usefulness of a more
    complicated plugin that also comes out of Microsoft Research;
    [Article Authoring Add-in for Microsoft Office Word
    2007](http://www.microsoft.com/downloads/details.aspx?familyid=09c55527-0759-4d6d-ae02-51e90131997e).
    This was supposed to let you author documents that were complaint
    with the complex NLM document Schema using Word. Again, it would
    have worked to lock documents to Word 2007 but I also found it to be
    pretty well unusable, and having seen a few of these classes of
    application over the years I didn't give it much chance of survival
    in the wild. Now, I guess its future is in doubt, and I'd still love
    to find the resources to try NLM authoring using the ICE system or a
    similar style-based system. I'm assuming that MS won't be under an
    injunction to drop styles support any time soon, although they
    have[done their best to bury them under the new user interface and
    make it less likely that people will use
    them](http://ptsefton.com/blog/2006/12/01/dont-bury-styles/).

-   I counselled my colleagues at Cambridge working on the
    [Chem4Word](http://research.microsoft.com/en-us/projects/chem4word/)plugin
    to be cautious, citing lock-in, usability and maintainability. I
    wonder if they have heard anything about what might happen to this
    tool now? (I still think the best approach would be to use OLE to
    embed the chemical editor and simple features like links, fields and
    styles for the rest, which would mean that the tool could
    interoperate between different word processors including older
    versions of Word).

So, if Microsoft is going to pull Custom XML out of Word, at least in
the USA, then I was right, it was a trap, it just turned out to have
even nastier teeth than I thought. Now, I'd be really happy to have our
group help any creators open source academic word processor plugins that
have been snared. We're happy to share our experience on how to build
interoperable, simple, robust authoring tools.

Copyright Peter Sefton, 2009. Licensed under Creative Commons
Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

[![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2009/12/m40ca94ba.png)](http://creativecommons.org/licenses/by-sa/2.5/au/)

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>
