---
Author: ptsefton
Comments: true
Date: 2009-11-02 04:44:35+00:00
Slug: a-bit-more-on-wave-as-a-scholarly-html-editor

Title: A bit more on Wave as a Scholarly HTML editor
Wordpress_id: 386
excerpt: http://ptsefton.com/blog/2006/12/06/goog_docs/
---

<div>

<div class="page-toc">

-   [Impressions](#id1)
-   [The Wave (non)Document Model](#id3)

</div>

<div>

This is a quick follow-up to [my post last week about using Google Wave
as a collaborative editor for scholarly
works](http://ptsefton.com/2009/10/21/wave-as-an-html-editor.htm). I
will start with some impressions of using the thing then go on to look
at the Wave model.
# <span id="id1"></span></a>Impressions

[Cameron Neylon](http://blog.openwetware.org/scienceintheopen/) has
invited me to a Wave looking at a scientific article; he’s pasted one in
to Wave as an experiment and there’s a discussion going on about how to
structure things. I have to say that for a document of this length the
performance is abysmal, looking at this on the weekend at home on a two
year old low-end desktop machine I was unable to use the system at all
effectively <span class="spCh spChx2013">–</span> even scrolling is
jerky and annoying and the replay is unusable. Also, it seems that for
Wave to take off people are going to have to hang out there like they do
in email or Twitter. So far this doesn’t seem to be the case. I have
been invited to a couple of things but there’s not much happening so I
forget to open Wave, which means that, well, there’s not much happening.
This will change when we have our whole team in there, I guess. So this
week’s impression is it’s:
-   Going to take a while to generate critical mass in groups of users.
    (OK, so that’s obvious.)
-   Too ‘messagey’ to be useful as a document editor. The idea that
    robots and gadgets will be useful, [as discussed by Cameron
    Neylon](http://blog.openwetware.org/scienceintheopen/2009/08/23/reflecting-on-a-wave-the-demo-at-science-online-london-2009/)
    seems right, but I think we might need to use those in a different
    client <span class="spCh spChx2013">–</span> I’m not sure if that
    will actually be a Wave client, though. Even though Google docs also
    has awful HTML it’s much more workable as an editor. Can gadgets run
    there?

# <span id="id3"></span></a>The Wave (non)Document Model

I said last week that I thought Wave had some potential as an editor
that could output HTML even with its dodgy HTML, but I was wrong, I
think. As [Richard M. Davis](http://dablog.ulcc.ac.uk/) rightly [pointed
out in the
comments](http://ptsefton.com/2009/10/21/wave-as-an-html-editor.htm/comment-page-1#comment-833),
we really do need editing tools that can understand basic structures
like lists. [I
agree](http://ptsefton.com/2009/10/21/wave-as-an-html-editor.htm/comment-page-1#comment-837)
that if we are going to have useful Wave robots then they will need to
be able to work with proper structure, like being able to identify the
quotes in an article. The thing is that I had Wave completely wrong.
It’s a messaging system with a very tenuous relationship to HTML. It’s a
bit hard to find documentation on exactly what is going on behind the
scenes, but the [Draft Protocol Spec for the Google Wave Conversation
Model](http://www.waveprotocol.org/draft-protocol-specs/wave-conversation-model)
makes it clear just how far from being an HTML editor this thing is.
Here’s the example of a ‘blip’ document:
    <contributor name="dadams@acmewave.com">

    <body>

            <line></line>There is a theory which states that if ever anybody

            <line></line>discovers exactly what the Universe is for and why it

            <line></line>is here, it will instantly disappear and be replaced by

            <line></line>something even more bizarre and inexplicable. There is another

            <line></line>theory which states that this has already happened.

    </body>

This is very discouraging from a document point of view. It has explicit
line breaks in what looks to me like a paragraph. This probably explains
why there is the weird (`<p>text<br></p>`) markup in the HTML source of
a Wave. Waves in real life don’t seem to be broken up like this, it’s
almost like the `body` element in this example is equivalent to a `p`
element in HTML. This is more like a model for a chat client than a word
processor, and we need to bear this in mind. I have yet to figure out
the relationship between this line-based model and the formatting
buttons in the wave editor. Regarding structures like quotes or lists I
had an idea that maybe it would be possible to use Wave’s inherent
nesting/threading to make structured documents, so you’d have a ‘blip’
when you want a list and embed another in it when you want a nested list
but as you can’t copy or move blips, and you can’t put them between
paragraphs (or lines) then that’s unworkable in the current version.
Unfortunately, I think that Wave is too much a messaging system to be a
useful editor in the short term. That’s not to say it won’t be a useful
collaboration tool, but for drafting long structured documents I’m very
skeptical. Quite a while ago Stijn Dekeyser and Richard Watson here at
USQ [looked at using Google Docs to author
papers](http://ptsefton.com/blog/2006/12/06/goog_docs/) and concluded
that the collaborative tools were great, and it would make a nice text
editor in which to co-author LaTeX. I think maybe Wave would work for
LaTeX or Markdown or another wiki-like text-based format better than as
a WYSIWYG HTML editor at this stage; with collaborative editing of the
marked-up document, and rendering as a separate process. At the time of
posting I have a handful of invites to Wave, so drop me a line if you’re
interested. <span class="spCh spChxa9">©</span> Peter Sefton 2009.
Licensed under Creative Commons Attribution-Share Alike 2.5 Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

</div>

</div>
