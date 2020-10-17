---
Author: ptsefton
Comments: true
Date: 2013-02-05 03:25:49+00:00
Slug: putting-data-on-the-web
Category: ScholarlyHTML
Title: Putting data on the web
Wordpress_id: 1660
---

<article>
<section>
I attended this [data
newsroom](http://www.eventbrite.com/event/4900494511) (\#datanews) event
in Melbourne Monday Feb 3^rd^ [Correction - it was the 4th] 2013. David
Flanders asked me to come prepared to give a talk on tools and
techniques for embedding data into web pages, particularly using
Schema.org, the corporate sponsored ontology of everything that matters
for commerce.

So here are my semantically rich[^[i]^](#_edn1) notes for the
presentation. This is neither a tutorial nor a coherent story, so you
may want to leave now, but there is a picture of Tim Berners-Lee about
half way through.

<section typeof="http://purl.org/ontology/bibo/Slide">
#### Why embed data in web pages?

You can make new things happen. Let other people or machines do things
with the data. [Here’s an example by Tim
Sherratt](http://wraggelabs.com/shed/presentations/ndf2012/storydata/)
showing how data embedded in the page (left) can drive new behaviour
(the stuff on the right).

![](/wp-content/uploads/2013/02/wpid-putting-data-copy.html.html_putting-data-copy_filesimage0021.png)

</section>
<section typeof="http://schema.org/" vocab="http://schema.org/">
#### What is this Schema.org?

(I have added a couple of tags to discuss later)

> Many sites are generated from structured data, which is often stored
> in databases. When this data is formatted into HTML, it becomes very
> difficult to recover the original structured data. Many applications,
> especially search engines, can benefit greatly from direct access to
> this structured data. On-page markup **[\#inlinedata]** enables search
> engines to understand the information on web pages and provide richer
> search results in order to make it easier for users to find relevant
> information on the web. Markup **[\#semanticsyntax]** can also enable
> new tools and applications that make use of the structure.
>
> A shared markup vocabulary **[\#sharedvocab]** makes it easier for
> webmasters to decide on a markup schema and get the maximum benefit
> for their efforts. So, in the spirit of sitemaps.org, search engines
> have come together to provide a shared collection of schemas that
> webmasters can use.
>
> http://schema.org/

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
#### Use Schema.org – get snippets

![](/wp-content/uploads/2013/02/wpid-putting-data-copy.html.html_putting-data-copy_filesimage0041.png)

</section>
The point of this, for the vast majority of web practitioners is to get
into the world of ‘rich snippets’. If you use the schema.org way then
you get ‘better’ search results – but you’re also allowing the search
engines, and anyone else who views your page to use the data. Right now
if I search for movie times at my local cinema I enter a Google-trap
which shows me films and when they’re on with no link to the cinema site
itself. It’s also hard to tell what role Schema.org plays in all these
search engine things – some of the data you see is harvested using older
conventions for data services and who knows, maybe the cinemas just give
Google a spreadsheet with the movie times in it.

For data journalism and research, we presumably want to get the data out
in a form that it can be reused so the concerns are different – you want
the data to be used, and your part in its collection or creation to be
cited.

<section typeof="http://purl.org/ontology/bibo/Slide">
#### The other thing you need to know about: RDF

RDF is the Resource Description Framework.

> The<span class="apple-converted-space"> </span>**Resource Description
> Framework**<span class="apple-converted-space"> </span>(**RDF**) is a
> family of<span class="apple-converted-space"> </span>[World Wide Web
> Consortium](http://en.wikipedia.org/wiki/World_Wide_Web_Consortium "World Wide Web Consortium")<span
> class="apple-converted-space"> </span>(W3C)[specifications](http://en.wikipedia.org/wiki/Specification "Specification")<span
> class="apple-converted-space"> </span>[^[1]^](http://en.wikipedia.org/wiki/Resource_Description_Framework#cite_note-1)<span
> class="apple-converted-space"> </span>originally designed as a<span
> class="apple-converted-space"> </span>[metadata](http://en.wikipedia.org/wiki/Metadata "Metadata")<span
> class="apple-converted-space"> </span>[data
> model](http://en.wikipedia.org/wiki/Data_model "Data model"). It has
> come to be used as a general method for conceptual description or
> modeling of information **[\#sharedvocabularies]** that is implemented
> in web resources, using a variety of syntax formats
> **[\#semanitcsyntax]**.
>
> <http://en.wikipedia.org/wiki/Resource_Description_Framework>
>
</section>
In the work I do in eResearch systems and repositories, RDF is clearly a
very good framework for extensible metadata, and the associated “Linked
data” approach of using URIs to describe things and concepts is a good
way to implement shared vocabularies, but RDF is very hard to get to
grips with as a general modelling framework.

Now it’s time to over-simplify the process of getting data into web
pages via schema.org et al.

<section typeof="http://purl.org/ontology/bibo/Slide">
#### Putting data on the web?

-   Is it in some kind of web ready format?\*

    -   **Yes**: Put it on the web as-is **\#justpublish**

    -   **No**:  Make it into a web ready format. Options:

        1.  Reformat to a spreadsheet or something **\#justpublish**

        2.  Embed the data in human readable HTML

            **\#inlinedata** and **\#semanticmarkup**  

        3.  Publish as a stand-alone RDF resource\*\*

-   In any case publish a web page *about* it\*\*\*

-   Include metadata in the web page. **\#pagelevelmetadata**

-   Make the metadata standards-based and proper\*\*\*\*.
    **\#sharedvocab**

-   Choose a syntax for the embedding **\#semanticsyntax**

</section>
<section>
#### The fine print

\*What is a web-ready format depends on how much of a pedant you are –
for some only gold-plated RDF is good enough

\*\*And, you know, keep the web page UP.

\*\*\* At [Tim
Berners-Lee](http://en.wikipedia.org/wiki/Tim_Berners-Lee)’s talk in
Melbourne that night David Flanders asked him what advice he had for
researchers re data – should they put it on the web?

Tim’s response was that researcher should work with their data in the
format that suits them but they should get a ‘shim’ or adaptor built to
provide an RDF interface to the data so others could use it as part of
the semantic web.

I think that’s easy for Sir Tim to say and he’s right that it would be a
Good Thing, but experience has shown that projects like that run to
about \$200K in Australia and don’t always get results, so I’d add “and
while you’re working on the RDF adaptor, publish what you have in the
format in which you have it with as much metadata as you can manage”.

\*\*\*\*Good luck. If anybody comments at all it will be to ask “why
didn’t you use the European/ISO/W3C Standard” (which will turn out to be
a document that has been in development for 5 years but expected to be
released in six months for the last four of those years)

![](/wp-content/uploads/2013/02/wpid-putting-data-copy.html.html_putting-data-copy_filesimage0061.png)

Figure 1 Tim Berners-Lee (right) dwarfed by the happy head on a
sponsor's banner, which in turn is dwarfed by Art - at the University of
Melbourne

<section typeof="http://purl.org/ontology/bibo/Slide">
#### Google Scholar

![](/wp-content/uploads/2013/02/wpid-putting-data-copy.html.html_putting-data-copy_filesimage008.png)

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
#### Case study Getting a scholarly work into Google Scholar

-   A repository somewhere advertised the existence of the work via
    extensive use of the venerable meta-tag. \#page-level-metadata

-   Google found the data, entered it in its database.

-   When you search it puts the metadata back in the page so other
    software can scrape it out \#microformats\*

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
#### \*Microformats mean

Worst-case: maintaining a web-load of converters – see this from [a
patch](https://github.com/zotero/translators/issues/432) to keep the
Zotero reference manager working with Google Scholar. Google changes
their page? You change your code and redeploy to millions of people.

> '//div[@class="gs\_r"]/div[@class="gs\_fl"]/a[contains(@href,"q=related:")]') +      
> '//div[@class="gs\_r"]//div[@class="gs\_fl"]/a[contains(@href,"q=related:")]')  

These are XPath expressions looking in the webpage for stuff that Google
coded for their own reasons, probably to make it *look* right, not
primarily for data interchange.

</section>
You see what’s happening there? Google indexes pages that conform to a
standard they defined (not the one the repository community uses for its
own interchange). Then to get the data back out the scholarly community
has to keep track of a non-standard convention, again invented by
Google.

<section typeof="http://purl.org/ontology/bibo/Slide">
#### Sounds like a case for Schma.org?

You’d certainly think so.

But don’t underestimate the power of commercial interests to distort the
shape of the semantic web.

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
#### There are (at least) two things to be standardised in web semantics

-   The (hopefully) shared vocabulary / world view - “ontology”
    **\#sharedvocab**

-   The encoding method; how the meaning is embroidered on to the web
    **\#semanticsyntax**

And of course we have multiple overlapping but incomplete standards,
best practices, worst practices and flame-wars for both.

</section>
There are four basic ways to embed data into web pages.

<section typeof="http://purl.org/ontology/bibo/Slide">
#### Four ways to \#inlinedata

-   Metadata about a *whole page* via meta tags in the head
    \#pagelevelmetadata  \#traditional

-   Metadata/data about parts of a page: \#semanticsyntax

    -   [Microformats](http://en.wikipedia.org/wiki/Microformat)
        (obsolete but persisting) using conventions \#byconvention

    -   [Microdata](http://en.wikipedia.org/wiki/Microdata_(HTML)) –
        part of the (non W3c) HTML5 spec  simple, flawed, controversial
        \#worksbutpissedpeopleoff

    -   [RDFa](http://en.wikipedia.org/wiki/Rdfa) - obscenely
        complicated unless you use RDFa 1.1 lite \#theonetrueway

</section>
</section>
I have been working with researchers at the Hawkesbury Institute for the
Environment at UWS and the technical folks at Intersect NSW to implement
an HTML readme file to accompany environmental researcher data sets –
we’re working on a case-study that goes into how we made the choice of
RDFa (\#semanticsyntax) and how we chose which vocabularies and terms to
use (\#sharedvocab) which we’ll publish as soon as possible.

\

------------------------------------------------------------------------

[^[i]^](#_ednref1) Semantically rich? Look at the source – I’ve used a
web-police-approved mechanism for embedding slides in my prose. That is,
I have used a standard vocabulary (the bibliographic ontology
\#sharedvocab) and a syntactic specification (RDFa 1.1 lite
\#semanticsyntax) for saying that some parts of the page are special.

</section>
</article>

