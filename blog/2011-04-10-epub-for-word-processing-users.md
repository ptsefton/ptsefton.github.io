---
Author: ptsefton
Comments: false
Date: 2011-04-10 22:46:29+00:00
Slug: epub-for-word-processing-users

Title: EPub for word processing users
Wordpress_id: 715
---

<div>

<div class="page-toc">

-   [<span>Summary</span>](#id2)
-   [<span>Initial impressions</span>](#id4)
-   [<span>Demonstration software</span>](#id5)
-   [<span>Where next?</span>](#id7)
-   [<span>Lessons learned</span>](#id9)

</div>

<div>

[This is a repost of [<span
class="Hyperlink">http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/) -
if you have comments please make them [<span class="Hyperlink">over on
there on the jiscPUB
blog</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/).]

<div class="Table3"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------------------+--------------------------------------+
| Author:                              | <p>                                  |
|                                      | <span                                |
|                                      | rel="http://purl.org/dc/elements/1.1 |
|                                      | /creator"                            |
|                                      | resource="http://trove.nla.gov.au/pe |
|                                      | ople/541658"><span                   |
|                                      | property="http://xmlns.com/foaf/0.1/ |
|                                      | name"                                |
|                                      | resource="http://trove.nla.gov.au/pe |
|                                      | ople/541658">[<span                  |
|                                      | class="Internetlink">Peter           |
|                                      | Sefton</span>](http://ontologize.me/ |
|                                      | ?tl_p=http://purl.org/dc/terms/creat |
|                                      | or&triplink=http://purl.org/triplink |
|                                      | /v/0.1&tl_o=http://trove.nla.gov.au/ |
|                                      | people/541658)</span></span>         |
|                                      | \<                                   |
|                                      | <script type="text/javascript">      |
|                                      | <!--                                 |
|                                      | h='&#112;&#116;&#x73;&#x65;&#102;&#1 |
|                                      | 16;&#x6f;&#110;&#46;&#x63;&#x6f;&#x6 |
|                                      | d;';a='&#64;';n='&#112;&#116;';e=n+a |
|                                      | +h;                                  |
|                                      | document.write('<a h'+'ref'+'="ma'+' |
|                                      | ilto'+':'+e+'" clas'+'s="em' + 'ail" |
|                                      | >'+'<span class="Internetlink">pt@pt |
|                                      | sefton.com</span>'+'<\/'+'a'+'>');   |
|                                      | // -->                               |
|                                      | </script>                            |
|                                      | <noscript>                           |
|                                      | \<span                               |
|                                      | class="Internetlink"\>pt@ptsefton.co |
|                                      | m\</span\>                           |
|                                      | (pt at ptsefton dot com)             |
|                                      | </noscript>                          |
|                                      | \>                                   |
|                                      | </p>                                 |
+--------------------------------------+--------------------------------------+
| Date:                                | Time-stamp: \<2011-04-05 15:38:38\>  |
+--------------------------------------+--------------------------------------+
| Description:                         | First informal report on progress    |
|                                      | with [<span                          |
|                                      | class="Internetlink">Workpackage     |
|                                      | 3</span>](http://jiscpub.blogs.edina |
|                                      | .ac.uk/2011/03/03/workpackage-3/).   |
|                                      | Looks at tools for turning word      |
|                                      | processing documents such as         |
|                                      | Microsoft Word documents into epub.  |
+--------------------------------------+--------------------------------------+

</div>

# <span id="id2"></span><span></span></a>Summary

Last week I started on the JISCPub project on [<span
class="Internetlink">workpackage
3</span>](http://jiscpub.blogs.edina.ac.uk/2011/03/03/workpackage-3/).
My role on this project is to be the <span
class="spCh spChx201c">“</span>Wordprocessing Tool Expert<span
class="spCh spChx201d">”</span>.

I started by considering the first use case, seeing how a PhD thesis
could be converted to EPUB for mobile use. I happen to have a very
worthy test file in the form of Danny Kingsley's Creative Commons
Licensed: <span class="spCh spChx201c">“</span>The effect of scholarly
communication practices on engagement with open access: Australian study
of three disciplines<span class="spCh spChx201d">”</span> from 2008.

I am working three kinds of deliverable:

-   Blog reports. This is the first.

-   Demonstration software <span class="spCh spChx2013">–</span> I have
    produced a simple demo that can covert word documents into EPUB
    files <span class="spCh spChx2013">–</span> you [<span
    class="Internetlink">try it
    out</span>](http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/odt),
    assuming you can work out how, or read on for more background about
    the service, how raw it is, excuses about its somewhat agricultural
    interface and the fact that it might not work very well yet.

-   Demonstration files showing the results of various processes. I have
    set up a dropbox.com folder for the project team, where I will be
    keeping records of the experiments I'm doing with various bits of
    software. This will be available as a data set at the end of the
    project. One demo is this post, formatted as an EPUB file <span
    class="spCh spChx2013">–</span> using the tool I discuss below. I
    tried to upload it to WordPress but it does not meet security
    requirements, you can [<span>grab the post in EPUB format from
    here</span>](http://dl.dropbox.com/u/24994372/JISCPub-wpack3-post1.epub).
    Comments welcome <span class="spCh spChx2013">–</span> this is a
    test process only.

# <span id="id4"></span><span></span></a>Initial impressions

I started this investigation by assuming that I had a thesis I wanted to
publish as an ebook, via EPUB and doing various Google searches for
stuff like <span class="spCh spChx201c">“</span>How to make an EPUB<span
class="spCh spChx201d">”</span>. Theo Andrew is going to talk to some
real users about this soon <span class="spCh spChx2013">–</span> so
we'll find out a lot more about what kinds of assumptions are valid to
make about our users, graduate students and academics.

There are some sites which review software, notably [<span
class="Internetlink">Jedisaber's</span>](http://www.jedisaber.com/eBooks/tutorial.asp),
which has reviews of many software packages related to EPUB and ebooks
in general, and a how-to on making an EPUB from scratch, by hand. I have
been trying out various bits of software against the uses cases for this
project <span class="spCh spChx2013">–</span> without a great deal of
success <span class="spCh spChx2013">–</span> and I will document this
behind the scenes and save input and output documents as part of the
data set for this project.

As it says in the plan for this workpackage the most obvious bit of
software to try out is [<span
class="Internetlink">Calibre</span>](http://calibre-ebook.com/) which is
a mature open source ebook management application available for all the
major platforms. Calibre is a very feature-rich application with a
somewhat quirky interface which doesn't do the one thing I wanted for my
first experiment. It doesn't convert Microsoft Word .doc files into
`.epub` format. Yes, you can deal with Word docs by doing a 'Save as
HTML' but that's not the ideal process for casual users. Calibre does do
open document format (`.odt`) files, though, so I tried that with
Danny's thesis, using open office to save it as `.odt`, after some minor
tweaking in OpenOffice. I found that:

-   On large files like the thesis it takes around 100-200 minutes to
    convert the document, in the background, using the GUI on my modest
    desktop PC.

-   Some graphics are not supported, for example embedded vector
    drawings. I don't think there's a good solution for this that does
    not involve firing up a word processor to render some things <span
    class="spCh spChx2013">–</span> I will come back to this in a future
    post on the current (terrible) state of the art in Word processor to
    HTML conversion, and what could be done about it.

(I am wondering if the speed of Calibre is the reason I never heard back
from the odt2ebook.com site, which offered free conversions; there was
supposed to be an email notification but it has been a few days.)

# <span id="id5"></span><span></span></a>Demonstration software

After about half a day of investigation, It became clear that there was
a big crater in the ebook software landscape. There is no obvious way to
make an ebook from a Word document. Yes there are a some word processing
packages which will do it, but nothing simple or online. Liza Daly <span
class="spCh spChx2013">–</span> the ebook expert on this project
confirmed this so I set out to at least try to fill that gap. My
starting point was the [<span
class="Internetlink">ICE</span>](http://ice.usq.edu.au/) software I
established at the [<span class="Internetlink">University of
Sout</span><span class="Internetlink">hern
Queensland</span>](http://www.usq.edu.au/), where I worked until very
recently Over the years this has evolved into a very capable word
processing format converter for the web. It is mainly designed to work
with documents with a known input format, using its own set of styles,
but it can also deal with generic documents with standard headings. It
already had some EPUB export but only for collections of documents, not
for a single word processing file via a simple web service.

The idea was to use ICE to generate HTML then write code to break it up
and store it a zip file, EPUB style. ICE does a reasonable job of
converting the test thesis to HTML by looking for standard heading
styles (Heading 1 .. n) and guessing that 'Quote' is a style for
quotations. There are no widely used standards for word processing
styles, so some heuristics are required; the current ICE code does not
do a lot of this, but it could be extended.

What I did was:

-   Looked at building on work already in ICE and other USQ software
    that makes EPUB files. I got something running, but in the process
    of developing it, I discovered the command line features in Calibre
    were probably a better option.

-   Set up a possibly temporary [<span class="Internetlink">code
    repo</span><span class="Internetlink">sitory at Google
    Code</span>](http://code.google.com/p/integrated-content-environment/source/checkout)
    and checked in the latest trunk of ICE.

-   Added simple code to the ICE conversion service to [<span
    class="Internetlink">call
    Calibr</span>](http://calibre-ebook.com/user_manual/cli/ebook-convert-3.html#html-input-to-epub-output)e
    on the ICE-generated HTML. The command currently looks like this.

    `ebook-convert "/tmp/ICE-u6hayU.ice/Kingsley-Formatted PhD 12May09.htm" "/tmp/ICE-u6hayU.ice/Kingsley-Formatted PhD 12May09.epub"  --chapter "//*[name()='h1']"  --level1-toc "//*[name()='h1']" --level2-toc "//*[name(``)='h2']" --title "The effect of scholarly communication practices on engagement " --authors "" --publisher "" --pubdate ""  `

-   Using Word docs there are some problems, like the way the title is
    truncated above, and other metadata is missing. I'll come back to
    metadata in a future post making sure that works are correctly
    described and labelled is an important dimension of scholarship. I
    see metadata as a gateway feature (as in gateway drug) for improving
    the semantic content of documents in general and I think once people
    see the power of embedding metadata semantics in their documents
    <span class="spCh spChx2013">–</span> so they don't have to retype
    stuff all the time <span class="spCh spChx2013">–</span> they'll be
    ready to deal with citations and rhetorical structure, and
    domain-specific semantics.

-   Set up a [<span class="Internetlink">test/demo server in Amazon's
    cloud
    services</span>](http://ec2-50-16-170-243.compute-1.amazonaws.com/api/convert/odt).
    Here's [<span>Danny's thesis as rendered by the
    service</span>](http://dl.dropbox.com/u/24994372/test-2011-04-05-Kingsley-Formatted_PhD_12May09.epub).
    The input document was a word document, the output is a EPUB file.
    It takes about ten minutes to create.

    -   Try it out with a couple of sample files (these might change
        during the project as we get more ambitious) by uploading the
        documents into the service or pasting the URL into the form.

        -   A word document using a sample thesis template from the
            University of Edinburgh:
            [<span>http://dl.dropbox.com/u/24994372/thesis-test-document.doc</span>](http://dl.dropbox.com/u/24994372/thesis-test-document.doc)

        -   An ICE-version of the same thing in OpenDocument form using
            the ICE style-set with a few more examples of formatting,
            such as bullets and pre-formatted text.
            [<span>http://dl.dropbox.com/u/24994372/test-thesis-ice-styles.odt</span>](http://dl.dropbox.com/u/24994372/test-thesis-ice-styles.odt)

The test service uses ICE to convert .doc and .odt documents to HTML
<span class="spCh spChx2013">–</span> you can feed it generic documents
using Heading styles and it will do its best. ICE deals with all sorts
of images and maths etc., it does a better job than most processors
because it uses the OpenOffice.org word processor to create images using
its rendering engine <span class="spCh spChx2013">–</span> most tools
can't deal with some kinds of content because they can't render them.
Then the service calls Calibre's HTML to EPUB conversion tools. To start
with I coded this to treat `<h1>` elements in the HTML as the major
sections in the document. This contrasts with the way Calibre attempts
to generate HTML directly from the `.odt `file, which means that lots of
graphics won't be able to be rendered at all.

Status:

-   Alpha code only.

-   Might break.

-   Slow (circa 5 minutes for a big document, though, not 100-ish)

-   I will endeavour to keep this up and running for the life of this
    project.

Later in the project I plan to work with Theo and his focus group users
to see whether the ICE approach for styles is viable for thesis
production and for the various other use cases. Other questions include:

1.  Should long documents such as theses be managed as multiple parts or
    single documents?

2.  What's the demand for being able to integrate other kinds of
    resources (spreadsheets, images, other data like chemistry) and are
    there viable ways to embed this stuff in EPUB documents? The
    question here is whether EPUB is suitable for the 'research object
    of the future' where publications are not just documents, but need
    to be embedded in or carry-around more of their context.

3.  Should we be thinking about EPUB converters as part of repository
    deposit processes?

Known issues with the ICE/EPUB generator:

-   Sometimes he first section of the document appears in the TOC as
    'unnamed'. I don't want to resort to hacks like adding a heading
    called 'frontmatter' to the document, but I might.

-   I have been focussing initial testing on the Firefox addon for EPUB:
    [<span
    class="Internetlink">https://addons.mozilla.org/en-us/firefox/addon/epubreader/</span>](https://addons.mozilla.org/en-us/firefox/addon/epubreader/)
    more testing and validation required (this goes for all the tools I
    have been looking at.)

# <span id="id7"></span><span></span></a>Where next?

Potential next steps include:

-   Improving and glamorising the test conversion service.

-   Creating new calibre plugin to use ICE as an HTML generator <span
    class="spCh spChx2013">–</span> this could be used to add Word
    support, and potentially improve Open Document support.

# <span id="id9"></span><span></span></a>Lessons learned

Even if you start from good quality HTML, writing an automated tool for
creating EPUB is likely to be quite a big job. Calibre already does it,
has lots of configuration options and seems to be a good starting point
for a conversion tool <span class="spCh spChx2013">–</span> I'm
interested in comments about this though. A couple of days of my own
coding didn't get me close to what I could do with Calibre in about an
hour learning what command-line options to use (there were several hours
spent refining the initial options, though). And it's not just me,
others of the staff at USQ have spent a fair bit of time getting basic
EPUB support working; the one thing that makes me think it might be
worth tackling is the glacial speed of Calibre <span
class="spCh spChx2013">–</span> but that might just be because Calibre
is doing all sorts of important things and a new converter could be just
as slow.

[This is a repost of [<span
class="Hyperlink">http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/) -
if you have comments please make them [<span class="Hyperlink">over on
there on the jiscPUB
blog</span>](http://jiscpub.blogs.edina.ac.uk/2011/04/05/epub-for-word-processing-users/).]

Copyright Peter Sefton, <span
rel="http://purl.org/dc/elements/1.1/date">[<span
class="Internetlink">20</span><span
class="Internetlink">11</span>](http://ontologize.me/?tl_p=http://purl.org/dc/terms/date&triplink=http://purl.org/triplink/v/0.1)</span>.
Licensed under Creative Commons Attribution-Share Alike 2.5 Australia.
\<[<span
class="Internetlink">http://creativecommons.org/licenses/by-sa/2.5/au/</span>](http://creativecommons.org/licenses/by-sa/2.5/au/)\>
<span rel="http://purl.org/dc/elements/1.1/publisher"
resource="http://ptsefton.com/"><span
property="http://xmlns.com/foaf/0.1/name"
resource="http://ptsefton.com/">[<span class="Internetlink">Published by
http://ptsefton.com</span>](http://ontologize.me/?tl_p=http://purl.org/dc/terms/publisher&triplink=http://purl.org/triplink/v/0.1&tl_o=http://ptsefton.com/)</span></span>

<span
class="DefaultParagraphFont"><a name="graphics1"><span></span></a>![](/wp-content/uploads/2011/04/m40ca94ba.png)</span>

This post was written in OpenOffice.org, using templates and tools
provided by the [<span class="Internetlink">In</span><span
class="Internetlink">tegrated Content
Environment</span>](http://ice.usq.edu.au/) project and published to
WordPress.

</div>

</div>
