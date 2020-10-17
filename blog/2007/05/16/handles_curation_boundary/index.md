---
Title: "Another good use for handles: identifying items in the ICE content management system throughout thier lifecycle"
Slug: handles_curation_boundary
Date: 2007-05-16

---
<div>

Back to talking about persistent identifiers, specifically handles, and
this time it's to do with the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project.

I have mentioned that I was a handles
[skeptic](http://ptsefton.com/blog/2006/11/01/repository-maintenance),
but now I'm [coming
around](http://ptsefton.com/blog/2007/03/16/killer_handles).

In writing-up how [ICE](http://ice.usq.edu.au/) can be used for a
multimedia thesis for my paper at [ETD
2007](http://epc.ub.uu.se/etd2007/) it became clear that there is a
workflow issue to with identifying and linking to multimedia content. My
paper is on in [this
session](http://epc.ub.uu.se/etd2007/sessions/1.html) <span
class="spCh spChx2013">–</span> maybe the full text will show up there
at some point.

The indetifier / linking problem is that right from the draft stage you
want to be able to distribute a thesis to supervisors or reviewers in
two forms; online, and in print.

One crucial stage is the examination stage; how can we deal with
distribution? The easy way is electronically. If you're sending to
reviewers electronically then the multimedia will just be there, and it
can be linked relative to the text. But what about a printed version?
The print copy should include URLs that can be used to fetch the media
file. But how does the author know what that URL will be? And who will
change it when the thesis goes into the institutional repository?

These are all issues to do with the [curation
boundary](http://ptsefton.com/blog/2007/02/07/curation-boundary) which
is now documented in an
[article](http://www.ariadne.ac.uk/issue51/treloar-groenewegen/)
(Treloar and Groenewegen 2007).

Enter handles. If everything in an ICE repository had a persistent ID in
the [handles](http://handle.net/) infrastructure then ICE could take
care of the URL for you. All the author would have to do is link to the
media they'd like to include in the usual way, and the ICE system would
make a new handle and update links to use a handle resolver. The result
of all this would be that authors would not have to worry about finding
appropriate copies of their work, the ICE system would be able to take
care of all that, and the URL for a media file that might be out there
in an examiner's copy of the thesis would still work years later even if
the thesis itself has moved around since then.

Without some system like handles the author and/or support staff would
need to be continually editing documents as they moved through different
stages and were distributed for different purposes.

How would this work? (Warning <span class="spCh spChx2013">–</span> gets
detailed and boring from here down)

For my thesis I want to link my piano performance.

1.  Get the sound file and put it in ICE.

2.  Find the file in the ICE file manger.

3.  Right click on the file and copy the URL. It might look something
    like:

        http://localhost:8000/pacakges/phd/media/performance.m4a

4.  Paste into an ICE document with the URL showing up as text either
    in-line or in the references section. Now I've got a text document
    with a link to the sound file that a reader can type in to their web
    browser.

5.  Render the document into PDF using ICE. Magically the URL changes to
    be something like:

        http://resolver.usq.edu.au/hdl/xxxx.x/385329084239058239058

6.  If you visit that URL then it would resolve to something like:

        http://ice-repos.usq.edu.au/pacakges/phd/media/performance.m4a

7.  Behind the scenes ICE will do some technical stuff:

    -   Assign unique ID to the sound file, say 385329084239058239058.
        ICE can be offline to do this step.

    -   When ICE is online, change the link I used to use the handle and
        tell the handle server that this document now lives in my ICE
        repository <span class="spCh spChx2013">–</span> this way I can
        move or rename the file in ICE without breaking the link.

    -   On rendering the document within ICE, change from the handle
        back to a relative link.

    -   On creating a PDF file change the link that I inserted to show a
        handle ID.

    -   On export to a repository change ALL the links within the thesis
        to use handles and change the handle records to resolve to the
        item's new home in the repository,.

    -   On export to an ordinary web server change all the links back to
        ordinary paths.

# <span id="id62"></span>Bibliography

Treloar, A, and D Groenewegen. 2007. ARROW, DART and ARCHER: A Quiver
Full of Research Repository and Related Projects. *Ariadne*.
<http://www.ariadne.ac.uk/issue51/treloar-groenewegen/> (accessed May
16, 2007).

</div>
