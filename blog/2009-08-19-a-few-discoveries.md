---
Author: ptsefton
Comments: true
Date: 2009-08-19 00:28:17+00:00
Slug: a-few-discoveries

Title: A few discoveries
Wordpress_id: 369
excerpt: In which I build a discovery service for Southampton to better find papers
  by Les Carr
---

<div>

<div class="page-toc">

</div>

<div>

I have been thinking lately about repository architecture, and
[wondering](http://ptsefton.com/2009/08/05/im-beginning-to-hate-the-word-repository.htm)
about whether the term 'repository' is actually skewing our idea of what
we should be doing to preserve and disseminate via Open Access, and
report on research output and the other things we want out repositories
to do.

One of the ideas I'm keen on exploring is what librarians call a <span
class="spCh spChx201c">“</span>discovery service<span
class="spCh spChx201d">”</span> or a <span
class="spCh spChx201c">“</span>discovery layer<span
class="spCh spChx201d">”</span>, basically a web-view of a number of
different services brought together in a smart index, with faceted
browsing, like the National Library of Australia's [Single Business
Discovery Service prototype](http://sbdsproto.nla.gov.au/)which uses
Apache Solr indexes to search across eight different types of resource
all at once. In this post I want to give an example of another place
where this might be useful, using an example that I came across when I
was looking for examples for the conversation with Les Carr about
[PowerPoint
dismantling](http://ptsefton.com/2009/08/17/more-progress-on-exploded-powerpoints-in-a-desktop-repository.htm).

I'm not picking on Southampton here, they're leaders in Open Access or
the EPrints software they have given our community, which is wonderful
(in parts) but I would like to use their two (are there more than two?)
EPrints repositories as an example of the advantages of a Solr-powered
discovery layer.

How this came about was, I was poking around the Southampton EPrints
site and I grabbed a PowerPoint presentation to use as an example; I
knew that it was by Liz Lyon and Les Carr because that metadata was in
the file, and The Fascinator managed to extract it. (Turns out there was
a bunch of other authors listed on the EPrint, but maybe they were not
authors of the PowerPoint.)

Now, lets see if I can find it again. What you're about to read below
might reflect badly on my search skills but this is roughly what I did,
I'm sure there are other bumblies out there like me.

A search on [e-Prints at Southampton](http://eprints.soton.ac.uk/) has 8
matches for the string <span class="spCh spChx201c">“</span>[Les
Carr](http://eprints.soton.ac.uk/perl/search?simple=les+carr&simple_merge=ALL&_order=byname&_action_search=Search)<span
class="spCh spChx201d">”</span>. But thing I'm after is not in that
list. Took me a while to remember (and I did have to remember, the site
doesn't tell you this) but there's another EPrints site for the School
of Electronics and Computer Science (branded EPrints rather than
e-Prints). So, having found the ECS EPrints site, I had a search for Les
Carr. [No
results](http://eprints.ecs.soton.ac.uk/cgi/search/quicksearch?basic_srchtype=ALL&basic=Les+Carr&full_text_status=&_satisfyall=ALL&_order=byyear&_default_action=search&_action_search=search).
Searching for plain-old Carr in either site gave me too many results to
sort through. After that I went back to the blog post where I talked
about the thing and found a [direct
link](http://eprints.soton.ac.uk/11039/) <span
class="spCh spChx2013">–</span> and yes it's there in the Southampton IR
(not ECS) but the name I was after is Carr, Leslie. I can find it using
that search (and I note that it was deposited by Carr, Dr Leslie).
Right. Got it.

With my team, I did a little experiment, harvesting both the Soton
repositories into our repository software, The Fascinator. It's running
on the Amazon EC2 cloud, so it might go away at some time in the future,
but here you can see a portal Bron Chandler set up for an [aggregated
view of the two
repositories](http://75.101.164.238:9999/portal/search/all_soton): or
drill down by facet to look at the two of them separately. The advantage
of a faceted interface like this is that even if the data remain
un-normalized, you can pick out what you might be looking for a bit
easier than in the raw EPrints software, at least you can see the range
of aliases this character operates under <span
class="spCh spChx2013">–</span> here's an edited view of the list of
authors when you do a simple search for Carr.

> Author
>
> -   [Carr,
>     Les](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20Les%22?t:ac=all_soton/carr)(56)
>
> -   [Carr,
>     Leslie](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20Leslie%22?t:ac=all_soton/carr)(55)
>
> -   [Carr, Les
>     A.](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20Les%20A.%22?t:ac=all_soton/carr)(38)
>
> -   [Carr,
>     LA](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20LA%22?t:ac=all_soton/carr)(15)
>
> -   [Carr,
>     L](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20L%22?t:ac=all_soton/carr)(10)
>
> -   [Carr, Leslie
>     A.](http://75.101.164.238:9999/portal/search:addfacet/f_creator%3A%22Carr%2C%20Leslie%20A.%22?t:ac=all_soton/carr)(10)
>
On one level It's actually the function of a repository to preserve this
seeming chaos <span class="spCh spChx2013">–</span> the different
contexts in which Carr, Dr Leslie operates have resulted in different
forms of the name and the repository needs to remember them for
bibliographic integrity, I'll talk below about name authorities, but The
Discovery service approach means I was able to discover all these
name-forms across both repositories, which is a huge win over the more
limited native EPrints search.

Note that this was just a quick 'n' dirty experiment, we're not sure if
we harvested everything and we did zero special configuration, but it
seems like a pretty useful view of the Soton repostiories to me.

I think EPrints has unbeatable workflows for item management and ingest
and so on, but the interface is very beatable.

Stepping back a bit I note that these EPrints sites are not that easy to
find <span class="spCh spChx2013">–</span> I got to them by typing in
the URL, but if you go to the university home page and browse to
[Research](http://www.soton.ac.uk/research/researchdir/index.html) it's
not obvious where the EPrints are. A search for Les Carr works, as you
can get to his home page where there are of course links to recent
publications in EPrints. That's better than what you get searching for
[Peter
Sefton](http://websearch.usq.edu.au/search?q=peter+Sefton&btnG=Go&entqr=0&entsp=0&sort=date%3AD%3AL%3Ad1&output=xml_no_dtd&client=default_frontend&sa.x=0&ud=1&oe=UTF-8&ie=UTF-8&sa.y=0&proxystylesheet=default_frontend&site=default_collection)
on the USQ site where a lot of the hits are from things like the test
content that ships with ICE. No sign of my EPrints stuff in the first
couple of pages).

At USQ we're using Google, which seems to pick up the ICE site over
other content, presumably because it has more incoming links than the
other pages at USQ with my name (mostly from here at this blog I guess
:-), whereas the Southampton search seems to be driven by SharePoint. In
both cases, I think a discovery-service approach could be a real winner;
instead of the Google-style metadata-poor view why not build your own
faceted view of your own university's stuff?

Here at USQ I'd like to see the main site brought together with EPrints,
and the ePortfolio system and maybe courseware (particularly if we get
around to taking Open Courseware seriously), and with any other
databases of our stuff, like the [library
catalogue](http://www.usq.edu.au/library/), which is already powered by
Solr.

I'll finish with a quick comment on name authorities. I [talked about
them on CAIRSS
blog](http://caulcairss.wordpress.com/2009/07/21/nicnames-and-people-australia-some-thoughts-for-cairss/)
recently. Of particular interest is the NicNames software which can help
to link up all the instances of Les Carr, Carr, Leslie and Carr, Dr
Leslie. NicNames should be able to suck up data from any repository and
try to work out via subject codes and so on who is who, and let a
repository administrator have the final say on name-authority matters.
Once that's done and the system is trained to know that we have, say a
Carr, L working in web systems and maybe another in physiology then when
you're putting in a new record the system will be able to give you a
choice between the two, and add an ID as well as the variant of the name
string that happens to be on the item; there are two ways to approach
this <span class="spCh spChx2013">–</span> one would be to integrate
this service directly in ePrints, but another would be to leave them as
separate services and bring them together at the discovery level. More
on that soon.

</div>

</div>
