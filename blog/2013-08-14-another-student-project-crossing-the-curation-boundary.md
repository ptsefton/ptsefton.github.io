---
Author: ptsefton
Comments: false
Date: 2013-08-14 07:20:06+00:00
Slug: another-student-project-crossing-the-curation-boundary

Title: Another student project – crossing the curation boundary
Wordpress_id: 1760
---

<article>
[![Creative Commons
Licence](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB)\
<span property="dct:title" dct="http://purl.org/dc/terms/">Another
student project – crossing the curation boundary</span> by <span
property="cc:attributionName" cc="http://creativecommons.org/ns#">Peter
Sefton</span> is licensed under a [Creative Commons
Attribution-ShareAlike 3.0 Unported
License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB).

<section>
## Another student project – crossing the curation boundary

I wrote last week about a [student project on HTML
slide-viewing](http://ptsefton.com/2013/08/07/html-slide-presentations-students-to-the-rescue.htm)
for which I'm the client. This week I met with another group to talk
about a project which has more direct application to my job as eResearch
manager at the University of Western Sydney.

The next cohort are going to be looking at a system for getting working
data into an eResearch application. Specifically they are going to have
a go at building an uploader add-in to ownCloud, the Open Source
Dropbox.com-like system so it can feed data to the [HIEv data management
application used by the Hawkesbury Institute for the
Environment](http://eresearch.uws.edu.au/blog/projects/data-capture-for-climate-change-and-energy-research/).
This project was inspired by two things:

-   The fact that we're working with ownCloud in a trial at UWS, and our
    [cr8it data packaging and archiving
    application](http://eresearch.uws.edu.au/blog/projects/capturing-data-and-files-into-a-research-data-catalogue/)
    is based on ownCloud, so getting some students working in this area
    will help us better understand oC and build expertise around UWS.

-   A meeting with Gerry Devine, the data manager at HIE – where he was
    explaining how the institute is trying to improve the quality of
    data in HIEv; at this stage a least they don't want *everything*
    uploaded, and files need to conform to naming
    conventions[^1^](#sdfootnote1sym).

These two things go very nicely together; OwnCloud has a sync-service
like Dropbox that can replicate folders full of files across machines,
via a central server, and a web-view of the files, it has a plugin
architecture so it is easy to add actions to files, and HIEv has an API
that can accept uploads. The application is simple:

-   For certain file types, those that might have data like .csv files,
    show an 'Upload to HIEv' button in the web interface.

-   Present the user with aform, to collect metadata about the file;
    what date range does it represent, which experimental facility is it
    from, via a drop-down list etc (and yes automated metadata
    extraction would be nice to have, if the students have time).

-   Use the metadata to generate file-names based on the metadata.

-   Upload to HIEv.

I think that should be a reasonable scope for a third year assignment,
with plenty of room to add nice add-on features if there's time. A
couple of obvious ones:

-   Extracting metadata from files (eg working out the data-range).

-   Making the metadata form configurable eg with a JSON file.

Beyond that, there is a potentially much more ground-breaking extension
possible. Instead of having to set up the metadata form for every
context of research, what if information about the research context
could be harvested from the web and the user could pick their context
from that?

I have been talking this idea through with various eResearch and
repository people. I submitted it as an idea to the Open Repositories
Dev challenge (late, as usual). Nobody bit, but I think it's important:

> <span lang="en-US">If you are building a repository for </span><span
> lang="en-US">research</span><span lang="en-US"> data, then you need to
> be able to record a lot of contextual metadata about the data being
> collected. For example, you might have some way to attach data to
> instruments . We typically see designs with hierarchies something like
> Facility / Experiment / Dataset / File. Problem is, if you design this
> into the application, for </span><span lang="en-US">example via
> database table then that makes it much harder to adapt to a new domain
> or changing circumstances, where you might have more or fewer levels,
> or hierarchies of experiment or instrument might become important
> etc.</span>
>
> <span lang="en-US">So, what I’d like to see would be a semantic wiki
> or CMS for describing </span><span lang="en-US">research</span><span
> lang="en-US"> </span><span lang="en-US">context</span><span
> lang="en-US"> with some built-in concepts such as “Institute”,
> “Instrument”, “Experiment”, “Study”, “Clinical Trial” (but extensible)
> which could be used by researchers, data librarians and repository
> managers to describe </span><span lang="en-US">research</span><span
> lang="en-US"> </span><span lang="en-US">context</span><span
> lang="en-US"> as a series of pages or nodes, and thus create a series
> of URIs to which data in any repository anywhere can point: the
> </span><span lang="en-US">research</span><span lang="en-US"> data
> repository could then concentrate on managing the data, and link the
> units of data (files, sets, databases, collections) to the
> </span><span lang="en-US">context</span><span lang="en-US"> via RDF
> assertions such as ‘\<file\> generatedBy \<instrument\>’. Describing
> new data sets would involve look-up and auto-completes to the
> </span><span lang="en-US">research</span><span
> lang="en-US">-</span><span lang="en-US">context</span><span
> lang="en-US">-semantic-wiki – a really interesting user interface
> challenge.</span>

It would be great to see someone demonstrate this architecture, building
on a wiki or CMS framework such as Drupal or maybe one of the NoSQL
databases, or maybe as a Fedora 4 app, showing how describing research
context in a flexible way can be de-coupled from one or more
data-repositories. In fact the same principle would apply to lots of
repository metadata – instead of configuring input forms with things
like institutional hierarchies, why not set up semantic web sites that
document research infrastructure and processes and link the forms to
them?

Back to UWS and my work with Gerry Devine. Turns out Gerry has been
working describing the research context for his domain, the Hawkesbury
Institute for the Environment. Gerry has a draft web site which
describes the research context in some detail – all the background you'd
like to have to make sense of a data file full of sensor data about life
in [whole tree
chamber](https://sites.google.com/site/hievuws/facilities/whole-tree-chambers)
number four. It would be great if we could get the metadata in systems
in HIEv pointing to this kind of online resource with statements like
this:

> \<this-file\> generatedBy
> <https://sites.google.com/site/hievuws/facilities/eucface>

To support this we'd meed to add some machine readable metadata to
supplement Gerry's draft human-readable web site. Ideally such a site
would be able to support versioned descriptions of context so you could
link data to the particular configurations of the research context, in
the interests of maximising research integrity as per the [Singapore
Statement](http://www.singaporestatement.org/statement.html):

> ***4. Research Records:*** Researchers should keep clear, accurate
> records of all research in ways that will allow verification and
> replication of their work by others.
>
> ***5. Research Findings:*** Researchers should share data and findings
> openly and promptly, as soon as they have had an opportunity to
> establish priority and ownership claims.

> [1](#sdfootnote1anc)I know there are some strong arguments that IDs
> should be semantically empty – ie that that should not contain
> metadata but there are good practical reasons why data files with good
> names are necessary, and anyway the ID for a data set is not the same
> as its filename when it happens to be on your laptop.

</section>
</article>

