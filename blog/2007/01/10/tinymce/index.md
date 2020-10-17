---
Title: "Unfinished: Online authoring using ICE Styles"
Slug: tinymce
Date: 2007-01-10

---
<div>

I have had a bad habit on this site of not posting things until they are
at least partly finished. This means lots of interesting bits and pieces
of experimental code have been sitting on my hard disk; some will
eventually appear in ICE or via [RUBRIC](http://rubric.edu.au/), but not
all. So, I've resolved to start writing up these explorations, partly as
documentation for myself and partly for your entertainment. I'll tag
these posts with
[unfinished](http://del.icio.us/ptsefton/ptsefton+unfinished).

First up, I have been thinking about online authoring tools. We'll need
an online version of [ICE](http://ice.usq.edu.au/) for the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project as many
research students don't have just one computer they use. Initially the
online ICE will be based on downloading documents, editing in a word
processor and re-uploading, or maybe via WebDAV. But in the longer term,
it would be good to edit documents straight from the browser.

I have written a couple of [rants about what an awful job Google Docs
does](http://del.icio.us/ptsefton/ptsefton+googledocs) of editing word
processing documents, so I did some experimenting to see if I could do
better.

My idea was to see if we could build an in-browser editor based on the
same kind of structure as a word processor – ie a document that consists
of paragraphs with styles on them with no hierarchical list or section
structures. Lists in particular seem to cause real problems for these
online editors, so why not ignore the listed nested structure of HTML in
the editing phase and use the same style names as we use in ICE? This
would allow easy interchange with word processors.

So, an ICEHTML document would look like this during the editing phase:

    <p class='li1b'>This is a bulleted list</p>

    <p class='li2n'>With a numbered list in it.</p>

    <p class='li2n'>With a numbered list in it.</p>

    <p class='li1b'>This is a bulleted list</p>

And would be stored as proper HTML later; it would be trivial to turn it
back into ICEHTML:

    <ul>

    <li><p class='li1b'>This is a bulleted list</p>

    <ol>

    <li><p class='li2n'>With a numbered list in it.</p></li>

    <li><p class='li2n'>With a numbered list in it.</p></li>

    </ol></li>

    <li><p class='li1b'>This is a bulleted list</p></li>

    </ul>

I chose to experiment with [TinyMCE](http://tinymce.moxiecode.com/).
There may be other options.

My very simple, unfinished [example is
here](http://ptsefton.com/files/tinymce/examples/example_pt.htm). You
can't save stuff back to the server. I have made one change from the ICE
styles, in that this version requires a different style for the first
item in a list. The editor should be able to work this out for you in a
real version of this idea.

**The main problem** is that browsers don't actually support CSS
counters properly, so while the lists number correctly Firefox shows
them with bullets. Safari handles CSS worse because it mangles the
numbering even though the display is better. I'm assuming there's some
kind of acceptable solution; but I didn't find one in a couple of hours
of mucking around last week. But you can forget about Safari for this
demo anyway – the text is not editable.

To use the demo, click in a paragraph and use the style drop down to
change the paragraph style – really a CSS class. You can click the HTML
button to see what you're generating. The CSS is
[here](http://ptsefton.com/files/tinymce/examples/example_pt.css).

**Note** that if you highlight across two or more paragraphs the editor
puts in a span element and adds the class to that, not the behaviour
we'd want in a real version.

Things we'd need **to do** to use something like this in ICE:

1.  Lose all the formatting buttons .

2.  Add promote and demote buttons that look like the current
    list-buttons, but which apply classes .

3.  Work out CSS hacks that work with (at least) Firefox, preferably
    other browsers.

4.  Write Javascript to restart lists in the right places.

5.  Customize the new Python-based HTML formatter in ICE so it can
    understand ICEHTML.

6.  Write an round trip OpenDocument to ICEHTML converter.

</div>
