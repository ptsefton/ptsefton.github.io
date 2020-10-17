---
Author: ptsefton
Comments: true
Date: 2007-12-18 06:47:07+00:00
Slug: ice-mashups-part-one

Title: ICE Mashups, part one
Wordpress_id: 22
---

<div>

<div class="page-toc">

</div>

<div>

I recently [reported on an application called
FieldHelper,](http://ptsefton.com/2007/12/11/clever-collections.htm)
that I saw at *Clever Collections*.
[FieldHelper](http://acl.arts.usyd.edu.au/fieldhelper/) inspired me to
buy a data cable for my GPS (a yellow Garmin
[eTrex](https://buy.garmin.com/shop/shop.do?pID=6403)). The cable's not
a great success, I went for a USB version off eBay and it only works on
Tuesdays and only on the Windows box at home, no luck with the Mac so
far.

Anyway, I took the GPS on the regular Sunday morning ride with the
[Toowoomba Bicycle Users Group](http://toowoombabug.blogspot.com/). This
group is friendly easy-paced and lycra-optional, not a racing pack. The
original plan was to try to use FieldHelper to synchronize the time data
on some photos with the GPS track so I could show them on a map with
little flags, but the camera I took thinks it's main calling in life is
as a telephone and it doesn't seem to have added a proper timestamp.
Still, I was able to import the tracklog via
[GPSBabel](http://www.gpsbabel.org/), load it into Google Earth, export
as KML then upload into [Bikely](http://bikely.com/). I know that's a
bit complex, but we're doing this in the name of automation <span
class="spCh spChx2013">–</span> our aim is to make it all much easier.

Here it is, an interactive map.

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

If you click on the title at the top of the map it takes you to
[Bikely](http://bikely.com/) where you can do stuff like see the
elevation profile of the ride (click on Show / Elevation profile to see
that we climbed 471m and apparently ended 8m below where we started,
which may be to do with me editing the log so it doesn't start and end
from my house).

To make this happen, Ron Ward added a feature to
[ICE](http://ice.usq.edu.au/), along the lines of the hack I did to
[include CML in posts](http://ptsefton.com/blog/2007/06/22/cml_demo/).

As this is the first time out, **I had to do a few steps**:

1.  Visit the map at my Bikely account.

2.  Click on the *Share / Display this map on your blog or websi*te
    link.

3.  Copy and paste the HTML code they gave me into a new file. (And edit
    the code to work around a Firefox bug with empty elements.)

4.  Copy the file up to my website. (I only had to this 'cos of a
    limitation of ICE that will be fixed soon, in the future you will
    just save it in ICE).

5.  Capture a screenshot of the map and paste it into my document, to
    serve as the print rendition.

6.  Link the screenshot to the online version of the map.

When that's all done and I look at the document in ICE it includes the
interactive map in my web page while using the screenshot in the PDF.
This is a really useful generic mechanism for including inline web
stuff, could be used for lots of things where you want a **live version
for the web** and a **dead version for print**.

Too complicated?

What we'll do to make this work better in future is **use the
forthcoming ICE plugin system**. All you will need to do is drop the
tracklog from the GPS into ICE and it will make both a print-renderable
map and the code you need for a live map. The same plugin system will
work for stuff like CML, and countless other data driven visualization
tools.

</div>

</div>
