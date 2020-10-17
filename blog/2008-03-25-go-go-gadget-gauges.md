---
Author: ptsefton
Comments: true
Date: 2008-03-25 02:16:16+00:00
Slug: go-go-gadget-gauges

Title: Go go gadget gauges
Wordpress_id: 99
---

<div>

<span class="pdf-rendition-link">[View as
PDF](/wp-content/uploads/2008/03/go-go-gadget-gauge.pdf)</span>
<div class="page-toc">

</div>

<div>

Google have released some new toys:
[visualizations](http://code.google.com/apis/visualization/) AKA
gadgets.

This is what we've been waiting for without quite knowing what we were
waiting for.

If you have some data in a Google spreadsheet, or another application
that implements the API (are there any?) then you can hook it up to a
visualization. See the
[gallery](http://code.google.com/apis/visualization/).

This was not available when I looked at graphing [just a couple of
months ago](http://ptsefton.com/2008/01/04/graphing-with-ice.htm),
although maybe I could have done something with Google spreadsheet
charts.

I thought I'd see how easy it would be to build a new web service.
Imagine if I wanted to add a 'rate this post' function to my blog. (I
don't, but I might want something along those lines for document
collaboration. I've [talked before about the potential for a dashboard
for documents](http://ptsefton.com/blog/2006/11/09/or07/).)

So, I went to Google and made a blank spreadsheet. From there I was able
to make a form (via `Share`) with a simple multiple choice where you can
rate this post 1,2,3,4 or 5. I grabbed the form and pasted saved it, and
embedded in this post. Once I worked out where the form values were
being saved it was simple to add a cell that calculated an average
rating. Not worrying about rounding or precision or niceties like that
at this stage.

<span
style="display: block"><a name="graphics2"></a>![graphics2](/wp-content/uploads/2008/03/59232e0d.png)</span>

So here's the form, in this table:

<div class="Table48"
style="width: 100%; margin: 0px; padding: 0px; text-align:left;">

+--------------------------------------+--------------------------------------+
| <div class="embedded-html">          | <div class="embedded-html">          |
|                                      |                                      |
| # rating                             | <iframe frameborder="0" height="228" |
|                                      |  scrolling="no" src="http://4jqhndr1 |
| <form action="http://spreadsheets.go | -a.gmodules.com/ig/ifr?up__table_que |
| ogle.com/formResponse?key=pUSYtWNVDu | ry_url=http%3A%2F%2Fspreadsheets.goo |
| JJ5gmzKq3XsKA" method="post">        | gle.com%2Ftq%3Frange%3DD2%253AD2%26k |
| <div class="ss-form-entry">          | ey%3DpUSYtWNVDuJJ5gmzKq3XsKA%26gid%3 |
|                                      | D0%26pub%3D1&amp;up__table_query_ref |
| <span class="ss-q-title">Rate this   | resh_interval=0&amp;up_title=Rating& |
| post</span> <span                    | amp;up_minvalue=0&amp;up_maxvalue=5& |
| class="ss-q-help"></span>            | amp;up_greenrange=3-5&amp;up_yellowr |
| -   <input name="group:0" type="radi | ange=2-3&amp;up_redrange=0-1&amp;up_ |
| o" value="5"></input>                | minorticks=1&amp;url=http%3A%2F%2Fww |
|     5                                | w.google.com%2Fig%2Fmodules%2Fgauge. |
| -   <input name="group:0" type="radi | xml" style="border: 1px solid #ccccc |
| o" value="4"></input>                | c" width="299">                      |
|     4                                | <!-- -->                             |
| -   <input name="group:0" type="radi | </iframe>                            |
| o" value="3"></input>                |                                      |
|     3                                | </div>                               |
| -   <input name="group:0" type="radi |                                      |
| o" value="2"></input>                |                                      |
|     2                                |                                      |
| -   <input name="group:0" type="radi |                                      |
| o" value="1"></input>                |                                      |
|     1                                |                                      |
|                                      |                                      |
| </div>                               |                                      |
|                                      |                                      |
| <input type="submit" value="Submit"> |                                      |
| </input>                             |                                      |
| </form>                              |                                      |
| <span class="ss-powered-by">powered  |                                      |
| by Google Docs</span>                |                                      |
|                                      |                                      |
| <small>[Terms of                     |                                      |
| Service](http://www.google.com/accou |                                      |
| nts/TOS) -                           |                                      |
| [Additional                          |                                      |
| Terms](http://www.google.com/google- |                                      |
| d-s/terms.html)</small>              |                                      |
|                                      |                                      |
| </div>                               |                                      |
+--------------------------------------+--------------------------------------+

</div>

On the right is a simple gauge-style visualization, which shows the
average rating from 1 to 5. I have rated the post pretty highly to start
off with, so if you'd like to see the needle move you'd better vote
several times with low numbers. I won't be offended. Note that it seems
to cache results so you won't get a new view every time you refresh.

Ok, so this instance is a trivial toy, but it opens up a whole lot of
new possibilities. Can't wait to see what [Jim
Downing](http://wwmm.ch.cam.ac.uk/blogs/downing/) does; <span
class="spCh spChx201c">“</span>I want to play<span
class="spCh spChx201d">”</span>, says he via
[del.icio.us](http://del.icio.us/ojd20/blogfeed#2008-03-20). There's
great potential here not just to make visualizations that plug into
Google Spreadsheets, but to use the same APIs and/or general approach to
do the same for research repositories. The repository community needs to
respond quickly to this, lest important research data ends up being
hosted in personal Google accounts outside of any preservation regime.

We're doing a demo tomorrow with a mockup of an assignment submission /
marking system using the same technology. Faculty, do not try this at
home.

</div>

</div>
