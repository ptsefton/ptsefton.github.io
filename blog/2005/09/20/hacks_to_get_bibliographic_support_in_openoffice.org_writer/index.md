---
Title: "Hacks to get bibliographic support in OpenOffice.org Writer"
Slug: hacks_to_get_bibliographic_support_in_openoffice.org_writer
Date: 2005-09-20

---
<div>

OpenOffice.org has some good points, and some bad points. Then there's
the bibliography database; which ranks as horrific rather than merely
bad.

Bruce D'Arcus says:

> This point is clear in higher ed. Despite being a co-project lead for
> an offical OOo project, I still cannot recommend the suite to my
> colleagues, which is pretty much the point at which both OOo and Linux
> might become a real option for them. Without good bibliographic
> support, OOo simply has no chance in higher ed.

> <http://netapps.muohio.edu/blogs/darcusb/darcusb/archives/2005/09/19/the-state-of-openoffice>

In the [ICE project](http://www.usq.edu.au/dec/staff/ice.htm) we're
working with courseware where bibliographic support is important.
Surprisingly enough some of our pilot users don't currently use
bibliographic software, but then some of them didn't [use
styles](http://ptsefton.com/blog/2005/03/02/use_styles) either.

As the project lead on a project that's built around OpenOffice.org, in
higher ed., I'm looking for a solution that will let my colleagues work
with OOo, and I'm confident that at least within the context of the ICE
project we will be able to get people working.

Here's my current thinking on how:

1.  We use will use EndNote as the reference manager. Apparently it has
    some problems, but we have a campus license.

    But EndNote doesn't work with OpenOffice.org to format citations or
    bibliographies because Writer's rtf export does not support the
    styles we are using, so we have a seek another solution.

2.  A user will maintain their library in EndNote and paste temporary
    in-text citations into their ICE documents, in OOo Writer. When
    they're ready to have a bibliography generated they will export
    their library to a place ICE can find it.

    (When we get around to MS Word support Word uers can just use
    EndNote directly on their Word docs if they choose, or do it the way
    I'm describing here)

3.  Behind the scenes, ICE will convert their library to
    [MODS](http://www.loc.gov/standards/mods/) format, using
    [Bibutils](http://www.scripps.edu/~cdputnam/software/bibutils/bibutils.html)
    and crack open all their documents, turn the citations into an XML
    format, either based on DocBook or a new proposed format for
    OpenOffice.org, then create a bibliography in a separate
    OpenDocument document, either for an entire course or
    module-by-module.

    To perform this amazing feat we are likely to use a system called
    [CiteProc](http://bibliographic.openoffice.org/citeproc/index.html),
    created by the aforementioned Bruce D'Arcus. Bruce has devised a
    citation language (CSL) that is designed to be independent of
    particular software implementations, so you can specify citation and
    bibliographic formats once only and have them work in any output
    format. We'll see how it goes in practice.

All this is still a bit speculative, but the experiments I have
performed so far are promising, and the general approach should be able
to evolve to deal with software other than EndNote, and improvements to
OpenOffice.org.

And yes I know this is not an elegant solution, but it's a first step,
and it should mean we can use OpenOffice.org in relative comfort while
the OpenOffice.org community, us included, goes through the proper
process to add real bibliographic support.

I think Bruce has a vision of a suite of open source tools and shared
bibliographic data that will completely eclipse EndNote and other
commercial tools, and we'd love to help.

****

</div>
