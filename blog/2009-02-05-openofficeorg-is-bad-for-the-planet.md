---
Author: ptsefton
Comments: true
Date: 2009-02-05 01:43:14+00:00
Slug: openofficeorg-is-bad-for-the-planet

Title: OpenOffice.org is bad for the planet
Wordpress_id: 278
---

<div>

<div class="page-toc">

</div>

<div>

It's been a while since I have [whinged here about how hard it is to
make web documents with Office
tools](http://delicious.com/ptsefton/xhtmlchallenge).

This is actually old news, but did you know that in OpenOffice.org
Writer the Save as HTML is completely stupid?

If you embed an image, lets say a 5Mb photo in your document and size it
to fit within the margins, and then save as HTML, Writer will create an
HTML image tag with sensible looking dimensions, say
`width=”400” height=”640”` but it simply writes out he photo at full
resolution. If you put that on the web then everyone will have to
download the full image and then spend CPU cycles resizing it, which
will lead to global warming, amongst other things.

Even worse, if you crop the image then the HTML export won't bother with
the cropping and will just show the whole image.

In the [ICE system](http://ice.usq.edu.au/) we have to code around this
kind of crap all the time. We've been dealing with the resize issue
since day one and it looks like we will have to look at cropping as well
now that our users are complaining.

See what happens when Linda Octalina from the ICE team puts in a bug
report:

> After the image being cropped in ODT file, when doing Save AS HTML,
> the image shown in html is the original Image and is resized to
> cropped image size.
>
> <http://www.openoffice.org/issues/show_bug.cgi?id=98639>

She got this response:

> @linda\_octa:
>
> This is not a valid bug report.
>
> When you tried to save the document in in HTML format you got a
> message "This document may contain formatting or content that cannot
> be saved...", and that's just that what happened here: as far as I
> know 'HTML 4.0 Transitional' has no possibility to show cropped
> images, and so this information will be lost during export to HTML.
>
> Pls. feel free to reopen this issue as ENHANCEMENT request if you find
> out that
>
> 'HTML 4.0 Transitional' syntax contains "crop image" information.

And this doesn't sound good:

> Even if we would implement this enhancement, we cannot because due to
> lack of resources. The HTML project is stalled.
>
> Thank you for your comprehension.

Over on the GullFOSS blog they're [talking about the new features
they're putting
in](http://blogs.sun.com/GullFOSS/entry/new_chart_features_in_openoffice1),
such as <span class="spCh spChx201c">“</span>Flexible positioning of
axes and axis labels<span class="spCh spChx201d">”</span> in charts. And
[making menus a little
nicer](http://blogs.sun.com/GullFOSS/entry/making_menus_a_little_nicer).
So there's still money to work on this OOo thing then.

It's obvious that there is some confusion here between using HTML as a
core document format (Microsoft actually managed that with Word 2000
with some problems ensuing) and the thing most people are going to want
to do, which is to export to HTML.

Maybe Kay Ramme cares? This matters for the [ODF@WWW
project](http://blogs.sun.com/GullFOSS/entry/odf_www_an_odf_wiki) which
turns office documents into web pages.

Maybe Sun's Tim Bray could give the OOo team a call to explain that
there should be a way for people using Writer to publish their documents
to the web? In Tim's (2004) terms Writer is '[just
broken](http://www.tbray.org/ongoing/When/200x/2004/03/26/OpenOffice)'
cos it doesn't have a 'Blog This' button.

ICE has a blog this button (Atompub), which you can use with
Openffice.org. To demonstrate I will now insert a picture of a man
called Space Cowboy spruiking his stuffed-animal freak show at last
year's Woodford Festival. The original is 4.8 MB (4995351 bytes) <span
class="spCh spChx2013">–</span> the one you're looking at is much
smaller, reducing global warming and computing costs.

<span
style="display: block"><a name="graphics1"></a>![graphics1](/wp-content/uploads/2009/02/36d4bd4a-191x254.jpg)</span>In
case you've just wandered in, we're big supporters of OpenOffice.org and
we use and recommend it, we're just bemused by some of the priorities at
Sun. If I had Google breathing down my neck I wouldn't be treating 'The
HTML project' as 'stalled'. But to be fair to Sun, the web's only about
17 years old.

</div>

</div>
