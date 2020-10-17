---
Title: "Challenge: Produce XHTML and print from a Writer document"
Slug: the_web_with_writer
Date: 2007-07-03

---
[View this page as PDF](/blog/2007/07/03/the_web_with_writer/100.pdf)

<div>

I'm working on a paper about how we [use
styles](http://del.icio.us/ptsefton/usestyles) in the
[ICE](http://ice.usq.edu.au/) system to structure and format documents
for print and the web. I posted
[earlier](http://ptsefton.com/blog/2007/07/02/the_web_with_word) about
how I went trying to format a document for HTML using Word 2003 on
Windows, which is the latest version I had to hand.

Now it's time to try with OpenOffice.org Writer, actually I'm using the
latest NeoOffice for the Mac but it's essentially the same thing. I
wrote about this some time ago when I [got
cranky](http://ptsefton.com/blog/2005/10/31/why_do_i_keep_going_on_about_html_export_from_word_processors%3F)
about the HTML export in OpenOffice.org. Back then, in 2005, I had awful
trouble with trying to use the list styles that come with Writer, the
word processor.

The challenge is to take my recent paper, [An integrated approach to
preparing, publishing, presenting and preserving
theses](http://eprints.usq.edu.au/archive/00002653/) for the ETD
conference and see if I can make a decent HTML document from it.

Thought I'd try a different approach this time, and create a new HTML
document in Writer. In that mode there's a weird thing that you can look
at the HTML source, but once you do so you can't switch back to any
other view so you have to close the document and reopen it. And it turns
out that if you work in HTML mode you don't get headers and footers.
Solution is to create Writer document, then save as HTML and the headers
and footers remain. You'd probably just want to do a Save as HTML at the
end as an export anyway.

The first bit went better than Word. I was able to format the first
chunk of my document using a `Heading 1`, some default text and a style
called `Quotations` <span class="spCh spChx2013">–</span> not sure why
that's plural, but the resulting HTML is ugly but not too bad.

It has a nice clean heading and some paragraphs:

    <H1>Introduction</H1> 

    <P STYLE="margin-bottom: 0cm">This paper describes progress made

     on a project funded by the Australian government to create a free

     (as in open source) software application and associated

     documentation. The project is known as the <I>Integrated Content

     Environment for research and scholarship</I> or ICE-RS. The

     project is tasked with creating and/or documenting software and

     work practices that allow academics and students writing-up

     research to create documents, collaborate, manage, publish and

     deposit their work in repositories. An overview of the project,

    derived from the successful proposal document is available on the

     ICE website (Sefton 2006b) .</P> 

And blockquotes. It's not XHTML, but it could presumably be transformed
into XHTML pretty easily.

    <BLOCKQUOTE>In the institutional repository world, the Adobe PDF

     format is currently the expected norm for document

     delivery.</BLOCKQUOTE>

    <BLOCKQUOTE>Even though institutional repositories are web-

    based systems most content is not available in the native web

     format, HTML. HTML is more usable and flexible than PDF in many situations, allowing users to skim and sample content more

     easily that PDF. PDF, on the other hand, is a good solution

     for printing long documents and can be configured to make

     reading even book-length content a comfortable

     experience.</BLOCKQUOTE> 

So score one for Writer.

Now, I've said before that I can't figure out how to use the built in
list styles in Writer, and today they make no more sense to me that they
did nearly two years ago, so I decided to go with the format-only
approach.

Here's the target text:

![graphics4](/blog/2007/07/03/the_web_with_writer/1.jpg)

Using the lists in Writer is still a surreal experience, partly because
the bullets and numbering toolbar comes and goes as you click in and out
of a list.

I figured out how to get a list to look roughly right on the screen.

1.  You can make a list item by clicking on the number button:

    ![graphics1](/blog/2007/07/03/the_web_with_writer/2.jpg)

    Once you've done that, though I'm not sure how you're meant to add
    paragraphs to the first item, so they are indented underneath it.

2.  One thing I tried was *Insert Unnumbered Entry*, the button that
    looks like this:

    ![graphics2](/blog/2007/07/03/the_web_with_writer/3.jpg),

    But you have to click that to make an entry then copy-paste text
    into it, you can't use it like most other buttons to format things.

The result, as of when I gave up in disgust, in Firefox is this:

<div>

![graphics3](/blog/2007/07/03/the_web_with_writer/4.jpg)

</div>

The first list item (1.) is the result of a lot of laborious clicking of
*Insert Unnumbered Entry*, and dragging in text, I have no idea how the
second item (also 1.) can be made to number correctly. The follow-on
paragraph in the second item was put there using the indent button, it
looks OK in Writer but not in Firefox.

The resulting HTML is a bloody disgrace. The structure starts with a
one-item list.

    <OL>

        <LI><P CLASS="western" STYLE="margin-bottom: 0cm">Initially the

        handle will resolve to the server-side ICE repository, which because

        it is in the Subversion system is web-addressable, although usually

        authentication will be required.</P>

    </OL>

Which is followed up by a no-item list. That's right, a list with no
list items. At least it got the preformatted tag right, but I'm not
quite sure that the two `<FONT>` elements are doing in there. I'm also
not sure what this <span class="spCh spChx201c">“</span>western<span
class="spCh spChx201d">”</span> bit is but that's cool cos I'm in
Toowoomba. We might be part of South East Queensland, but we're west of
Brisbane.

    <OL>

        <P CLASS="western" STYLE="margin-bottom: 0cm">The author need not

        worry about handles at all: they can use links in the usual way to

        manage their content and the system will manage the creation and

        management of handles when content is exported from the system.</P>

        ...

        <pre class="western" style="margin-bottom:

        0.5cm;">http://localhost:8000/some-path</pre>

        <p class="western" style="margin-bottom: 0cm;">

        <font face="Times New Roman, serif"><font size="3">When

        exported it

        would use a handle resolver:</font></font></p>

    </OL>

# <span id="id2"></span>Conclusion

This sux.

Which is the same verdict as for Word 2003.

Not usable out of the box for writing a technical paper that needs to be
delivered in print and web formats. Writer does make PDF, though, which
is a plus.

</div>
