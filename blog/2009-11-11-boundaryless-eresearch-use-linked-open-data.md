---
Author: ptsefton
Comments: true
Date: 2009-11-11 23:23:57+00:00
Slug: boundaryless-eresearch-use-linked-open-data

Title: 'Boundaryless eResearch: Use Linked Open Data'
Wordpress_id: 425
---

<div>

<div class="page-toc">

</div>

<div>

I am at the eResearch Australasia conference, official tag
[\#eraust09](http://twitter.com/#search?q=%23eraust09). Yesterday
afternoon Anna Gerber, Peter Murray-Rust and I convened a Birds of a
Feather (BoF) session: [Boundaryless eResearch: use the Web, use Linked
Open Data](http://www.eresearch.edu.au/2009bof05).

I [put up some thoughts about what I'd like to see from the
session](http://ptsefton.com/2009/10/21/some-thoughts-for-our-bof-session-on-boundaryless-eresearch-for-eraust09.htm).
It was well attended, and the discussion took off nicely into issues
well beyond technology. Jim Richardson tweeted it, [summarised
here](http://bit.ly/eraust09LOD).

Anna's wrap-up is here:

> Linked Open Data is not a silver bullet that tries to resolve all
> issues surrounding publishing of data online: questions of data
> quality, privacy, institutional policy, persistent access, and so on,
> remain. It is a technical solution, providing a set of principles for
> publishing data so that it will be discoverable from and linkable
> (mashable) with other data available on the web.
>
> When describing the LOD vision, we often talk about a web of data,
> however we need to consider how to integrate this emerging web with
> our existing web of documents (as well as with datasets and documents
> that are not yet published online). Technologies like RDFa that can be
> retrofitted to existing web documents to link them with LOD datasets
> will be crucial towards this end, as will enabling researchers to
> publish their data with RDF generated from tools that they already use
> within their research practice (like word processors, workflow tools,
> etc).

Here are the few slides we used to seed discussion on the day, with a
couple of late additions. A talk by Anne Cregan earlier in the day
provided a good introduction to Linked Open Data: [Linked Open Data: a
new resource for eResearch](http://www.eresearch.edu.au/cregan2009).

<div class="slide">

# Linked data (ptsefton)

TBL [says](http://www.w3.org/DesignIssues/LinkedData.html):

> Like the web of hypertext, the web of data is constructed with
> documents on the web.<span style="font-style:normal; "><span
> class="T3"> [...]</span></span>
>
> -   Use URIs as names for things
>
> -   Use HTTP URIs so that people can look up those names.
>
> -   When someone looks up a URI, provide useful information, using the
>     standards (RDF, SPARQL)
>
> -   Include links to other URIs. so that they can discover more
>     things.
>
> Simple.  In fact, though, a surprising amount of data isn't linked in
> 2006, because of problems with one or more of the steps.[...]
>
> <http://www.w3.org/DesignIssues/LinkedData.html>

</div>

<div class="slide">

# Simple? (ptsefton)

What does this mean?

> Copyright Peter Sefton, Jim Downing, Anna Gerber & Peter Murray-Rust
> 2009. Licensed under Creative Commons Attribution-Share Alike 2.5
> Australia. \<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

<span style="font-style:normal; "><span class="T3">Does everything that
cites the URL </span></span>[<span style="font-style:normal; "><span
class="T3">http://creativecommons.org/licenses/by-sa/2.5/au/</span></span><span
style="font-style:normal; "><span class="T3">
</span></span>](http://creativecommons.org/licenses/by-sa/2.5/au/)get
the license?

[[Professor Tom
Cochrane](http://www.tils.qut.edu.au/about/officeofthed/tomcochrane.jsp),
co-leader of the [Creative Commons](http://www.creativecommons.org.au/)
project for which QUT is the institutional partner for Australia just
happened to be there. It turns out that the convention of linking one of
the little CC badges is what signifies intent to license a work,
although my wording is probably good, but the point stands that there is
not unambiguous way to tell a machine the difference between a link
which is intended to license the work and one which is citing or
pointing at the license for some other purpose.]

</div>

<div class="slide">

# Our goal: insulate users from this stuff (ptsefton)

    <!-- /Creative Commons License -->

    <!--

    <rdf:RDF xmlns="http://web.resource.org/cc/"

        xmlns:dc="http://purl.org/dc/elements/1.1/"

        xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

    <Work rdf:about="">

       <dc:date>2005</dc:date>

       <dc:creator><Agent>

          <dc:title>Peter Murray&amp;#45;Rust</dc:title>

       </Agent></dc:creator>

       <dc:rights><Agent>

          <dc:title>Peter Murray&amp;#45;Rust</dc:title>

       </Agent></dc:rights>

       <dc:type rdf:resource="http://purl.org/dc/dcmitype/Text" />

       <license rdf:resource="http://creativecommons.org/licenses/by-nc-nd/2.0/" />

    </Work>

    <License rdf:about="http://creativecommons.org/licenses/by-nc-nd/2.0/">

       <permits rdf:resource="http://web.resource.org/cc/Reproduction" />

       <permits rdf:resource="http://web.resource.org/cc/Distribution" />

       <requires rdf:resource="http://web.resource.org/cc/Notice" />

       <requires rdf:resource="http://web.resource.org/cc/Attribution" />

       <prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" />

    </License>

    </rdf:RDF>

    -->

Is that valid? <http://www.w3.org/RDF/Validator/ARPServlet> [PMR]

</div>

<div class="slide">

# 1. Issues with URIs for everything (AG)

-   persistence of URIs - what is the lifespan of the data

-   how to mint new ones (persistent identifier services eg ANDS)

-   human readable vs non-human readable (eg
    <http://example.or/data/myexperiment> vs
    <http://handle.net/1093489345878937453495873294>)

-   human readable may become outdated/ no longer accurately describe
    the content

-   who makes choices on these policies?
    (researcher/institution/community)

-   how to discover the URI used by other members of the research
    community for a given concept? 

-   use of dictionaries/thesaurus or agreed databases eg LOC, dbpedia

-   academics may not be comfortable using terms from non-academic
    sources eg wikipedia/dbpedia 

</div>

<div class="slide">

# 3. Issues with RDF as URI (AG)

-   how much data/metadata to describe using RDF? 

-   raw RDF vs styled/presented vs embedded (RDFa)

-   what about data/documents that have already been published - adding
    RDFa

    -   level of granularity of markup

    -   maintaining integrity of documents if embedding RDFa

    -   publishing at existing URIs adding \#thing1 \#thing2 for
        existing URIs

-   what vocab/ontology to use (reuse, mix them up)

    -   even if there is an established ontology for the domain,
        applying ontology terms to a given data set may not be
        straightforward

</div>

<div class="slide">

# 4. Issues with links to other resources (AG)

-   providing these links at the URI as RDF vs querying stand-off triple
    stores: the same data may be used by several research communities -
    should data specific to each community be directly available at that
    URI or in discipline-specific datastores?

-   Provenance of data : can it be trusted? in many cases the data being
    published is not the raw data - need to identify who has
    interpreted/cleaned up the data

</div>

<div class="slide">

# Licensing <span class="spCh spChx2013">–</span> the 'open' bit (PMR)

> The biggest danger is not making the assertion that the data is open.

The Panton Principles:
<http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=1939>

[Via Jim Richardson more resources:
<a name="msgtxt5612935141"></a>[<span
style="font-size:9pt; font-style:normal; font-variant:normal; font-weight:normal; text-transform:none; "><span
class="T8">http://bit.ly/2eZlOG</span></span>](http://bit.ly/2eZlOG)]

</div>

<div class="slide">

# Example DbPedia (PMR)

     SELECT ?resource

    WHERE { 

    ?resource <http://dbpedia.org/ontology/Person/birthPlace> <http://dbpedia.org/resource/Sydney> ;

    <http://dbpedia.org/ontology/Person/deathPlace> <http://dbpedia.org/resource/Sydney>

    }

    ORDER BY ?resource

     http://dbpedia.org/snorql/?describe=http%3A//dbpedia.org/resource/Sydney 

     http://dbpedia.org/snorql/?query=SELECT+%3Fresource%0D%0AWHERE+{+%0D%0A%3Fresource+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FPerson%2FbirthPlace%3E+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2FSydney%3E+%3B%0D%0A%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FPerson%2FdeathPlace%3E+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2FSydney%3E%0D%0A}%0D%0AORDER+BY+%3Fresource 

</div>

<div class="slide">

# Discussion points (all)

-   Who has used RDF? How did it go?

-   AG:

    -   Embedding data in documents and web pages eg via RDFa is crucial
        in linking existing web of documents with emerging web of data 

    -   Don't sweat the details just get the data out there in an open
        format

-   ptsefton:

    -   **Getting tools into the** hands of researchers so they can
        <span class="spCh spChx2018">‘</span>do<span
        class="spCh spChx2019">’</span> linked data.

    -   **Getting the web into the scholarly communications process as a
        first-class citizen:** [Scholarly
        HTML](http://delicious.com/ptsefton/ptsefton+scholarlyhtml).

    -   **Bringing the web to the desktop.** [The
        Fascinator](http://fascinator.usq.edu.au/)
        [Lensfield](http://code.google.com/p/lensfield/) Anna & team's
        [Firefox Add In for creating compound semantic-web objects, for
        literary
        scholars](http://www.ijdc.net/index.php/ijdc/article/view/116).

-   

</div>

<div class="slide">

# Examples

-   [**The Aus-e-Lit
    project**](http://www.itee.uq.edu.au/~eresearch/projects/aus-e-lit/)
    is a NeAT-funded project that aims to address the eResearch needs of
    researchers involved in the study of Australian literature and
    Australian print culture. The project enhances and extends the
    existing AustLit web portal with data integration and search
    services, empirical reporting services, compound object authoring,
    editing and publishing services and collaborative annotation
    services.

-   [**The OREChem
    project**](http://journal.webscience.org/112)<a name="ZOTERO_BREF_cuJAklsjxLex"></a>
    is a Microsoft-funded collaboration between Cambridge, Cornell,
    Indiana, Penn State and Southampton Universities that aims to make
    existing chemistry data sources available as LOD, to develop new LOD
    creation resources using grid computing, to develop and converge on
    standard ontologies for chemistry knowledge representation, and to
    further the state of the art in extracting semantic chemistry data
    from published PDF.

-   **Talis Connected Commons** is an initiative whereby Talis offer
    free Linked Data infrastructure for open datasets. Nick Day and Jim
    Downing at the University of Cambridge are working to publish
    semantic data from the CrystalEye<span style="font-size:6pt; "><span
    class="T7">8</span></span> system through Talis Connected Commons.
    No, we need a r*elation* something like *has-license* <span
    class="spCh spChx2013">–</span> the challenge is to let ordinary
    researchers.

</div>

Copyright Peter Sefton, Jim Downing, Anna Gerber & Peter Murray-Rust
2009. Licensed under Creative Commons Attribution-Share Alike 2.5
Australia. \<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

[![HTTP://DBPEDIA.ORG/SNORQL/?QUERY=SELECT+%3FRESOURCE%0D%0AWHERE+{+%0D%0A%3FRESOURCE+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%2FBIRTHPLACE%3E+%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FRESOURCE%2FSYDNEY%3E+%3B%0D%0A%3CHTTP%3A%2F%2FDBPEDIA.ORG%2FONTOLOGY%2FPERSON%](/wp-content/uploads/2009/11/m40ca94ba.png)](http://creativecommons.org/licenses/by-sa/2.5/au/)

This post was written in OpenOffice.org, using templates and tools
provided by the [Integrated Content Environment](http://ice.usq.edu.au/)
project and published to WordPress using [The
Fascinator](http://fascinator.usq.edu.au/desktop/desktop.htm).

</div>

</div>
