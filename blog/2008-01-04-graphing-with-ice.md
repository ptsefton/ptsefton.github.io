---
Author: ptsefton
Comments: true
Date: 2008-01-04 01:43:09+00:00
Slug: graphing-with-ice

Title: Graphing with ICE
Wordpress_id: 56
---

<div>

<div class="page-toc">

-   [Google Chart API](#id1)
-   [Flot](#id2)
-   [Chart tool in Writer](#id3)
-   [Raw data](#id4)
-   [And the winner is?](#id5)

</div>

<div>

Peter Murray Rust followed up [my post on publishing interactive
maps](http://ptsefton.com/2008/01/02/ice-mashups-part-one-take-two.htm),
with a post about graphing.

> XY graphs are so common and so important that we ought to be able to
> cut and paste them, preserving he semantics of the underlying data.
> One of my New Year
> [WIBNI](http://www.acronymfinder.com/acronym.aspx?rec=%7B940EEE99-89E8-11D4-8351-00C04FC2C2BF%7D)s.
> [Link added by ptsefton as I had to look up WIBNI]
>
> <http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=905>

As I said in the last post, what I'm trying to do, with the help of the
ICE team is to find ways for people to publish both data and
visualizations of the data, preferably interactively.

Why?

Well an example is; in my last post there was an anomaly in the data, or
the graph of the data. I'm not sure which, but it should be possible for
people to find out, because the data is all out there in the open. More
on that later.

Inspired by Peter's WIBNI, I've been poking around the web this morning
to see what graphing tools are out there for HTML, and found the
modestly titled [*Definitive guide to charts and
graphs*](http://gavinbenda.com.au/2007/12/06/definitive-guide-to-charts-and-graphs/)
which surveys methods of embedding graphs in HTML.

I'm still thinking about the possibilities, but here are a few quick
experiments with graphing, using OpenOffice.org Writer (NeoOffice) and
the [ICE](http://ice.usq.edu.au/) system. As you will see, this post is
far from a definitive guide.

# <span id="id1"></span><!--id1--></a>Google Chart API

First up, I explored the [Google Chart
API](http://code.google.com/apis/chart/). As it says on the site, *The
Google Chart API lets you dynamically generate charts using a URL*. All
the data are encoded in the URL itself, which makes copying and pasting
really easy, but you would need to find the API document to decode the
data.

Here's an attempt to reproduce one of the diagrams we use to explain
ICE. The Google Chart API will only let me have three circles so it
doesn't really work in this case.

<div class="Table48"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------------------+--------------------------------------+
| Original diagram                     | Google Chart version                 |
+--------------------------------------+--------------------------------------+
| <span                                | <span                                |
| style="display: block"><a name="grap | style="display: block">[![graphics3] |
| hics2"></a>![graphics2](/wp-content/ | (/wp-content/uploads/2008/01/34acf69 |
| uploads/2008/01/m56e8260bs268x2686.j | fs267x1336.jpeg)](http://chart.apis. |
| peg)</span>                          | google.com/chart?cht=v&chs=200x100&c |
|                                      | hd=t:80,80,80,30,30,30,10&chdl=XHTML |
|                                      | %7CWord%7COpenDocument)</span>[Follo |
|                                      | w                                    |
|                                      | the link to see the chart direct     |
|                                      | from google's                        |
|                                      | API.](http://chart.apis.google.com/c |
|                                      | hart?cht=v&chs=200x100&chd=t:80,80,8 |
|                                      | 0,30,30,30,10&chdl=XHTML)            |
+--------------------------------------+--------------------------------------+

</div>

Here's another chart showing the average rainfall for Toowoomba in mm,
using [data that I downloaded from the Bureau of Meteorology in CSV
Format](http://www.bom.gov.au/clim_data/cdio/tables/text/IDCJCM0036_041103.csv).
To use the data I converted it to a percentage of 150mm <span
class="spCh spChx2013">–</span> hope I got it right.

<span
style="display: block">[![graphics4](/wp-content/uploads/2008/01/5871fe856.png)](http://chart.apis.google.com/chart?chtl=Average+monthly+rainfall+for+Toowoomba%7C1869-2007&cht=lc&chg=150.0,25.0&chs=500x200&chd=t:88.1,80.7,63.1,41.3,38.9,37.9,34.7,26.3,31.1,48.1,59.7,80.0&chxt=x,y&chxl=0:%7CJan%7CFeb%7CMar%7CApr%7CMay%7CJun%7CJul%7CAug%7CSep%7COct%7CNov%7CDec%7C1:%7C0+mm%7C50+mm%7C100+mm%7C150+mm)</span>

Follow the link on the picture to see the data encoded in a URL<span
class="spCh spChx2013">–</span> but there has been some data loss
because of the requirement to encode the data for the Google Chart API.

# <span id="id2"></span><!--id2--></a>Flot

Next I tried [Flot](http://people.iola.dk/olau/flot/examples/)(found via
[a
comment](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=905#comment-98476)
on PMR's post).

<span style="display: block"></span>

<div class="embedded-html">

**Average monthly rainfall in Toowoomba, 1869-2007**

<div id="placeholder"
style="width: 600px; height: 300px; position: relative;">

<canvas height="300" width="600">
</canvas>
<canvas height="300" style="position: absolute; left: 0px; top: 0px;" width="600">
</canvas>
<div style="font-size: smaller; color: rgb(84, 84, 84);">

<div class="gridLabel"
style="position: absolute; top: 285px; left: -20.5833px; width: 95.1667px; text-align: center;">

0.0

</div>

<div class="gridLabel"
style="position: absolute; top: 285px; left: 85.1574px; width: 95.1667px; text-align: center;">

2.5

</div>

<div class="gridLabel"
style="position: absolute; top: 285px; left: 190.898px; width: 95.1667px; text-align: center;">

5.0

</div>

<div class="gridLabel"
style="position: absolute; top: 285px; left: 296.639px; width: 95.1667px; text-align: center;">

7.5

</div>

<div class="gridLabel"
style="position: absolute; top: 285px; left: 402.38px; width: 95.1667px; text-align: center;">

10.0

</div>

<div class="gridLabel"
style="position: absolute; top: 285px; left: 508.12px; width: 95.1667px; text-align: center;">

12.5

</div>

<div class="gridLabel"
style="position: absolute; top: 275.5px; left: 0pt; width: 22px; text-align: right;">

-1.5

</div>

<div class="gridLabel"
style="position: absolute; top: 228.833px; left: 0pt; width: 22px; text-align: right;">

-1.0

</div>

<div class="gridLabel"
style="position: absolute; top: 182.167px; left: 0pt; width: 22px; text-align: right;">

-0.5

</div>

<div class="gridLabel"
style="position: absolute; top: 135.5px; left: 0pt; width: 22px; text-align: right;">

0.0

</div>

<div class="gridLabel"
style="position: absolute; top: 88.8333px; left: 0pt; width: 22px; text-align: right;">

0.5

</div>

<div class="gridLabel"
style="position: absolute; top: 42.1667px; left: 0pt; width: 22px; text-align: right;">

1.0

</div>

<div class="gridLabel"
style="position: absolute; top: -4.5px; left: 0pt; width: 22px; text-align: right;">

1.5

</div>

</div>

</div>

Flot supports user interactions. It's currently still a bit primitive,
but you can enable the user to click on the plot and get the
corresponding x and y values back.

Try clicking on the plot above. <span id="result"></span>

<script language="javascript" src="http://ptsefton.com/interacting_files/jquery_002.js" type="text/javascript"><!-- --></script>
<script language="javascript" src="http://ptsefton.com/interacting_files/jquery.js" type="text/javascript"><!-- --></script>
<script language="javascript" type="text/javascript">
 <!--//
$(function () {
    var d = [[1, 132], [2,121], [3,94.6], [4,61.9],[5,58.4],[6,56.8],[7,52.0],[8,39.5],[9,46.7],[10,72.2],[11,89.5],[12,120.0]];


    $.plot($("#placeholder"), [ d ], {
    lines: { show: true },
    points: { show: true },
    xaxis: {
    ticks: [0, [1, "Jan"], [2, "Feb"],[3, 'Mar'], [4, 'Apr'], [5, 'May'], [6, 'Jun'], [7,'Jul'],[8,'Aug'],[9,'Sep'],[10,'Oct'],[11,'Nov'],[12,'Dec']]
    },
    grid: { clickable: true }}

   );

    $("#placeholder").bind("plotclick", function (e, pos) {
        // the values are in pos.x and pos.y
        $("#result").text('You clicked on (' + pos.x.toFixed(2) +  ', ' + pos.y.toFixed(2) + ')');
    });
});
 //-->
</script>

</div>

</span>Flot is a Javascript solution. I took one of the examples from
the site and played with the data until I got this, which has some
rudimentary interactivity <span class="spCh spChx2013">–</span> you can
click to see the x and y values for the spot you clicked on, not that
useful at present, but it should be possible to make it much more useful
with a bit of work.
</p>
To make this work I used the same technique I wrote about for maps. I
put a copy of the Flot HTML page on my server, took a screenshot, pasted
it in here and [linked it](http://ptsefton.com/tmb-rainfall.html) to the
HTML. ICE used the HTML for online use and the image for print/PDF.

[Update: Fixed! WP has this bizarre feature that adds paragraph tags to
your code when it renders a page, even in the middle of a script. I
turned it off using a plugin called Disable WPAUTOP.]

# <span id="id3"></span><!--id3--></a>Chart tool in Writer

Finally, I did the obvious thing and tried the OpenOffice.org Chart
tool. This was by far the quickest and easiest way to go. I put the data
into a table, clicked `Insert`, `Object`, `Chart` and I was away. It's
not interactive for the end user, but **I** can click on it to change
the chart, as could you if I gave you access to my source document or
exposed the chart as a download that you could play with in an
OpenDocument aware application.

<a name="Object1"></a>![Object1](/wp-content/uploads/2008/01/523c8a31.gif)

# <span id="id4"></span><!--id4--></a>Raw data

<div class="Table49"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------------------+--------------------------------------+
| Jan                                  | Feb                                  |
+--------------------------------------+--------------------------------------+
| 132.1                                | 121.1                                |
+--------------------------------------+--------------------------------------+

</div>

# <span id="id5"></span><!--id5--></a>And the winner is?

As far as I can see, word processing users are reasonably well served
with tools for making static charts. The point-n-click wizards in
Microsoft Office and OpenOffice.org are hard to beat for usability. The
best thing to do now is probably to expose the data so that others can
graph it themselves. There's no way that most authors will want to use
something like Flot or the Google Chart API until there are wizard tools
to let them point at a table of data and graph it with a few clicks.

None of the solutions I looked at today that are close to meeting
Peter's requirement; *XY graphs are so common and so important that we
ought to be able to cut and paste them, preserving he semantics of the
underlying data*<span style="font-style:normal; "><span
class="T2">:</span></span>

1.  The Google Chart API format is cute <span
    class="spCh spChx2013">–</span> and it's very copy-and-pastable, but
    it:

    1.  Is very painful to use.

    2.  Does not work with raw data <span
        class="spCh spChx2013">–</span> you have to encode the data,
        thus loosing its integrity.

2.  Flot is also cute, but is also a pain to use, and copying and
    pasting is out of the question at present as the data are embedded
    in Javascript in an array.

3.  The office-suite based solution is sub-optimal because it's not a
    web format but it seems to be the best compromise at present.

For options 1 and 2 above it wouldn't be too hard, though, to write some
code to pull data from a table in your document, and slap on an easy to
use front-end.

Of course this was a survey of ad hoc charting tools <span
class="spCh spChx2013">–</span> there's lots of scope to automate things
where people are using the same kind of data over and over again. If,
for example you wanted to deal with rainfall data a lot you could set up
an automated process to take the data and turn into an Google Chart API
URL or a Flot chart.

(I have left in one deliberate error I made with the data for keen
readers to discover - I wonder how many accidental errors there are
though?)

</div>

</div>
