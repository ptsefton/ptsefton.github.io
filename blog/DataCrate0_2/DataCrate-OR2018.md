---
title:  >
  DataCrate - a progress report on creating a data packaging format for research data
date: 2018-06-29
slug: DataCrate_2018
category: Repositories
author: ptsefton
---

This is a presentation that I gave at [Open Repositories 2018 in Bozeman Montana](http://www.or2018.net/). I have made some minor edits to slides and updated the slide notes to reflect what I spoke about.

I put together the presentation and wrote the spec, but lots of people have contributed:


Thanks to:
-  Cameron Neylon for being customer number one

-  Liz Stokes for working on metadata crosswalking/mapping

-  Mike Lake for coding and ideas

-  Conal Tuohy, Duncan Loxton & Eoghan Ó Carragáin for help with the draft spec & Katrin Leinweber for edits

-  Amir Aryani for discussions about metadata

-  Gerard Devine and Christian Evenhuis for starting to build tools

-  Katrina Trewin for grooming data in Farms to Freeways

-  The team at Artefactual for feedback


And the mainly Sydney-based metadata group who met in the leadup to this work
Piyachat Ratana, Sharyn Wise, Michael Lynch, Craig Hamilton, Vicki Picasso, Gerard Devine, Katrin Trewin, Ingrid Mason, Peter Bugeia



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.001.jpeg' alt='DataCrate - a progress report on creating a data packaging format for research data

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This presentation is about a developing standard for research data packaging, DataCrate, which will be at version 0.2 or higher by the time of OR 2018. The purpose of DataCrate is to allow distribution of data sets via a single file (using Zip, TAR or a disc image format as appropriate) and/or via a URL with integrity checks. Another goal is to be able to host a dataset on a web server with appropriate access controls in a way that allows people to inspect the data set via an HTML page which summarises the data set and (optionally) describes the contents in detail, file by file or directory by directory.

The aim is to maximise the utility of the data for researchers (including researchers’ ‘future selves’). Given that a researcher has found a DataCrate package they should be able to tell what it is, how the data may be used and what all the files contain, to enable discovery of the data by exposing metadata as widely as possible and to enable automated ingest into repositories or catalogues.

DataCrate uses existing standards including schema.org and ontologies from the SPAR ontologies, as well as Bagit for data packaging.







</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.002.jpeg' alt='' border="1" />

<details open="open">

<summary>

### Notes

</summary>

The image on this slide  is of a container ship carrying standardised shipping containers.

What is DataCrate?

It’s a standard for Packaging data for distribution, built on other standards.  We created this standard because there was no general purpose way of shipping arbitrary research data
 with human readable metadata.


Image
[source](
https://www.flickr.com/photos/volvob12b/27321575845/in/photolist-HCjdCv-cjfUe3-LJwM9q-9njAr9-9ngy2K-9ngxBZ-tHaVtw-9ngzv4-QVwfJJ-RxKFMH-RpcY6S-eRdT6Q-XGDTVG-vcK3GH-9zc5oo-cjfR8q-cnzqCQ-vvwYTC-zmsA82-ddUxfq-bbts1K-HXcKUS-24HMuUK-F9sD5A-uzDKoq-bbtrmX-A8S742-A8SXie-JnWNPg-xiTosq-xhkiDG-xkbohz-yLDPn6-xiZtco-wnQSV9-xkeHki-x34aJU-wnzTFh-wnB2SL-xiR1Bq-HPp9VF-wnNzfT-xhuVXA-x3bCWq-x3byuC-Nkc2vV-PosH4z-CZHcba-QYUL7t-JLujsJ
).

Image license:  <
https://creativecommons.org/publicdomain/zero/1.0/>




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.003.jpeg' alt='Requirements

A packaging/display format with:
An HTML manifest that describes as many of the files in a package as possible
Linked-data semantics in JSON-LD
Checksums, data by reference
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This is a summary of the requirements for the system - having something, an HTML page,  that a person can read that explains what the package *contains* is important. How many times have we all opened a zipped data file from the Downloads folder and tried to work out what it is and how to cite it?



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.004.jpeg' alt='Prior packaging art
Frictionless data packages
Not JSON-LD
Packaging semantics are implied not explicit
Research Object + BagIt
Semantics oriented towards very nuanced human authorship roles
Uses many annotation files

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

The [DataCrate github project](https://github.com/UTS-eResearch/datacrate/blob/master/README.md) goes through some of the background research we did into other formats. In summary - we didn’t use the Frictionless data packaging because it was not based on recognized metadata standards. And the Research Object + BagIt standard had some unresolved issues around its use of BagIt, had a complicated multi-file system for describing files in JSON-LD and used metadata which was mainly specialised around nuances to do with authorship, but that said, we are
aligning
 DataCrate with it where possible.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.005.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

In DataCrate there is an index.html file in the root of each package
 which is designed to:

*  Show a datacite citation if
there is enough metadata to make one
*  Describe the dataset at a high level


Packages are suitable for web display, or for zipping (or otherwise packaging) for distribution.




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.006.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

There is a dataset-level metadata description, presented as a table.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.007.jpeg' alt='
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

In this talk I want to highlight a point about name ambiguity which serves to illustrate why using a linked data approach is useful.

 Here’s a dataset by four authors where the potential for name ambiguity is very high as the family names are very common.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.008.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide was not in the presentation I gave at OR2018 - it is a screenshot showing the first of ten pages of [results in Google Scholar matching profiles for J. Lu](https://scholar.google.com.au/citations?view_op=search_authors&mauthors=Lu,+j&hl=en&oi=ao).




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.009.jpeg' alt='
&quot;creator&quot;: [
        {

&quot;@id&quot;: &quot;http://orcid.org/0000-0002-8367-6908&quot;

},
        {
          &quot;@id&quot;: &quot;http://orcid.org/0000-0003-0690-4732&quot;
        },
        {
          &quot;@id&quot;: &quot;http://orcid.org/0000-0003-3960-0583&quot;
        },
        {
          &quot;@id&quot;: &quot;https://orcid.org/0000-0002-6953-3986&quot;
        }
      ],

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Behind the scenes there is JSON-LD that links these people using their ORCIDs. This does away with the ambiguity completely.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.010.jpeg' alt='{
      &quot;@id&quot;: &quot;http://orcid.org/0000-0003-0690-4732&quot;,
      &quot;@type&quot;: &quot;Person&quot;,
      &quot;affiliation&quot;: &quot;University of Technology Sydney&quot;,
      &quot;familyName&quot;: &quot;Lu&quot;,
      &quot;givenName&quot;: &quot;J&quot;,
      &quot;name&quot;: &quot;J. Lu&quot;
    },

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This is what a description looks like  in JSON-LD for [Prof Jie Lu](https://www.uts.edu.au/staff/jie.lu) from UTS.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.011.jpeg' alt='' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Here is a screen shot of the same information

Note that her name is linked - the link resolves to Prof Lu’s page at Orcid,
preventing her work from being lost amongst the many other instances of the name
Lu, J. in the literature.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.012.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide shows
a screenshot of the HTML summary of information about a file from a [DataCrate of speleological data](https://data.research.uts.edu.au/examples/v0.2/Victoria_Arch_pub/).

What do the little arrows mean? They’re offsite links.
The link on [encodingFormat](https://schema.org/encodingFormat) points to the documentation for the schema.org property `encodingFormat`.




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.013.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide show a screenshot of the Schema.org defitintion for encodingFormat.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.014.jpeg' alt='' border="1" />

<details open="open">

<summary>

### Notes

</summary>

But even more interestingly, if we follow the link to Polygon File Format we get to the [UK National
Archives’ Pronom Registry which describes the .ply format](http://www.nationalarchives.gov.uk/PRONOM/fmt/831).

Next I go on to look very briefly at how this DataCrate was made.





</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.015.jpeg' alt='

https://github.com/richardlehane/siegfried
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

[CalcyteJS], the tool used to
generate the DataCrate we’re looking at
 uses [Siegfried](
https://github.com/richardlehane/siegfried)

by Richard Lehane at the State Archives of NSW to characterise files.




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.016.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide, which shows [a map of the USA with states coloured red, blue and grey](https://upload.wikimedia.org/wikipedia/commons/6/6e/U.S._Lt._Governors_by_party_affiliation_2009.jpg)
has nothing to do with datacrate is designed to bring to mind
 the concept of...


Image

</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.017.jpeg' alt='
Affiliation
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

… affiliation.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.018.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Trying to represent affiliation is complex
 and has been a problem in metadata systems for a long time. On paper it is often represented by superscipt indices.

This slide shows a screenshot of a [paper at Plosone](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0181020) where
13 authors have 11 affiliations to sub-parts of organizations (mostly universisities).




</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.019.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

To create this DataCrate I used [CalcyteJS] – a work-in-progress tool we’re developing at UTS.





</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.020.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide shows how the creators of the data set are listed in an Excel spreadsheet that describes the data set. This is in the “Collection” tab that describes the entire datacrate - each of the creators of the dataset is listed.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.021.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide shows a screenshot of the  Person tab where each person is described, and their affiliations listed using shorthand IDs as in the paper (1 … n).



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.022.jpeg' alt='  {   &quot;@id&quot;: &quot;http://orcid.org/0000-0002-6756-6119&quot;,
      &quot;@type&quot;: &quot;Person&quot;,
      &quot;affiliation&quot;: [{
&quot;@id&quot;: &quot;1&quot;
}, {&quot;@id&quot;: &quot;2&quot;}, {&quot;@id&quot;: &quot;3&quot;}, {&quot;@id&quot;: &quot;4&quot;}],
      &quot;family Name&quot;: &quot;Agar&quot;,
      &quot;given Name&quot;: &quot;Meera&quot;,
      &quot;identifier&quot;: &quot;http://orcid.org/0000-0002-6756-6119&quot;,
      &quot;name&quot;: &quot;Meera Agar&quot;
    },

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

This slide shows is a JSON-LD view of the data for the person with the most affiliations.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.023.jpeg' alt='{    &quot;@id&quot;: &quot;1&quot;,
      &quot;@type&quot;: &quot;Organization&quot;,
      &quot;address&quot;: &quot;Ultimo&quot;,
      &quot;country&quot;: &quot;Australia&quot;,
      &quot;identifier&quot;: &quot;1&quot;,
      &quot;memberOf&quot;: {
&quot;@id&quot;: &quot;http://uts.edu.au&quot;
},
      &quot;name&quot;: &quot;Faculty of Health, University of Technology Sydney&quot;,
      &quot;state&quot;: &quot;New South Wales (NSW)”
},

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Here’s a description of one of the affiliations,
“Faculty of Health, University of Technology Sydney”
which is a sub-part of an
 organisation - this relationship is encoded using the schema.org property [memberOf](
https://schema.org/memberOf), pointing to UTS, which is the organisation that our administrators would like people to use as their affiliation.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.024.jpeg' alt='
{
      &quot;@id&quot;: &quot;http://uts.edu.au&quot;,
      &quot;@type&quot;: &quot;Organization&quot;,
      &quot;identifier&quot;: &quot;http://uts.edu.au&quot;,
      &quot;name&quot;: &quot;University of Technology Sydney&quot;
    },

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

And here is the metadata for UTS.

The point of this little demo of complex affiliation is to show that a linked data approach lets us describe
complex
 things in a way that make it easy for machines to track, and via the HTML index page in each DataCrate, for people to explore by
clicking
 links.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.025.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

I also wanted to demonstrate how an entire web-based collection can be exported as a datacrate. This is a screenshot of the [Farms to Freeways](http://omeka.uws.edu.au/farmstofreeways/) repository, created by Katrina Trewin at Western Sydney University using some funding from the Australian National Data Service, made with the [Omeka Classic](
https://omeka.org/classic/
) software.

From the about page:

> This research project, titled Western Sydney Women's Oral History Project
'From farms to freeways: Women's memories of Western Sydney' , sought to analyse
the experiences of women who had lived in the Blacktown and Penrith areas since
the early 1950s, including their responses to social changes brought about by
rapid suburbanisation in the Western Sydney region in the post-war period.
> <http://omeka.uws.edu.au/farmstofreeways/>



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.026.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Using some [proof of concept code](
https://github.com/UTS-eResearch/omeka-datacrate-tools
)
 I exported the data from the Omeka  site.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.027.jpeg' alt='
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

In to a Data Crate which is accessible <
https://data.research.uts.edu.au/examples/v0.2/farms_to_freeways/
>

This demonstrates the use of the [Portland Common Data Model](https://pcdm.org/2016/04/18/models) to describe a [collection](
http://pcdm.org/models#Collection)
 of data. The resulting DataCrate can be used, via its index.html page like a static version of the Omeka site, but could also be reconstituted into a new repository, such as the [new “S” version of Omeka](https://omeka.org/s/).



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.028.jpeg' alt='' border="1" />

<details open="open">

<summary>

### Notes

</summary>

Another thing I wanted to show was that adding thumbnails was easy, because of
the use of linked data. This image shows a screenshot of a mocked up dataset
where there is a microscope image that has a thumbnail. In order to implement
thumbnails, all that was needed was to add a few lines to the [calcytejs] tool
to look for the schema.org [thumbnail](https://schema.org/thumbnail) property in
the CATALOG.json file and to render that as an image. This demonstrates the
power of taking a semantic approach and drawing on an existing standard, rather
than  making up our own property, or *worse*, using conventions such as magic
filenames.



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.029.jpeg' alt='A walk through the
spec



' border="1" />

<details open="open">

<summary>

### Notes

</summary>

In the talk I briefly scrolled through [version 0.2 of the DataCrate specification](
https://github.com/UTS-eResearch/datacrate/blob/master/spec/0.2/data_crate_specification_v0.2.md)





</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.030.jpeg' alt='

' border="1" />

<details open="open">

<summary>

### Notes

</summary>

In looking at the spec I pointed out that
 DataCrate also (optionally) uses the BagitSpec to lay-out the files in the DataCrate, with checksums



</details>
</section>
<br/><br/><hr/>



<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}DataCrate-OR2018 (3).pptx_md.031.jpeg' alt='Help wanted
Spec Review
Additional coverage  (eg representing software provenance, recommended ontologies for scientific data)
Tooling - write a data crate exporter
' border="1" />

<details open="open">

<summary>

### Notes

</summary>

The final slide was a request for help - we’d like people to read and comment on the DataCrate spec and we’d love more tool-makers to start building tools.

## Tool summary

[HIEv DataCrate](https://github.com/gdevine/hiev_datacrate) by Gerry Devine: at the Hawkesbury Institute for the Environment at Western Sydney University, a bespoke data capture application (HIEv) harvests a wide range of environmental data (and associated file level metadata) from both automated sensor networks and analysed datasets generated by researchers. Leveraging built-in APIs within the HIEv a new packaging function has been developed, allowing for selected datasets to be identified and packaged in the DataCrate standard, complete with metadata automatically exported from the HIEv metadata holdings into the JSON-LD format. Going forward this will allow datasets within HIEv to be published regularly and in an automated fashion, in a format that will increase their potential for reuse.

Calcytejs
 is a command line tool for packaging data into DataCrate developed at the University of Technology Sydney which allows researchers to describe any data set via the use of spreadsheets which the tool auto-creates in a directory tree.

Omeka DataCrate Tools
 is a collection proof of concept tool for exporting data from Omeka Classic repositories into the DataCrate format I wrote  in Python.




</details>
</section>
<br/><br/><hr/>

[calcytejs]: https://code.research.uts.edu.au/eresearch/CalcyteJS
