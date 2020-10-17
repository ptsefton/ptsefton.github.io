---
Author: ptsefton
Comments: true
Date: 2013-03-01 00:39:08+00:00
Slug: repositories-what-are-they-good-for

Title: Repositories! (What are they good for?)
Wordpress_id: 1672
---

<article>
[![Creative Commons
License](http://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/deed.en_US)\
<span property="dct:title" dct="http://purl.org/dc/terms/">Repositories!
(What are they good for?)</span> by <span property="cc:attributionName"
cc="http://creativecommons.org/ns#">Peter Sefton</span> is licensed
under a [Creative Commons Attribution 3.0 Unported
License](http://creativecommons.org/licenses/by/3.0/deed.en_US).

<section>
# Repositories! (What are they good for?)

Georgina Edwards has invited me to [Intersect
NSW](http://intersect.org.au) to give a talk to the software engineering
team about repositories in eResearch. There were also quite a few
eResearch analysts in attendance, not to mention a couple of members of
the senior management team. (Just in case you’re wondering, the answer
to the question in the title is *not* “absolutely nothing”).

\
 Here are my notes, with embedded slides, which I put together on the
train to and from the CBD (ie quick and dirty).

**The summary:** repository means a lot of different things, but the
main sense I talked about with the Intersect team was ‘data-store
component’. I tried to cover why using a repository in an eResearch
project might be important because repositories can provide a lot of
ready-made functionality, particularly in the area of digital
preservation, but also access to indexing services and
content-transcoding to generate new formats from things ingested. I
talked about one aid for thinking about repository services which I
think is useful – the Repository Micro-services framework from the
California Digital Libraries, and ran through some of the repository
frameworks that people in the eResearch.au world might encounter.

The liveliest discussion was around RDF, the [Resource Description
Framework](What%25E2%2580%2599s%2520a%2520repository%2520to%2520me%3F%2520%2520The%2520first%2520time%2520many%2520of%2520us%2520heard%2520the%2520term%2520repository%2520in%2520Higher%2520Education%2520was%2520in%2520connection%2520with%2520the%2520Open%2520Access%2520movement,%2520when%2520a%2520few%2520forward%2520thinking%2520universities%2520in%2520Australia%2520QUT,%2520UQ,%2520USQ%2520and%2520even%2520some%2520others%2520outside%2520of%2520Queensland%2520began%2520to%2520set%2520up%2520Institutional%2520Repositories,%2520using%2520software%2520like%2520Eprints%2520or%2520Dspace.%2520These%2520were%2520essentially%2520online%2520databases%2520of%2520PDF%2520files,%2520with%2520bibliographic%2520metadata),
and what *it’s* good for. I made the assertion that RDF was the best
practice approach to storing metadata, allowing for built-in
extensibility. RDF uses URIs as names for both things and relations,
which reduces ambiguity and aids interoperability. But I think it’s
important to draw the line between RDF as a good way to do metadata, and
annotation and the assumption that an RDF query language (via an RDF
triple-store) is always going to be needed or even work. I’m sceptical
about the promise of RDF as some kind of super semantic world-wide web
of knowledge you can query for the answer to anything, but it’s clearly
a good way to do metadata – there’s no excuse for inventing a new
metadata schema that is not RDF based these days.  (Use the comments if
you want to discuss).

<section>
## The talk

I thought I’d start from something that the developers would be familiar
with. Source-code repositories.

<section typeof="http://purl.org/ontology/bibo/Slide">
## To a bunch of software developers…

… a repository is a place to put code

</section>
But it’s not just a place to *put* things. On a development project, the
repository offers a number of services, like integration with task
management systems, versioning, search and collaboration. I’m sure
everyone in the professional eResearch world would be horrified to find
a development project that wasn’t using source-code management via a
code-repository: Git, Mercurial, or at the very least something ancient
like Subversion.

</section>
<section>
## What’s a repository to me?

The first time many of us heard the term repository in Higher Education
was in connection with the Open Access movement, when a few forward
thinking universities in Australia [QUT](http://eprints.qut.edu.au/),
[UQ](http://espace.library.uq.edu.au/),
[USQ](http://eprints.usq.edu.au/) and even some others outside of
Queensland began to set up Institutional Repositories, using software
like Eprints or Dspace. These were essentially online databases of PDF
files for academic works, with bibliographic metadata. They were also
seen as sites for preservation of materials, and had services to
advertise their contents to the world, via the
[OAI-PMH](http://www.openarchives.org/pmh/) metadata harvesting
standard, and via metadata embedded in the web pages that described the
academic works.

A group of us put together [a presentation for Open Repositories last
year on the growth of Institutional Research Data Repositories,
alongside the ‘traditional’ Institutional Publications
repository](http://ptsefton.com/2012/07/24/think-local-act-global-institutional-data-repositories-being-built-in-australia-with-lessons-learned-from-institutional-publications-repositories.htm).

<section typeof="http://purl.org/ontology/bibo/Slide">
## There are a few senses of the word:

-   Repository-as-database

-   Repository-as-application

    Institutional Repository or Data Repository

-   Repository-as-lifestyle (ie analogous to a ‘library’)

</section>
People tend not to be very careful about these senses of the word
repository and indeed the boundaries are actually quite blurry. If you
have chosen to call your application a repository, then that term brings
a certain gravitas, you’d expect the repository-as-application to be
something that’s not just for Christmas, but something you’ve made a
commitment to feeding and walking at least for *some* time.

With that  in mind, the point of this discussion: is what might a
repository-as-data store be good for in an eResearch project?

<section typeof="http://purl.org/ontology/bibo/Slide">
## Services in a typical repository-as-datastore underneath an application:

-   If the app goes away the data is/are safe independently of the
    application services,

    -   with all digital objects stored in standard formats

    -   with standardised metadata

    -   so they can be preserved\*.

-   You get OAI-PMH (pull/out) and SWORD (push/in) built in

-   Built in security/access control

    (but beware of actual real-world performance)

-   Content transcoding

    (thumbnails / image viewers / video versions)

</section>
Nobody put up their hand and said “Hey that’s just a CMS” (Content
Management System), but the answer would have been, yes, of course. A
repository-as-application is just a serious CMS, one designed for
maintaining important stuff in a well-managed way. Indeed, the
University of Queensland is moving its Institutional Repository to a
[Drupal](http://drupal.org/)-based system, and leaving behind the
repository-as-data-store that used to sit underneath it.

The [Repository Micro-services
framework](http://journals.tdl.org/jodi/index.php/jodi/article/view/1605/1766)
from the University of California captures all these services really
nicely.

<section typeof="http://purl.org/ontology/bibo/Slide">
## Repository Micro-services

<http://journals.tdl.org/jodi/index.php/jodi/article/view/1605/1766>

![](/wp-content/uploads/2013/03/wpid-repositories.docx.html_repositories.docx_filesimage002.png)

This is implemented in <http://merritt.cdlib.org/>, which does not seem
to have an obvious application to download.

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
## Repository micro-services

## ![](/wp-content/uploads/2013/03/wpid-repositories.docx.html_repositories.docx_filesimage004.png)

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
## Some repository software you may hear about

-   [Eprints](http://www.eprints.org/) (Perl)

    Good for publications repositories, has been used for cultural
    collections, learning – has every imaginable interface to repository
    content

-   [DSpace](http://dspace.org) good for a range of digital object
    collections

    eg Andrea Schweer’s talk on a data capture app [Building a
    repository for freshwater quality
    data](http://www.caul.edu.au/content/upload/files/cairss/cairss2012schweer.pdf)

-   Fedora Commons (back end)

    -   [Islandora](http://www.islandora.ca/) application/platform
        (Drupal PHP)

    -   [The
        Fascinator](https://github.com/the-fascinator/the-fascinator)
        platform / ReDBOX Application (Java + Jython)

    -   [Hydra](https://wiki.duraspace.org/display/hydra/The+Hydra+Project)
        platform (Rails)

-   [CKAN](http://ckan.org/) – a Research data Hub app (Python)

-   Micro-service components like
    [BagIt](http://en.wikipedia.org/wiki/BagIt) for packaging and
    [PairTree](https://wiki.ucop.edu/display/Curation/PairTree) for
    efficient file-storage.

NOTE: All of the above apart form Eprints include built-in search using
[Apache Solr](http://lucene.apache.org/solr/).

</section>
In conclusion, I asked: why use one of the above, particularly when on
first acquaintance, something like Fedora can look like an anchor,
impeding forward progress?

The basic answer is that if in the long run your project is going to
require some large percentage of the repository micro-services discussed
above, then you’re going to end up writing your *own* Fedora-like thing.
Also, I think it’s better to be part of a community looking at these
things together. For example Fedora is not a magic solution to being
able to re-use repository content between applications, but it is
reassuring to know that the Hydra and Islandora communities are talking
about interop via their
[Hylandora](https://www.conftool.net/or2012/index.php?page=browseSessions&form_session=62)
project and there is a significant amount of preservation-work happening
in the Fedora world.

To some of us, the idea of doing *certain kinds* of eResearch project
without a back-end repository (as in something that has managed services
around preservation under some kind of serious governance) would be like
doing software development without a code repository. The question, of
course is which kinds of project? And of course, if you do need one,
where do you put the repository part in the architecture.

</section>
</section>
</article>

