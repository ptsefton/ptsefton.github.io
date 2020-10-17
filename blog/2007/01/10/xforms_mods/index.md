---
Title: "Unfinished: Editing MODS metadata using XForms"
Slug: xforms_mods
Date: 2007-01-10

---
<div>

In a similar vein to my [previous
post](http://ptsefton.com/blog/2007/01/10/tinymce), here's a bit of
unfinished exploration. This time, relevant to the [RUBRIC
project](http://rubric.edu.au/).

Thinking about repository ingestion services, I began to wonder if there
was a better way of mapping from an XML schema to an HTML form?

-   [FEZ](http://sourceforge.net/projects/fez/) does it using a very
    complex HTML interface, which may have usability issues, and (I
    think) stores the mapping rules in a database. It's a great
    achievement for the FEZ developers to have performed this amazing
    feat using PHP but I fear that it may prove to be a maintenance
    headache in the longer term and I am not of the opinion that this
    kind of configuration needs to be point and click in any case.

-   [VTLS Valet](http://www.vtls.com/Products/)does it using a
    rudimentary intermediate XML format that you transform into XML
    metadata via XSLT. VALET is one way only, and does not use the
    Fedora repository back-end for its workflow.

-   [VTLS Vital](http://www.vtls.com/Products/vital.shtml) doesn't even
    try. It uses an XML editor. I have had the opportunity to express my
    opinion on this matter via the ARROW developers group. I think this
    is not acceptable, and there needs to be a way of editing complex
    metadata in a browser (and not through a generic XML editor
    component either! ).

-   [DSpace](http://www.dspace.org/) and [GNU
    Eprints](http://www.eprints.org/software/)  both do it using
    configuration files that cannot deal with hierarchies in metadata. I
    have [written
    before](http://ptsefton.com/blog/2006/06/06/the_affiliation_issue_in_institutional_repository_software)
    about how flat metadata causes problems.

I like the idea of using configuration files for this kind of work, as
they are easy to version control, and typically more robust than
elaborate interface code.

A bit of poking around led me to XForms, a W3C recommendation with very
limited support.

Even though browser support is still a way off  XForms does have ways of
expressing mapping rues from an example data document to a forms
interface. I used the free [FormFaces](http://www.formfaces.com/)
software which is a single Javascript file that magically turns your
browser into an XForms engine.

[Here's my unfinished simple
demo](http://ptsefton.com/files/formfaces-unfinished/xforms-example.html).
The html page loads a [mods data
file](http://ptsefton.com/files/formfaces-unfinished/data.xml) and rules
in the page map it to form widgets. You can't save the data anywhere,
but there are buttons there that allow you to add new subjects – and yes
it does deal with hierarchy, so it should be OK with t[he affiliation
issue](http://ptsefton.com/blog/2006/06/06/the_affiliation_issue_in_institutional_repository_software).
Worth exploring, if anyone has the time.

</div>
