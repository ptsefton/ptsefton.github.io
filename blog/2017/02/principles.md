---
title: Principles for eResearch Systems Development and Selection
date: 2017-03-09
slug: eresearch-principles
category: eResearch
author: ptsefton
---

This was originally [posted] on 2014-08-08 at the eResearch Blog at the (then)
University of Western Sydney where I led the eResearch team. These were the
principles we used to inform our work on eResearch systems, as written up by
the wry, sardonic David Clarke and me.

I'll see what the folks at UTS think...


This blog post is a first attempt at a set of principles and best practices that
we should strongly encourage for eResearch.

# Summary manifesto

-   Thou Shalt Have No Data Without Metadata

-   RDF is best practice for Metadata

-   Use Metadata Standards where they exist

-   Use URIs rather than Scalars (eg Strings) as names

-   Name all data and metadata ASAP

-   Thou Shalt Separate Thy Concerns

-   Use "Small Pieces, Loosely Joined" in preference to big monolithic
    applications

-   Processes over Tools

-   Separate safe storage of Data-plus-metadata from processing, analysing,
    searching viewing and other functions

-   Access all services via APIs

-   Data Is Everything^[Yes, pedants, we know: Data Are Everything], Everything Is^[This one we are sure about] Data

-   Stuff collected, created and crafted in the process of research

    -   Code, workflow and process descriptions

    -   Publications and documentation

  ... they’re all data, and hence, should not be without metadata.

# No Data Without Metadata

Metadata tells you what the corresponding data actually is, without it we do not know what the data really means. We should capture metadata as soon as practical, preferably with the data to which it applies.

Using URIs for subjects, predicates and (where applicable) values give us precision and clarity. The semantics of ontologies are well defined, and the ability to refer to data objects via a globally-unique, completely unambiguous reference will support the reuse of that data – one of the main pillars of eResearch. In general, Tim Berner’s-Lees’ Five Stars of Linked Open Data are relevant, but note that not all research data can or should be made available as open data, although linked data is better than non-linked data.

While we acknowledge that science data formats and instrument makers have their own metadata formats, as do the library community and agencies such as The Australian National Data Service, which may not be RDF or Linked Data ready, we should use RDF and/or URIs as identifiers wherever possbile. This includes storing metadata as RDF in our repositories. The abilities this give us to link data and to search the metadata are too powerful to give up.

# Separation Of Concerns

We strongly suspect that finding one single system which can do all things for all researchers is not going to happen. Instead, we believe that we should look to building ecosystems of collaborating systems, talking to each other over (preferably) standard APIs with each system doing specific tasks and doing them well.

Exposing services via well defined APIs gives several benefits:

-   workflow scripts can be developed to facilitate use of the services.

-   we can provide multiple implementations of a given function within the
    ecosystem, allowing users to choose one that gives them the facilities they
    need.

-     we can upgrade, or even completely change, services. As long as the
      implementations support the appropriate APIs, workflows should not be
      affected.  we can incorporate new systems into this ecosystem relatively
      easily, extending the range of services in the ecosystem Tools are all
      well and good, and in an ideal world all our systems would work together
      to give us a shiny, synergistic whole. However, back on planet reality we
      have to be aware that there will be gaps between the tools. You know what?
      That can be OK. Small numbers of manual steps in a tool-chain don’t
      invalidate the process. Having said that, manual steps are potential
      sources of random mistakes and we should work towards minimising them.

# Data Are Everything

Data includes inputs, results, physical specimens

Metadata includes information about all the context in which research is
   conducted where, what machines, which chemicals, which edition of the book,
   the temperature of the apartus, anything that might influence the results.

At the core of eResearch practice is keeping data safe (remember: No Data Without Metadata). Different classes of data are safest in different homes, but ideally each data set or item should live in a repository, where:

-  It can be given a URI

-  It can be retrieved/accessed via a URI by those who should be allowed to see it, and not by those who should not

-  There are plans in place to make sure the URI resolves to something useful as long is it is likely to be needed (which may be "as long as possible").

-  If we take the idea of separation of concerns seriously then a web view, search, query services are part of the repository. Indexes and web-interfaces are separate concerns.

Types of repositories include:

-  Databases, where available

-  Digital object repositories that group together related files as data-sets, or items with common metadata

-  Code repositories for code and documentation

-  Publication and documentation repositories


Yes, we should add references to this document.

Creative Commons License:
Principles for eResearch Systems Development and Selection by David Clarke & Peter Sefton is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.



[posted]: https://web.archive.org/web/20150301103735/http://eresearch.uws.edu.au/blog/2014/08/08/principles-for-eresearch-systems-development-and-selection/
