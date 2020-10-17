---
Author: ptsefton
Comments: true
Date: 2013-09-10 07:04:02+00:00
Slug: round-table-on-vocabularies-for-describing-research-data-wheres-my-semantic-web
Category: ScholarlyHTML
Title: 'Round table on vocabularies for describing research data: where''s my semantic
  web?'
Wordpress_id: 1771
---

<article>
<section>
[UPDATE: Fixed some formatting]

[![Creative Commons
Licence](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB)\
<span property="dct:title" dct="http://purl.org/dc/terms/">Round table
on vocabularies for describing research data: where's my semantic
web?</span> by <span property="cc:attributionName"
cc="http://creativecommons.org/ns#">Peter Sefton</span> is licensed
under a [Creative Commons Attribution-ShareAlike 3.0 Unported
License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB).

**Summary:** in this post I talk about an experimental semantic website
for describing what I'm calling 'research context', wondering if such as
site can be used as a 'source of truth' for metadata entry, for example
when someone is uploading a file into a research data repository. The
post assumes some knowledge of linked data and RDF and/or an interest in
eResearch software architecture.

Thanks to twitter correspondents **[<u>**Jodi
Schneider**</u>](https://twitter.com/jschneider),** **[<u>**Kristi
Holmes**</u>](https://twitter.com/kristiholmes)** **and** **[Christopher
Gutteridge](https://twitter.com/cgutteridge).**

**[‏](https://twitter.com/cgutteridge)**

On Friday 7th September I attended a meeting at Intersect about metadata
vocabularies for managing research data, in the context of projects
sponsored by the Australian National Data Service
([ANDS](http://ands.org.au/)). Ingrid Mason asked me to talk about my
experiences describing research data. I approached this by starting with
a run-through of the [talk Peter Bugeia and I put together for Open
Repositories](http://ptsefton.com/2013/07/26/4a-data-management-acquiring-acting-on-archiving-and-advertising-data-at-the-university-of-western-sydney.htm)
with an emphasis on our attempts to use Linked Data principles for
metadata. In this work we encountered two big problems, which I brought
to the round-table session as questions.

1.  It's really hard to work out which ontology, or set of vocabulary
    terms to use to describe research context. Take 'experiment' what is
    a good linked data term for that?

    **Q. What to use as a URI for an experiment?**

2.  In trying to build linked-data systems I have not found any easy to
    use tools. (I got lots of useful leads from Kristy Holmes and Jodi
    Schneider on Twitter, more on that below).

    **Q. Where's my semantic web!**

Answers at the end of the post, but you have to read the whole thing
anyway.

The problem I'm working on at the moment with colleagues at the
University of Western Sydney is how we can provide a framework for
metadata about research data. We're after efficient interfaces for
researchers to contextualise research data sets, across lots of
different research domains where the research context looks quite
different.

For example, take the HIEv system at the Hawkesbury Intitute for the
Environment (HIE). HIEv is basically a file-repository for research data
files. It has information about each file (size, type, date range etc)
and contextual metadata about the research context, in this case using a
two-part hierarchy: Facility / Experiment where facilities are
associated with multiple experiments and files are associated with
experiments. Associating a data file with research context is easy in
HIEv because it's built in to the system. A human or machine uploading a
data file associates it with an experiment using a form, or a JSON data
structure respectively. The framework for describing research context is
built-in to the application, and the data lives in its internal
database.

This approach works well, until:

1.  **We try to re-use the software behind HIEv in another context**,
    maybe one where the research domain does not centre on facilities,
    or experiment is not quite the right concept, or the model needs to
    be further elaborated.

    **Example:** In the MyTardis project, a development team added an
    extra element to that package's research hierarchy – porting the
    application to new domains means substantial rework. See this
    [message on their mailing
    list](https://groups.google.com/d/msg/tardis-devel/tJYLphu_BpM/j44-5L3sFYIJ).

2.  **We want to re-use the same contextual descriptions to describe
    research data in another system** where we are faced with either
    programming a whole new framework for the same context, or adding a
    new interface for our new system to talk to the research context
    framework in the old one.

    **Example:** At HIE, [with the help of some computing
    students](http://ptsefton.com/2013/08/14/another-student-project-crossing-the-curation-boundary.htm),
    Gerry Devine and I are exploring the use of OwnCloud (the
    dropbox-like Share/Sync/See application) to manage working files,
    with a simple forms interface to add them to HIEV. As it stands the
    students have to replicate the Facility/Experiment data in their
    system, meaning they are hard-coding facility / Experiment
    hierarchies into HTML forms.

\
Gerry Devine and I have been sketching an architecture designed to help
out in both of these situations. The idea is to break-out the
description of the research-context into a well-structured application.
This [temporary site of
Gerry's](https://sites.google.com/site/hievuws/), shows what it might
look like in one aspect, a web site which describes stuff at HIE;
facilities, and their location, experiments taking place at those
facilities, and projects. The question we're exploring is: can we
maintain a description of the HIE research context in one place, such as
an institute research site or wiki, and have our various data-management
applications use that context, rather than having to build the same
research-context framework into each app and populate with lists of
values? Using a human-readable website as the core home for research
context information is appealing because it solves another problem,
getting some much needed documentation on the research happening at our
organisation online.

Here's an interaction diagram showing what might transpire when a
researcher wants to use a file management application, such as ownCloud
(app) to upload some data to HIEv, the working data repository at the
institute:

![](/wp-content/uploads/2013/09/wpid-research-context-rdf.html_research-context-rdf_html_m59a3b4c5.png)\

We don't have much of this implemented, but last week I had a play with
the research context website part of the picture (the system labelled
'web', in the above diagram). I wanted to see if I could create a web
site like the one Gerry made, but with added semantics, so that when an
application, like an ownCloud plugin asked 'gimme research context' it
could return a list of facilities, experiments and projects in machine
readable form.

For a real institute or organisation-wide research context management
app, you'd want to have an easy to use point and click interface, but
for the purposes of this experiment I decided to go with one of the many
markdown-to-html tools. See [this page which summarises why you'd want
to use](http://nanoc.ws/about/#similar-projects)one and[lists an A-Z of
alternatives](http://nanoc.ws/about/#similar-projects).This is the way
many of the cool kids make their sites theses days – they maintain pages
as markdown text files, kept under version control and run a script to
spit out a static website. Probably the best-known of these is Jekyl,
which is built in to GitHub. I chose Poole because it's Python, a
language in which I can get by, and it is super-simple, and this is
after-all just an experiment.

So, here's what a page looks like in Markdown. The top part of the file,
up to '-----' is metadata which can be used to lay out the page in a
consistent way. Below the line, is structured markup. \# Means “Heading
level 1” (h1), \#\# is 'h2' and so on.

    title: Glasshouse S30
    long: 150.7465
    lat:  -33.6112
    typeOf: @facility
    full_name: Glasshouse facility at UWS Hawkesbury building S30
    code: GHS30
    description: Glasshouse in the S-precinct of the University of Western Sydney, Hawkesbury Campus, containing eight naturally lit and temperature-controlled compartments (3 x 5 x 3.5m, width x length x height). This glasshouse is widely used for short-term projects, often with a duration of 2-3 months. Air temperature is measured and controlled by an automated system at user-defined targets (+/- 4 degrees C) within each compartment. The concentration of atmospheric carbon dioxide is controlled within each compartment using a system of infrared gas analyzers and carbon dioxide injectors. Supplementary lighting will be installed in 2013.
    ---

    Contact: Renee Smith (technician, R.Smith@uws.edu.au), John Drake (Post-doc, je.drake@uws.edu.au), Mike Aspinwall (Post-doc, m.aspinwall@uws.edu.au).

    # References: 

    Smith, R. A., J. D. Lewis, O. Ghannoum, and D. T. Tissue. 2012. Leaf structural responses to pre-industrial, current and elevated atmospheric CO2 and temperature affect leaf function in Eucalyptus sideroxylon. Functional Plant Biology 39:285-296.

    Ghannoum, O., N. G. Phillips, J. P. Conroy, R. A. Smith, R. D. Attard, R. Woodfield, B. A. Logan, J. D. Lewis, and D. T. Tissue. 2010. Exposure to preindustrial, current and future atmospheric CO2 and temperature differentially affects growth and photosynthesis in Eucalyptus. Global Change Biology 16:303-319.



    # Data organisation overview

    There have been a large number of relatively short-duration experiments in the Glasshouse S30 facility, often with multiple nested projects within each experiment.  The file naming convention captures this hierarchy.



    # File Naming Convention

    Convention: GHS30_<EXPERIMENT>_<PROJECT>_<VARIABLE COLLECTION CODE>_<DATA PROCESSING>_<DATE or DATERANGE>[_<VERSION>].<filetype>

The resulting HTML looks like this:

![](/wp-content/uploads/2013/09/wpid-research-context-rdf.html_research-context-rdf_html_meaf00e9.png)

But wait, there's more! Inside the human-readable HTML page is some
machine-readable code to say what this page is about using linked-data
principles. The best way I have been able to work out how to describe a
facility is using the Eagle-I ontology, where I think the appropriate
term for what HIE calls a facility is 'core-laboratory'. You can [browse
the
ontology](https://search.eagle-i.net/model/#q=Core%20Laboratory&t=http://vivoweb.org/ontology/core%23CoreLaboratory&of=score)
and tell me if I'm right. This says that the glasshouse facilty is a
type of core-laboratory.

    <section
    resource="http://uws.edu.au/facilities/glasshouse-s30.html"
    typeof="http://vivoweb.org/ontology/core#CoreLaboratory">
    <h1 property="dc:title">Glasshouse facility at UWS
    Hawkesbury building S30</h1>

(I'm not an RDF expert so if I have this wrong somebody please tell me!
And yes, I know there are issues to consider here What URIs should we
use for naming facilities and other contextual things? Should we use
Handles? PURLS? Plain old URLs like the one above?)

\
The code that produced this snippet is really simple, but I did have to
code it:

    def hook_postconvert_semantics():
        for p in pages:
            if p.typeOf <> None:
                p.html = "\n\n<section resource='http://hie.uws.edu.au/research-context/%s' \
                    typeof='%s'>\n\n%s\n\n<section>\n\n" % (p.url, types[p.typeOf], p.html)

Now, the part that I'm quite excited about is that if you point an RDFa
distiller at this you get the following. This is JSON-LD format which is
(sort of) RDF wrapped up in JSON. Part time programmers like me often
find RDF difficult to deal with, but everyone loves JSON, you can slurp
it up into a variable in your language of choice and access the data
using native idioms.

    {
        "@context": {
            "dcterms": "http://purl.org/dc/terms/"
        }, 
        "@graph": [
          
            {
                "@id": "facilities/glasshouse-s30.html", 
                "@type": "http://vivoweb.org/ontology/core#CoreLaboratory", 
                "http://www.w3.org/2003/01/geo/wgs84_pos#long": {
                    "@value": "150.7465", 
                    "@language": "en"
                }, 
                "dcterms:title": {
                    "@value": "Glasshouse facility at UWS Hawkesbury building S30", 
                    "@language": "en"
                }, 
                "http://www.w3.org/2003/01/geo/wgs84_pos#lat": {
                    "@value": "-33.6112", 
                    "@language": "en"
                }
            }
        ]

That might look horrible to some, but should be easy for our third-year
comp-sci students to deal with. Iterate over the items in the @graph
array, find those where @type is equal to
"<http://vivoweb.org/ontology/core#CoreLaboratory>", get the title, and
build a drop-down list for the user, to associate their data file with
this facility (using the ID). This potentially lets us de-couple our
file management app from our HIEv repository, from our Research Data
repository, and let them all share the same 'source of truth' about
research context. In library terms, my hacked-up version of Gerry's
website is acting as a name-authority for entities in the HIE space.

There is a lot more to cover here, including how experiments are
associated with facilities, and how, when a user publishes a data set
from HIEv a file can be linked to a facility/experiment combination
using a relation “wasGeneratedBy” from the World Wide Web Consortium's
[PROV](http://www.w3.org/TR/2013/REC-prov-o-20130430/) (provenance)
ontology.

As I noted above, the markdown based approach is not going to work for
some user communities. What is needed to support this general design
pattern, assuming that one would want to, is some kind of combination of
a research-context database application and a web content management
system (CMS). A few people, including Jodi Schneider suggested I look at
Drupal, the open source CMS. Drupal does 'do' RDF, but [not without some
serious
configuration](http://lin-clark.com/blog/drupal-8-now-has-schemaorg-rdf-mappings-dont-pop-champagne-yet).

Jodi also pointed me to VIVO, which is used for describing research
networks, usually focussing on people more than on infrastructure or
context. I remember from a few years ago a presentation from one of the
VIVO people that said very explicitly that VIVO was not designed to be a
source of primary data so I wondered if it was appropriate to even
consider it as a place to enter, rather than index and display data. The
VIVO wiki says [it is
possible](https://wiki.duraspace.org/display/VIVO/Manual+Data+Entry),
but building a site with the same kind of content as Gerry's would be a
lot of work just as it would be in Drupal.

Oh, and those answers? Well thanks to Arif Shaonn from the University of
New South Wales, I know that <http://www.w3.org/ns/prov#Activity> is
probably a good general type for experiments (no, I'm going to define an
ontology of my own, I already have enough pets).

And **where's my semantic web?** Well, I think we may need to build a
little more proof-of-concept infrastructure to see if the idea of a
research-context CMS acting as a source of truth for metadata makes
sense, and if so, make the case for building it as part of future
eResearch data-management apps.

My dodgy code including the input and output files for a small part of
Gerry's website is [on
github](https://github.com/ptsefton/experiment-rescontext), to run it
you'll need to [install Poole
first](https://bitbucket.org/obensonne/poole).

</section>
</article>

