---
Author: ptsefton
Comments: true
Date: 2013-08-07 06:39:33+00:00
Slug: html-slide-presentations-students-to-the-rescue
Category: ScholarlyHTML
Title: HTML Slide presentations, students to the rescue
Wordpress_id: 1754
---

<article>
<section>
[![Creative Commons
Licence](http://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/deed.en_GB)\
<span property="dct:title" dct="http://purl.org/dc/terms/">HTML Slide
presentations, students to the rescue</span> by <span
property="cc:attributionName" cc="http://creativecommons.org/ns#">Peter
Sefton</span> is licensed under a [Creative Commons Attribution 3.0
Unported
License](http://creativecommons.org/licenses/by/3.0/deed.en_GB).

Thanks to Andrew Leahy's organising skills I am now the client for a
group of third year computing students from the School of Computing,
Engineering and Mathematics at the University of Western Sydney who have
chosen to work on an HTML slide viewer project for their major project.
I'm not going to name them here or point to their work without their
permission, but who knows, they might start up an open source project as
part of this assignment.

You might have noticed that on this blog I have been experimenting with
embedding slide presentations in posts, like this [conference
presentation on research data
management](http://ptsefton.com/2013/07/26/4a-data-management-acquiring-acting-on-archiving-and-advertising-data-at-the-university-of-western-sydney.htm)
which embeds slide images originally created in the Google Drive
presentation app along with speaker notes, or [this one on the same
topic](http://ptsefton.com/2013/05/22/research-data-the-university-of-western-sydney-introducing-a-data-deposit-management-plan-to-the-research-community-at-uws.htm)
where the slides are HTML sections rather than images. These posts mix
slides with text, so you can choose to read the story or watch the show
using an in browser HTML viewer. I think this idea has potential to be a
much better way of preserving and presenting slides than throwing
slide-decks online, but at the moment the whole experience on this blog
is more than a bit clunky and leaves lots to be desired, which is where
the students come in.

Hang on, there are dozens of HTML slide-viewer applications out there –
so why do I think we need a new one?

There are a few main requirements I had which are not met by any of the
existing frameworks, that I know of. These are:

-   **It should be possible to mix slide and discursive content.**

    That is, slides should be able to sprinkled through an otherwise
    'normal' HTML document which should display as plain-old-html
    without any tricks.

-   **Slide markup should be declarative and use modern semantic-web
    conventions.**

    That is, the slides and their parts should be identified by markup
    using URIs instead of the framework assuming, for example that
    \<section\> or \<div\> means 'this is a slide'. Potentially,
    different viewing engines could consume the same content. You could
    have a dedicated viewer for use in-venue with speaker notes on one
    screen and presentation on another and another to show a slide
    presentation embedded in a WordPress post.

-   **Following from (2), the slide show behaviour should be completely
    independent of the format for the slides.**

    That is adding the behaviour should be a one or two liner added to
    the top, or even better dropping the HTML into a 'slide-ready'
    content management system like, um, my blog.

There are plenty of frameworks with some kind of open license that
students should be able to adapt for this project. That's what I did
with my attempt, I wrote a few lines of code to take slides embedded in
blog posts, get rid of other HTML and marshal the result into the
venerable W3C [Slidy](http://www.w3.org/Talks/Tools/Slidy2/#(1)) format.
The format is declarative, and the documents don't 'do' anything at all
until a wordpress plugin sniffs-out slide markup hiding in them.

I'm going to be working with the team to negotiate what seems like a
reasonable set of goals for this project, but my current thinking is
something like the following:

-   **In consultation with me, define a declarative format for embedding
    slides in HTML** that can cover (at least):

    -   Identifying slides using a URI.

    -   Identify parts of slides (the slide vs notes etc).

-   **Allow slides to consist of one or both of an image of the slide or
    a text/HTML version of** **the same thing**. Eg a nicely rendered
    image of some bullet points from PowerPoint with equivalent HTML
    formatting also available to search engines and screen-readers.

-   **Improve on the current slide-viewing experience in WordPress**
    with:

    -   Some kind of player that works in-post (ie without going
        fullscreen). A simple solution that came up in our meeting would
        be to automatically add navigation that just skips between
        slides, with some kind of care taken to show the slide at the
        top of the screen with context below it.

    -   An improved full-screen player that can (at least) recognise
        when a full-screen image version of the slide is available and
        display that scaled to fit rather than the sub-optimal thing I
        have going on now with Slidy putting a heading at the and the
        image below.

There are lots more things that could be done with this, given time,
which might make good material for future projects:

1.  Adding support for this format to
    [Pandoc](http://johnmacfarlane.net/pandoc/) or similar.

2.  Creating a converter or exporter for slide presentations in common
    formats (.pptx, odp) targeting the new format.

3.  Extending the support I have [already built into
    WordDown](https://code.google.com/p/jischtml5/wiki/WordDown) and the
    ICE content converter to allow authors to embed slides in word
    processing documents.

4.  Adding support for syncronised audio and video.

5.  Allowing more hyper-presentations like [prezi.](http://prezi.com/)

6.  Dealing with progressive slide builds.

7.  Slide transitions.

8.  Different language versions of the same content.

9.  Synchronising display on multiple machines, eg student's ipads or a
    second computer.

10. Master slides and branding – point to a slide template somewhere?
    Include a suggested slide layout somehow?

11. Adding a presenter mode with slides on one screen and notes on
    another.

12. For use with mult-screen rigs like Andrew Leahy's Wonderama maybe
    the extra screens could be used to show more context, slides on one
    screen video of presenter on another – photos, maps on other
    screens. Eg a Wonderama presentation rig could look for geo-coded
    stuff in the presentation and throw up maps or Google Earth viz on
    spare screens, or other contextual material.

Of course depending on which framework, if any, the students decide to
adopt and/or adapt some of the above may come for free.

</section>
</article>

