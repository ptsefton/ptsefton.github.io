---
Author: ptsefton
Comments: true
Date: 2012-06-22 06:37:33+00:00
Slug: researcher-data-australia-down-to-earth

Title: Research Data Australia down to Earth
Wordpress_id: 1079
---

<article itemscope="itemscope" itemtype="http://schema.org/ScholarlyArticle">
<section>
## Context: free cloud servers, a workshop and an idea

In this post I look at some work we’ve been doing at the University of
Western Sydney eResearch group on visualizing metadata about research
data, in a geographical context. The goal is to build a data discovery
service; one interface we’re exploring is the ability to ‘fly’ around
Google Earth looking for data, from [Research Data
Australia](http://services.ands.org.au/home/orca/rda/search) (RDA). For
example, a researcher could follow a major river and see what data
collections there are along its course that might be of (re-)use. True,
you can [search the RDA site by dragging a marker on a
map](http://services.ands.org.au/home/orca/rda/search#!/q=*%3A*/p=1/tab=All/n=-79.632238/e=167.042438/s=-64.643345/w=103.761188)
but this experiment is a more immersive approach to exploring the same
data.

The post is a quick update on a work in progress, with some not very
original reflections on the use of cloud servers. I am putting it here
on my own blog first, will do a human-readable summary over at UWS soon,
any suggestions or questions welcome.

You can try this out if you have Google Earth by [downloading a KML
file](http://eresearch.uws.edu.au/geo/rda.kml). This is a demo service
only – let us know how you go.

This work was inspired by a workshop on cloud computing: this week
Andrew (Alf) Leahy and I  attended  a
[NeCTAR](http://nectar.org.au/)<span
class="apple-converted-space"> </span>and Australian National Data
Service (ANDS) one day event, along with several UWS staff. The
unstoppable David Flanders from ANDS asked us to run a ‘dojo’, giving
technically proficient researchers and eResearch collaborators a hand-on
experience with the NeCTAR research cloud, where all Australian
University researchers with access to the Australian Access Federation
login system are entitled to run free cloud-hosted virtual servers. Free
servers! Not to mention post-workshop beer[^[i]^](#_edn1). So senseis
Alf and and PT  worked with a small group of ‘black belts’ in a workshop
loosely focused on geo-spatial data. Our idea was “Visualizing the
distribution of data collections in Research Data Australia using Google
Earth”[^[ii]^](#_edn2). We’d been working on a demo of how this might be
done for a few days, which we more-or less got running on the train from
the Blue Mountains in to Sydney Uni in the morning.

</section>
<section>
## The demo

We will work some more on this little very part-time project, but here’s
a snapshot of where we are at the moment with our mission of getting RDA
data into Google Earth.

[![](/wp-content/uploads/2012/06/image0011.png "image001")](/wp-content/uploads/2012/06/image0011.png)

Figure 1 Screenshot of data sets from Research Data Australia mapped
onto the earth (visualized via their bounding boxes from the data
collection metadata) from a long way up (the sets with the (claimed)
broadest geographical coverage show up first, more appear as you zoom
in)

Right now the experience is basic, but engaging, just using the geometry
provided in RDA collections and without changing any of the default ANDS
styles you can see a ‘heat map’ of where data have been collected.
Speaking of heat it seems Aussie researchers prefer the more northerly
latitudes to the South pole, as a place to take a few readings, or catch
[a few
rays](http://services.ands.org.au/home/orca/rda/view/?key=AODN%3A516811d7-cc5c-207a-e0440003ba8c79dd).

[![](/wp-content/uploads/2012/06/image004.jpg "image004")](/wp-content/uploads/2012/06/image004.jpg)\>

Figure 2 Zooming in on research hotspots like The Reef shows how crowded
it is there – we’re limiting this to 40 boxes or points per screen, so
keep drilling to find more

[![](/wp-content/uploads/2012/06/image005.png "image005")](/wp-content/uploads/2012/06/image005.png)

Figure 3 You can click on a marker to pull up a description

</section>
<section>
## Why?

Why are we doing this?

-   To **test out the NeCTAR Research Cloud**, so we can advise
    researchers at UWS on how and when to use it – we’ll cover this in
    future posts and publish advice on the UWS eResearch site. Initial
    observations include:

    -   It’s good for testing out ideas quickly – you can fire up a
        tool, pull in data from a networked source and do something to
        it, but some planning is required to package the tools and get
        them to operate as turnkey appliances. At the moment you need
        command-line skills and patience.

    -   This infrastructure is a game-changer – it can take months for
        university IT departments to deliver a virtual machine to a
        research or dev group and policy prevents many of us from buying
        commercial cloud services on corporate credit cards.

    -   The lack of easy-to access persistent cloud storage which had
        not yet come on line from NeCTAR’s sister project [Research Data
        Storage
        Infrastructure](http://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CFcQFjAA&url=http%3A%2F%2Frdsi.uq.edu.au%2F&ei=ys_jT4foJ9HKmQXkrPSMCw&usg=AFQjCNEPdhhaRjWkTW91_E0p8v_nm24GzA&sig2=kasKimfJKr70JzioZSauKQ)
        RSDSI is a bit of a problem, there is no simple way to mount a
        device with all your data on it.

    -    A specific lesson from our demo: being able to fire up servers
        on demand to handle peak loads, such as building a big
        geo-spatial index (we only built a tiny one) seems promising but
        we’d like to see this made as easy as possible for people who
        want to get research done rather than mess with computers.

-   To see how Alf’s considerable expertise in **practical, easy to
    deploy low-end visualization combined with my experience in
    repositories, harvesting metadata etc might be applied to resource
    discovery**. Being able to fly around the landscape means you can
    follow geographical features and maybe discover useful data sets
    along the way.

-   To explore **how the ReDBOX Research Data Catalogue application
    might be able to geo-index collections** (see notes on this below).

</section>
<section>
## The technical stuff

The current architecture of our demo is, to say the least, baroque.
There is a lot of backwards and forwards between systems to get to the
interaction between a user and Google Earth (bottom right of the
diagram). That’s perfect for exploring cloud services but maybe not
ideal for a ‘real’ service. It does show, however that using existing
systems with open interfaces you can stitch something together fairly
quickly. This will improve as packaged eResearch appliances start
appearing at NeCTAR.

We have now deployed part of this on our own server so we can leave it
running and shut down the NeCTAR servers so they don’t use up our
allowances.

Key to the diagram:

-   [ReDBox](http://redboxresearchdata.com.au) is a research data
    catalogue application which I helped design.

-   GeoHarvester is a  python script
    ([rdamap.py](http://code.google.com/p/uws-eresearch/source/browse/trunk/geo/rdamap.py))
    that sucks data out of the Solr server in ReDBox and turns it into
    something that another Solr set up for geospatial queries can index.
    You can see the Solr index here if you’re interested via the
    [default search interface](http://eresearch.uws.edu.au/solr/admin/).
    Or try a [geo-spatial
    query](http://eresearch.uws.edu.au/solr/select?wt=json&indent=true&fl=id%20container&q=*:*&fq=%7b!geofilt%20pt=-35,151%20sfield=store%20d=100%7d&facet=true&facet.field=container),
    which could [lead you to some
    KML](http://eresearch.uws.edu.au/solr/select?q=id:0528213d31aec0e88fa7377bfed125dc).

-   KMLServer is a little web app that fields queries from Google Earth
    (what data sets are ‘in view’) and talks to the Solr server. Alf has
    coded it to give you [stuff from the Great Barrier
    Reef](http://eresearch.uws.edu.au/kmlgeo/) by default.

Note that the only user-facing system is Google Earth all the rest is
back-end stuff. None of the work we did needed any kind of user
interface at all.

If  you’re really brave, you can [check out the
code](https://code.google.com/p/uws-eresearch/source/browse/#svn%2Ftrunk%2Fgeo)
and try to get it to run by following the readme file. Warning, there
are hard-coded URLS everywhere that one bit talks to another that you
WILL need to change. I’ll help if you email me but this is not a
packaged application, it’s a demo.

[![Description: ReDBox -\> RDA : Fetch collection data over\\nOAI-PMH
protocol in RIF-CS format ReDBox -\> ReDBox : Index data into Solr index
GeoHarvester -\> ReDBox : Fetch all data with\\ngeo-information from
ReBOX Solr index ReDBox -\> GeoHarvester : Return paginated JSON data
GeoHarvester -\> RDA : Fetch KML for each collection \\n(not included in
the RIF-CS) RDA -\> GeoHarvester : Return KML (with default style)
GeoHarvester -\> "KMLServer/Solr" : Index collections and cache KML
GeoHarvester -\> "KMLServer/Solr" : Divide bounding-boxes\\ninto points
and index each point create KML "KMLServer/Solr" -\> KML : Create KML
file\\nwith a dynamic data loader GoogleEarth -\> KML : Load file
User -\> GoogleEarth : Change view GoogleEarth -\> "KMLServer/Solr" :
What collections are in view? "KMLServer/Solr" -\> GoogleEarth : Return
KML file with all in-view\\nbounding boxes and\\ncollection descriptions
GoogleEarth -\> User : \<collections drawn on
globe\>](/wp-content/uploads/2012/06/image007.png "image007")](/wp-content/uploads/2012/06/image007.png)

Figure 4 We could possibly have made this more complicated, but it's
hard to see how

Building this first-take has taken us a step closer to our goal of
having an immersive demo for exploring data collections, ready for
eResearch Australasia. Along the way we learned a few lessons.

-   Apache Solr (which is the text/data Indexer in both ReDBOX and RDA)
    has basic but working geo-search features. You can only have one
    point per index entry so to index large shapes we approximated them
    to a simple box, then filled in a set of points (at this stage
    chunking by whole degrees), indexing each point individually with a
    reference back to the container object. Solr’s faceting feature
    makes it easy to find the biggest boxes first and prevent Google
    earth from trying to draw 20,000 collections at once.

-   Yes, RDA has a [search by bounding
    box](http://services.ands.org.au/home/orca/rda/search#!/q=*%3A*/p=1/tab=All/n=-33/e=152/s=-35/w=150),
    but it’s slow, we don’t want to barrage it with thousands of hits,
    and it returns multiple HTML pages. By indexing the data ourselves
    we get exactly what we want.

-   Yes, ReDBOX has Solr inside but it’s too old a version to support
    geo-searching well, and we’d also require some non-trivial changes
    to allow the aforementioned indexing of multiple points etc. It’s
    probably better to wait a bit for Solr to improve, which it does
    inexorably thanks to the Solr community, before trying to add this
    kind of search to ReDBox and the underlying Fascinator platform.

As usual, there’s lots TODO:

-   Make the KML styles customizable so we can provide better
    visualizations – we’d like to be able to fly through a data
    mountain-range or city or forest or something. Likewise, improve the
    heat-map that suggests where data might be concentrated.

-   Get rid of the Google Earth desktop app and use the new web version.

-   Get rid of the GeoHarvester code, by building it into a version of
    the existing ReDBOX harvester or take ReDBOX out of the tool chain
    and harvest directly from RDA.

-   Allow search by subject or keyword to select just some of the data.

-   See if we can auto-fetch actual data rather than just location
    metadata (especially maps and tracks).

-   Index some other data sources – which Alf is busy sourcing from UWS
    researchers.

-   But above all, see if this is useful enough to researchers or the
    eReseach/ANDS community to continue the experiment.

    \

    ------------------------------------------------------------------------

[^[i]^](#_ednref1) My partner said “Beer! Is it free?”, I said “Yes”,
and she said “What, as in beer?”, she’ll be using Linux next.

[^[ii]^](#_ednref2) As it turned out we didn’t look at this demo in our
Dojo, instead we tackled getting a resource hungry desktop application
called [Gplates](http://gplates.org), which does interactive
visualization of plate-tectonics, running on the cloud. We got it going,
but didn’t solve the problem of how to move the heavy number crunching
to the cloud and have the result display back at the desk.

</section>
Copyright Peter Sefton 2012. Licensed under [Creative Commons
Attribution-Share Alike 2.5
Australia.](http://creativecommons.org/licenses/by-sa/2.5/au/)

</article>

