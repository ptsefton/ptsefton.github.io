---
Title: "Practical Word Processor Interoperability"
Slug: wordprocessorinterop
Date: 2004-08-16

---
There's a been a bit of talk lately about Word processor formats, and
some well reasoned arguments that XHTML would be a good core format for
an application. But it isn't, yet. [Last time I
said](http://localhost:8000/blog/2004/08/09/futureoffice):

> I have decided the way forward is to adapt the existing leading word
> processors using their programmable interfaces (APIs), their template
> and style systems, and their macro languages that make them
> programmable.

This time I will *start* the process of looking at how we can get
Microsoft Word and OpenOffice to work together using templates, macros,
glue and string. I can't go and write a Word Processor but I can adapt
the ones I have to hand. I will develop the ideas here in the blog, and
start to compile the coherent bits into a manual: "Word processing for
Content Management" or some sexier title.

Read on for the project goals.

### Why are we here

We are here to look at how you might couple a word processor to a
Content Management System. Specifically, to start off with I will look
at Microsoft Word and OpenOffice.org.

What's Content Management?

I say: "It's the process of treating some or all of your electronic data
as set of related stuff, so that you can stick in on the web, amongst
other things you might do with it".

People usually talk about a "Content Management System" (CMS) as if it
were a computer application, but in my opinion, that's like talking
about a "Quality Management System" as though it were a computer
application; you probably know that it isn't; it's one of your core
business systems. Isn't it?

To manage content I think you probably need to know a little bit about
your content, and the formats and standards you use to create it and
store it. And that involves looking beyond the CMS software you may or
may not need, to processes.

Having a CMS *application*is important, though, because it will allow
you to treat your content as, well, content, and treat the business of
turning it into one or more web sites, or CDs, or local repositories, or
whatever as a separate issue.

(Another reason we're here is that I'm getting tired of typing documents
like this in the wiki-like formatting used by the Leonardo web site
software used here. I end up using Word anyway, to get the spill chucker
and the automatic saving and document recovery. I want to be able to use
my work machine in Word, touch up content at home in OpenOffice.org and
publish from either to here where the colour *de jour* will be
automatically applied.)

### The goal (as of 2004-08-16)

-   Design interoperable, generic templates for Word and OO.o sutiable
    for print and web publishing.
-   Specify extension mechanisms for domain or site specific
    requirements.
-   Provide ways of getting documents from both Word Processors into
    XHTML with usable graphics.
-   Provide simple-as-possible to use publishing to as many CMS's as
    possible, maybe using the ATOM protocol.
-   Use OO.o as a rendering engine to produce PDF, both for printing and
    for web distribution.

Why OO.o and Word? Well one is free, and cross platform and almost
comfortable if you don't try anything too trickly like resizing cropping
an image, and one is unavoidable. Other contenders like WordPerfect
simply don't have the market share to make it worthwhile paying for
licenses and learning them unless they have some extremely redeeming
feature, like a good inbuilt XML editor that could interoperate with the
documents *as word processing documents*, which I'm pretty sure
WordPerfect nearly but not quite has; I am looking for other contenders
to add to the project.
