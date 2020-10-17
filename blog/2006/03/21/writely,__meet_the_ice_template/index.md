---
Title: "Writely, meet the ICE template"
Slug: writely,__meet_the_ice_template
Date: 2006-03-21

---
<div>

Tom Worthington,
[writes](http://www.tomw.net.au/blog/2006/03/google-word-processor.html)
that Writely has been acquired by Google.

This made me remember that I have a Writely account, so I went back to
have a look. I have one document sitting in there.

Tom says:

> Writely is limited by being provided over the web, via a web browser.
> You type your document in a window on the web browser. Most of the
> time this is fine, but every now and then when Writely needs to do
> something complicated, you have to wait while the data is sent from
> browser to server and back. But you can use Writely from (almost) any
> computer with a web browser and Internet connection.
>
> Writely is far from OpenOffice.Org, which does try to be a rival to
> Ms-Office, has lots of functionality, but is therefore very complex. I
> spend a lot of my time removing extraneous formatting put in by
> "features" of Ms-Word and OOO documents so they can be put on the web
> efficiently or be used in typesetting systems.

> <http://www.tomw.net.au/blog/2006/03/google-word-processor.htm>

So lets talk about the process of "removing extraneous formatting" Tom
mentions. My one and only Writely document was originally imported from
an OpenOffice.org document. I chose an article I wrote about
OpenOffice.org- to-XHTML export. The thing looked roughly like my
original document but with one major problem. None of the lists came
through properly; so there were numbered lists that went, like, 1, 0, 2,
3 instead of 1, 2, 3, 4. And where there should have been plain-old
`<p>` tags there was this nonsense :

    <p align="left" lang="en-US" style="MARGIN-TOP: 0.08in; MARGIN-BOTTOM: 0in; FONT-STYLE: normal"> 

So is the Writely's fault? Well no. This kind of behavior is pretty much
what you'd get if you exported an HTML file from OpenOffice.org. That
is, it looks like crap.

Why is it crap? Because the word processor has one model for things like
lists and styles and so on and HTML has another. They're not the same.
And no software in the world is going to be able to divine what I meant
by my styles (or the lack of them). I [wrote about
this](http://ptsefton.com/blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)
last year.

Sigh.

If only there was a stylesheet/template one could use that would let one
reliably map word processing documents to HTML. (Yeah I know, I invented
it).

Using such a stylesheet is a kind of contract between the author and the
tools. If I use a paragraph of style 'p' then the tools are allowed to
make me a plain \<p\> without all the formatting info.

And if I have paragraphs with styles on them for lists, blockquotes, and
code? I'm writing this in OpenOffice.org, so I can show you, using my
special Styles menu I can apply these things with a few clicks or
key-strokes. Watch this:

1.  {stlyle: li1n} This is an item in a numbered list.

2.  {stlyle: li1n} This is also part of a numbered list. But let's
    include something the user would type:

        {style: pre2}>svn co http://ice.usq.edu.au/svn/ice/trunk

3.  {stlyle: li1n} More list.

    -   {style: li2b} And a sub list that quotes someone else?

    -   {style: li2b} Spencer the puppy dog says:

        > {style: bq3} Get out of my yard birdy!
        >
        > -   {style: li4b} Woof
        >
        > -   {style: li4b} Woof
        >
        > -   {style: li4b} Woof
        >
Did you see how **my** tools were smart enough to work out that the
barking bullets above were part of the blockquote, and the blockquote
was part of a list item, and the list item was part of a list and the
list was part of a list item...

You get the idea. Pure, lovely XHTML. Go on, look at the source.

(The style names are just there to help you see what's happening - I
don't have to type them in)

What could be done differently over at Writely so they can reliably
import documents and get the lists right, and better still, let people
start off in Writely online and produce word processing docs to send out
to others?

The Writely / Google people could design a well thought out, freely
available generic word processing template that works more or less
equally well in various different word processing environments (hint -
you'll need some clean-up code to help the poor word processors keep
their lists straight).

It would help if other services and software used it as well so people
could move stuff around more freely than they can now. Or they could use
the well thought out, freely available generic word processing template
from the ICE project (they may not be able to use the GPL licensed code
that goes with it, but it would not be hard to write. Even my colleague
Ian Barnes who is a mere computer science lecturer managed to do it,
using the exact same ICE template, and there is a [PDF
presentation](http://www.apsr.edu.au/Open_Repositories_2006/ian_barnes.pdf)
to prove it).

Online word processor people, [drop me a line](mailto:pt@ptsefton.com)
and I'll help you out.

</div>
