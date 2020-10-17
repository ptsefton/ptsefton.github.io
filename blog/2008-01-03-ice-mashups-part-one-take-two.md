---
Author: ptsefton
Comments: true
Date: 2008-01-03 05:13:59+00:00
Slug: ice-mashups-part-one-take-two

Title: ICE Mashups, part one, take two
Wordpress_id: 46
---

<div>

<div class="page-toc">

-   [The end result: an interactive map](#id1)
-   [But what am I trying to achieve?](#id2)
-   [How do you make a map like this?](#id3)
-   [How do you publish a map like this?](#id4)
-   [Issues](#id5)

</div>

<div>

[Update 2008-01-03 <span class="spCh spChx2013">–</span> fixed a
technical issue]

I showed my [recent post on embedding maps into blog
posts](http://ptsefton.com/2007/12/18/ice-mashups-part-one.htm) to my
long-suffering partner.

She said that while the embedded Google map was cool, the explanation
was incomprehensible to her. Me, I would prefer that even if some of the
technical detail went over her head that she at least got the point,
which apparently she didn't, on account of it was, well,
incomprehensible.

(And then she went on to read a few more posts and pointed out some
really bad sentences that I had written in the recent past. I think it's
my eyes that are causing the problem; they don't focus on text like they
used to, but it could well be my brain.)

Here's another try at the same post with the word processor zoomed in to
150% so I can see what I'm typing.

# <span id="id1"></span><!--id1--></a>The end result: an interactive map

First up, I invite you to admire this map which shows the route of a
bike ride I went on with the [Toowoomba Bicycle Users
Group](http://toowoombabug.blogspot.com/).

<div class="embedded-html">

<div id="routemapiframe"
style="width: 450px; border: 1px solid #d0d0d0; background: #755; overflow: hidden; white-space: nowrap;">

<span
style="display: block; font: bold 11px verdana, arial; padding: 2px;">[Toowoomba -
Gowrie - Highfields
Loop](http://www.bikely.com/maps/bike-path/Toowoomba-Gowrie-Junction-Highfields-Loop)</span>
<iframe frameborder="0" id="rmiframe" scrolling="no" src="http://www.bikely.com/maps/bike-path/Toowoomba-Gowrie-Junction-Highfields-Loop/embed/1" style="height:360px;  background: #eee;" width="100%">
<!-- -->
</iframe>
<span
style="display: block; font: normal 10px verdana, arial; text-align: right; padding: 1px;">[Share
your bike routes @ Bikely.com](http://www.bikely.com/)</span>

</div>

</div>

If you click on the map you can drag it around.

Use the `+` and `–` buttons to zoom in and out.

And if you click on the title at the top (open it in a new window) it
will take you to Bikely where you can look at the ups and downs of
riding on the Darling Downs by clicking on `Show` then
`Elevation profile`.

<a name="graphics4"></a>![graphics4](/wp-content/uploads/2008/01/m518e62b6s364x1364.jpeg)

Which shows you this:

<span
style="display: block"><a name="graphics5"></a>![graphics5](/wp-content/uploads/2008/01/m49664bcas552x3024.jpeg)</span>

(Note: I think there's something wrong; it shows a very dramatic dip in
the ride that I don't remember, around the 26km mark).

# <span id="id2"></span><!--id2--></a>But what am I trying to achieve?

This is not just about putting up maps on a website. We are trying to
develop tools so that authors can **embed all kinds data into their
publications** and then visualize and explore and verify the data. As we
work for a university we are particularly interested in this for
educational and research purposes. We want to give authors tools to do
three things:

1.  Allow them to **capture or link to some data**.

2.  Generate a static **2d representation of the data** that they can
    paste into a word processing document and use for print or PDF.

3.  Publish **rich interactive views of their data** to the web:

> Instead of publishing a bike route as a picture, why not embed an
> interactive map in a web document?
>
> Instead of publishing a chemical formula for a molecule, [why not show
> an interactive 3d
> model?](http://ptsefton.com/blog/2007/06/22/cml_demo/)
>
> Instead of citing chapter and verse in a classical text, why not have
> the citations turn into links to multiple translations of the text?
> (Have a look at [this list of
> tools](http://www.perseus.tufts.edu/cgi-bin/perscoll?collection=Perseus:collection:PersInfo&type=interactive+resource)
> and think about how they could be integrated with an online text.)
>
> Instead of a table of data or a static chart, why not show a chart
> tool where the reader can zoom in an out, and otherwise explore the
> data?

This stuff is not easy at the moment. For example see this [post by
Peter Murray Rust about the difficulties of trying to paste a fragment
of Wikipedia code into his
blog](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=896), following on
from an [earlier
post](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=894). Peter mentions
the [Integrated Content Environment](http://ice.usq.edu.au/) project
that I lead at USQ where we are trying to help solve these problems.

Now, I'm going to explain how I captured the data to make this map, and
describe some of the challenges involved, and finish up by looking at
some of the issues raised.

# <span id="id3"></span><!--id3--></a>How do you make a map like this?

If you want to make a map like mine, the short answer is: join
[Bikely](http://www.bikely.com/) and draw one yourself using the
instructions on the site. It's a simple-yet-fiddly process of clicking
on a map to draw your route.

But there is a much more complicated way which, of course, is what I
decided to do.

I decided to use a [GPS
device](http://en.wikipedia.org/wiki/Global_Positioning_System) to
record a bike ride, upload the data onto my computer, then upload that
to Bikely. I used a free program called
[GPSBabel](http://www.gpsbabel.org/) to do the upload. (I had trouble
with the USB cable I bought for my Garmin eTrex GPS. If you're planning
to do this maybe choosing the absolute cheapest cable off eBay is not
the best plan.)

Once I got the upload working I ended up with a big file, with a couple
of years worth of random data from the GPS as well as the route I
wanted. Bikely wants to use the [GPX interchange
format](http://www.topografix.com/gpx.asp), but it didn't want **all**
my data <span class="spCh spChx2013">–</span> when I uploaded the whole
lot it gave up in disgust. Eventually I figured out that I could load
the data into Google Earth edit it down to just the route in question,
then export it and upload to Bikely. That worked.

# <span id="id4"></span><!--id4--></a>How do you publish a map like this?

So having made the map at the Bikely site you can capture it:

-   Click on `Share`.

-   Choose `Display this map on your blog or website`.

<dl>
<dd>
![graphics1](/wp-content/uploads/2008/01/m795256cds524x4924.jpeg)
</dd>
<dd>
The result is a fragment of HTML you can paste into the source of a web
page.
</dd>
<dd>
![graphics2](/wp-content/uploads/2008/01/m64ed2ed2s529x2154.jpeg)
</dd>
</dl>
Only trouble is that if you are working in a word processor, and you
paste in code like this all you get is ugly code in your document.
Besides, the code by itself doesn't give me the static version of the
map I want for the print / PDF version of the document.

So, Ron Ward has extended the existing 'embed' feature in ICE, for
embedding stuff like audio and video. To use it I have to do three
things:

1.  Put the *Bikely on-my-site* code into a file somewhere that it can
    be accessed over the web. In the future we're going to make this
    really easy, so you don't have to think about it, but for now I had
    to create the file and copy it to my website. (You also need to
    change the empty `iframe` tag to contain a blank comment because of
    a Firefox rendering bug).

2.  Paste in a screenshot of the image, like this (on the Mac I hit
    `Cmd Ctrl Shift 4`, then selected the area I wanted to capture, and
    pasted into this document):

<dl>
<dd>
![graphics3](/wp-content/uploads/2008/01/2306b635s529x4574.jpeg)
</dd>
</dl>
1.  Link the image to the file. In my case the link looks like this:

2.  [http://ptsefton.com/map3.html?embed](http://ptsefton.com/map2.html)

3.  View the document in ICE, and the HTML version is magically turned
    into a live map, while the PDF version, which you can't see here,
    has a static image like the one immediately above.

Now, I know all that is complicated, but eventually we will automate the
process so making a map is as easy as uploading the data from the GPS
(which is hard enough on its own). ICE will automagically turn a
tracklog into a map, and generate the printable version of the image for
you. But this will not be a one-off development. There will be a plugin
system so programmers can add formatters for lots of different kinds of
data.

# <span id="id5"></span><!--id5--></a>Issues

While this process works, it raises some interesting questions, for
which I don't have any answers:

-   In a scholarly context, would it be OK for me to edit my GPS log, as
    I have admitted to doing here? Depending on what the map is for that
    might be alright, but there are some kinds of data that really
    should not be edited.

-   If I expose the raw GPS data how do you know whether I have edited
    it? Would you trust it if it was signed by the GPS device so you
    could tell if I had tampered with it? Do you trust me not to hack my
    GPS device? Would you prefer it if I took along a witness? What
    about if you sent your GPS device with me, with a tamper-proof seal?
    Do I trust you?

    (A quick search GPS units that can sign their data turned up a
    patent, but it's designed for shopping, not science [<span
    style="vertical-align: super;"><span
    class="endnote">1</span></span>](#ftn1))

-   If I do expose my data, and link off to the the Google map how do I
    preserve or future-proof my publication? Can I put the data file in
    my institutional repository? What if it's really big data, like the
    stuff[<span style="vertical-align: super;"><span
    class="endnote">2</span></span>](#ftn2) the [ARROW team recently
    added to the Monash repository](http://www.tardis.edu.au/data.html)?
    What happens when Bikely disappears, or changes its terms of
    service? (Something like AONS[<span
    style="vertical-align: super;"><span
    class="endnote">3</span></span>](#ftn3) should hep here).

-   How can we make the whole process work seamlessly so that working
    researchers to use it?

These are the kinds of questions the research and higher-education
community will be looking at in Australia as part of activities going on
around the new Australian National Data Service[<span
style="vertical-align: super;"><span
class="endnote">4</span></span>](#ftn4) (ANDS).

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="endnote">[1](#ftn1-text) Bradford H Needham and David
Cowperthwaite, *EP1485842 Intel european software patent -
Authenticatable positioning data - Gauss* (2003),
<http://gauss.ffii.org/PatentView/EP1485842> (accessed December 19,
2007).</span>

</div>

<div style="font-size: .9em;">

<span class="endnote">[2](#ftn2-text) Carlos J. Rosado et al., <span
class="spCh spChx201c">“</span>A Common Fold Mediates Vertebrate Defense
and Bacterial Attack,<span class="spCh spChx201d">”</span> *Science*
317, no. 5844 (September 14, 2007),
<http://www.sciencemag.org/cgi/content/abstract/317/5844/1548> (accessed
December 20, 2007).</span>

</div>

<div style="font-size: .9em;">

<span class="endnote">[3](#ftn3-text) Curtis et al., <span
class="spCh spChx201c">“</span>AONS - An obsolescence detection and
notification service for Web archives and digital repositories,<span
class="spCh spChx201d">”</span> *New Review in Hypermedia and
Multimedia* 13, no. 1 (January 2007),
<http://dx.doi.org/10.1080/13614560701423711> .</span>

</div>

<div style="font-size: .9em;">

<span class="endnote">[4](#ftn4-text) The ANDS Technical Working Group,
*Towards the Australian Data Commons. A proposal for an Australian
National Data Service* (Canberra: Australian Government Department of
Science Education and Trainining, 2007),
<http://www.pfc.org.au/twiki/pub/Main/Data/TowardstheAustralianDataCommons.pdf>
.</span>

</div>

</div>

</div>
