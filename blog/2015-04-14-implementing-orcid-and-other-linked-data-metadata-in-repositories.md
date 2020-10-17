---
Author: ptsefton
Comments: true
Date: 2015-04-14 00:38:25+00:00
Slug: implementing-orcid-and-other-linked-data-metadata-in-repositories

Title: Implementing ORCID and other linked-data metadata in repositories
Wordpress_id: 1997
---

<section typeof="http://purl.org/ontology/bibo/Slide">
# Implementing linked data metadata systems

## Peter Sefton

### University of Technology, Sydney

<details open="open"> This is a short presentation for the
[ORCID](http://orcid.org/) (Open Researcher and Contributor ID)
implementers Roundtable in Canberra April 14, 2015.

The [ORCID](http://orcid.org/) site says:

> ORCID provides a persistent digital identifier that distinguishes you
> from every other researcher and, through integration in key research
> workflows such as manuscript and grant submission, supports automated
> linkages between you and your professional activities ensuring that
> your work is recognized.

I will post this so I can present - and come back later to expand, and
clean up typos, so this post will evolve a bit.

This event is launching a document:

> The ‘[Joint Statement of Principle: ORCID - Connecting Researchers and
> Research](http://www.ands.org.au/discovery/orcid-discussion-paper20150306.pdf)'
> [PDF 297KB] proposes that Australia's research sector broadly embrace
> the use of ORCID (Open Researcher and Contributor ID) as a common
> researcher identifier. The statement was drafted by a small working
> group coordinated by the Australian National Data Service (ANDS)
> comprised of representatives from Universities Australia (UA), the
> Council of Australian University Librarians (CAUL) and the
> Australasian Research Management Society (ARMS). Representatives of
> the Australian Research Council and the National Health and Medical
> Research Council also provided input through the working group.

In this presentation I talk about some of the details of how to
implement the ORCID. Just how do you *use* an ORCID ID in a
institutional repository?

This is not that simple, as most of our systems are set up to expect
string-values for names, not IDs.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# This talk is not *all* about ORCIDs...

... it's about *implemeting* linked data principles

<details open="open">

This talk is about why ORCIDs are important, as part of the linked-data
web. I will give examples of some of the work that's going on at UTS and
other institutions on linked-data approaches to research data management
and research data publishing and conclude with some comments about the
kinds of services I think ORCID needs to offer.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# Modern metadata should be linked-data

> -   Thou Shalt Have No Data Without Metadata
>
> -   RDF is best practice for Metadata
>
> -   Use Metadata Standards where they exist
>
> -   Use URIs rather than Scalars (eg Strings) as names
>
> -   Name all data and metadata ASAP
>
> [Clarke and Sefton
> 2014](http://eresearch.uws.edu.au/blog/2014/08/08/principles-for-eresearch-systems-development-and-selection)

<details open="open"> But using URIs as names for thing is not easy to
do. Most repository software doesn't support this out of the box, and
it's difficult to graft URIs onto a lot of existing metadata schemas,
such as the ubiquitous Dublin Core which in its simple, flat form has no
way for URIs to be used as metadata values.

And while it's easy enought to say "RDF is best practice for Metadata"
*entering* RDF metadata is non-trivial for humans. So I wanted to show
you some of the work we've been doing to make it possible to build
research data systems that are compliant with the above principles.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# 1. ReDBOX

[![namelookup](/wp-content/uploads/2015/04/namelookup-1024x454.png)](/wp-content/uploads/2015/04/namelookup.png)

Screenshot from the UTS Stash data catalogue showing a party lookup, to
get a URI that identifies a person.

<details open="open"> The ANDS-funded ReDBOX project embraced linked
metadata principles from the very beginning, it has a name-authority
service, Mint which is a clearing house for sources of truth about
people, organisational units, subject codes, grant codes etc.

But, the ReBOX/Mint partnership is a very close one, there's no general
way to lookup other name authorities, without loading them into Mint.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
[![Picture1](/wp-content/uploads/2015/04/Picture1-1024x768.png)](/wp-content/uploads/2015/04/Picture1.png)

<details open="open">

In 2014 I asked, what if there were a *general* way to do this, so that
we could use URIs from a wide range of sources, and a team of developers
from NZ and the UK responded as part of the Developer Challenge Event at
that year's Open Repositories conference in Helsinki, supported by Rob
Peters from ORCID, who is at this meeting in Canberra.

Slide by:

-   Adam Field : iSolutions, University of Southampton
-   Claire Knowles: Library Digital Development Manager, University of
    Edinburgh
-   Kim Shepherd: Digital Development, University of Auckland Library
-   Jared Watts: Digital Development, University of Auckland Library
-   Jiadi Yao: EPrints Services, University of Southampton

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# Enter Fill my List

<div class="figure">

![Members of the Fill My List team (minus Claire Knowles who took the
pic) hard at work at Open Repositories
2014](/wp-content/uploads/2015/04/fml-300x225.jpg)
Members of the Fill My List team (minus Claire Knowles who took the pic)
hard at work at Open Repositories 2014

</div>

<details open="open">

See their [git repo](https://github.com/gobfrey/OR2014-chalege).

This modest github repository might not look like much, but as far as I
know, it's the first example of an attempt to create an easy-to use
protocol for web developers to make lookup services.

Fill my list enabled auto-complete lookup to multiple sources of truth
including ORCID, so a user can find the particular Lee or Smith they
want to assert is a creator of a work, specify which kind of Python they
mean for the subject of a work and get a URI. The FML team did prototype
implementations for ePrints and Dspace software.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
[![Screen Shot 2015-04-13 at 9.56.39
am](/wp-content/uploads/2015/04/Screen-Shot-2015-04-13-at-9.56.39-am.png)](/wp-content/uploads/2015/04/Screen-Shot-2015-04-13-at-9.56.39-am.png)

Looking up the Schools Online Thesaurus (ScOT) for the URI for
"Billabongs".

!!!SPOILER ALERT!!!

it's <http://vocabulary.curriculum.edu.au/scot/9962>

<details open="open"> We have since picked FML up at UTS, and are using
it to make high quality metadata for our Australian National Data
Service funded Major Open Data Collections project.

The above screenshot shows a prototype lookup service which shows
auto-complete hints as you type.

Note that typing "Oxb" find the same URI - Billabongs are also know as
'oxbow lakes'.

Note that in the screenshot you can see one of the important changes we
made to the Omeka repository software to support linked data, as part of
the [Ozmeka](https://github.com/ozmeka/ozmeka) project.

Instead of just a string field for the subject there is a URI as well.
So, even though some records might say "Billabongs" and some might say
"Oxbow lakes" both would have the same URI.

Note that to make this work we had to hack the Omeka software we're
using because like most repository software it didn't have good support
for using URIs as metadata values.

</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# So, why am I telling you all this?

[![Screen Shot 2015-04-13 at 10.29.28
am](/wp-content/uploads/2015/04/Screen-Shot-2015-04-13-at-10.29.28-am.png)](/wp-content/uploads/2015/04/Screen-Shot-2015-04-13-at-10.29.28-am.png)

The raw, machine-readable Fill My List protocol in action, looking up an
ORCID index.

<details open="open">

When we refer to researchers on the web, we should use their ORCID ID,
in the form of a URI. But to be *able* to do this we often have to
update repository software (as my tean at UTS are doing with Omeka).
</details>

</section>
<section typeof="http://purl.org/ontology/bibo/Slide">
# In conclusion

The ORCID API (machine to machine interface) provides pretty good but
not perfect open lookup services so...

Repository developers can make their repositories linked-data compliant

But it's a lot of work and it will involve a community effort to update
our repository systems, many of which are open source.

<details open="open"> We have made a lot of progress on improving the
quality of metadata in the Australian research sector - and a lot of
that has been community driven, for example the ReBOX project's
insistence on using URIs led to the first URIs for Australian grant
being minted by developers from Griffith and USQ, because it was the
right thing to do.

Now, a few years later, the government is making its own URIs and the
Australian National Data services is providing vocab services.

ORCID does have a public API to allow us to build Fill My List type
lookup services - allowing to query on name-parts, it would be better if
it included bibliographic information, wich might help someone entering
metadata choose between two people with the same name.

</details>

</section>

