---
Title: "Batch tools for repository migration: the RUBRIC solution"
Slug: migration-toolkit
Date: 2007-06-04

---
<div>

On the [RUBRIC project](http://rubric.edu.au/) we do a lot of moving of
data between Institutional Repository software applications. Here are a
few notes on the approach we've taken to data migration and
batch-ingest, I hope that this will eventually be written up as a paper.
There was a poster that Caroline Drury gave at OpenRepositories 2007 but
it doesn't seem to be available online, we'll have to remedy that.

When we started, we tried using the batch-upload that comes with the
Vital repository solution. It uses XML configuration files to describe a
migration scenario. It suffered a little bit from a lack of
documentation, but the biggest problem was more fundamental than that:
it was the complexity of trying to deal with the kinds of real-world
migration we see <span class="spCh spChx2013">–</span> how do you
express what do do with different kinds of files? How to understand some
arbitrary export format from another application? Apart from all that we
also wanted to work with DSpace.

So, I decided to take an alternative approach and to use a general
purpose programming language, rather than struggling with increasingly
complex configuration.

[Corey Wallis](http://techxplorer.com/), who worked too-briefly with the
RUBRIC tech team wrote the first batch of scripts, using Python, with
one script per migration scenario. But the design turned out not to be
optimal, as the scripts ended up needing too many configuration options
and before too long we were approaching the kind of complexity we were
trying to get around. (Not Corey's fault, mine).

Our second attempt has been coded mostly by [Tim McCallum and Bron
Dye](http://techteam.wordpress.com/), using the Unix approach of <span
class="spCh spChx201c">“</span>Do one thing, do it well.<span
class="spCh spChx201d">”</span> [<span
style="vertical-align: super;"><span
class="footnote">1</span></span>](#ftn0).

Let's take the example of migrating content from and
[ADT](http://adt.caul.edu.au/) (Australasian Digital Theses) repository
into a Fedora based repository. We have a proper
[procedure](http://rubric.edu.au/techreports/tech_report-adt_harvest_to_foxml.htm)
up for this if you want all the detail, but I'll run through some of the
main ideas.

We use the DSpace Simple Archive Format as an intermediate file format,
the advantage of this as the instead of going all the way to Fedora, you
can '[Get off at
Redfern](http://www.urbandictionary.com/define.php?term=get+off+at+redfern)'
and put stuff into a DSpace repository or run a few more scripts and go
through terminate at Fedora. The simple archive format uses one
directory per compound object, with a metadata file and all the required
data streams and dead-simple manifest file. We wrote a Python class to
handle the format, so scripts can easily open or create an archive and
do CRUD [<span style="vertical-align: super;"><span
class="footnote">2</span></span>](#ftn1) operations on it.

(When there are better standards for cross-repository ingest and export
formats it will make sense to switch over to using those. More on this
after I visit the UK next week amongst other things I will find out
about [SWORD](http://www.ukoln.ac.uk/repositories/digirep/index/SWORD):

> SWORD (Simple Web-service Offering Repository Deposit) will take
> forward the Deposit protocol developed by a small working group as
> part of the JISC Digital Repositories Programme by implementing it as
> a lightweight web-service in four major repository software platforms:
> EPrints, DSpace, Fedora and IntraLibrary. The existing protocol
> documentation will be finalised by project partners and a prototype
> <span class="spCh spChx2018">‘</span>smart deposit<span
> class="spCh spChx2019">’</span> tool will be developed to facilitate
> easier and more effective population of repositories. The project
> intends to take an iterative approach to developing and revising the
> protocol, web-services and client implementation through evaluative
> testing and feedback mechanisms. Community acceptance and take-up will
> be sought through dissemination activities. The project is led by
> UKOLN, University of Bath, with partners at the University of Wales,
> Aberystwyth, the University of Southampton and Intrallect Ltd. The
> project aims to improve the efficiency and quality of repository
> deposit and to diversity and expedite the options for timely
> population of repositories with content whilst promoting a common
> deposit interface and supporting the Information Environment
> principles of interoperability.
>
> <http://www.ukoln.ac.uk/repositories/digirep/index/SWORD>

)

The first script in a thesis migration is one that's specific to ADT. A
harvester that screen-scrapes ADT pages and extracts metadata <span
class="spCh spChx2013">–</span> we use Python's extensive web-powers for
this. It writes the results out into a the simple archive format.

One of the most useful scripts is one that iterates over an archive and
runs an XSLT transformation. We use this a lot, for taking the
not-terribly-well standardized Dublin Core metatadata used by various
ADT repositories and transforming it to MARCXML format, for transforming
that into a new Dublin Core data stream. (Different sites in the ADT
program use different capitalisation on their dublin core elements names
for example).

Speaking of XSLT, of course we use
[UTF-X](http://utf-x.sourceforge.net/) to unit-test all our XSLT
transformations. What happens is the tech team get advice from [Metadata
Speciast Neil Godfrey](http://metalogger.wordpress.com/tag/metadata/)
about a particular cross-walk they need to code. They encode Neil's
advice as a series of UTF-X tests then write the XSLT. The tests help a
lot in preventing regression and serve to document the crosswalk. Here's
a bit grabbed at random to illustrate what a test looks like:

    <!-- Abstract Element -->

    <utfx:test>

    <utfx:name>Abstract Element</utfx:name>

    <utfx:assert-equal>

    <utfx:source validate="no">

    <eprintsdata >

    <record>

    <field name="abstract">[Introduction]: European Australians have always had trouble</field>

    </record>

    </eprintsdata>

    </utfx:source>

    <utfx:expected validate="no">

    <oai_dc:dc xmlns:dc="http://purl.org/dc/elements/1.1" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc">

    <dc:description>[Introduction]: European Australians have always had trouble</dc:description>

    </oai_dc:dc>   

    </utfx:expected>

    </utfx:assert-equal>

    </utfx:test>

This test shows that in our input data `<field name="abstract">` maps to
the Dublin Core element `<dc:description>`. Not much to it, but it
**really helps** **to do this first**, and then write the XSLT.

(Note that the UTF-X tests aren't up on the public download site yet as
they contain bits of real data <span class="spCh spChx2013">–</span>
it's all open access but we want to confirm with our partners that they
don't mind it being up there)

I love walking in to our office, looking across to someone's computer
and seeing that all the tests are green. Here's a screenshot of some
tests for something or other <span class="spCh spChx2013">–</span> each
line represents one test and the green [OK] means that it passes.

![graphics1](/blog/2007/06/04/migration-toolkit/1.jpg)

We have other scripts to extract full-text from PDF files, and turn the
simple archive format into FOXML for ingest into the Fedora repository
and still more to do various little fixups that seem to be required like
having namespaces declared in special spots in XML files, even though it
shouldn't matter where they are declared.

So far I'm really happy with the *do one thing* approach, and I bet that
even as repositories get better at talking to each other our toolkit
will still be useful for munging data from outside the repository
echo-chamber.

PS.

Just after I wrote this we ran into an issue with namespaces in some of
the data migration stuff for one of our partners; because there was a
substantial bank of unit tests in place the total time to completely
change a couple of stylesheets was only about half an hour, and at the
end of that we're confident that they are working exactly the same way
as they were before.

------------------------------------------------------------------------

<div style="font-size: .9em;">

<div class="footnote">

[1](#ftn0-text)Wikipedia contributors, <span
class="spCh spChx201c">“</span>Unix philosophy - Wikipedia, the free
encyclopedia,<span class="spCh spChx201d">”</span> 2007,
http://en.wikipedia.org/wiki/Unix\_philosophy\#McIlroy:\_A\_Quarter\_Century\_of\_Unix
(accessed June 4, 2007).\

</div>

</div>

------------------------------------------------------------------------

<div style="font-size: .9em;">

<div class="footnote">

[2](#ftn1-text)Wikipedia contributors, <span
class="spCh spChx201c">“</span>Create, read, update and delete -
Wikipedia, the free encyclopedia,<span class="spCh spChx201d">”</span>
http://en.wikipedia.org/wiki/CRUD\_(acronym) (accessed June 4, 2007).\

</div>

</div>

</div>
