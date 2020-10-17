---
Author: ptsefton
Comments: true
Date: 2013-08-27 06:22:05+00:00
Slug: trip-report-open-repositories-2013
Category: Repositories
Title: 'Trip report: Open Repositories 2013'
Wordpress_id: 1765
---

<article>
<section>
[![Creative Commons
License](/wp-content/uploads/2013/08/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US)\
<span property="dct:title" dct="http://purl.org/dc/terms/">Trip report:
Open Repositories 2013</span> by <span property="cc:attributionName"
cc="http://creativecommons.org/ns#">Peter Sefton</span> is licensed
under a [Creative Commons Attribution-ShareAlike 3.0 Unported
License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).

Update 2015-04-22 - fixed some formatting

From July 8th to July 12th I was on Prince Edward Island in Canada for
the Open Repositories conference. I try to participate as a member of
the OR committee, particularly in matters relating to the developer
challenge which is a key part of the conference, when I can manage the
early-morning conference calls with Europe and the North America. My
trip was funded by my employer, the University of Western Sydney. In
this report I'll talk about the conference overall, the developer
challenge and the paper I presented, written with my colleague Peter
Bugeia.

This was my first trip to Canada. I liked it.

[![wpid-trip-report-for-ptsefton.com-final.html\_trip-report-for-ptsefton.com-final\_html\_1715e81a.jpg](/wp-content/uploads/2013/08/wpid-trip-report-for-ptsefton.com-final.html_trip-report-for-ptsefton.com-final_html_1715e81a-1024x768.jpg)](/wp-content/uploads/2013/08/wpid-trip-report-for-ptsefton.com-final.html_trip-report-for-ptsefton.com-final_html_1715e81a.jpg)
*Prince Edward Island's largest land mammal is the lighthouse.*

<section>
## Summary

The main-track conference started and ended with talks which, to me at
least, were above all about [Research
Integrity](http://www.singaporestatement.org/statement.html). We started
with Vitoria Stodden's *Re-use and Reproducibility: Opportunities and
Challenges*, which I'll cover in more detail below*.* One of Stodden's
main themes was the gap in our scholarly practice and infrastructure
where code and data repositories should be. It is no longer enough to
publish research articles that make claims if those claims are
impossible to evaluate or substantiate in the absence of the data and
the code that support them. The closing talk touched on some of the same
issues, looking at the current flawed and corruptible publishing system,
claiming for example that the journal based rewards system encourages
cheating. Both of these relate to repositories, in overlapping ways.

But OR is not just about the main track, which was well put together by
Sarah Shreeves and Jon Dunn, it remains a practical, somewhat technical
conference where software user and developer groups are also important
strands and the Developer's Challenge is a key part of the event.

</section>
<section>
## The conference: the “Two Rs and a U”

First up, the main conference. The theme this year was “Use, Reuse,
Reproduce”. The call for proposals said:

> **Some specific areas of interest for OR2013 are:**
>
> -   Effective re-use of content--particularly research data--enabled
>     by embedded repository tools and services
>
> -   Effective re-use of software, services, and infrastructure to
>     support repository development
>
> -   Facilitation of reproducible research through access to data,
>     workflows, and code
>
> -   Services making use of repository metadata
>
> -   Focused, disciplinary or community-based software, services, and
>     infrastructure for use and reuse of content
>
> -   Integration of data, including linked data, and external services
>     with repositories to provide solutions to specific domains
>
> -   Added-value services for repositories
>
> -   Long-term preservation of repositories and their contents
>
> -   Role and impact of repositories in the research ecosystem
>
These are all great things to talk about, and show how repositories, at
least in universities as expanding from publications to data. The
catch-phrase “Use, Reuse, Reproduce” is worthy, but I think maybe we're
not there yet. What I saw and heard, which was of course just a sample,
was more along the lines of “Here's what we're doing with research data”
rather than stories about re-use of repository content or reproducible
research. I hope that some of the work that's happening the Australian
eResearch scene on Virtual Labs and eResearch tools finds its way to
OR2014, as I think that these projects are starting to really join-up
some of the basic data management infrastructure we've been building
courtesy of the Australian National Data Service
([ANDS](http://ands.org.au/)) with research practices and workflows.
It's the labs that will start to show the Use and Reuse and maybe some
Reproduction.

</section>
<section>
## Keynote:

<span lang="en-US">Victoria Stodden's </span>[opening
keynote](http://or2013.net/sites/or2013.net/files/OR2013-July92013-STODDEN.pdf)<span
lang="en-US"> was a coherent statement of some of the challenges facing
scholarship, which is currently evaluated on the basis publications,
citations and journals. But publications are most often not supported by
data and/or code that can be used to check them, Stodden talked mainly
about computationally-based research, but the problem affects many
disciplines. For a keynote I found it little dry – there was only one
picture, and I would have preferred a few stories or metaphors to make
it more engaging. I was also hoping she'd talk about </span><span
lang="en-US">the difference between repeatability and reproducibility,
which she did in </span>[another
talk](http://stodden.net/AMP2011/slides/RRJuly152011-STODDEN.pdf)<span
lang="en-US">. Our community needs to get on top of this, so here's an
'aside-slide' from another of her talks:</span>

> Aside: Terminology
>
> -   Replicability (King 1995)\*: Now: regenerate results from existing
>     code, data.
>
> -   Reproducibility (Claerbout 1992)\*: Now: independent recreation of
>     results without existing code or data,
>
> -   Repeatability: re-run experiments to determine the sensitivity of
>     results when underlying measurements are retaken,
>
> -   Veriﬁcation: the accuracy with which a computational model
>     delivers the results of the underlying mathematical model,
>
> -   Validation: the accuracy of a computational model with respect to
>     the underlying data (model error, measurement error).
>
> See: V. Stodden, “Trust Your Science? Open Your Data and Code!” Amstat
> News, 1 July 2011. http://
> magazine.amstat.org/blog/2011/07/01/trust-your-science/

\*These citations are not in the reference list in the slide-deck.

Stodden made some references to repositories, summarized thus on The
Twitter:

> **[<span lang="en-US">**Simon
> Hodson**</span>](https://twitter.com/simonhodson99)**[<span
> lang="en-US"> ‏</span>](https://twitter.com/simonhodson99)[<span
> lang="en-US">@</span>](https://twitter.com/simonhodson99)[<span
> lang="en-US">simonhodson99</span>](https://twitter.com/simonhodson99)[<span
> lang="en-US">10
> Jul</span>](https://twitter.com/simonhodson99/status/355023275014893568)
>
> “[<span
> lang="en-US">@</span>](https://twitter.com/sparrowbarley)[<span
> lang="en-US">sparrowbarley</span>](https://twitter.com/sparrowbarley)<span
> lang="en-US">: </span>[<span
> lang="en-US">\#</span>](https://twitter.com/search?q=%23OR2013&src=hash)**[<span
> lang="en-US">OR2013</span>](https://twitter.com/search?q=%23OR2013&src=hash)**<span
> lang="en-US"> keynote, V </span>**<span
> lang="en-US">Stodden</span>**<span lang="en-US"> called for sharing of
> data & code to "perfect the scholarly record" & "root out error"”
> </span>[<span
> lang="en-US">\#</span>](https://twitter.com/search?q=%23jiscmrd&src=hash)[<span
> lang="en-US">jiscmrd</span>](https://twitter.com/search?q=%23jiscmrd&src=hash)
>
> **[<span lang="en-US">**Peter
> Ruijgrok**</span>](https://twitter.com/pruijgrok)**[<span
> lang="en-US"> ‏</span>](https://twitter.com/pruijgrok)[<span
> lang="en-US">@</span>](https://twitter.com/pruijgrok)[<span
> lang="en-US">pruijgrok</span>](https://twitter.com/pruijgrok)[<span
> lang="en-US">9
> Jul</span>](https://twitter.com/pruijgrok/status/354619168194179073)
>
> [<span
> lang="en-US">\#</span>](https://twitter.com/search?q=%23or2013&src=hash)**[<span
> lang="en-US">or2013</span>](https://twitter.com/search?q=%23or2013&src=hash)**<span
> lang="en-US"> Victoria </span>**<span
> lang="en-US">Stodden</span>**<span lang="en-US">: A publication is
> actually an advertisement. Data and software code is what it is about
> as proof / reproducing</span>

This was a useful contribution to Open Repositories – Reuse,
Replicability, Reproducibility et al have to be amongst our *raisons de
etre.* Just as the Open Access movement drove the initial wave of
institutional *publications* repositories, the R words will drive the
development of *data and code repositories*, both institutional and
disciplinary. OR is a very grounded conference, for practitioners more
than theorists, so I would expect that over the next decade we'll be
talking about how to build the infrastructure to support researchers
like Victoria, and the researchers we've been working with at UWS, which
brings us to our talk.

</section>
<section>
## Our paper: 4a Data Management

<span lang="en-US">The presentation I gave, written with Peter Bugeia
talks about how UWS collaborated with Intersect, using money from the
Australian National Data Service to work on a suite of projects that
cover the four As. It's </span>[up on the UWS eResearch
blog](http://eresearch.uws.edu.au/blog/2013/07/24/4a-data-management-acquiring-acting-on-archiving-advertising-research-data-at-the-university-of-western-sydney/)<span
lang="en-US"> and with slightly cleaned-up formatting </span>[<span
lang="en-US">on my own
site</span>](http://ptsefton.com/2013/07/26/4a-data-management-acquiring-acting-on-archiving-and-advertising-data-at-the-university-of-western-sydney.htm)<span
lang="en-US">. </span>

At the University of Western Sydney we've been working on end-to-end
data management. The goal of being able to support the R words for
researchers is certainly behind what we're doing but before we get
results in that area we have to build some basic infrastructure. For the
purposes of this paper, then, we settled on the idea of talking about a
set of 'A' words that we have tried to address with useful services:

1.  Acquiring data

2.  Acting on data

3.  Archiving data

    (we could maybe have made more of the importance of including as
    much context about research as possible, including code, but we
    certainly did mention it).

4.  Advertising data

(note the accidental alignment with Victoria Stodden's comment that an
article is an ad.)

Note that the A words have been retrofitted to the project as a
rhetorical device, this is not the framework used to develop the
services

Everyone in the repository world knows that “if we build it they will
come” is not going to work, which is why this is not just about
Archiving and Advertising, two core traditional repository roles, it's
about providing services for Acquiring and Acting data for researchers.
Reproducibility et al are going to be more and more important to the
conduct of research, and as awareness of this spreads the most
successful researchers will be the ones who are already making sure
their data and code are well looked after and well described.

</section>
<section>
## The closing plenary

Jean-Claude Guédon's wrap up complemented the opening well, drawing
together a lot of familiar threads around open access, and looking at
the way the scholarly rewards system has created a crisis in research
integrity, he rehearsed the familiar argument that journal-level metrics
are not useful, and can be counter-productive, calling for an
article-level measuring system which can operate independently of the
publishing companies who control so much of our current environment. He
warned against letting corporations take 'our' data and sell that back
to us as well. There was nothing really ground breaking here, but it was
a timely reminder to think about why we're even at a conference called
Open Repositories.

Like Stodden, Guédon didn't offer much of a roadmap for the repository
movement, which after all is our job, although he did try talk in
context maybe a little more than Stodden's opening which, while it did
reference repositories had the air of a well-practiced stump-speech.

</section>
<section>
## \
The developer challenge

This year the develop challenge judging panel was decisively chaired by
Sarah Shreeves who was also on the program committee. We struggled to
get entrants this time – this still needs some analysis, but at this
stage it looks like the relatively remote location meant that many
developers didn't get funding to attend, and we had a little confusion
around a new experiment for this year which was a non-compulsory
hackfest a few kilometers from the main venue which left a couple people
thinking they'd missed out on a chance to join in. And the big one was
that there was no dedicated on-the-ground dev wrangler on hand; for the
last several years JISC have been able to send staff, notably Mahendra
Mahey. I did try to encourage teams to enter, with modest success, but
Mahendra was definitely missed.

So who won?

> **[**William J
> Nixon**](https://twitter.com/williamjnixon)**[ ‏](https://twitter.com/williamjnixon)[@](https://twitter.com/williamjnixon)[williamjnixon](https://twitter.com/williamjnixon)[11
> Jul](https://twitter.com/williamjnixon/status/355347457992966144)
>
> [\#](https://twitter.com/search?q=%23OR2013&src=hash)**[<u>OR2013</u>](https://twitter.com/search?q=%23OR2013&src=hash)**
> Developers **challenge** winners - Team Raven’s PDF/A and Team ORCID.
> Congratulations. More details on these at
> [http://or2013.net/content/or-2013-dev-challenge-event …](http://t.co/2EHFV0y3OZ)

This year we based the judging on [the criteria I put together last
year](http://ptsefton.com/2012/09/05/open-repositories-developer-challenge-draft-manifesto-v0-1.htm)
in the form of a manifesto about the values of the conference. I think
that helped focus the judging process and feedback was generally good
from the panel but we'll see how people feel after some reflection. I
talked about this in the wrap-up. Torsten Reimer got the heart of it:

> ****[<u>Torsten
> Reimer</u>](https://twitter.com/torstenreimer)****[ ‏](https://twitter.com/torstenreimer)[@](https://twitter.com/torstenreimer)[torstenreimer](https://twitter.com/torstenreimer)**[11
> Jul](https://twitter.com/torstenreimer/status/355346887827660801)**
>
> [\#](https://twitter.com/search?q=%23OR2013&src=hash)**[OR2013](https://twitter.com/search?q=%23OR2013&src=hash)**
> Developer **Challenge** co-judge
> [@](https://twitter.com/ptsefton)[ptsefton](https://twitter.com/ptsefton)
> summarises the dev manifesto
> [http://bit.ly/1dmQ8UQ ](http://t.co/KcUAS7JPwN) creating new networks
> is key

Robin Rice (front left) had organized a photo of the smuggler's den in
which we convened:

> **[**Robin
> Rice**](https://twitter.com/sparrowbarley)**[ ‏](https://twitter.com/sparrowbarley)[@](https://twitter.com/sparrowbarley)[sparrowbarley](https://twitter.com/sparrowbarley)[10
> Jul](https://twitter.com/sparrowbarley/status/355065962334134273)
>
> The Dev **Challenge** judges are convening in an appropriate venue.
> [\#](https://twitter.com/search?q=%23OR2013&src=hash)**[OR2013](https://twitter.com/search?q=%23OR2013&src=hash)**
> [pic.twitter.com/ToIkzQueeb](http://t.co/ToIkzQueeb)

The committee is putting together a manual for future organizers, and I
will be suggesting something along these lines:

-   Dev facilities should be as close as possible to the main conference
    rooms, even remote rooms in the same facility cause problems as
    people need to be able to be in and out of presentations.

-   There needs to be a dedicated mentor for the dev challenge to help
    teams coalesce and do stuff like make sure that winners are
    announced formally.

</section>
<section>
## The future of Fedora

I was really interested in the new [Fedora Futures / Fedora 4
project](https://wiki.duraspace.org/display/FF/Fedora+Futures+Home%5C)
(FF). Fedora is the back-end repository component behind projects like
[Islandora](http://en.wikipedia.org/wiki/Islandora),
[Hydra](https://wiki.duraspace.org/display/hydra/The+Hydra+Project)
(parts of which power the [HCS virtual
laboratory](http://hcsvlab.org.au/)) and optionally for
[ReDBOX](http://www.redboxresearchdata.com.au/).

The new Fedora project is not ready for real use yet, but it shows lots
of promise as a simple-to-use linked-data-ready data storage layer for
eResearch projects, where you want to keep data and metadata about that
data. New built-in self-repairing clustering and a simple REST interface
make it appealing.

I was particularly excited about the (promised) ability for FF to be
able to run on top of an existing file tree and provide repository-like
services over the files. This is exactly what we have been looking for
in the [Cr8it
project](http://eresearch.uws.edu.au/blog/projects/capturing-data-and-files-into-a-research-data-catalogue/),
where the idea is to bridge the yawning chasm from work-in-progress
research files to well described data sets. Small detail: doesn't
*actually* do what I fondly hoped it would yet I wanted to be able to
point it at a set of files, have it extract metadata and generate
derived views and previews, allow extra metadata to be linked to files
and watch for changes. Working on that.

</section>
<section>
## The venue and all that

Prince Edward Island took some getting to for some of us, but it was
worth it. Mark Leggot's team at UPEI and the related spin-off company
Discovery Garden were consummate hosts and Charlottetown was a great
size for a few hundred conference attendees; it was impossible not to
network unless you stayed in your hotel room. I didn't. I particularly
appreciated the local CD in the conference bag. Mine is [Clocks and
Hearts Keep Going](http://www.tanyadavis.ca/fr_music.cfm) by Tanya
Davis, laid-back pop-folk, which kind of reminded me of [The Be Good
Tanyas](http://en.wikipedia.org/wiki/The_Be_Good_Tanyas), in a good way,
and no not because of the Tanya thing, but it may be a Canadian thing.
And there were decent local bands at the conference dinner, which was
held in three adjacent restaurants and involved oysters and lobsters,
like just about every other meal on PEI.

[![wpid-trip-report-for-ptsefton.com-final.html\_trip-report-for-ptsefton.com-final\_html\_m463f855a.jpg](/wp-content/uploads/2013/08/wpid-trip-report-for-ptsefton.com-final.html_trip-report-for-ptsefton.com-final_html_m463f855a-1024x768.jpg)](/wp-content/uploads/2013/08/wpid-trip-report-for-ptsefton.com-final.html_trip-report-for-ptsefton.com-final_html_m463f855a.jpg)

*Just about everyone I went to dinner with was obsessed with these
things, and I do think they might be better than the ones we have here*

There was pretty good fish and chips too.

</section>
</section>
</article>

