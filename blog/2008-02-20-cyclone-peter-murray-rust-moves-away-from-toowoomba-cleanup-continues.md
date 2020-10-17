---
Author: ptsefton
Comments: true
Date: 2008-02-20 01:26:43+00:00
Slug: cyclone-peter-murray-rust-moves-away-from-toowoomba-cleanup-continues

Title: Cyclone Peter Murray-Rust moves away from Toowoomba. Cleanup continues.
Wordpress_id: 86
---

<div>

<div class="page-toc">

</div>

<div>

Last week we hosted Peter Murray-Rust in Toowoomba. The ICE team have
been busy getting ready for some other visitors, so I have not had time
to write about the visit. Peter has blogged about his stay a few times,
describing it as [intensive talk and
hacking](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=982). Intensive
indeed.

He talked about ICE <span class="spCh spChx2013">–</span> emphasis is
mine:

> I<span class="spCh spChx2019">’</span>ve had the chance to look
> closely at[<span class="Strong_20_Emphasis"> ICE</span>: The
> Integrated Content Environment](http://ice.usq.edu.au/)- an authoring
> environment for academic material. USQ eat their own dog-food and over
> 100 academic staff at USQ use it routinely for authoring their course
> material. USQ is very committed to high-quality distance education -
> they have an impressive enrollment from overseas and they put a lot of
> work into the material which supports it. So their material can be
> repurposed as notes, lecturer<span class="spCh spChx2019">’</span>s
> copies, slides, summaries, etc. All this is managed through
> stylesheets - which are the key to ICE. The content is written once
> but delivered in many ways. Because the material is in XML it is also
> possible to amend it with XML-aware tools or to generate new material
> programmatically. A key aspect is that the structure of the
> document(s) can be managed in XML. *So I am now convinced that for
> academic work it is (a) fit-for-purpose (b) reconfigurable (c)
> powerful. It<span class="spCh spChx2019">’</span>s still <span
> class="spCh spChx201c">“</span>early-adopter<span
> class="spCh spChx201d">”</span> for theses, but as it can do so many
> new things I can<span class="spCh spChx2019">’</span>t see any real
> competition.*
>
> [<span style="font-style:normal; "><span
> class="T3">http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=982</span></span>](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=982)<span
> style="font-style:normal; "><span class="T3"> </span></span>

Here's a quick summary of what the ICE team did with Peter on his visi.

We introduced Peter to ICE, and showed him how to blog with it. We'll be
very interested in feedback on this, does it work? Is it better for some
posts than the WordPress editor? If so, which types of post? We'll also
try some other collaboration with Peter & team.

**Oliver Lucido** extended our work on embedding Chemical Markup
Language (CML) into publications. CML lets your describe molecules and
reactions and the like. We've come a long way since [my first post on
CML](http://ptsefton.com/blog/2007/06/22/cml_demo/) last year. You can
now put a CML file into your working directory, and ICE will turn it
into a variety of formats for you automatically. See [Daniel's
screencast.](http://ice.usq.edu.au/presentations/demos/cml_ice_ice.htm)
Now we start to think about similar services for other disciplines, drop
me a line or comment here if you have any suggestions.

Also related to CML, PMR is interested in being able to create what he
calls a *data overlay journal*, taking bits of data gathered from
various publications and aggregating them by type. So **Ron Ward**
worked on something that turns ATOM feeds with chemistry in them into
OpenDocument Format documents. Peter seemed pleased with the results,
which are really just a proof of concept for now. Using Ron's new code
we scraped some data from the Crystaleye service, turned into an ODF,
then PMR sent it to [his
blog](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=979) over the Atom
Publishing Protocol. You can't see the PDF version just yet, or interact
with the molecules via JMOL but we'll sort that out soon. (When I say
'we' obviously I mean Oliver.)

We're wondering if this might be useful in other situations, like for
celebrity bloggers who want to turn their blog into a book. Point it at
a feed of the relevant content and it will put it into a word processing
format you can edit and send off to a publisher. Might also be useful
when quoting web material. Me, I'd like to be able to get hold of posts
from sources that I quote often in ODF rather than having to copy and
paste HTML and re-style it.

Peter supplied a chemistry thesis and with a bit of word processor
magic, I broke it up into a number of chapters which we fed into ICE.
Daniel de Byl did a bit more work to fix up some character encoding
issues. Oliver worked with Peter to find the chemistry that's embedded
in the thesis, which is authored using an application called ChemDraw.
Peter has some code that can break open the proprietary ChemDraw format
and extract open standard CML, and Oliver was able to hook this in to
ICE to automate the process: find the ChemDraw pictures, turn them into
CML and then re-render molecules using non-proprietary open source
software. Still a lot of rough edges, but when Daniel's back from a
break in a couple of weeks we will show how ICE can be used to create a
thesis in both HTML **and** PDF with the data linked-in and machine
accessible.

Peter gave a spirited and inspiring performance of his genre of talk,
this time on semantic publishing. I see lots of potential for the
semantic web in some domains, particularly where the data are very
bounded and structured like chemistry. But rather than trying to deal
with the **huge mess of unstructured** data out there, the ICE team try
to find or create the right tools to help people create a huge **mess of
structured data**, with some semantic information embedded. It's slow
work, but PMR thinks 2008 is the year some of this will start to break
out of the labs.

Peter presents using his presentation toolkit, which contains lots of
material on a range of topics which he jumps around during the talk.

> I gave my talk in HTML as normal - a series of ca. 100 major topic
> with 2-20 <span class="spCh spChx201c">“</span>slides<span
> class="spCh spChx201d">”</span> under each. I select each <span
> class="spCh spChx201c">“</span>slide<span
> class="spCh spChx201d">”</span> as I go along and stop at the time
> limit. At least this means I never overrun. The system has evolved
> over the years and now has a vertical menu for each topic and a
> horizontal one within the topic.
>
> <http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=960>

I have been looking at how we might be able to capture Peter's slides in
ICE, and provide an interface that can assemble them into presentation
packages (not necessarily linear). One thing that would be nice is for
the slides themselves to have some notes. I'm going to see if we can do
something like the ICE brochure where there is a [document you can
read](http://ice.usq.edu.au/introduction/about.htm), with a [slide
presentation](http://ice.usq.edu.au/introduction/about.slide.htm) that
is automagically derived from it.

I was feeling a bit weathered after all of that hence the title of this
post.

I was curious about cyclone naming. Turns out that Pete is on the list
for a cyclone in the Brisbane region. The way I read it, it's about
40^th^ on the list. Found this:

> Requests by the public for tropical cyclone names
>
> The Bureau of Meteorology receives many requests from the public to
> name Tropical Cyclones after themselves, friends, etc. The Bureau is
> unable to grant all these requests as they far out-number the number
> of Tropical Cyclones that occur in the Australian region.
>
> The Bureau will only accept requests received in writing (not e-mail).
> The request cannot be immediately granted but the name will be added
> to a supplementary list. When a name is retired of similar gender and
> initial, a name can be included from this supplementary list (subject
> to checks to ensure it is not on the Southern Hemisphere retired name
> list or offensive in any of the languages of our intern ational
> neighbours.)\
> Note that it can take many decades for a suitable slot to become
> available, then a further 10-20 years for the names to cycle through,
> so it is likely to be well over 50 years before your requested name is
> allocated to a cyclone.
>
> <http://www.bom.gov.au/weather/cyclone/about/cyclone-names.shtml>

</div>

</div>
