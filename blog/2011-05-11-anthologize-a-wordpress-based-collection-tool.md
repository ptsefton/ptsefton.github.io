---
Author: ptsefton
Comments: false
Date: 2011-05-11 09:02:02+00:00
Slug: anthologize-a-wordpress-based-collection-tool
Category: jiscPUB
Title: 'Anthologize: a WordPress based collection tool'
Wordpress_id: 801
---

<div>

<div class="page-toc">

</div>

<div>

[This is a copy of a post on the jiscPUB project <span
class="spCh spChx2013">–</span> if you have comments please do so over
there:
[<span>http://jiscpub.blogs.edina.ac.uk/2011/05/11/anthologize-a-wordpress-based-collection-tool/</span>](http://jiscpub.blogs.edina.ac.uk/2011/05/11/anthologize-a-wordpress-based-collection-tool/)]
In this post I’ll look at
[<span>Anthologize</span>](http://anthologize.org/). Anthologize lets
you write or import content into a WordPress instance, organise the
‘parts’ of your ‘project’ and publish to PDF or EPUB, HTML or into TEI
XML format. This is what I referred to in my last post [<span>about
WordPres</span>](http://ptsefton.com/2011/05/11/wordpress-and-the-jiscpub-project.htm)s
as an aggregation platform.
# <span id="id2"></span></a>Anthologize background and use-cases

Anthologize was created in an interesting way. It is the (unfinished as
yet) outcome of a one-week workshop conducted at the Centre for History
and New Media <span class="spCh spChx2013">–</span> the same group that
brought us Zotero and Omeka, which is one good reason to take it
seriously. They produce very high quality software.
> <span class="Strong_20_Emphasis"><span
> style="background-color:transparent; color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T2">Anthologize</span></span></span><span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3"> is a project of </span></span>[<span
> style="background-color:transparent; color:#25589a; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none; "><span
> class="T4">One Week | One
> Tool</span></span>](http://www.oneweekonetool.org/)<span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3"> a project of the </span></span>[<span
> style="background-color:transparent; color:#25589a; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none; "><span
> class="T4">Center for History and New
> Media</span></span>](http://chnm.gmu.edu/)<span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3">, </span></span>[<span
> style="background-color:transparent; color:#25589a; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none; "><span
> class="T4">George Mason
> University</span></span>](http://www.gmu.edu/)<span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3">. Funding provided by the National Endowment for the
> Humanities. <span class="spCh spChxa9">©</span> 2010, Center for
> History and New Media. For more information,
> contact </span></span><span class="Strong_20_Emphasis"><span
> style="background-color:transparent; color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T2">infoATanthologizeDOTorg</span></span></span><span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3">. Follow </span></span>[<span
> style="background-color:transparent; color:#25589a; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-decoration: line-through; text-decoration: underline; text-transform:none; "><span
> class="T4">@anthologize</span></span>](http://www.twitter.com/anthologize)<span
> style="color:#333333; font-size:11pt; font-style:normal; font-variant:normal; font-weight:normal; letter-spacing:normal; text-transform:none; "><span
> class="T3">.</span></span>

Anthologize is a WordPress plugin that adds import and organisation
features to WordPress. You can author posts and pages as normal, or you
can import anything with an RSS/Atom feed. The imported documents don’t
seem to be able to be published for others to view but you can edit them
locally. This could be useful <span class="spCh spChx2013">–</span> but
introduces a whole lot of management issues around provenance and
version control. When you import a post from somewhere else the images
stay on the other site, so you have a partial copy of the work with
references back to a different site. I can see some potential problems
with that if other sites go offline or change.

Let’s remind ourselves about the use-cases in [<span>workpackage
3</span>](http://jiscpub.blogs.edina.ac.uk/2011/03/03/workpackage-3/):

> The three main use cases identified in the current plan, and a fourth
> proposed one: [numbering added for this post]
>
> 1.  Postgrad serializing PhD (or conference paper etc) for mobile
>     devices
> 2.  Retiring academic publishing their <span
>     class="spCh spChx2018">‘</span>best-of<span
>     class="spCh spChx2019">’</span> research (books)
> 3.  Present final report as epub
> 4.  Publish course materials as an eBook (Proposed extra use-case
>     proposed by Sefton)
>
> [<span>http://jiscpub.blogs.edina.ac.uk/2011/03/03/workpackage-3/</span>](http://jiscpub.blogs.edina.ac.uk/2011/03/03/workpackage-3/)

Many documents like (a) theses or (c) reports are likely to be written
as monolithic documents in the first place, so it would be a bit strange
to write, say, a report in Word, or LaTeX or asciidoc (which is how I
think Liza Daly will go about writing the landscape paper for this
project) , export that as a bunch of WordPress posts for dissemination,
then reprocess back into an Anthologize project, and then to EPUB.
There’s much more to go wrong with that, and information to be lost than
going straight from the source document to EPUB. It is conceivable that
this would be a good tool for thesis by publication, where the
publications were available as HTML that could be fed or pasted in to
WordPress.

I do see some potential with (d) courseware here <span
class="spCh spChx2013">–</span> it seems to me that it might make sense
to author course materials in a blog-post like way covering topics one
by one. I have put some feelers out for someone who might like to test
publishing course materials, without spending too much of this project’s
time as this is not one of the core use cases. If anyone wants to try
this or can point me to some suitable open materials somewhere with
categories and feeds I can use then I will give it a go.

There is also some potential with (c), project reports, particularly if
anyone takes up the [<span>JiscPress</span>](http://jiscpress.org/) way
of doing things and creates their project outputs directly in
WordPress+digress.it. It would also be ideal for compiling stuff that
happens on the project blog as a supporting Appendix. So, an EPUB that
gathers together, say all the blog posts I have made on WorkPackage 3 or
the whole of the jiscPUB blog might make sense. These could be
distributed to JISC and stakeholders as EPUB documents to read on the
train, or deposited in a repository.

The retiring academic (b) (or any academic really) might want to make
use of Anthologize too <span class="spCh spChx2013">–</span>
particularly if they’ve been publishing online. If not they could paste
their works into WordPress as posts, and deal with the HTML conversion
issues inherent in that, or try to post from Word to WordPress. The test
project I chose was to convert the blog posts I have done for jiscPUB
into an EPUB book. That’s use case (c) more or less.

# <span id="id3"></span></a>How did the experiment go?

I have documented the basic process of creating an EPUB using
Anthologize below, with lots of screenshots, but here is a summary of
the outcomes. Some things went really well.
-   Using the control panel at my web host I was able set up a new
    WordPress website on my domain, add the Anthologize plugin and make
    my first EPUB in well under an hour. (But as usual, it takes a lot
    longer to back-track and investigate and try different options, and
    read the google group to see if bugs have been reported and so on).
-   The application is easy to install and easy to use <span
    class="spCh spChx2013">–</span> with some issues I note below.
-   Importing a feed just works if you search to find out how to do it
    on a standard WordPress host (although I think there might be issues
    trying to get large amounts of content if the source does not
    include everything in the feed).
-   Creating parts and dragging in content is simple.
-   Anthologize *looks* good.

The good looks and simple interface are deceptive, lots of functionality
I was expecting to be there just wasn’t <span
class="spCh spChx2013">–</span> yet. I have been in contact with the
developers and noted my biggest concerns, but here’s a list of the major
issues I see with the product at this stage of its development:
-   There does not seem to be a way to publish the project (or the
    imported docs) directly to the web <span
    class="spCh spChx2013">–</span> rather than export it. Seems like an
    obvious win to add that. I can see that being really useful with
    Digress.it for one thing. The other big win there would be if the
    Table of Contents could have some semantics embedded in it so it
    could act like an ORE resource map – meaning that machines would be
    able to interpret the content. (I will come back to this idea soon
    with a demo of using Calibre to make an EPUB)
-   There are no TOC entries for the posts within a ‘part’ that is, if
    you pull in a lot of WordPress posts, they don’t get individual
    entries in the EPUB ToC.
-   Links, even internal ones, like the table of contents links on my
    posts all point back to the original post <span
    class="spCh spChx2013">–</span> this makes packaging stuff up much
    less useful <span class="spCh spChx2013">–</span> you’d need to be
    online, and you lose the context of an intra-linked resource.
    [<span>This is a known
    problem</span>](http://anthologize.org/trac/ticket/106), and the
    developers say they are going to fix it.
-   Potentially a problem is the way Anthologize EPUB export puts all
    the HTML content for the whole project into one HTML file <span
    class="spCh spChx2013">–</span> I gather from poking around with
    Calibre etc that many book readers need their content chunked into
    multiple files.
-   There’s a wizard for exporting your EPUB, and you can enter some
    metadata and choose some options <span
    class="spCh spChx2013">–</span> all of which is immediately
    forgotten by the application, so if you do it again, you have to
    re-enter all the information.
-   Epubcheck complains about the test book I made:
    -   It says the mimetype (a simple file that MUST be there in all
        EPUB) is wrong <span class="spCh spChx2013">–</span> looks OK to
        me.
    -   It complains about the XHTML containing stuff from the TEI
        namespace and a few other things.
-   Finally, PDF export fails on my blog with a timeout error <span
    class="spCh spChx2013">–</span> but that’s not an issue for this
    investigation.

# <span id="id5"></span></a>Summary

For the use case of bundling together a bunch of blog posts (or anything
that has a feed) into a curated whole Anthologize is a promising
application, but unless your needs are very simple it’s probably not
quite ready for production use. I spent a bit of time looking at it
though, as it shows great promise and comes from a good stable. Here’s
the result I got importing the first handful of posts from my work on
this project.
<span
style="display: block">![graphics8](/wp-content/uploads/2011/05/39b75480_643x345.jpeg)</span>Illustration
1: The test book in Adobe Digital Edtions – note some encoding problems
bottom right and the lack of depth in the table of contents. There are
several posts but no way to navigate to them. Also, clicking on those
table of contents links takes you back to tbe jiscPUB blog not to the
heading.

# <span id="id6"></span></a>Walk through

<span
style="display: block">![graphics1](/wp-content/uploads/2011/05/5eb1e9cf.png)</span>Illustration
2: Anthologize uses ‘projects’. These are aggregated resources, in many
cases they will be books but project seems like a nice media-neutral
term.

<span
style="display: block">![graphics2](/wp-content/uploads/2011/05/m45bc0c57_643x257.jpeg)</span>Illustration
3: A new project in a fresh WordPress install <span
class="spCh spChx2013">–</span> only two things can be added to it until
you write or import some content.

<span
style="display: block">![graphics3](/wp-content/uploads/2011/05/m4c92efc2_643x192.jpeg)</span>Illustration
4: Importing the feed for workpackage 3 in the jiscPUB project.
http://jiscpub.blogs.edina.ac.uk/category/workpackage-3/feed/atom/

<span
style="display: block">![graphics4](/wp-content/uploads/2011/05/m6c4a7bd6_643x301.jpeg)</span>Illustration
5: You can select which things to keep from the feed. Ordering is done
later. Remember that imported documents are copies, so there is
potential for confusion if you edit them in Anthologize.

<span
style="display: block">![graphics5](/wp-content/uploads/2011/05/48fc7a8b_643x472.jpeg)</span>Illustration
6: Exporting content is via a wizard, easy to use but frustrating
becuase it asks some of the same questions every time you export.

<span
style="display: block">![graphics6](/wp-content/uploads/2011/05/m38722fbe_643x480.jpeg)</span>Illustration
7: Having to retype the export information is a real problem as you can
only export one format at a time. Exported material is not stored in the
WordPress site, either, it is downloaded, so there is no audit trail of
versions. [This is a copy of a post on the jiscPUB project <span
class="spCh spChx2013">–</span> if you have comments please do so over
there:
[<span>http://jiscpub.blogs.edina.ac.uk/2011/05/11/anthologize-a-wordpress-based-collection-tool/</span>](http://jiscpub.blogs.edina.ac.uk/2011/05/11/anthologize-a-wordpress-based-collection-tool/)]

Copyright <span rel="http://purl.org/dc/elements/1.1/creator"
resource="http://trove.nla.gov.au/people/541658"><span
property="http://xmlns.com/foaf/0.1/name"
resource="http://trove.nla.gov.au/people/541658">Peter
Sefton</span></span>, 2011-05-04. Licensed under <span
rel="http://creativecommons.org/licence">Creative Commons
Attribution-Share Alike 2.5 Australia</span>.
\<http://creativecommons.org/licenses/by-sa/2.5/au/\>

<span class="Default_20_Paragraph_20_Font"><span
style="country:US; language:en; "><span
class="T1">![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2011/05/m40ca94ba2.png)</span></span></span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span>Integrated Content
Environment</span>](http://ice.usq.edu.au/) project.

</div>

</div>
