---
Title: "Presenting Slidy ICE"
Slug: presenting_slidy_ice
Date: 2006-05-23

---
<div>

The other day Jon Udell wrote about [HTML
Slidy](http://www.w3.org/Talks/Tools/#slidy/), a javascript library that
allows you to make presentations using HTML conforming to a sort of
microformat. I have spent a few hours working out how to add Slidy to
the [ICE](http://ice.usq.edu.au/)content management system. This means I
can write a document in my word processor, sprinkle it with slides,
click a button to blog it, another button to make a presentation and one
more button to make a PDF version.

More on how I did this below, with links to the results, but first some
background, sprinkled with Slidy slides. If you're viewing this via the
atom feed then you'll need to come to the website to see the slides.
You'll recognize them 'cos they have my usual top-notch
finger-down-the-throat graphic design.

<div class="slide">

# Jon Udell on Slidy

Jon
[says](http://www.infoworld.com/article/06/05/17/78280_21OPstrategic_1.html):

> Given my skills and inclinations, it’s no surprise that I’m an instant
> convert. To use it, you create a single XHTML file that pulls in CSS
> stylesheets and JavaScript code. Each slide’s content is wrapped in a
> DIV tag decorated with a class attribute of “slide.” Folks like me,
> who compose directly and easily in HTML, will love it.
>
> <http://www.infoworld.com/article/06/05/17/78280_21OPstrategic_1.html>

</div>

Given my propensities, I was plotting to make ICE spit out Slidy
presentations as soon as I saw this. Later, there was a follow up from
Jon about some of the political aspects of presentations and the web.
This contained a call to action, to the effect that we **should create
easy ways for people to publish presentations in a web friendly
format**. So, I sprang into action. As springy as I get, anyway.

<div class="slide">

# Jon Udell on the politics of presentation software

Jon Udell again – with emphasis by me.

> That said, I'll argue that it's democratic, not elitist, to believe
> that presentations ought to be first-class citizens of the web,
> viewable by any standards-based browser with full interactive
> fidelity. If we've failed to **fully democratize the necessary
> authoring software** -- as, so far, we have -- then shame on us.
> There's no longer any good reason why we couldn't make it **easy for
> people to create effective presentations** through the web as well as
> for the web, and there are plenty of good reasons why we could and
> should.
>
> [http://weblog.infoworld.com/udell/2006/05/22.html\#a1452](http://www.infoworld.com/article/06/05/17/78280_21OPstrategic_1.html)

</div>

For our ICE users at USQ and beyond (numbering a couple of dozen and
growing) this new technique using ICE + Slidy will be an easy to use
avenue to create presentations. But more that that, it will allow a new
amalgam of presentation and document about which I'm very excited.
Courseware written using ICE is already sprinkled with little boxes
containing activities, readings and the like. I think there's great
potential for picking out key points, quotes and images and highlighting
them as slides. This will make the print and full-text versions a bit
livelier, and you'll get a presentation for nothing, without the hassles
of syncing between two different sources.

All this of course depends on the great work that Dave Raggett did on
Slidy. A real triumph. Thanks!

Here's how it works in my proof-of-concept implementation.

<div class="slide">

# ICE + Slidy: how to use it

-   Use ICE as usual, using OpenOffice.lorg Writer or MS word and the
    ICE template.

-   Use autotext to insert a slide in-text.

-   Fill out the slide (pictures, bullets, blockquotes, whatever you
    like).

-   View your page through your ICE web site.

-   Click 'Slidy' to see the presentation.

-   Save the presentation from your browser.

</div>

Some background might help here: ICE runs on your computer as a little
web server that watches your files and converts them to HTML and PDF for
you. ICE is extensible, so it only took a few minutes to add the button
that says 'Slidy' to my ICE site.

<div class="slide">

# ICE + Slidy: How it works

-   ICE now recognizes a one-column, two row table with a paragraph of
    style 'h-slide' as a slide.

-   ICE turns slides into [HTML
    Slidy](http://www.w3.org/Talks/Tools/#slidy/) compatible divs.

-   ICE pages display as normal, with slides inline. You can use CSS to
    format the slides.

-   A new button in ICE generates a document containing only your
    slides, and applies an HTML Slidy template to it.

-   At this stage, you can save the resulting presentation from the
    browser.

</div>

Now there's a number of things to do to get this into production.

<div class="slide">

# Next Steps for ICE

To get ICE + Slidy out to the public:

-   Tidy up the code.

-   Add autotext entries for slides to ICE templates.

-   Add the 'Present' button to ICE / integrate into IMS packge output.

-   Document in the ICE guide.

-   Get real designers (not me!) to make some default CSS.

-   (Later) Support incremental display and outlines.

</div>

<div class="slide">

# Next Slidy steps for me

-   Make my presentation for [Ausweb
    '06](http://ausweb.scu.edu.au/aw06/conf/program.html)using ICE+
    Slidy.

-   Write a document/presentation about ICE to give to Sun , you know,
    the computer company.

</div>

<div class="slide">

# Summary

-   This post is courtesy of [ICE,](http://ice.usq.edu.au/)

-   Built-in [HTML Slidy](http://www.w3.org/Talks/Tools/#slidy/) slides
    formatted as dead-simple tables.

-   ICE created:

    1.  The full-text for the blog

    2.  [A PDF](http://ptsefton.com/files/slidy/slidy-demo.pdf)

    3.  [The
        presentation](http://ptsefton.com/files/slidy/slidy-demo.htm)

-   See the source document:

    1.  [OpenDocument](http://ptsefton.com/files/slidy/slidy-demo.odt)

    2.  [Microsoft Word](http://ptsefton.com/files/slidy/slidy-demo.doc)

</div>

</div>
